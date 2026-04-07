import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

# --- CONFIGURATION ---
SENDER_EMAIL = "coder0214h@gmail.com"
SENDER_PASSWORD =  "howr mmem euqy lhlb" 
SUBJECT = "Your Copy of The Cracked Dev Playbook"
PDF_FILE = "The Cracked Dev Playbook.pdf"
IMAGE_FILE = "cover.png"

# Manual Email List [cite: 10, 191]
recipients = [

    "yusufakinola69@gmail.com", "alikesuccesszeno@gmail.com", "joshuaejiformah@gmail.com"
]

def send_launch_emails():
    try:
        # Step 1: Establish Secure Connection (The Operator's Move) [cite: 144, 150]
        # Using Port 465 for SSL to avoid 'Operation Timed Out' on MacOS
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Step 2: Load the 'Frontend' and 'Value' assets [cite: 56, 110]
        with open("template.html", "r", encoding="utf-8") as f:
            html_body = f.read()
        
        with open(PDF_FILE, "rb") as f:
            pdf_data = f.read()

        with open(IMAGE_FILE, "rb") as f:
            img_data = f.read()

        # Step 3: Iterate and Deliver
        for email in recipients:
            msg = MIMEMultipart("related")
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg['Subject'] = SUBJECT

            # Attach HTML Content
            msg_alt = MIMEMultipart("alternative")
            msg.attach(msg_alt)
            msg_alt.attach(MIMEText(html_body, "html"))

            # Embed Cover Image (cid:cover_image matches template.html) [cite: 58, 60]
            msg_image = MIMEImage(img_data)
            msg_image.add_header('Content-ID', '<cover_image>')
            msg.attach(msg_image)

            # Attach the actual PDF [cite: 191, 203]
            msg_pdf = MIMEApplication(pdf_data, _subtype="pdf")
            msg_pdf.add_header('Content-Disposition', 'attachment', filename=PDF_FILE)
            msg.attach(msg_pdf)

            server.send_message(msg)
            print(f"🚀 Delivered to: {email}")

        server.quit()
        print("\n✅ All Playbooks delivered. The industry is open.")

    except Exception as e:
        print(f"⚠️ Infrastructure failure: {e}")

if __name__ == "__main__":
    send_launch_emails()