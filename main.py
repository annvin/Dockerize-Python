import gspread
import os
import json
credentials = {
  "type": "service_account",
  "project_id": "sheets-tutorial2-359012",
  "private_key_id": "c29118ac8322584a972904e469dc2aa1cc0bf262",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDlmHtvQ7vtmSmJ\nV6rGeNcMZyWglHTtP4u+jXpDF0BNFuG7A54LBiZqpyqTNszdT21iS/LubpfSIxtj\n70j3+/GWL5EFMDO/mDa+FdBxwjAK1NNTRO5I4jjNhGpeG0tteGkHpsRbfey7c16o\n0GbUOiFQaj7ytsOL9MXDUaHgr0JZc/98/jpv01oCJjElbfIK2x/PW7K//fA88/8u\nzEaNqMtUgv6osfbmdmt/otDK9dVD1RqoRjukvGtMSUrnSSGlhWmrVEDliA9Rvylc\nM0raoSQm1EIfj2dOWI8xvf/4Be5wLBFgsDjau/T+vG0cLowJeBQgpDFcXw4NocCo\nj/JkZUahAgMBAAECggEAJ+cOXNIK0UpzO5lu5ruNtGwgz/29LJaEtQNlok9iL4Ow\ni44fY48YEiUncxptFHF/czv75pB19mF/myi1J9QzsoRl0d8Ev2G28eZcqci0DM3c\nRHaQaz5V3PIMgnp/63Cn4FqNedEy2Yk9hF1j4bKQo6czdX9qEOLjlASV+7S59U2t\nVzVIPcMVyyz8QDW6PoX5ufZddP+N1QfMbUdu4P2oJv7z5AVxwvuRnY8QNgno05Fs\nE1AIfgSeCq8KLl5kDWCz6dVHZYvz3xrWCO+gqZkmtQo0Xm3/ON+b6J20zjvUaQjL\n+p/QVQ9UI2dpoSkk5GBmFXTrdYQ3E3++FE2GzK9EoQKBgQD963pnK9eHGxG+/H6F\nyZ0IfUOU8i8qUvnoOPrwrXAe9dLaDEd3UyF+yRBx+BJVvTpCnz+x1zSv/SmHdco1\nik75ydINIpRryckqGuRAUTvlXCawiRW/9zj8a1npriU2BLby2f+4EvDa1HCHK592\nhWESTYHZQLCnTMD++5GHX8xVLQKBgQDnef2/Jg+c0ePds9YmWWvvrLb9I2sBr8XS\nswXKYZSS6ZvlEoTjzuhl1SsqnC4CNlDFf6aSHiYM3gBSoLoowFkn2zBFxMOwOonF\nz9u0Py802mP+/GrfVKHe6wkHJCYoA/OXMIWNe22TYi55/2upMXCKZCu373TCjR7B\nIqQs2FGHxQKBgHbJaXrIfMx8smGZd4sZFXh6OVp9rejr5nNn7KUZTiF9uMU/B1Pg\nNQQ+BY57kgBARPgTzdVhqwlFst7nENDZQjcC3lw8uBhwzsX+zJb2KcITyRm/F8i1\nXBhiFC8Iw+mwbPHRYBr56WlGBtqFYtUscowAbGV5KOsrMgJXJ+6ft1SFAoGBAL48\npwtCl5A1e4VIeFZ6JVgL5TPzuMzhDb7VPIwQWE/JSEMiTi7/bEXMxLY3NyTASO+X\nsmjh+DmY9kDyMSyusFcuL+UXChC6e2IkKxde2kgguA/mmVrELmiLV5cT4Xv/i2GV\nEh2t8+ctyK6g+XVK2YgTPU7ksFv4KO9nre/hNFhVAoGAWvGhMcJ3MwInDoB2SgpQ\nMKA0Ne8k73vo3019l2/G1lOUMVbbarvUFjCPSVKxCjV9NQ2ox/AJrpI+uaczCapN\nWuFDxZR5XQi94msSZcMzKKwTV7sNVLHqv46L0uXAPWWM0E1U/bQ4o6kAzDECzf4P\nua9lDRpSMD/iQA6aP0xOzwI=\n-----END PRIVATE KEY-----\n",
  "client_email": "annvin@sheets-tutorial2-359012.iam.gserviceaccount.com",
  "client_id": "116604688392651274875",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/annvin%40sheets-tutorial2-359012.iam.gserviceaccount.com"
}
#path = r'C:\\Users\\ashvi\\Executable'
#file = 'sample.json'
#json_object = json.dumps(credentials, indent=4)
 
# Writing to sample.json
#with open(os.path.join(path, file), "w") as outfile:
    #outfile.write(json_object)

gc = gspread.service_account_from_dict(credentials)

sh = gc.open_by_key('1WNguv2p9k_V9pvgSS6fmzJqusgxAP4PXB2KFskl-HMc')
worksheet = sh.sheet1

res = worksheet.get_all_records()
print(res)
#file2 = 'output.json'
#json_object = json.dumps(res, indent=4)
#with open(os.path.join(path, file2), "w") as outfile:
    #outfile.write(json_object)
