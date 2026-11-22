"use client"
import * as React from "react"
import { AnimatePresence, motion, useAnimate, useMotionTemplate, useMotionValue, useReducedMotion, useSpring, useTransform } from "framer-motion"
import { RotateCcw } from "lucide-react"
import { cn } from "@/lib/utils"

export interface ContactFormValues {
  name: string
  email: string
  message: string
}

export type SubmitState = "idle" | "sending" | "sent" | "error"

export interface LiveContactFormProps {
  title?: string
  description?: string
  /** Max message length. Default 500. */
  maxLength?: number
  /** Shortest message we accept. Default 20. */
  minLength?: number
  /** Resolve to confirm, reject to show the error state. */
  onSubmit?: (values: ContactFormValues) => Promise<void>
  className?: string
}

type FieldName = keyof ContactFormValues
type Feedback = { tone: "hint" | "ok" | "error"; text: string }

function feedbackFor(field: FieldName, value: string, min: number, showErrors: boolean): Feedback {
  const v = value.trim()
  const soft = showErrors ? "error" : "hint"
  if (field === "name") {
    if (!v) return showErrors ? { tone: "error", text: "We need a name to address you by." } : { tone: "hint", text: "What should we call you?" }
    if (v.length < 2) return { tone: "hint", text: "Just a little more." }
    return { tone: "ok", text: `Nice to meet you, ${v.split(/\s+/)[0]}.` }
  }
  if (field === "email") {
    if (!v) return showErrors ? { tone: "error", text: "Without an email we can't write back." } : { tone: "hint", text: "We only use it to reply to you." }
    if (/\s/.test(v)) return { tone: "error", text: "Spaces can't live in an email address." }
    if (!v.includes("@")) return { tone: soft, text: "There's no @ in there yet." }
    const [local, domain = ""] = v.split("@")
    if (!local) return { tone: soft, text: "Something should come before the @." }
    if (!domain) return { tone: soft, text: "The part after the @ is missing." }
    if (!domain.includes(".") || domain.endsWith(".")) return { tone: soft, text: "Almost. The domain needs an ending like .com." }
    return { tone: "ok", text: "Looks right." }
  }
  if (!v) return showErrors ? { tone: "error", text: "Write a few words so we know what this is about." } : { tone: "hint", text: "A sentence or two is plenty." }
  if (v.length < min) return { tone: soft, text: `${min - v.length} more characters and we can send this.` }
  return { tone: "ok", text: "That's enough to work with." }
}


const GRADIENT = "linear-gradient(110deg,#5a49f0 0%,#7c5cff 35%,#ff6b6b 70%,#5a49f0 100%)"
const ACCENT_TEXT = "text-primary dark:text-[color-mix(in_oklab,var(--primary),white_45%)]"
const sp = { type: "spring" as const, stiffness: 300, damping: 24 }

function Ring({ value, max, min }: { value: number; max: number; min: number }) {
  const r = 11, c = 2 * Math.PI * r
  const pct = Math.min(1, value / max), left = max - value
  const reduce = useReducedMotion()
  const tone = left < 0 ? "text-red-600 dark:text-red-300" : left <= 40 ? "text-amber-700 dark:text-amber-300" : value >= min ? ACCENT_TEXT : "text-muted-foreground"
  return (
    <div className="flex items-center gap-2" role="img" aria-label={`${value} of ${max} characters used`}>
      <AnimatePresence>
        {left <= 40 && <motion.span initial={{ opacity: 0, x: reduce ? 0 : 6 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0 }} className={cn("text-xs font-medium tabular-nums", tone)}>{left}</motion.span>}
      </AnimatePresence>
      <motion.svg width="30" height="30" viewBox="0 0 28 28" className={cn("-rotate-90 transition-colors", tone)} aria-hidden
        animate={{ scale: !reduce && value === min ? [1, 1.35, 1] : 1, filter: value >= min ? "drop-shadow(0 0 5px currentColor)" : "drop-shadow(0 0 0 transparent)" }} transition={{ duration: 0.4 }}>
        <circle cx="14" cy="14" r={r} fill="none" strokeWidth="3" className="stroke-border" />
        <motion.circle cx="14" cy="14" r={r} fill="none" strokeWidth="3" strokeLinecap="round" stroke="currentColor" strokeDasharray={c} initial={false}
          animate={{ strokeDashoffset: c * (1 - pct) }} transition={reduce ? { duration: 0 } : { type: "spring", stiffness: 140, damping: 11 }} />
      </motion.svg>
    </div>
  )
}

