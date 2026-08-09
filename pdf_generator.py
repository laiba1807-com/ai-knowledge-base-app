import os
from reportlab.pdfgen import canvas

def create_pdf(filename, title, lines):
    # Initialize the PDF document canvas
    c = canvas.Canvas(filename)
    
    # Set title formatting and draw it
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 780, title)
    
    # Set body text formatting
    c.setFont("Helvetica", 12)
    y = 740
    
    # Iterate and draw each line
    for line in lines:
        c.drawString(50, y, line)
        y -= 25
        
    c.save()

# Ensure target directories exist
os.makedirs("backend/data", exist_ok=True)
os.makedirs("eval", exist_ok=True)

# Document 1: SOC Triage Guidelines
doc1_title = "Security Operations Center Triage Guidelines"
doc1_lines = [
    "1. Alert Acknowledgment: L1 analysts must acknowledge critical alerts within 15 minutes.",
    "2. Escalation Protocol: Incidents involving suspected lateral movement must be ",
    "   escalated to L2 within 30 minutes.",
    "3. Incident Framework: All initial triage reporting must follow the standard CompTIA ",
    "   Security+ incident response life cycle terminology.",
    "4. False Positives: Repeated false positives from the same host must be documented ",
    "   in the exception tracker before tuning the rule."
]

# Document 2: Detection Engineering Setup
doc2_title = "Detection Engineering Lab Architecture"
doc2_lines = [
    "1. Microsoft Sentinel: All endpoint logs must be ingested into Microsoft Sentinel ",
    "   using the designated Log Analytics Workspace.",
    "2. Sysmon Configuration: Endpoints must deploy Sysmon with Event ID 1 ",
    "   (Process Creation) and Event ID 3 (Network Connection) enabled.",
    "3. Adversary Emulation: Atomic Red Team must be executed in a dedicated, ",
    "   isolated sandbox environment. It is never permitted in production.",
    "4. Retention Policy: Raw endpoint telemetry is retained for 90 days in ",
    "   hot storage before being archived."
]

# Document 3: IoT Cryptography Framework
doc3_title = "IoT Network Hybrid Cryptography Standards"
doc3_lines = [
    "1. Algorithm Selection: Resource-constrained IoT devices must utilize ASCON for ",
    "   lightweight authenticated encryption.",
    "2. Key Exchange: Elliptic Curve Cryptography (ECC) shall be used for secure ",
    "   key exchange protocols.",
    "3. Prohibited Architectures: A pure ECC model is strictly prohibited for all ",
    "   communication phases due to excessive computational overhead.",
    "4. Performance Goals: The hybrid ASCON-ECC framework aims to reduce device ",
    "   battery consumption by 30% compared to legacy AES deployments."
]

# Generate the PDFs in the target folder
create_pdf("backend/data/soc_triage_guidelines.pdf", doc1_title, doc1_lines)
create_pdf("backend/data/detection_engineering_lab.pdf", doc2_title, doc2_lines)
create_pdf("backend/data/iot_security_framework.pdf", doc3_title, doc3_lines)

print("Successfully generated 3 PDFs in backend/data/")
