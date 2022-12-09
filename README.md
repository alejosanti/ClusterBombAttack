# ClusterBombAttack
It is a python script that performs a ClusterBombAttack. 

I did it because using Burp, in its free version, the attack takes too long, so it's a good alternative if you don't have the pro version.

At first, the code translates a raw HTTP GET request, returning a set of dictionaries as a result. After that, you choose which part of the request you want to change in every send.

Make sure the raw request format matches the placeholder:
![image](https://user-images.githubusercontent.com/50599731/206592631-754549db-5b14-4bc3-b025-eef20b6846a4.png)
- The first line must be the request line
- The second line must have the host
- The third line must have the cookies (if the request has any)
- The rest of the request should be the headers
- Don't leave blank lines before or after the request in the string
- Leave a blank space after the ":" separator in each header

In my case, I used it to do a blind SQL injection, injecting code into a cookie. 
As you can see, on each submission I change the admin password index and compare each position to a set of lowercase letters and digits. In every response, I check that  the response has the message "Welcome back", which means that the condition is met.
