import  requests
import smtplib
import time
import os

URL = 'https://api.quotable.io/quotes/random'

response = requests.get(URL)

data_content = response.json()[0]['content']
data_author = response.json()[0]['author']
print(data_content)
print(data_author)


while True:
    my_email = 'jaimevillalbaoyola@gmail.com'
    password = os.environ.get('PASSWORD_EMAIL')
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls() #make the conection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email, 
                            msg=f"Subject:Motivacional Quote\n\n{data_content}\n{data_author}"
                            )    
    time.sleep(3600) #send every day