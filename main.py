import qrcode
import cv2
from pyzbar.pyzbar import decode


def register():
    name = input("Enter Name: ")
    section = input("Enter Section: ")
    return name, section

def generate_qr(name, section):
    data = f"Name: {name}\nSection: {section}"
    qr = qrcode.make(data)
    qr.save(f"{name}_{section}.png")
    print(f"QR Code generated for {name} in section {section}.")

def scan_qr():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for code in decode(frame):
            student_id = code.data.decode('utf-8')
            print("Scanned ID:", student_id)
            cap.release()
            cv2.destroyAllWindows()
            return student_id

        cv2.imshow("Scan QR Code - Press 'q' to quit", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

if __name__ == '__main__':
    choice = input("[1] Register\n[2] Scan Qr Code\nEnter: ")
    if choice == "1":
        name, section = register()
        generate_qr(name, section)
    else:
        scan_qr()