/** Field wrapper: leans toward the pointer (magnetic) and runs a light around its border while focused. */
function Shell({ children, tone }: { children: React.ReactNode; tone: Feedback["tone"] }) {
  const reduce = useReducedMotion()
  const x = useSpring(0, { stiffness: 200, damping: 16 }), y = useSpring(0, { stiffness: 200, damping: 16 })
  const [focus, setFocus] = React.useState(false)
  return (
    <motion.div style={{ x, y }}
      onPointerMove={(e) => { if (reduce) return; const b = e.currentTarget.getBoundingClientRect(); x.set(((e.clientX - b.left) / b.width - 0.5) * 6); y.set(((e.clientY - b.top) / b.height - 0.5) * 4) }}
      onPointerLeave={() => { x.set(0); y.set(0) }}
      onFocusCapture={() => setFocus(true)} onBlurCapture={() => setFocus(false)}
      className={cn("relative rounded-xl p-[1.5px] transition-colors", tone === "error" ? "bg-red-500/70" : tone === "ok" ? "bg-primary/50" : "bg-border")}>
      <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden rounded-xl">
        <motion.div className="absolute left-1/2 top-1/2 aspect-square w-[260%] -translate-x-1/2 -translate-y-1/2"
          style={{ background: "conic-gradient(from 0deg, transparent 0 55%, #22d3ee 70%, #6c5cff 82%, #ff6b6b 94%, transparent)" }}
          initial={false} animate={{ opacity: focus ? 1 : 0, rotate: reduce ? 0 : 360 }} transition={{ opacity: { duration: 0.25 }, rotate: { duration: 2.4, repeat: Infinity, ease: "linear" } }} />
      </div>
      <div className={cn("relative rounded-[10px] bg-background transition-shadow", focus && "shadow-[0_0_24px_-4px_color-mix(in_oklab,var(--primary)_55%,transparent)]")}>{children}</div>
    </motion.div>
  )
}

const inputBase = "block min-h-11 w-full rounded-[10px] bg-transparent px-3 py-2.5 text-sm text-foreground placeholder:text-muted-foreground outline-none disabled:opacity-60"

const PATH: [number, number][] = [[0, 0], [50, -80], [150, -170], [270, -270]]

