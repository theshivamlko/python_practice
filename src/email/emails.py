import smtplib

myEmail = "sahamansinha@gmail.com"
mypassword = "RhaB123DodoN"

connect = smtplib.SMTP("smtp.gmail.com",port=25)
connect.starttls()

connect.login(user=myEmail, password=mypassword)

connect.sendmail(from_addr=myEmail, to_addrs="theshivamlko@gmail.com", msg="Hello")
connect.quit()
print("sent")
