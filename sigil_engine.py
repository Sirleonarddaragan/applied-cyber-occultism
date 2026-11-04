"""
Applied Cyber-Occultism // Module 3
Austin Osman Spare (AOS) Sigil Compiler & Vector Hash Runtime (SIGIL.EXE)
Specification: The Undefined Behavior Series, Vol. 1
Author: Sir Leonard Daragan
"""

import sys
import os
import re
import math
import hashlib
import argparse
from typing import List, Dict, Tuple, Any

# Ensure stdout uses UTF-8 encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Classical Ilm al-Huruf Abjad mapping aligned with Module 3 Table (G=3, H=5, T=400, S=60)
ABJAD_TABLE: Dict[str, int] = {
    'A': 1,   'B': 2,   'C': 20,  'D': 4,   'E': 5,
    'F': 80,  'G': 3,   'H': 5,   'I': 10,  'J': 10,
    'K': 20,  'L': 30,  'M': 40,  'N': 50,  'O': 70,
    'P': 80,  'Q': 100, 'R': 200, 'S': 60,  'T': 400,
    'U': 6,   'V': 6,   'W': 6,   'X': 60,  'Y': 10,
    'Z': 7
}

VOWELS = set('AEIOU')

# Anatomical stroke primitives for Austin Osman Spare letter reduction
LETTER_PRIMITIVES: Dict[str, List[str]] = {
    'B': ['vertical_spine', 'top_loop', 'bottom_loop'],
    'C': ['left_arc'],
    'D': ['vertical_spine', 'right_loop'],
    'F': ['vertical_spine', 'top_horizontal', 'mid_horizontal'],
    'G': ['left_arc', 'mid_horizontal_inward'],
    'H': ['left_vertical', 'right_vertical', 'mid_horizontal'],
    'J': ['top_horizontal', 'center_vertical_hook'],
    'K': ['vertical_spine', 'upper_diagonal', 'lower_diagonal'],
    'L': ['vertical_spine', 'bottom_horizontal'],
    'M': ['vertical_spine', 'left_diagonal_down', 'right_diagonal_up', 'right_vertical'],
    'N': ['vertical_spine', 'diagonal_down', 'right_vertical'],
    'P': ['vertical_spine', 'top_loop'],
    'Q': ['outer_circle', 'bottom_diagonal_spur'],
    'R': ['vertical_spine', 'top_loop', 'lower_diagonal'],
    'S': ['s_curve'],
    'T': ['top_horizontal', 'vertical_spine'],
    'V': ['left_diagonal_down', 'right_diagonal_up'],
    'W': ['w_down_up_down_up'],
    'X': ['diagonal_cross_forward', 'diagonal_cross_backward'],
    'Y': ['upper_v_branch', 'vertical_spine'],
    'Z': ['top_horizontal', 'diagonal_down_left', 'bottom_horizontal']
}


