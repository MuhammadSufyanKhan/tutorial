import smtplib as s 
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('isabella.9782k18@gmail.com','75369514852')
subject="Hello"
body="lol"
message="subject:{}\n\n{}".format(subject,body)
listadd=['sufyane.9782k18@gmail.com','sufyane.9782k18@gmail.com']
ob.sendmail('isabella.9782k18@gmail.com',listadd)
print("send mail")
ob.quit()
