"""
Applied Cyber-Occultism // Module 4
POSIX Servitor Deployment Manifest Generator & TTL Decay Engine (SERVITOR.EXE)
Specification: The Undefined Behavior Series, Vol. 1
Author: Sir Leonard Daragan
"""

import time
import math
import hashlib
from typing import Dict, Any, List, Optional

# Valid Enums per Module 4 Specification
HOST_SUBSTRATE_TYPES = [
    "CRYPTO_TOKEN_COLD_STORAGE",
    "HARDWARE_SECURITY_KEY",
    "ENGRAVED_METALLIC_TALISMAN",
    "AIRGAPPED_SILICON_WAFER",
    "PARCHMENT_ORGANIC_MATRIX"
]

GARBAGE_COLLECTION_MODES = [
    "PHYSICAL_STORAGE_PURGE",
    "THERMAL_DECOMPOSITION",
    "CRYPTO_SHRED_ZEROIZE"
]

TARGET_VECTORS = [
    "COGNITIVE_INGRESS_MONITORING",
    "PERIMETER_HOSTILE_MEMETIC_DEFENSE",
    "OPPORTUNITY_VECTOR_PROBABILITY_BIAS",
    "AUTONOMIC_STABILIZATION"
]

OPERATING_MODES = [
    "EVENT_DRIVEN_DORMANT",
    "CRON_SCHEDULED_BURST",
    "INTERRUPT_DRIVEN_SUBTHRESHOLD"
]

PROHIBITED_POWER_SOURCES = [
    "AUTONOMIC_SLEEP_DISTURBANCE",
    "CIRCADIAN_CORTISOL_HARVESTING",
    "UNAUTHORIZED_HEBBIAN_RECURSION"
]


def calculate_ttl_decay(half_life_days: float, initial_potency: float = 100.0, days_range: int = 60) -> Dict[str, Any]:
    """
    Computes exponential decay differential equation:
    dN/dt = -lambda * N(t)
    N(t) = N0 * exp(-lambda * t)
    where lambda = ln(2) / T_half
    """
    if half_life_days <= 0:
        raise ValueError("half_life_days must be strictly positive.")
    
    decay_lambda = math.log(2) / half_life_days
    
    curve_points = []
    for day in range(days_range + 1):
        potency = initial_potency * math.exp(-decay_lambda * day)
        curve_points.append({"day": day, "potency": round(potency, 2)})
        
    return {
        "half_life_days": half_life_days,
        "decay_lambda": round(decay_lambda, 6),
        "days_to_50_percent": round(half_life_days, 1),
        "days_to_25_percent": round(half_life_days * 2, 1),
        "days_to_10_percent": round(-math.log(0.1) / decay_lambda, 1),
        "days_to_1_percent": round(-math.log(0.01) / decay_lambda, 1),
        "curve_points": curve_points
    }


def generate_manifest(
    process_name: str,
    target_vector: str,
    host_substrate: str,
    physical_id: str,
    ttl_half_life_days: float,
    attention_minutes_daily: int = 10,
    operating_mode: str = "EVENT_DRIVEN_DORMANT",
    garbage_collection: str = "PHYSICAL_STORAGE_PURGE",
    event_listeners: Optional[List[Dict[str, str]]] = None,
    passphrase: str = "ABRAHADABRA_TERMINATE_0x7F"
) -> Dict[str, Any]:
    """
    Generates a production-grade Servitor Deployment Manifest conforming to Module 4 v1.0.
    """
    now = int(time.time())
    hard_kill_seconds = int(ttl_half_life_days * 2 * 86400) # Standard hard kill at 2 half-lives (25% potency)
    hard_kill_epoch = now + hard_kill_seconds
    decay_calc = calculate_ttl_decay(ttl_half_life_days)
    
    # Generate unique hex PID from name + creation epoch
    pid_payload = f"{process_name}:{now}:{physical_id}".encode('utf-8')
    pid_hash = hashlib.sha256(pid_payload).hexdigest()
    unique_pid = f"0x{pid_hash[:6].upper()}"
    passphrase_hash = hashlib.sha256(passphrase.encode('utf-8')).hexdigest()
    
    if not event_listeners:
        event_listeners = [
            {"trigger": "HOSTILE_MEMETIC_INTRUSION_DETECTED", "action": "EXECUTE_IMMEDIATE_0.1HZ_VAGAL_CLAMP"},
            {"trigger": "SOCIAL_MANIPULATION_PATTERN_IDENTIFIED", "action": "ALERT_OPERATOR_VIA_GASTRIC_SALIENCE_INTERRUPT"}
        ]
        
    manifest = {
        "apiVersion": "cyberoccult.daemon/v1alpha1",
        "kind": "ServitorDeploymentManifest",
        "metadata": {
            "process_name": process_name,
            "unique_pid": unique_pid,
            "author_uid": 0,
            "creation_epoch_utc": now,
            "host_substrate_type": host_substrate,
            "host_physical_id": physical_id
        },
        "lifecycle_and_ttl": {
            "ttl_half_life_days": float(ttl_half_life_days),
            "hard_kill_epoch_utc": hard_kill_epoch,
            "decay_differential_lambda": decay_calc["decay_lambda"],
            "garbage_collection_mode": garbage_collection
        },
        "execution_envelope": {
            "target_vector": target_vector,
            "operating_mode": operating_mode,
            "event_listeners": event_listeners
        },
        "resource_allocation": {
            "attention_compute_budget": f"{attention_minutes_daily}_MINUTES_DAILY_AT_0.1HZ",
            "maximum_memory_leak_threshold": "OBSESSION_SCORE_GT_3",
            "prohibited_power_sources": PROHIBITED_POWER_SOURCES
        },
        "interrupt_handlers": {
            "sigterm_graceful_shutdown": {
                "passphrase_sha256": passphrase_hash,
                "procedure": "DE_PROVISION_RITUAL_AND_TOKEN_ZEROIZATION"
            },
            "sigkill_emergency_halt": {
                "procedure": "IMMEDIATE_TRIGEMINAL_COLD_PLUNGE_AND_TOKEN_DESTRUCTION"
            }
        }
    }
    
    yaml_str = manifest_to_yaml(manifest)
    systemd_str = generate_systemd_unit(process_name, unique_pid, hard_kill_epoch)
    
    return {
        "manifest": manifest,
        "yaml_content": yaml_str,
        "systemd_unit": systemd_str,
        "ttl_decay": decay_calc
    }


