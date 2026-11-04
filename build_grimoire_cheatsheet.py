"""
Builds a high-density, professional 2-page Developer Grimoire Reference Cheatsheet PDF:
'Applied_Cyber_Occultism_Developer_Grimoire_Cheatsheet.pdf'
Uses ReportLab.
Author: Sir Leonard Daragan // The Undefined Behavior Series
"""

import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Ensure UTF-8 stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_PDF = r"C:\Users\rick\.gemini\antigravity\scratch\applied-cyber-occultism\Applied_Cyber_Occultism_Developer_Grimoire_Cheatsheet.pdf"

def build_pdf():
    # Margins: 0.35 inch for high-density cheatsheet
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=25,
        rightMargin=25,
        topMargin=22,
        bottomMargin=22
    )

    styles = getSampleStyleSheet()

    # Dark cyber-occult theme colors
    c_void = colors.HexColor("#07090e")
    c_panel = colors.HexColor("#0d1117")
    c_card = colors.HexColor("#161b22")
    c_amber = colors.HexColor("#d97706") # readable amber on white/grey
    c_cyan = colors.HexColor("#0284c7")  # readable cyan/blue
    c_dark = colors.HexColor("#0f172a")
    c_dim = colors.HexColor("#475569")
    c_border = colors.HexColor("#cbd5e1")

    # Typography styles
    style_header_title = ParagraphStyle(
        'HeaderTitle',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        textColor=c_dark
    )
    style_header_sub = ParagraphStyle(
        'HeaderSub',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=c_dim
    )
    style_sec_title = ParagraphStyle(
        'SecTitle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=c_amber
    )
    style_body = ParagraphStyle(
        'CheatsheetBody',
        fontName='Helvetica',
        fontSize=7,
        leading=8.5,
        textColor=c_dark
    )
    style_code = ParagraphStyle(
        'CheatsheetCode',
        fontName='Courier',
        fontSize=6.5,
        leading=8.0,
        textColor=colors.HexColor("#094a6d")
    )
    style_bold_label = ParagraphStyle(
        'CheatsheetBold',
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=c_dark
    )

    story = []

    # =========================================================================
    # PAGE 1: PRIVILEGE RINGS, AOS SIGIL PIPELINE & ABJAD LETTRISM
    # =========================================================================
    
    # Header Bar Table
    header_data = [
        [
            Paragraph("<b>APPLIED CYBER-OCCULTISM // DEVELOPER QUICK-REFERENCE RUNBOOK</b>", style_header_title),
            Paragraph("<b>VOL. 1: THE UNDEFINED BEHAVIOR SERIES</b><br/>Sir Leonard Daragan · Codex Press", style_header_sub)
        ]
    ]
    t_header = Table(header_data, colWidths=[400, 160])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_amber, spaceAfter=5))

    # SECTION 1: COGNITIVE PRIVILEGE RINGS
    story.append(Paragraph("<b>1. THE COGNITIVE PRIVILEGE RINGS (NEURO-ARCHITECTURAL MODEL)</b>", style_sec_title))
    rings_data = [
        [
            Paragraph("<b>RING</b>", style_bold_label),
            Paragraph("<b>SYSTEM SUBSYSTEM</b>", style_bold_label),
            Paragraph("<b>NEUROLOGICAL SUBSTRATE</b>", style_bold_label),
            Paragraph("<b>OPERATIONAL FUNCTION & CONSTRAINTS</b>", style_bold_label)
        ],
        [
            Paragraph("<b>Ring 3</b>", style_bold_label),
            Paragraph("User Space (Narrative Ego)", style_body),
            Paragraph("Default Mode Network (mPFC, PCC)", style_body),
            Paragraph("Discursive internal monologue, autobiographical simulation, conscious doubts. Contains Psychic Censor. Cannot execute arbitrary state changes directly.", style_body)
        ],
        [
            Paragraph("<b>Ring 1</b>", style_bold_label),
            Paragraph("Device Drivers & Filters", style_body),
            Paragraph("Thalamic Reticular Nucleus (TRN)", style_body),
            Paragraph("Sensory gating packet filter. Drops 99% of raw sensory inputs. Modulated via sensory deprivation, rhythm, or hyper-arousal to bypass default filters.", style_body)
        ],
        [
            Paragraph("<b>Ring 0</b>", style_bold_label),
            Paragraph("Kernel Space (Biological)", style_body),
            Paragraph("Autonomic Nervous System, Brainstem", style_body),
            Paragraph("Vagal brake (Cranial Nerve X), heart rate, endocrine releases, visceral reactions. Executes raw compiled non-semantic visual hashes (Sigils) and background daemons.", style_body)
        ],
        [
            Paragraph("<b>Ring -1/-2</b>", style_bold_label),
            Paragraph("Substrate Hypervisor", style_body),
            Paragraph("Pre-Informational Reality Fabric", style_body),
            Paragraph("The Wheeler 'It from Bit' participatory quantum substrate. Probabilistic wavefunctions compiled JIT at the moment of conscious observation/measurement.", style_body)
        ]
    ]
    t_rings = Table(rings_data, colWidths=[45, 120, 140, 255])
    t_rings.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_rings)
    story.append(Spacer(1, 6))

    # SECTION 2: MODULE 3 AOS SIGIL COMPILATION PIPELINE
    story.append(Paragraph("<b>2. MODULE 3: THE 5-STAGE AOS SIGIL COMPILATION PIPELINE</b>", style_sec_title))
    
    stages_data = [
        [
            Paragraph("<b>STAGE</b>", style_bold_label),
            Paragraph("<b>OPERATION</b>", style_bold_label),
            Paragraph("<b>COMPILER SPECIFICATION & MATHEMATICAL RULES</b>", style_bold_label),
            Paragraph("<b>CANONICAL WORKED EXAMPLE</b>", style_bold_label)
        ],
        [
            Paragraph("<b>Stage 1</b>", style_bold_label),
            Paragraph("Lexical Source Code", style_body),
            Paragraph("Draft in Syslog. Invariant present-tense affirmative. Zero future tense ('will be'). <b>Strict Negation Purge:</b> Kernel drops negative booleans (NOT, NEVER, NO) → trips Censor.", style_body),
            Paragraph("<code>\"MY STARTING SALARY IS EIGHTY THOUSAND DOLLARS\"</code>", style_code)
        ],
        [
            Paragraph("<b>Stage 2</b>", style_bold_label),
            Paragraph("UNIX <code>strip</code> (Vowel Purge)", style_body),
            Paragraph("Normalize to uppercase ASCII. Purge all whitespace, punctuation, and linguistic vowels (A, E, I, O, U) to destroy semantic syntax and phonetic melody.", style_body),
            Paragraph("<code>MYSTRTNGSLRYSGHTYTHSNDDLLRS</code> (Len: 27)", style_code)
        ],
        [
            Paragraph("<b>Stage 3</b>", style_bold_label),
            Paragraph("Shannon Deduplication", style_body),
            Paragraph("Eliminate repeating consonants. Preserve strict first-occurrence order. Maximizes Shannon Entropy H(X) = -Σ p(x) log₂ p(x) to eradicate visual redundancy.", style_body),
            Paragraph("<code>[ M, Y, S, T, R, N, G, L, H, D ]</code> (Vector Len: 10)<br/>H(X) = 3.204 bits", style_code)
        ],
        [
            Paragraph("<b>Stage 4</b>", style_bold_label),
            Paragraph("Topological Graph Reduction", style_body),
            Paragraph("Deconstruct consonants into geometric primitives (vertical spines, horizontal bars, loops, diagonals). Fuse shared stems onto central axis; close Eulerian loop.", style_body),
            Paragraph("Shared Spine (T,D,L,R,M,N) + Eulerian Bézier curve. Mutual info I(X;Y) → 0.", style_code)
        ],
        [
            Paragraph("<b>Stage 5</b>", style_bold_label),
            Paragraph("Abjad Checksum & Enclosure", style_body),
            Paragraph("Calculate classical Ilm al-Huruf lettristic sum. Draw unbroken circular boundary constraint (Memory Boundary Container) to isolate executable process in Ring 0.", style_body),
            Paragraph("Abjad Sum = <b>802</b><br/>SHA-256 Process Hash<br/>Bounded Circular Ring", style_code)
        ]
    ]
    t_stages = Table(stages_data, colWidths=[45, 95, 230, 190])
    t_stages.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_stages)
    story.append(Spacer(1, 6))

    # SECTION 3: CLASSICAL ILM AL-HURUF ABJAD TABLE
    story.append(Paragraph("<b>3. CLASSICAL ILM AL-HURUF ABJAD NUMERICAL MATRIX</b>", style_sec_title))
    abjad_row1 = [
        Paragraph("<b>LET</b>", style_bold_label), Paragraph("A", style_body), Paragraph("B", style_body), Paragraph("C", style_body), Paragraph("D", style_body), Paragraph("E", style_body), Paragraph("F", style_body), Paragraph("G", style_body), Paragraph("H", style_body), Paragraph("I", style_body), Paragraph("J", style_body), Paragraph("K", style_body), Paragraph("L", style_body), Paragraph("M", style_body)
    ]
    abjad_val1 = [
        Paragraph("<b>VAL</b>", style_bold_label), Paragraph("1", style_code), Paragraph("2", style_code), Paragraph("20", style_code), Paragraph("4", style_code), Paragraph("5", style_code), Paragraph("80", style_code), Paragraph("3", style_code), Paragraph("5", style_code), Paragraph("10", style_code), Paragraph("10", style_code), Paragraph("20", style_code), Paragraph("30", style_code), Paragraph("40", style_code)
    ]
    abjad_row2 = [
        Paragraph("<b>LET</b>", style_bold_label), Paragraph("N", style_body), Paragraph("O", style_body), Paragraph("P", style_body), Paragraph("Q", style_body), Paragraph("R", style_body), Paragraph("S", style_body), Paragraph("T", style_body), Paragraph("U", style_body), Paragraph("V", style_body), Paragraph("W", style_body), Paragraph("X", style_body), Paragraph("Y", style_body), Paragraph("Z", style_body)
    ]
    abjad_val2 = [
        Paragraph("<b>VAL</b>", style_bold_label), Paragraph("50", style_code), Paragraph("70", style_code), Paragraph("80", style_code), Paragraph("100", style_code), Paragraph("200", style_code), Paragraph("60", style_code), Paragraph("400", style_code), Paragraph("6", style_code), Paragraph("6", style_code), Paragraph("6", style_code), Paragraph("60", style_code), Paragraph("10", style_code), Paragraph("7", style_code)
    ]
    t_abjad = Table([abjad_row1, abjad_val1, abjad_row2, abjad_val2], colWidths=[30] + [37]*13)
    t_abjad.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_abjad)
    story.append(Spacer(1, 6))

    # SECTION 4: FIRING & GNOSIS INJECTION PROTOCOLS
    story.append(Paragraph("<b>4. GNOSIS INJECTION RUNBOOK (THE DEATH POSTURE / RETINAL BLEACHING)</b>", style_sec_title))
    gnosis_data = [
        [
            Paragraph("<b>PHASE 1: CHARGING</b>", style_bold_label),
            Paragraph("Lock gaze on sigil canvas. Engage 0.1 Hz vagal breathing. Suppress DMN internal monologue.", style_body),
            Paragraph("<b>PHASE 3: AFTERIMAGE BURN</b>", style_bold_label),
            Paragraph("Close eyes immediately. Watch high-contrast entoptic afterimage float against eyelids until it fades into void.", style_body)
        ],
        [
            Paragraph("<b>PHASE 2: RETINAL STROBE</b>", style_bold_label),
            Paragraph("Execute tachistoscopic retinal flash (140ms high-contrast strobe). Photoreceptors bleaches glyph into retina.", style_body),
            Paragraph("<b>PHASE 4: EXPULSION BANISH</b>", style_bold_label),
            Paragraph("Force a diaphragmatic laugh or cold water splash. Erase semantic memory. Never consciously dwell on intent.", style_body)
        ]
    ]
    t_gnosis = Table(gnosis_data, colWidths=[110, 170, 110, 170])
    t_gnosis.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_gnosis)

    # Page 1 footer
    story.append(Spacer(1, 6))
    story.append(Paragraph("<i>Applied Cyber-Occultism · Page 1 of 2 · Interactive Web Suite: https://sirleonarddaragan.github.io/applied-cyber-occultism/</i>", style_header_sub))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: SERVITORS, TAROT HEAP DUMP, & 0.1 HZ VAGAL PACER
    # =========================================================================

    # Header Bar Page 2
    header_data2 = [
        [
            Paragraph("<b>APPLIED CYBER-OCCULTISM // DEVELOPER QUICK-REFERENCE RUNBOOK</b>", style_header_title),
            Paragraph("<b>SYSTEM DEPLOYMENTS, TELEMETRY & CIR</b><br/>POSIX Daemons · Tarot Heap · 0.1 Hz Pacer", style_header_sub)
        ]
    ]
    t_header2 = Table(header_data2, colWidths=[380, 180])
    t_header2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_header2)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_cyan, spaceAfter=5))

    # SECTION 5: MODULE 4 POSIX SERVITORS
    story.append(Paragraph("<b>5. MODULE 4: POSIX AUTONOMOUS THOUGHTFORM DAEMONS (SERVITORS)</b>", style_sec_title))
    
    servitor_data = [
        [
            Paragraph("<b>MANIFEST BLOCK</b>", style_bold_label),
            Paragraph("<b>REQUIRED FIELDS (SCHEMA: v1alpha1)</b>", style_bold_label),
            Paragraph("<b>OPERATIONAL FUNCTION & FAILURE RISK</b>", style_bold_label)
        ],
        [
            Paragraph("<b>metadata</b>", style_bold_label),
            Paragraph("<code>process_name, unique_pid, author_uid: 0, host_substrate_type, host_physical_id</code>", style_code),
            Paragraph("Binds process to physical hardware anchor (YubiKey, cold talisman, silicon). Token destruction halts execution.", style_body)
        ],
        [
            Paragraph("<b>lifecycle_and_ttl</b>", style_bold_label),
            Paragraph("<code>ttl_half_life_days, hard_kill_epoch_utc, decay_differential_lambda, garbage_collection_mode</code>", style_code),
            Paragraph("<b>TTL Decay Differential:</b> dN/dt = -λN, where λ = ln(2)/T½. Hard-kill epoch at 2×T½ (25% potency). Prevents obsessive memory leaks.", style_body)
        ],
        [
            Paragraph("<b>execution_envelope</b>", style_bold_label),
            Paragraph("<code>target_vector, operating_mode: EVENT_DRIVEN_DORMANT, event_listeners: [{trigger, action}]</code>", style_code),
            Paragraph("Daemon must sleep in dormancy until explicitly triggered by environmental/biometric interrupt. No continuous polling.", style_body)
        ],
        [
            Paragraph("<b>resource_allocation</b>", style_bold_label),
            Paragraph("<code>attention_compute_budget: '10_MIN_DAILY', prohibited_power_sources: [SLEEP, CORTISOL, RECURSION]</code>", style_code),
            Paragraph("Restricts compute consumption to disciplined budget. Prohibits insomnia harvesting or obsessive emotional loops.", style_body)
        ],
        [
            Paragraph("<b>interrupt_handlers</b>", style_bold_label),
            Paragraph("<code>sigterm_graceful_shutdown: {passphrase_sha256}, sigkill_emergency_halt: {procedure: COLD_PLUNGE}</code>", style_code),
            Paragraph("<b>SIGTERM:</b> Graceful ritual de-provisioning.<br/><b>SIGKILL (CIR-01):</b> Uncatchable halt. Trigeminal 10°C cold plunge + physical token purge.", style_body)
        ]
    ]
    t_servitor = Table(servitor_data, colWidths=[90, 220, 250])
    t_servitor.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_servitor)
    story.append(Spacer(1, 6))

    # SECTION 6: MODULE 5 TAROT HEAP DUMP & STOCHASTIC RESONANCE
    story.append(Paragraph("<b>6. MODULE 5: 78-ELEMENT MEMORY HEAP DUMP & STOCHASTIC RESONANCE</b>", style_sec_title))
    tarot_info = [
        [
            Paragraph("<b>BISTABLE DOUBLE-WELL POTENTIAL:</b><br/>V(x) = -(a/2)x² + (b/4)x⁴<br/>Barrier Height: ΔV = a²/(4b) = 0.25", style_code),
            Paragraph("<b>KRAMERS ESCAPE RATE:</b><br/>r_K = (a / (√2·π)) · exp(-ΔV / D)<br/>Intuitive signal crosses from Subconscious (Well 1) to Conscious (Well 2) when noise floor D ≈ ΔV.", style_code),
            Paragraph("<b>3-REGISTER HEAP INTERROGATION:</b><br/><b>[CALL_STACK]:</b> Past causal architecture.<br/><b>[INSTRUCTION_PTR]:</b> Active executing state.<br/><b>[INTERRUPT_VECTOR]:</b> Probabilistic trend.", style_code)
        ]
    ]
    t_tarot_info = Table(tarot_info, colWidths=[180, 190, 190])
    t_tarot_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_tarot_info)
    story.append(Spacer(1, 4))

    # 4 Hardware Busses Table
    busses_data = [
        [Paragraph("<b>BUS CHANNEL</b>", style_bold_label), Paragraph("<b>SUITE</b>", style_bold_label), Paragraph("<b>REGISTER CODES</b>", style_bold_label), Paragraph("<b>SYSTEM HARDWARE TELEMETRY DOMAIN</b>", style_bold_label)],
        [Paragraph("<b>LOGIC / VECTOR</b>", style_body), Paragraph("Swords (Air)", style_body), Paragraph("<code>REG_SW_0x01 .. REG_SW_0x0E</code>", style_code), Paragraph("Mental processing, discursive algorithms, intellectual contention, error states.", style_body)],
        [Paragraph("<b>KINETIC / THERMAL</b>", style_body), Paragraph("Wands (Fire)", style_body), Paragraph("<code>REG_WA_0x01 .. REG_WA_0x0E</code>", style_code), Paragraph("Processing throughput, metabolic drive, kinetic momentum, active execution surges.", style_body)],
        [Paragraph("<b>HYDRO-VASCULAR</b>", style_body), Paragraph("Cups (Water)", style_body), Paragraph("<code>REG_CP_0x01 .. REG_CP_0x0E</code>", style_code), Paragraph("Neuro-endocrine cascades, interoceptive gut signaling, affective attachment leaks.", style_body)],
        [Paragraph("<b>PERSISTENT DISK</b>", style_body), Paragraph("Pentacles (Earth)", style_body), Paragraph("<code>REG_PN_0x01 .. REG_PN_0x0E</code>", style_code), Paragraph("Physical chassis, thermodynamic wear, capital assets, persistent storage infrastructure.", style_body)]
    ]
    t_busses = Table(busses_data, colWidths=[90, 75, 125, 270])
    t_busses.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_busses)
    story.append(Spacer(1, 6))

    # SECTION 7: MODULE 1.5 0.1 HZ VAGAL LOCK
    story.append(Paragraph("<b>7. MODULE 1.5: 0.1 Hz VAGAL LOCK RESONANT PACING (THE BIOLOGICAL CLEANROOM)</b>", style_sec_title))
    vagal_data = [
        [
            Paragraph("<b>FREQUENCY & CADENCE</b>", style_bold_label),
            Paragraph("<b>$0.10\\text{ Hz}$ ($6.0\\text{ breaths / minute}$).</b> 5.0s Inhale / 5.0s Exhale (or 4.0s Inhale / 6.0s Exhale for maximal vagal clamp).", style_body)
        ],
        [
            Paragraph("<b>BIOPHYSICAL RESONANCE</b>", style_bold_label),
            Paragraph("Phase-locks three major biological rhythms: (1) Respiratory Sinus Arrhythmia (RSA), (2) Mayer blood pressure waves, (3) Cerebral arterial perfusion. Heart Rate Variability (HRV) coherence peaks at ~100%.", style_body)
        ],
        [
            Paragraph("<b>NEUROLOGICAL EFFECT</b>", style_bold_label),
            Paragraph("Massive burst of afferent vagal signaling to Nucleus Tractus Solitarius (NTS). Shuts down amygdala threat alarms, suppresses DMN, and establishes the Zero-Trust somatic cleanroom.", style_body)
        ]
    ]
    t_vagal = Table(vagal_data, colWidths=[120, 440])
    t_vagal.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_vagal)
    story.append(Spacer(1, 6))

    # SECTION 8: COMMERCIAL CHANNELS & EMERGENCY RUNBOOKS
    story.append(Paragraph("<b>8. HARDENED ENTERPRISE COMMUNICATIONS & MONETIZATION CONDUITS</b>", style_sec_title))
    links_data = [
        [
            Paragraph("<b>AMAZON COLLECTOR'S EDITIONS</b><br/>Hardcover ($24.95) · Paperback ($17.99) · Kindle ($8.99)<br/><code>amazon.com/author/sirleonarddaragan</code>", style_body),
            Paragraph("<b>SUBSTACK CLASSIFIED DISPATCHES</b><br/>Zero-day rituals, hypervisor memory dumps.<br/><code>sirleonarddaragan.substack.com</code>", style_body),
            Paragraph("<b>KO-FI COMPUTE SPONSORSHIP</b><br/>Sponsor continuous cluster compute & tooling.<br/><code>ko-fi.com/sirleonarddaragan</code>", style_body)
        ]
    ]
    t_links = Table(links_data, colWidths=[185, 185, 190])
    t_links.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_links)

    # Page 2 footer
    story.append(Spacer(1, 6))
    story.append(Paragraph("<i>Applied Cyber-Occultism · Page 2 of 2 · Sovereign Node 0x00 · Copyright © 2026 Sir Leonard Daragan</i>", style_header_sub))

    doc.build(story)
    print(f"// SUCCESS: Grimoire cheatsheet generated at: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_pdf()
