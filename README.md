# HTTP APIs for Account and Password Management


## 執行 container 方式
### 取得 docker image
```
docker pull tszching/restapi_image:230620
```

啟動 container
```
docker run -d --name account_and_management -p 8000:8000 tszching/restapi_image:230620
```

## api 使用方法
啟動 conatiner 後也可到 http://127.0.0.1:8000/docs#/ 查看 api 文件
### API 1: Create Account
[POST] /api/account/register - 註冊帳號

帳號長度要求 3-32 碼  
密碼長度要求 8-32 碼，至少包含 1 個數字、1 個小寫英文字母及 1 個大寫英文字母  

#### Request body
```
{
  "username": "string",
  "password": "string"
}
```

#### Curl 語法
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/account/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "string",
  "password": "string"
}'
```

#### 註冊成功
回傳 Response 200  
Response body:
```
{
  "success": true
}
```
#### 註冊失敗
Response 403  
Response body:
```
{
  "success": "false",
  "reason": "Username already exists."
}
```

### API 2: Verify Account and Password
[POST] /api/account/verify - 註冊帳號

#### Request body
```
{
  "username": "string",
  "password": "string"
}
```

#### Curl 語法
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/account/verify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "string",
  "password": "string"
}'
```

#### 驗證成功
回傳 Response 200  
Response body:
```
{
  "success": true
}
```

#### 驗證失敗 
Response 400  
Response body:
```
{
  "success": "false",
  "reason": "Incorrect username or password."
}
```