def manifest_to_yaml(manifest: Dict[str, Any]) -> str:
    """Formats manifest into YAML per Module 4 specifications."""
    m = manifest["metadata"]
    l = manifest["lifecycle_and_ttl"]
    e = manifest["execution_envelope"]
    r = manifest["resource_allocation"]
    i = manifest["interrupt_handlers"]
    
    listeners_yaml = ""
    for el in e["event_listeners"]:
        listeners_yaml += f"""      - trigger: "{el['trigger']}"
        action: "{el['action']}"\n"""

    power_sources_yaml = ""
    for ps in r["prohibited_power_sources"]:
        power_sources_yaml += f"""      - "{ps}"\n"""

    yaml_text = f"""# ==============================================================================
# SERVITOR PRODUCTION DEPLOYMENT MANIFEST (V1.0)
# CANONICAL SCHEMA: cyberoccult.daemon/v1alpha1
# BOOK REFERENCE: APPLIED CYBER-OCCULTISM // MODULE 4 (SCHEMATIC 5)
# ==============================================================================
apiVersion: {manifest['apiVersion']}
kind: {manifest['kind']}

daemon_manifest:
  metadata:
    process_name: "{m['process_name']}"
    unique_pid: "{m['unique_pid']}"
    author_uid: {m['author_uid']}  # Sovereign Operator UID
    creation_epoch_utc: {m['creation_epoch_utc']}
    host_substrate_type: "{m['host_substrate_type']}"
    host_physical_id: "{m['host_physical_id']}"

  lifecycle_and_ttl:
    ttl_half_life_days: {l['ttl_half_life_days']}
    hard_kill_epoch_utc: {l['hard_kill_epoch_utc']} # Exactly {int(l['ttl_half_life_days'] * 2)} days post-provisioning
    decay_differential_lambda: {l['decay_differential_lambda']}
    garbage_collection_mode: "{l['garbage_collection_mode']}"

  execution_envelope:
    target_vector: "{e['target_vector']}"
    operating_mode: "{e['operating_mode']}"
    event_listeners:
{listeners_yaml}
  resource_allocation:
    attention_compute_budget: "{r['attention_compute_budget']}"
    maximum_memory_leak_threshold: "{r['maximum_memory_leak_threshold']}"
    prohibited_power_sources:
{power_sources_yaml}
  interrupt_handlers:
    sigterm_graceful_shutdown:
      passphrase_sha256: "{i['sigterm_graceful_shutdown']['passphrase_sha256']}"
      procedure: "{i['sigterm_graceful_shutdown']['procedure']}"
    sigkill_emergency_halt:
      procedure: "{i['sigkill_emergency_halt']['procedure']}"
"""
    return yaml_text


def generate_systemd_unit(process_name: str, pid: str, kill_epoch: int) -> str:
    """Generates standard POSIX systemd unit file for the background thoughtform daemon."""
    return f"""# /etc/systemd/system/{process_name}.service
# Managed by Applied Cyber-Occultism Daemonizer Runtime
# Process PID: {pid} // Hard-Kill Epoch: {kill_epoch}

[Unit]
Description=Autonomous Thoughtform Daemon ({process_name})
Documentation=https://sirleonarddaragan.github.io/applied-cyber-occultism/
After=network.target

[Service]
Type=simple
User=sovereign
Environment=THOUGHTFORM_PID={pid}
Environment=HARD_KILL_EPOCH={kill_epoch}
ExecStart=/usr/local/bin/servitor_daemon --name {process_name} --anchor-check
Restart=on-failure
RestartSec=5s
KillSignal=SIGKILL
TimeoutStopSec=10s

[Install]
WantedBy=multi-user.target
"""


if __name__ == "__main__":
    res = generate_manifest(
        process_name="daem_vulcan_sentinel_04",
        target_vector="COGNITIVE_INGRESS_MONITORING",
        host_substrate="CRYPTO_TOKEN_COLD_STORAGE",
        physical_id="YUBIKEY_SERIAL_941208",
        ttl_half_life_days=14.0
    )
    print("=== SERVITOR MANIFEST TEST ===")
    print(f"Generated PID: {res['manifest']['metadata']['unique_pid']}")
    print(f"Decay Lambda: {res['ttl_decay']['decay_lambda']}")
    print(f"Days to 10% Potency: {res['ttl_decay']['days_to_10_percent']} days")
    print("\n--- YAML OUTPUT ---\n")
    print(res['yaml_content'])