def compile_statement(statement: str) -> Dict[str, Any]:
    """
    Executes the 5-Stage AOS Compilation Pipeline:
    Stage 1: Lexical Source String & Censor Linting
    Stage 2: Normalization & UNIX strip (vowel purge: A, E, I, O, U)
    Stage 3: Shannon Entropy Filtering & Deduplication
    Stage 4: Topological Graph Reduction (Eulerian Merging & Vector Geometry)
    Stage 5: Classical Ilm al-Huruf Abjad Checksum & SHA-256 Process Hash
    """
    raw_statement = statement.strip()
    if not raw_statement:
        raise ValueError("ERR_0x00_EMPTY_INPUT: Source statement cannot be empty.")
    
    # Normalize typographical curly quotes from iOS/macOS
    cleaned_statement = re.sub(r'[\u2018\u2019]', "'", raw_statement)
    cleaned_statement = re.sub(r'[\u201c\u201d]', '"', cleaned_statement)

    # Stage 1: Check for negative operators (Psychic Censor alert)
    negation_warnings = []
    lower_s = cleaned_statement.lower()
    for neg in ['not', 'never', "don't", 'dont', 'wont', "won't", 'no', 'cannot', "can't"]:
        if re.search(r'\b' + re.escape(neg) + r'\b', lower_s):
            negation_warnings.append(
                f"ERR_0x01_CENSOR_TRIP: Detected negative operator '{neg}'. "
                "Subconscious kernel ignores negative booleans. Rephrase into invariant affirmative."
            )

    # Stage 2: Normalization & Character Stripping (UNIX strip)
    normalized_str = re.sub(r'[^A-Z]', '', cleaned_statement.upper())
    if not normalized_str:
        raise ValueError("ERR_0x01_NO_ALPHA: Source statement contains no alphabetic characters.")
    
    # Strip vowels
    vowels_stripped = [char for char in normalized_str if char not in VOWELS]
    intermediate_stream = "".join(vowels_stripped)
    if not intermediate_stream:
        raise ValueError("ERR_0x02_EMPTY_CONSONANTS: Statement consists exclusively of vowels; cannot compile consonant vector.")

    # Stage 3: Shannon Entropy Filtering & Deduplication
    seen = set()
    consonant_vector: List[str] = []
    dedup_trace: List[Dict[str, str]] = []
    
    for char in vowels_stripped:
        if char not in seen:
            seen.add(char)
            consonant_vector.append(char)
            dedup_trace.append({"char": char, "status": "RETAIN", "reason": "1st occurrence"})
        else:
            dedup_trace.append({"char": char, "status": "PURGE", "reason": "Duplicate consonant"})

    # Shannon Entropy calculation H(X)
    freqs = {}
    for c in intermediate_stream:
        freqs[c] = freqs.get(c, 0) + 1
    total_chars = len(intermediate_stream) if intermediate_stream else 1
    shannon_entropy = -sum((cnt / total_chars) * math.log2(cnt / total_chars) for cnt in freqs.values())

    # Stage 5: Abjad Checksum Verification
    abjad_breakdown = []
    composite_abjad_sum = 0
    for c in consonant_vector:
        val = ABJAD_TABLE.get(c, 0)
        composite_abjad_sum += val
        abjad_breakdown.append({"char": c, "val": val})

    # SHA-256 Process Hash
    hash_payload = f"{normalized_str}|{''.join(consonant_vector)}|{composite_abjad_sum}".encode('utf-8')
    process_hash = hashlib.sha256(hash_payload).hexdigest()

    # Stage 4: Topological Graph Reduction (Procedural Vector Geometry)
    svg_glyph = generate_procedural_sigil_svg(consonant_vector, composite_abjad_sum, process_hash, cleanroom=False)
    talisman_svg = generate_procedural_sigil_svg(consonant_vector, composite_abjad_sum, process_hash, cleanroom=True)

    return {
        "statement": raw_statement,
        "normalized": normalized_str,
        "vowels_stripped": intermediate_stream,
        "consonant_vector": consonant_vector,
        "consonant_string": "".join(consonant_vector),
        "dedup_trace": dedup_trace,
        "shannon_entropy": round(shannon_entropy, 4),
        "abjad_breakdown": abjad_breakdown,
        "composite_abjad_sum": composite_abjad_sum,
        "process_hash": process_hash,
        "svg_glyph": svg_glyph,
        "talisman_svg": talisman_svg,
        "negation_warnings": negation_warnings
    }


