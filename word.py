import PyPDF2
from tqdm import tqdm
import time

def banner():
    print("""
    ╔═══════════════════════════════════════╗
    ║        PDF Password Cracker           ║
    ║      (4-Digit PIN: 0000-999999)       ║
    ╚═══════════════════════════════════════╝
    """)

def try_password(pdf_path, password):
    """Try to decrypt PDF with given password"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if pdf_reader.is_encrypted:
                # Convert number to 4/6-digit string (e.g., 1 -> "0001")
                password_str = str(password).zfill(4)
                if pdf_reader.decrypt(password_str):
                    return True
        return False
    except:
        return False

def crack_pdf(pdf_path):
    """Try all 4-digit combinations (0000-999999)"""
    print("\n[*] Starting brute force attack...")
    print("[*] Testing all combinations from 0000 to 999999")
    
    # Try all combinations from 0000 to 9999
    for password in tqdm(range(0000,1000000), desc="Trying PINs"):
        password_str = str(password).zfill(4)
        
        if try_password(pdf_path, password):
            print(f"\n[+] Password found: {password_str}")
            
            # Save the password to a file
            with open("found_password.txt", "w") as f:
                f.write(f"PDF: {pdf_path}\nPassword: {password_str}")
            
            return password_str
    
    print("\n[-] Password not found")
    return None


def main(filepath):
    banner()
    
    # Get PDF file path
    pdf_path = filepath
       
    # Start timer
    start_time = time.time()
    
    try:
        # Try to open PDF file
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Check if PDF is encrypted
            if not pdf_reader.is_encrypted:
                print("\n[-] PDF is not password protected!")
                return
            
            # Start cracking
            password = crack_pdf(pdf_path)
            return password
            
            # Print results
            if password:
                print(f"\n[+] Success! Password has been saved to 'found_password.txt'")
            else:
                print("\n[-] Failed to find password")
            
            # Print time taken
            time_taken = time.time() - start_time
            print(f"\n[*] Time taken: {time_taken:.2f} seconds")
            
    except FileNotFoundError:
        print("\n[-] PDF file not found!")
    except Exception as e:
        print(f"\n[-] An error occurred: {str(e)}")

if __name__ == "__main__":
    main()