export function LiveContactForm({
  title = "Send us a note", description = "We usually reply within a working day.", maxLength = 500, minLength = 20, onSubmit, className,
}: LiveContactFormProps) {
  const uid = React.useId()
  const reduce = useReducedMotion()
  const [scope, animate] = useAnimate()
  const [values, setValues] = React.useState<ContactFormValues>({ name: "", email: "", message: "" })
  const [touched, setTouched] = React.useState<Record<FieldName, boolean>>({ name: false, email: false, message: false })
  const [attempted, setAttempted] = React.useState(false)
  const [state, setState] = React.useState<SubmitState>("idle")
  const [shake, setShake] = React.useState(0)
  const [flying, setFlying] = React.useState(false)
  const [full, setFull] = React.useState(300)
  const wrap = React.useRef<HTMLDivElement>(null)
  const alive = React.useRef(true)
  React.useEffect(() => { alive.current = true; return () => { alive.current = false } }, [])
  React.useEffect(() => {
    const el = wrap.current; if (!el) return
    const ro = new ResizeObserver(() => setFull(el.offsetWidth)); ro.observe(el); setFull(el.offsetWidth); return () => ro.disconnect()
  }, [])

  // card depth: tilt, parallax blobs, cursor light
  const mx = useMotionValue(0.5), my = useMotionValue(0.5)
  const rx = useSpring(useTransform(my, [0, 1], [6, -6]), { stiffness: 120, damping: 18 })
  const ry = useSpring(useTransform(mx, [0, 1], [-7, 7]), { stiffness: 120, damping: 18 })
  const ax = useSpring(useTransform(mx, [0, 1], [30, -30]), { stiffness: 60, damping: 20 }), ay = useSpring(useTransform(my, [0, 1], [30, -30]), { stiffness: 60, damping: 20 })
  const bx = useSpring(useTransform(mx, [0, 1], [-50, 50]), { stiffness: 40, damping: 20 }), by = useSpring(useTransform(my, [0, 1], [-50, 50]), { stiffness: 40, damping: 20 })
  const px = useMotionValue(-300), py = useMotionValue(-300)
  const glow = useMotionTemplate`radial-gradient(240px circle at ${px}px ${py}px, color-mix(in oklab, var(--primary) 20%, transparent), transparent 70%)`
  const onMove = (e: React.PointerEvent<HTMLFormElement>) => {
    const b = e.currentTarget.getBoundingClientRect()
    mx.set((e.clientX - b.left) / b.width); my.set((e.clientY - b.top) / b.height); px.set(e.clientX - b.left); py.set(e.clientY - b.top)
  }
  const onLeave = () => { mx.set(0.5); my.set(0.5) }

  const fb = (f: FieldName) => feedbackFor(f, values[f], minLength, touched[f] || attempted)
  const feedback = { name: fb("name"), email: fb("email"), message: fb("message") }
  const valid = (f: FieldName) => feedbackFor(f, values[f], minLength, false).tone === "ok" && values.message.length <= maxLength
  const set = (f: FieldName) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => { setValues((s) => ({ ...s, [f]: e.target.value })); if (state === "sent" || state === "error") setState("idle") }
  const blur = (f: FieldName) => () => setTouched((t) => ({ ...t, [f]: true }))

  const fly = async () => {
    if (reduce) return
    setFlying(true)
    await animate(".plane", { x: 0, y: 0, rotate: 0, scale: 1, opacity: 1 }, { duration: 0 })
    const xs = PATH.map((p) => p[0]), ys = PATH.map((p) => p[1])
    const dots = PATH.length * 3
    const trail = Array.from({ length: dots }, (_, i) => {
      const t = i / (dots - 1), seg = Math.min(PATH.length - 2, Math.floor(t * (PATH.length - 1))), u = t * (PATH.length - 1) - seg
      return [PATH[seg][0] + (PATH[seg + 1][0] - PATH[seg][0]) * u, PATH[seg][1] + (PATH[seg + 1][1] - PATH[seg][1]) * u] as const
    })
    await Promise.all([
      animate(".plane", { x: xs, y: ys, rotate: [-8, -38, -52, -30], scale: [1, 1.25, 1, 0.35], opacity: [1, 1, 1, 0] }, { duration: 1.15, ease: "easeInOut", times: [0, 0.3, 0.65, 1] }),
      ...trail.map(([x, y], i) => animate(`.dot-${i}`, { x, y, opacity: [0, 1, 0], scale: [0.2, 1, 0] }, { duration: 0.8, delay: (i / dots) * 1.05 })),
    ])
    setFlying(false)
  }

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (state === "sending") return
    setAttempted(true)
    if (!(valid("name") && valid("email") && valid("message"))) {
      setShake((n) => n + 1)
      const first = (["name", "email", "message"] as FieldName[]).find((f) => !valid(f))
      if (first) document.getElementById(`${uid}-${first}`)?.focus()
      return
    }
    setState("sending")
    try {
      await onSubmit?.(values)
      await fly()
      if (alive.current) setState("sent")
    } catch {
      if (alive.current) { setState("error"); setShake((n) => n + 1) }
    }
  }

  const field = (f: FieldName, label: string, node: (props: Record<string, unknown>) => React.ReactNode) => {
    const info = feedback[f]
    return (
      <div>
        <label htmlFor={`${uid}-${f}`} className="mb-1.5 block text-sm font-medium">{label}</label>
        <Shell tone={info.tone}>
          {node({ id: `${uid}-${f}`, value: values[f], onChange: set(f), onBlur: blur(f), disabled: state === "sending", "aria-invalid": info.tone === "error" || undefined, "aria-describedby": `${uid}-${f}-msg`, className: inputBase })}
        </Shell>
        <div id={`${uid}-${f}-msg`} aria-live="polite" className="relative mt-1.5 h-5 overflow-hidden text-xs">
          <AnimatePresence mode="wait" initial={false}>
            <motion.p key={info.text} initial={{ opacity: 0, y: reduce ? 0 : 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: reduce ? 0 : -10 }} transition={{ duration: reduce ? 0.01 : 0.16 }}
              className={cn("flex items-center gap-1.5", info.tone === "error" && "text-red-700 dark:text-red-300", info.tone === "ok" && ACCENT_TEXT, info.tone === "hint" && "text-muted-foreground")}>
              {info.tone === "ok" && <motion.svg viewBox="0 0 24 24" className="size-3.5" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" aria-hidden><motion.path d="M5 12.5l4.5 4.5L19 7.5" initial={{ pathLength: reduce ? 1 : 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3 }} /></motion.svg>}
              {info.text}
            </motion.p>
          </AnimatePresence>
        </div>
      </div>
    )
  }

  const round = state !== "idle" && state !== "error"
  const label = state === "error" ? "Couldn't send. Try again" : "Send message"

  return (
    <div className={cn("relative w-full max-w-md", className)} style={{ perspective: 1100 }}>
      <motion.div aria-hidden className="pointer-events-none absolute -inset-3 rounded-[2rem] bg-[conic-gradient(from_160deg,#6c5cff,#22d3ee,#ff6b6b,#6c5cff)] blur-2xl"
        animate={reduce ? { opacity: 0.3 } : { opacity: [0.25, 0.5, 0.25], scale: [1, 1.03, 1] }} transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }} />
      <motion.form ref={scope} onSubmit={submit} onPointerMove={onMove} onPointerLeave={onLeave} noValidate aria-label={title}
        style={{ rotateX: reduce ? 0 : rx, rotateY: reduce ? 0 : ry, transformStyle: "preserve-3d" }}
        initial={{ opacity: 0, y: reduce ? 0 : 24 }} animate={{ opacity: 1, y: 0 }} transition={{ type: "spring", stiffness: 140, damping: 18 }}
        className="relative rounded-2xl border border-border bg-card p-5 text-foreground shadow-[0_40px_70px_-35px_rgba(50,35,150,0.5)] sm:p-6">
        <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden rounded-2xl">
          <motion.div className="absolute -left-12 -top-16 size-48 rounded-full bg-[#6c5cff]/25 blur-3xl" style={{ x: ax, y: ay }} />
          <motion.div className="absolute -bottom-20 -right-10 size-48 rounded-full bg-[#ff6b6b]/20 blur-3xl" style={{ x: bx, y: by }} />
          {!reduce && <motion.div className="absolute inset-0" style={{ background: glow }} />}
        </div>
        <header className="relative mb-5" style={{ transform: "translateZ(24px)" }}>
          <h2 className="text-lg font-semibold leading-tight">{title}</h2>
          <p className="mt-1 text-sm text-muted-foreground">{description}</p>
        </header>
        <div className="relative space-y-3" style={{ transform: "translateZ(14px)" }}>
          {field("name", "Your name", (p) => <input type="text" autoComplete="name" placeholder="Alex Rivera" {...p} />)}
          {field("email", "Email", (p) => <input type="email" autoComplete="email" inputMode="email" placeholder="alex@example.com" {...p} />)}
          {field("message", "Message", (p) => (
            <div className="relative">
              <textarea rows={5} maxLength={maxLength + 40} placeholder="What's on your mind?" {...p} className={cn(p.className as string, "resize-none pb-9")} />
              <div className="pointer-events-none absolute bottom-2.5 right-2.5"><Ring value={values.message.length} max={maxLength} min={minLength} /></div>
            </div>
          ))}
        </div>

        <div ref={wrap} className="relative mt-3" style={{ transform: "translateZ(30px)" }}>
        <motion.div key={shake} className="relative flex min-h-14 justify-center"
          animate={shake && !reduce ? { x: [0, -9, 9, -6, 6, 0] } : { x: 0 }} transition={{ duration: 0.4 }}>
          <motion.button type="submit" disabled={state === "sending" || flying} aria-label={state === "sent" ? "Message sent" : state === "sending" ? "Sending" : label}
            initial={false} animate={{ width: round ? 56 : full, backgroundPositionX: reduce ? "0%" : ["0%", "200%"] }}
            transition={{ width: reduce ? { duration: 0 } : { type: "spring", stiffness: 260, damping: 18 }, backgroundPositionX: { duration: 5, repeat: Infinity, ease: "linear" } }}
            whileTap={reduce ? undefined : { scale: 0.95 }} whileHover={reduce || round ? undefined : { y: -2 }}
            style={{ background: state === "error" ? "#dc2626" : GRADIENT, backgroundSize: "250% 100%" }}
            className="relative grid h-14 place-items-center overflow-visible rounded-[28px] text-sm font-semibold text-white shadow-[0_12px_30px_-8px_rgba(108,92,255,0.75)] outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring disabled:cursor-wait">
            <AnimatePresence mode="popLayout" initial={false}>
              {!round && (
                <motion.span key={state} className="inline-flex items-center gap-2 whitespace-nowrap" initial={{ opacity: 0, y: reduce ? 0 : 12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: reduce ? 0 : -12 }} transition={sp}>
                  {state === "error" && <RotateCcw className="size-4" aria-hidden />}{label}
                </motion.span>
              )}
              {state === "sent" && (
                <motion.svg key="ok" viewBox="0 0 24 24" className="size-7" fill="none" stroke="currentColor" strokeWidth="2.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden initial={{ scale: 0.4, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={sp}>
                  <motion.path d="M6 12.5l4 4 8-9" initial={{ pathLength: reduce ? 1 : 0 }} animate={{ pathLength: 1 }} transition={{ delay: 0.1, duration: 0.45 }} />
                </motion.svg>
              )}
            </AnimatePresence>
            {state === "sent" && !reduce && [0, 1].map((i) => <motion.span key={i} aria-hidden className="pointer-events-none absolute size-14 rounded-full border-2 border-[#8b7bff]" initial={{ scale: 1, opacity: 0.7 }} animate={{ scale: 2.5, opacity: 0 }} transition={{ duration: 0.9, delay: i * 0.15 }} />)}
          </motion.button>
          {/* paper plane + trail live outside the button so they can leave the card */}
          <span aria-hidden className="plane pointer-events-none absolute left-1/2 top-1/2 z-10 -ml-4 -mt-4">
            <motion.span className="block" initial={false} animate={state === "sending" ? { opacity: 1, rotate: reduce ? 0 : [-8, 6, -8], y: reduce ? 0 : [0, -3, 0] } : { opacity: 0 }} transition={{ duration: 0.9, repeat: Infinity }}>
              <svg width="32" height="32" viewBox="0 0 24 24" fill="#fff" stroke="#5a49f0" strokeWidth="1.5" strokeLinejoin="round" style={{ filter: "drop-shadow(0 0 8px #8b7bff)" }}><path d="M3 11.5L21 3l-6.5 18-3.2-7.3L3 11.5z" /><path d="M11.3 13.7L21 3" fill="none" /></svg>
            </motion.span>
          </span>
          {Array.from({ length: PATH.length * 3 }).map((_, i) => <motion.span key={i} aria-hidden className={`dot-${i} pointer-events-none absolute left-1/2 top-1/2 -ml-1.5 -mt-1.5 size-3 rounded-full opacity-0 blur-[1px]`} style={{ background: ["#22d3ee", "#8b7bff", "#ff6b6b"][i % 3], boxShadow: "0 0 10px currentColor" }} />)}
        </motion.div>
        </div>
        <div aria-live="polite" className="relative min-h-5 text-center text-xs">
          {state === "sent" && <motion.p initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} className="mt-2 text-muted-foreground">Sent. We'll write back soon.</motion.p>}
          {state === "error" && <p role="alert" className="mt-2 text-red-700 dark:text-red-300">Your message is still here. Nothing was lost.</p>}
        </div>
      </motion.form>
    </div>
  )
}

/** Demo with invented behaviour: the first send fails, the second works. */
export default function Demo() {
  const tries = React.useRef(0)
  return <LiveContactForm onSubmit={async () => { await new Promise((r) => setTimeout(r, 1200)); if (tries.current++ === 0) throw new Error("offline") }} />
}

