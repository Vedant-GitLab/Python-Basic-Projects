import qrcode

#taking upi id as input
upi_id = input("Enter your UPI id : ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment url based on the UPI ID and the payment app
#you can modify these URLs based on the payment apps you want to support

phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#create QR codes for each payment app
phonepe_qr = qrcode.make(phonepay_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

#save the QR code to image file (optional) aur agr save nhi krna hai to isko skip kr skte ho
phonepe_qr.save("phonepe_qr.png")
google_pay_qr.save("google_pay_qr.png")
paytm_qr.save("paytm_qr.png")

#Display QR codes (you may need to install PIL/Pillow library)
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()