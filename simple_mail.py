import smtplib   
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #transport layer security
server.login('sreevidyachintala16@gmail.com','anil@1234')
server.sendmail('sreevidyachintala16@gmail.com','archanaelisala@gmail.com',"hii archana how are you")
print('successfully send...!')
