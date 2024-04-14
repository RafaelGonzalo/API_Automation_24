---
Title: cURL task 03/03/2024
author: "Rafael G. Alfaro Martinez"
date: 04/03/2024
---
# cURL task 03/03/2024
The task was performed using the site "https://clickup.com/"
The CRUD task was carried out using cURL as a tool, at the bottom there are both the commands and their outputs.

> Site: [app.clickup.com](https://app.clickup.com/login)

> API Documentation: https://clickup.com/api/

### Create
```shell
curl --location 'https://api.clickup.com/api/v2/space/90030958577/folder' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' --data '{"name": "New Folder From API Test"}' -v | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 54.66.203.97:443...
* Connected to api.clickup.com (54.66.203.97) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
* h2h3 [:method: POST]
* h2h3 [:path: /api/v2/space/90030958577/folder]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]
* h2h3 [content-length: 36]
* Using Stream ID: 1 (easy handle 0x556168188c80)
} [5 bytes data]
> POST /api/v2/space/90030958577/folder HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT
> content-length: 36
>
{ [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
100    36    0     0  100    36      0     11  0:00:03  0:00:03 --:--:--    11< HTTP/2 200
< date: Sun, 03 Mar 2024 16:43:35 GMT
< content-type: application/json; charset=utf-8
< content-length: 258
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 7202655012559454898
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709484276
< timing-allow-origin: *
<
{ [258 bytes data]
100   294  100   258  100    36     74     10  0:00:03  0:00:03 --:--:--    85
* Connection #0 to host api.clickup.com left intact
{
  "id": "90032315831",
  "name": "New Folder From API Test",
  "orderindex": 2,
  "override_statuses": false,
  "hidden": false,
  "space": {
    "id": "90030958577",
    "name": "Test API",
    "access": true
  },
  "task_count": "0",
  "archived": false,
  "statuses": [],
  "lists": [],
  "permission_level": "create"
}
```
### Read
```shell

curl -X GET "https://api.clickup.com/api/v2/folder/90032315831" --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' -v | jq    
Note: Unnecessary use of -X or --request, GET is already inferred.                                                                                                                            
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current                                                                                                               
                                 Dload  Upload   Total   Spent    Left  Speed                                                                                                                 
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 54.66.203.97:443...                                                                                  
* Connected to api.clickup.com (54.66.203.97) port 443 (#0)                                                                                                                                   
* ALPN: offers h2,http/1.1                                                                                                                                                                    
} [5 bytes data]                                                                                                                                                                              
* TLSv1.3 (OUT), TLS handshake, Client hello (1):                                                                                                                                             
} [512 bytes data]                                                                                                                                                                            
*  CAfile: /etc/ssl/certs/ca-certificates.crt                                                                                                                                                 
*  CApath: /etc/ssl/certs                                                                                                                                                                     
{ [5 bytes data]                                                                                                                                                                              
* TLSv1.3 (IN), TLS handshake, Server hello (2):                                                                                                                                              
{ [104 bytes data]                                                                                                                                                                            
* TLSv1.2 (IN), TLS handshake, Certificate (11):                                                                                                                                              
{ [4943 bytes data]                                                                                                                                                                           
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):                                                                                                                                      
{ [333 bytes data]                                                                                                                                                                            
* TLSv1.2 (IN), TLS handshake, Server finished (14):                                                                                                                                          
{ [4 bytes data]                                                                                                                                                                              
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):                                                                                                                                     
} [70 bytes data]                                                                                                                                                                             
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):                                                                                                                                   
} [1 bytes data]                                                                                                                                                                              
* TLSv1.2 (OUT), TLS handshake, Finished (20):                                                                                                                                                
} [16 bytes data]                                                                                                                                                                             
* TLSv1.2 (IN), TLS handshake, Finished (20):                                                                                                                                                 
{ [16 bytes data]                                                                                                                                                                             
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256                                                                                                                                  
* ALPN: server accepted h2                                                                                                                                                                    
* Server certificate:                                                                                                                                                                         
*  subject: CN=*.clickup.com                                                                                                                                                                  
*  start date: Dec  2 00:00:00 2023 GMT                                                                                                                                                       
*  expire date: Dec 30 23:59:59 2024 GMT                                                                                                                                                      
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"                                                                                                                      
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02                                                                                                                                             
*  SSL certificate verify ok.                                                                                                                                                                 
} [5 bytes data]                                                                                                                                                                              
* using HTTP/2                                                                                                                                                                                
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* h2h3 [:method: GET]                                                                                           
* h2h3 [:path: /api/v2/folder/90032315831]                                                                                                                                                    
* h2h3 [:scheme: https]                                                                                                                                                                       
* h2h3 [:authority: api.clickup.com]                                                                                                                                                          
* h2h3 [user-agent: curl/7.88.1]                                                                                                                                                              
* h2h3 [accept: */*]                                                                                                                                                                          
* h2h3 [content-type: application/json]                                                                                                                                                       
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]                                                                                                                           
* Using Stream ID: 1 (easy handle 0x55ae7c0bcc80)                                                                                                                                             
} [5 bytes data]                                                                                                                                                                              
> GET /api/v2/folder/90032315831 HTTP/2                                                                                                                                                       
> Host: api.clickup.com                                                                                                                                                                       
> user-agent: curl/7.88.1                                                                                                                                                                     
> accept: */*                                                                                                                                                                                 
> content-type: application/json                                                                                                                                                              
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT                                                                                                                                  
>                                                                                                                                                                                             
{ [5 bytes data]                                                                                                                                                                              
< HTTP/2 200                                                                                                                                                                                  
< date: Sun, 03 Mar 2024 22:53:47 GMT                                                                                                                                                         
< content-type: application/json; charset=utf-8                                                                                                                                               
< content-length: 456                                                                                                                                                                         
< server: nginx                                                                                                                                                                               
< x-dns-prefetch-control: off                                                                                                                                                                 
< expect-ct: max-age=0                                                                                                                                                                        
< strict-transport-security: max-age=31536000; includeSubDomains                                                                                                                              
< x-download-options: noopen                                                                                                                                                                  
< x-content-type-options: nosniff                                                                                                                                                             
< x-permitted-cross-domain-policies: none                                                                                                                                                     
< x-xss-protection: 0                                                                                                                                                                         
< access-control-allow-origin: *                                                                                                                                                              
< access-control-allow-credentials: true                                                                                                                                                      
< content-language: en-US                                                                                                                                                                     
< x-datadog-trace-id: 732658349290152657                                                                                                                                                      
< content-security-policy: frame-ancestors 'self'                                                                                                                                             
< cache-control: no-cache                                                                                                                                                                     
< cache-control: no-store                                                                                                                                                                     
< pragma: no-cache                                                                                                                                                                            
< expires: 0                                                                                                                                                                                  
< x-ratelimit-limit: 100                                                                                                                                                                      
< x-ratelimit-remaining: 99                                                                                                                                                                   
< x-ratelimit-reset: 1709506488                                                                                                                                                               
< timing-allow-origin: *                                                                                                                                                                      
<                                                                                                                                                                                             
{ [456 bytes data]                                                                                                                                                                            
100   456  100   456    0     0    138      0  0:00:03  0:00:03 --:--:--   138                                                                                                                
* Connection #0 to host api.clickup.com left intact                                                                                                                                           
{                                                                                                                                                                                             
  "id": "90032315831",                                                                                                                                                                        
  "name": "Updated Folder Name API Test",                                                                                                                                                     
  "orderindex": 0,                                                                                                                                                                            
  "override_statuses": false,                                                                                                                                                                 
  "hidden": false,                                                                                                                                                                            
  "space": {                                                                                                                                                                                  
    "id": "90030958577",                                                                                                                                                                      
    "name": "Test API",                                                                                                                                                                       
    "access": true                                                                                                                                                                            
  },                                                                                                                                                                                          
  "task_count": "0",                                                                                                                                                                          
  "archived": false,                                                                                                                                                                          
  "statuses": [                                                                                                                                                                               
    {                                                                                                                                                                                         
      "id": "p90030958577_oYagnw5E",                                                                                                                                                          
      "status": "to do",                                                                                                                                                                      
      "orderindex": 0,                                                                                                                                                                        
      "color": "#87909e",                                                                                                                                                                     
      "type": "open"                                                                                                                                                                          
    },                                                                                                                                                                                        
    {                                                                                                                                                                                         
      "id": "p90030958577_XVx98ya4",                                                                                                                                                          
      "status": "complete",                                                                                                                                                                   
      "orderindex": 1,                                                                                                                                                                        
      "color": "#008844",                                                                                                                                                                     
      "type": "closed"                                                                                                                                                                        
    }                                                                                                                                                                                         
  ],                                                                                                                                                                                          
  "lists": [],                                                                                                                                                                                
  "permission_level": "create"                                                                                                                                                                
}                                                                                                                                                                                             
                                                                                                                                                                                               
```
### Update
```shell
 curl --request PUT 'https://api.clickup.com/api/v2/folder/90032315831' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT'  --data '{ "name": "Updated Folder Name API Test"}' -v | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 54.66.203.97:443...
* Connected to api.clickup.com (54.66.203.97) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
* h2h3 [:method: PUT]
* h2h3 [:path: /api/v2/folder/90032315831]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]
* h2h3 [content-length: 41]
* Using Stream ID: 1 (easy handle 0x55766f253c80)
} [5 bytes data]
> PUT /api/v2/folder/90032315831 HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT
> content-length: 41
>
{ [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 200
< date: Sun, 03 Mar 2024 17:15:58 GMT
< content-type: application/json; charset=utf-8
< content-length: 262
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 5677381271353638075
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709486219
< timing-allow-origin: *
<
{ [262 bytes data]
100   303  100   262  100    41     96     15  0:00:02  0:00:02 --:--:--   111
* Connection #0 to host api.clickup.com left intact
{
  "id": "90032315831",
  "name": "Updated Folder Name API Test",
  "orderindex": 2,
  "override_statuses": false,
  "hidden": false,
  "space": {
    "id": "90030958577",
    "name": "Test API",
    "access": true
  },
  "task_count": "0",
  "archived": false,
  "statuses": [],
  "lists": [],
  "permission_level": "create"
}
```
### Delete
```shell
curl --request DELETE 'https://api.clickup.com/api/v2/folder/90032315831' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' -v | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 54.79.75.211:443...
* Connected to api.clickup.com (54.79.75.211) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
* h2h3 [:method: DELETE]
* h2h3 [:path: /api/v2/folder/90032315831]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]
* Using Stream ID: 1 (easy handle 0x563176988c80)
} [5 bytes data]
> DELETE /api/v2/folder/90032315831 HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT
>
{ [5 bytes data]
< HTTP/2 200
< date: Sun, 03 Mar 2024 17:21:20 GMT
< content-type: application/json; charset=utf-8
< content-length: 2
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 5853346938563891142
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709486540
< timing-allow-origin: *
<
{ [2 bytes data]
100     2    0     2    0     0      0      0 --:--:--  0:00:03 --:--:--     0
* Connection #0 to host api.clickup.com left intact
{}
```
## Negative cases
### Folder ID invalid
```shell
curl --request DELETE 'https://api.clickup.com/api/v2/folder/no_folder' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' -v |
jq                                                                                                                                                                                           
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 54.79.75.211:443...
* Connected to api.clickup.com (54.79.75.211) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* h2h3 [:method: DELETE]
* h2h3 [:path: /api/v2/folder/no_folder]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]
* Using Stream ID: 1 (easy handle 0x55d2711a7c80)
} [5 bytes data]
> DELETE /api/v2/folder/no_folder HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT
>
{ [5 bytes data]
< HTTP/2 400
< date: Sun, 03 Mar 2024 22:51:09 GMT
< content-type: application/json; charset=utf-8
< content-length: 47
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 7262958199916461608
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< timing-allow-origin: *
<
{ [47 bytes data]
100    47  100    47    0     0     16      0  0:00:02  0:00:02 --:--:--    16
* Connection #0 to host api.clickup.com left intact
{
  "err": "Folder ID invalid",
  "ECODE": "INPUT_011"
}
                                  
```
### Token invalid
```shell
 curl --location 'https://api.clickup.com/api/v2/space/90030958577/folder' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3T' -v | jq      
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 54.79.75.211:443...
* Connected to api.clickup.com (54.79.75.211) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* h2h3 [:method: GET]
* h2h3 [:path: /api/v2/space/90030958577/folder]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3T]
* Using Stream ID: 1 (easy handle 0x556147e29c80)
} [5 bytes data]
> GET /api/v2/space/90030958577/folder HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3T
>
{ [5 bytes data]
< HTTP/2 401
< date: Sun, 03 Mar 2024 22:52:04 GMT
< content-type: application/json; charset=utf-8
< content-length: 43
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 7022116553005499719
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< timing-allow-origin: *
<
{ [43 bytes data]
100    43  100    43    0     0     15      0  0:00:02  0:00:02 --:--:--    15
* Connection #0 to host api.clickup.com left intact
{
  "err": "Token invalid",
  "ECODE": "OAUTH_025"
}

```
### Route not found
```shell
}
❯ curl --location 'https://api.clickup.com/api/v2/space/90030958577/folder_no_valid' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' -v | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0*   Trying 3.105.185.43:443...
* Connected to api.clickup.com (3.105.185.43) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
* h2h3 [:method: GET]
* h2h3 [:path: /api/v2/space/90030958577/folder_no_valid]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.clickup.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* h2h3 [content-type: application/json]
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]
* Using Stream ID: 1 (easy handle 0x564c16919c80)
} [5 bytes data]
> GET /api/v2/space/90030958577/folder_no_valid HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.88.1
> accept: */*
> content-type: application/json
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT
>
{ [5 bytes data]
< HTTP/2 404
< date: Sun, 03 Mar 2024 17:48:20 GMT
< content-type: application/json; charset=utf-8
< content-length: 43
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 8914723640069692891
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709488161
< timing-allow-origin: *
<
{ [43 bytes data]
100    43  100    43    0     0     14      0  0:00:03  0:00:02  0:00:01    14
* Connection #0 to host api.clickup.com left intact
{
  "err": "Route not found",
  "ECODE": "APP_001"
}
```
### Create a folder without data
```shell
❯ curl -X POST 'https://api.clickup.com/api/v2/space/90030958577/folder' --header 'Content-Type: application/json' --header 'Authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT' -v | 
jq                                                                                                                                                                                            
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current                                                                                                               
                                 Dload  Upload   Total   Spent    Left  Speed                                                                                                                 
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 54.66.203.97:443...                                                                                  
* Connected to api.clickup.com (54.66.203.97) port 443 (#0)                                                                                                                                   
* ALPN: offers h2,http/1.1                                                                                                                                                                    
} [5 bytes data]                                                                                                                                                                              
* TLSv1.3 (OUT), TLS handshake, Client hello (1):                                                                                                                                             
} [512 bytes data]                                                                                                                                                                            
*  CAfile: /etc/ssl/certs/ca-certificates.crt                                                                                                                                                 
*  CApath: /etc/ssl/certs                                                                                                                                                                     
{ [5 bytes data]                                                                                                                                                                              
* TLSv1.3 (IN), TLS handshake, Server hello (2):                                                                                                                                              
{ [104 bytes data]                                                                                                                                                                            
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):                                                                
{ [4943 bytes data]                                                                                                                                                                           
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):                                                                                                                                      
{ [333 bytes data]                                                                                                                                                                            
* TLSv1.2 (IN), TLS handshake, Server finished (14):                                                                                                                                          
{ [4 bytes data]                                                                                                                                                                              
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):                                                                                                                                     
} [70 bytes data]                                                                                                                                                                             
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):                                                                                                                                   
} [1 bytes data]                                                                                                                                                                              
* TLSv1.2 (OUT), TLS handshake, Finished (20):                                                                                                                                                
} [16 bytes data]                                                                                                                                                                             
* TLSv1.2 (IN), TLS handshake, Finished (20):                                                                                                                                                 
{ [16 bytes data]                                                                                                                                                                             
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256                                                                                                                                  
* ALPN: server accepted h2                                                                                                                                                                    
* Server certificate:                                                                                                                                                                         
*  subject: CN=*.clickup.com                                                                                                                                                                  
*  start date: Dec  2 00:00:00 2023 GMT                                                                                                                                                       
*  expire date: Dec 30 23:59:59 2024 GMT                                                                                                                                                      
*  subjectAltName: host "api.clickup.com" matched cert's "*.clickup.com"                                                                                                                      
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02                                                                                                                                             
*  SSL certificate verify ok.                                                                                                                                                                 
} [5 bytes data]                                                                                                                                                                              
* using HTTP/2                                                                                                                                                                                
* h2h3 [:method: POST]                                                                                                                                                                        
* h2h3 [:path: /api/v2/space/90030958577/folder]                                                                                                                                              
* h2h3 [:scheme: https]                                                                                                                                                                       
* h2h3 [:authority: api.clickup.com]                                                                                                                                                          
* h2h3 [user-agent: curl/7.88.1]                                                                                                                                                              
* h2h3 [accept: */*]                                                                                                                                                                          
* h2h3 [content-type: application/json]                                                                                                                                                       
* h2h3 [authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT]                                                                                                                           
* Using Stream ID: 1 (easy handle 0x55f650867c80)                                                                                                                                             
} [5 bytes data]                                                                                                                                                                              
> POST /api/v2/space/90030958577/folder HTTP/2                                                                                                                                                
> Host: api.clickup.com                                                                                                                                                                       
> user-agent: curl/7.88.1                                                                                                                                                                     
> accept: */*                                                                                                                                                                                 
> content-type: application/json                                                                                                                                                              
> authorization: pk_3162662_1M9YD0VNY5Q7MP33XYV3EKEDXAC0MCFT                                                                                                                                  
>                                                                                                                                                                                             
{ [5 bytes data]                                                                                                                                                                              
< HTTP/2 400                                                                                                                                                                                  
< date: Sun, 03 Mar 2024 17:51:33 GMT                                                                                                                                                         
< content-type: application/json; charset=utf-8                                                                                                                                               
< content-length: 48                                                                                                                                                                          
< server: nginx                                                                                                                                                                               
< x-dns-prefetch-control: off                                                                                                                                                                 
< expect-ct: max-age=0                                                                                                                                                                        
< strict-transport-security: max-age=31536000; includeSubDomains                                                                                                                              
< x-download-options: noopen                                                                                                                                                                  
< x-content-type-options: nosniff                                                                                                                                                             
< x-permitted-cross-domain-policies: none                                                                                                                                                     
< x-xss-protection: 0                                                                                                                                                                         
< access-control-allow-origin: *                                                                                                                                                              
< access-control-allow-credentials: true                                                                                                                                                      
< content-language: en-US                                                                                                                                                                     
< x-datadog-trace-id: 1309136792950823393                                                                                                                                                     
< content-security-policy: frame-ancestors 'self'                                                                                                                                             
< cache-control: no-cache                                                                                                                                                                     
< cache-control: no-store                                                                                                                                                                     
< pragma: no-cache                                                                                                                                                                            
< expires: 0                                                                                                                                                                                  
< x-ratelimit-limit: 100                                                                                                                                                                      
< x-ratelimit-remaining: 99                                                                                                                                                                   
< x-ratelimit-reset: 1709488354                                                                                                                                                               
< timing-allow-origin: *                                                                                                                                                                      
<                                                                                                                                                                                             
{ [48 bytes data]                                                                                                                                                                             
100    48  100    48    0     0     17      0  0:00:02  0:00:02 --:--:--    17                                                                                                                
* Connection #0 to host api.clickup.com left intact                                                                                                                                           
{                                                                                                                                                                                             
  "err": "Project name invalid",                                                                                                                                                              
  "ECODE": "CAT_021"                                                                                                                                                                          
}                                                                                                                                                                                              
```