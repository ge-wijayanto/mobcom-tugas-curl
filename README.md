# Tugas CURL - Mobile Computing

## Task
Menggunakan CURL (atau metode lain) untuk login ke sebuah website melalui terminal / command line

## Step
1. Membuat form login sederhana
2. Membuat database untuk menyimpan data akun pada MySQL
3. Mengisi database
4. Melakukan attempt untuk login melalui terminal, menggunakan 2 metode :
   - Twill (Python) : https://twill-tools.github.io/twill/
   - CURL : https://curl.se/

## Command pada Terminal
Untuk melakukan login attempt, run command berikut pada terminal :

### Twill
Source code Python dapat diakses di :  [twill-login.py](./twill-login.py)
```
py twill-login.py
```

### CURL
CURL command yang lebih lengkap dapat diakses di :  [Full CURL Command](./full-curl-command.txt)
```
curl "http://localhost:3000/auth" ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -H "Origin: http://localhost:3000" ^
  -H "Referer: http://localhost:3000/" ^
  --data-raw "username=Gregorius_Evan&password=140810190040" -L
```