def generate_procedural_sigil_svg(
    consonants: List[str],
    abjad_sum: int,
    process_hash: str,
    size: int = 500,
    cleanroom: bool = False
) -> str:
    """
    Renders the Austin Osman Spare topological graph reduction inside a circular bounding container.
    Harmonized with client-side mathematical constants and includes permanent cryptographic watermarking.
    """
    cx = size / 2.0
    cy = size / 2.0
    outer_radius = size * 0.42
    inner_radius = size * 0.38
    
    stroke_gold = "#000000" if cleanroom else "#f59e0b"
    stroke_cyan = "#000000" if cleanroom else "#38bdf8"
    stroke_dim = "#333333" if cleanroom else "#06b6d4"
    fill_node = "#000000" if cleanroom else "#f59e0b"
    fill_loop = "none" if cleanroom else "rgba(6, 182, 212, 0.05)"
    
    seed_ints = [int(process_hash[i:i+4], 16) for i in range(0, 32, 4)]
    elements: List[str] = []
    
    # 1. Circular Enclosure (Memory Boundary Constraint)
    elements.append(f'  <!-- Circular Memory Boundary Constraint -->')
    elements.append(f'  <circle cx="{cx}" cy="{cy}" r="{outer_radius}" fill="none" stroke="{stroke_gold}" stroke-width="{2.5 if not cleanroom else 2.0}" opacity="0.95" />')
    elements.append(f'  <circle cx="{cx}" cy="{cy}" r="{inner_radius}" fill="none" stroke="{stroke_dim}" stroke-width="1.2" stroke-dasharray="4 6" opacity="{0.6 if not cleanroom else 0.8}" />')
    
    # Cardinal grounding ticks
    for angle in [0, 90, 180, 270]:
        rad = math.radians(angle)
        x1 = cx + (inner_radius - 8) * math.cos(rad)
        y1 = cy + (inner_radius - 8) * math.sin(rad)
        x2 = cx + (outer_radius + 6) * math.cos(rad)
        y2 = cy + (outer_radius + 6) * math.sin(rad)
        elements.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke_gold}" stroke-width="2.0" />')

    # 2. Central Shared Spine
    spine_len = inner_radius * 1.55
    y_top = cy - (spine_len / 2.0)
    y_bottom = cy + (spine_len / 2.0)
    elements.append(f'  <!-- Shared Vertical Spine (Primitive Fusion) -->')
    elements.append(f'  <line x1="{cx}" y1="{y_top:.1f}" x2="{cx}" y2="{y_bottom:.1f}" stroke="{stroke_cyan}" stroke-width="3.5" stroke-linecap="round" />')

    # 3. Concentric Abjad Harmonic Ring (Harmonized constant: +30)
    core_ring_r = (abjad_sum % 35) + 30
    elements.append(f'  <circle cx="{cx}" cy="{cy}" r="{core_ring_r:.1f}" fill="none" stroke="{stroke_gold}" stroke-width="2.0" opacity="0.85" />')

    # 4. Genuinely Parse Consonant Letter Primitives
    n = len(consonants)
    eulerian_pts: List[Tuple[float, float]] = []
    
    if n > 0:
        step_y = (spine_len * 0.75) / max(n, 1)
        for i, char in enumerate(consonants):
            char_val = ABJAD_TABLE.get(char, 10)
            primitives = LETTER_PRIMITIVES.get(char, ['vertical_spine', 'top_loop'])
            curr_y = y_top + (spine_len * 0.12) + (i * step_y)
            side = -1 if (i % 2 == 0) else 1
            
            elements.append(f'  <!-- Consonant Token: {char} (Abjad: {char_val}) -->')
            for prim in primitives:
                if 'loop' in prim:
                    loop_r = 12.0 + (char_val % 18)
                    loop_cx = cx + (side * loop_r)
                    elements.append(f'  <path d="M {cx} {curr_y - loop_r:.1f} A {loop_r} {loop_r} 0 0 {1 if side > 0 else 0} {cx} {curr_y + loop_r:.1f}" fill="{fill_loop}" stroke="{stroke_gold}" stroke-width="2.2" stroke-linecap="round" />')
                    eulerian_pts.append((loop_cx, curr_y))
                elif 'horizontal' in prim:
                    bar_w = 26.0 + (char_val % 30)
                    elements.append(f'  <line x1="{cx - (bar_w/2):.1f}" y1="{curr_y:.1f}" x2="{cx + (bar_w/2):.1f}" y2="{curr_y:.1f}" stroke="{stroke_cyan}" stroke-width="2.4" stroke-linecap="round" />')
                    eulerian_pts.append((cx + (side * bar_w / 2), curr_y))
                elif 'diagonal' in prim:
                    diag_len = 35.0 + (char_val % 25)
                    diag_angle = 35.0 if 'upper' in prim or 'up' in prim else -35.0
                    rad = math.radians(diag_angle)
                    dx = side * diag_len * math.cos(rad)
                    dy = -diag_len * math.sin(rad)
                    tx = cx + dx
                    ty = curr_y + dy
                    elements.append(f'  <line x1="{cx}" y1="{curr_y:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{stroke_gold}" stroke-width="2.2" stroke-linecap="round" />')
                    elements.append(f'  <circle cx="{tx:.1f}" cy="{ty:.1f}" r="3.5" fill="{fill_node}" stroke="{stroke_cyan}" stroke-width="1.2" />')
                    eulerian_pts.append((tx, ty))
                elif 'arc' in prim:
                    arc_r = 28.0 + (char_val % 20)
                    arc_h = arc_r * 1.6
                    elements.append(f'  <path d="M {cx - 10:.1f} {curr_y - arc_h/2:.1f} Q {cx - arc_r*1.5:.1f} {curr_y:.1f} {cx - 10:.1f} {curr_y + arc_h/2:.1f}" fill="none" stroke="{stroke_cyan}" stroke-width="2.2" stroke-linecap="round" />')
                    eulerian_pts.append((cx - arc_r, curr_y))
                elif 's_curve' in prim:
                    s_w = 24.0
                    s_h = 40.0
                    elements.append(f'  <path d="M {cx - s_w:.1f} {curr_y - s_h/2:.1f} C {cx + s_w:.1f} {curr_y - s_h/4:.1f}, {cx - s_w:.1f} {curr_y + s_h/4:.1f}, {cx + s_w:.1f} {curr_y + s_h/2:.1f}" fill="none" stroke="{stroke_gold}" stroke-width="2.2" stroke-linecap="round" />')
                    eulerian_pts.append((cx + (side * s_w), curr_y))

        # 5. Eulerian Continuity Interlock (Harmonized jitter: % 24 - 12)
        if len(eulerian_pts) >= 3:
            path_d = f"M {eulerian_pts[0][0]:.1f} {eulerian_pts[0][1]:.1f}"
            for i in range(1, len(eulerian_pts)):
                p_prev = eulerian_pts[i-1]
                p_curr = eulerian_pts[i]
                cpx = (p_prev[0] + p_curr[0]) / 2 + ((seed_ints[i % 8] % 24) - 12)
                cpy = (p_prev[1] + p_curr[1]) / 2 + ((seed_ints[(i+1) % 8] % 24) - 12)
                path_d += f" Q {cpx:.1f} {cpy:.1f} {p_curr[0]:.1f} {p_curr[1]:.1f}"
            cpx = (eulerian_pts[-1][0] + eulerian_pts[0][0]) / 2
            cpy = (eulerian_pts[-1][1] + eulerian_pts[0][1]) / 2
            path_d += f" Q {cpx:.1f} {cpy:.1f} {eulerian_pts[0][0]:.1f} {eulerian_pts[0][1]:.1f} Z"
            elements.append(f'  <!-- Eulerian Continuity Interlock -->')
            elements.append(f'  <path d="{path_d}" fill="{fill_loop}" stroke="{stroke_gold}" stroke-width="1.8" stroke-dasharray="6 3" opacity="{0.85 if not cleanroom else 0.9}" />')

    # 6. Terminal Crown & Grounding Plates
    elements.append(f'  <!-- Terminal Anchors -->')
    elements.append(f'  <path d="M {cx - 16} {y_top + 16} L {cx} {y_top} L {cx + 16} {y_top + 16}" fill="none" stroke="{stroke_gold}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />')
    elements.append(f'  <line x1="{cx - 24}" y1="{y_bottom}" x2="{cx + 24}" y2="{y_bottom}" stroke="{stroke_cyan}" stroke-width="3" stroke-linecap="round" />')
    elements.append(f'  <line x1="{cx - 14}" y1="{y_bottom + 8}" x2="{cx + 14}" y2="{y_bottom + 8}" stroke="{stroke_cyan}" stroke-width="2" stroke-linecap="round" />')
    elements.append(f'  <line x1="{cx - 6}" y1="{y_bottom + 14}" x2="{cx + 6}" y2="{y_bottom + 14}" stroke="{stroke_cyan}" stroke-width="1.5" stroke-linecap="round" />')

    # 7. Permanent Cryptographic Attribution & Watermark Frame (Commercial Viral Engine)
    if not cleanroom:
        elements.append(f'  <!-- Cryptographic Attribution Frame -->')
        elements.append(f'  <text x="24" y="32" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="1">APPLIED CYBER-OCCULTISM // VOL. 1</text>')
        elements.append(f'  <text x="{size - 24}" y="32" text-anchor="end" fill="#06b6d4" font-family="JetBrains Mono, monospace" font-size="10">RING 0 // RUNTIME</text>')
        elements.append(f'  <text x="24" y="{size - 24}" fill="#f59e0b" font-family="JetBrains Mono, monospace" font-size="9">SHA: {process_hash[:16]}...</text>')
        elements.append(f'  <text x="{size - 24}" y="{size - 24}" text-anchor="end" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="9">SIR LEONARD DARAGAN</text>')

    if cleanroom:
        bg_elements = ''
        filter_def = ''
        g_tag = '<g>'
    else:
        bg_elements = f'''  <rect width="{size}" height="{size}" fill="#07090e" />
  <circle cx="{cx}" cy="{cy}" r="{outer_radius + 20}" fill="url(#sigilGlow)" />'''
        filter_def = '''  <defs>
    <radialGradient id="sigilGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.18" />
      <stop offset="70%" stop-color="#f59e0b" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#07090e" stop-opacity="0" />
    </radialGradient>
    <filter id="neonBlur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>'''
        g_tag = '<g filter="url(#neonBlur)">'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">
{filter_def}
{bg_elements}
  {g_tag}
{chr(10).join(elements)}
  </g>
</svg>'''


def main():
    parser = argparse.ArgumentParser(description="Austin Osman Spare (AOS) Sigil Compiler // Applied Cyber-Occultism")
    parser.add_argument("-i", "--intent", type=str, default="MY STARTING SALARY IS EIGHTY THOUSAND DOLLARS", help="Statement of intent")
    parser.add_argument("-o", "--output", type=str, default="sigil.svg", help="Output SVG path")
    parser.add_argument("--cleanroom", action="store_true", help="Export in B&W cleanroom talisman format for laser-cutting or printing")
    args = parser.parse_args()

    result = compile_statement(args.intent)
    svg_data = result["talisman_svg"] if args.cleanroom else result["svg_glyph"]
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg_data)
        
    print(f"// COMPILED INTENT: '{result['statement']}'")
    print(f"// CONSONANTS: {result['consonant_vector']} (Len: {len(result['consonant_vector'])})")
    print(f"// ABJAD CHECKSUM: {result['composite_abjad_sum']}")
    print(f"// PROCESS HASH: {result['process_hash']}")
    print(f"// WRITTEN TO: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
