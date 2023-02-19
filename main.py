# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

# create a PdfFileWriter object
out = PdfFileWriter()

print("\nPDF Encryption and Decryption using Python\n")
print("\n1.Encrypt PDF")
print("\n2.Decrypt PDF")
print("\n3.Exit\n")
ch = int(input("Enter Your Choice : "))



if ch == 1:
    # Open our PDF file with the PdfFileReader
    file = PdfFileReader(input("Enter the name of the pdf with extension and Path also :-"))

    # Get number of pages in original file
    num = file.numPages

    # Iterate through every page of the original
    # file and add it to our new file.
    for idx in range(num):
        
        # Get the page at index idx
        page = file.getPage(idx)
        
        # Add it to the output file
        out.addPage(page)


    # Create a variable password and store
    # our password in it.
    password = "pass"

    # Encrypt the new file with the entered password
    out.encrypt(password)

    # Open a new file "myfile_encrypted.pdf"
    with open("encrypted.pdf", "wb") as f:
        
        # Write our encrypted PDF to this file
        out.write(f)

    print("\nPDF Encrypted Successfully To Local Dir :) ")
    print("\nSaved as - encrypted.pdf\n")
    print("Project by ")
    print("-Aniket Pitre")


if ch == 2:
    # Open encrypted PDF file with the PdfFileReader
    file = PdfFileReader(input("Enter the name of the pdf with extension and Path also :-"))

    # Store correct password in a variable password.
    password = "pass"

    # Check if the opened file is actually Encrypted
    if file.isEncrypted:

        # If encrypted, decrypt it with the password
        file.decrypt(password)

        # Now, the file has been unlocked.
        # Iterate through every page of the file
        # and add it to our new file.
        for idx in range(file.numPages):
            
            # Get the page at index idx
            page = file.getPage(idx)
            
            # Add it to the output file
            out.addPage(page)
        
        # Open a new file "myfile_decrypted.pdf"
        with open("decrypted.pdf", "wb") as f:
            
            # Write our decrypted PDF to this file
            out.write(f)

        # Print success message when Done
        print("\nPDF Decrypted Successfully To Local Dir :)")
        print("\nSaved as - decrypted.pdf\n")
        print("Project by ")
        print("-Aniket Pitre")
    else:
        
        # If file is not encrypted, print the
        # message
        print("File already decrypted.")

    


if ch == 3:
    print("Exited")
    print("\nENCRYPTION and DECRYPTION of PDF using Python")
    print("\nProject by")
    print("-by Aniket Pitre")

