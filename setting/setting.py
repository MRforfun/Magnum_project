import os, sys, time, requests, json, getpass, hashlib

if sys.platform in ["linux","linux2"]:
	w = "\033[0m"
	r = "\033[31;1m"
	g = "\033[32;1m"
	y = "\033[33;1m"
	b = "\033[34;1m"
	p = "\033[35;1m"
	c = "\033[36;1m"

else:
	w = ""
	r = ""
	g = ""
	y = ""
	b = ""
	p = ""
	c = ""

def main():
	t = open("tokenshow.lst","r").read()
	e = open("emailshow.lst","r").read()
	p = open("phoneshow.lst","r").read()
	try:
		token = open("../token.lst","r").read()
	except IOError:
		print("    %s[%s!%s] you are not loggin in "%(w,y,w))
		time.sleep(3)
		print("    %s[%s!%s] login now"%(w,y,w))
		id()

	if t == "on":
		print("       ____________[%stoken%s]____________"%(g,w))
		print("      %s[%s*%s] token    : %s"%(w,g,w,token))
		next
	if t == "off":
		next

	try:
		r = requests.get("https://graph.facebook.com/me?access_token="+token)
		asw = json.loads(r.text)
		name = asw["name"]
		print("       ___________[%sprofile%s]___________"%(g,w))
		print("      %s[%s*%s] name     : %s"%(w,g,w,name))
		print("      %s[%s*%s] id       : %s"%(w,g,w,asw["id"]))
		print("      %s[%s*%s] user     : %s"%(w,g,w,asw["username"]))
		print("      %s[%s*%s] birthday : %s"%(w,g,w,asw["birthday"]))
		next
	except KeyError:
		print("     %s[%s!%s] time session expired or checkpoint"%(w,c,w))
		time.sleep(3)
		print("     %s[%s!%s] please login again"%(w,c,w))
		id()

	if e == "on":
		try:
			r = requests.get("https://graph.facebook.com/me?access_token="+token)
			aa = json.loads(r.text)
			print("      %s[%s*%s] email    : %s"%(w,g,w,aa["email"]))
			next
		except KeyError:
			pass
			next
	if e == "off":
		try:
			r = requests.get("https://graph.facebook.com/me?access_token="+token)
			aa = json.loads(r.text)
			email = aa['email']
			print("      %s[%s*%s] email    : %s"%(w,g,w,"*" * len(email)))
			next
		except KeyError:
			pass
			next

	if p == "on":
		try:
			r = requests.get("https://graph.facebook.com/me?access_token="+token)
			bb = json.loads(r.text)
			print("      %s[%s*%s] phone    : %s"%(w,g,w,bb["mobile_phone"]))
			next
		except KeyError:
			pass
			next

	if e == "off":
		try:
			r = requests.get("https://graph.facebook.com/me?access_token="+token)
			cc = json.loads(r.text)
			phone = cc["mobile_phone"]
			print("      %s[%s*%s] phone    : %s"%(w,g,w,len(phone) * "*"))
		except KeyError:
			pass
			next

	print("       _______________________________")
	print("   %s[%s1%s]%s show token ==> %s"%(g,w,g,w,t))
	print("   %s[%s2%s]%s show email ==> %s"%(g,w,g,w,e))
	print("   %s[%s3%s]%s show phone ==> %s"%(g,w,g,w,p))
	print("   %s[%s9%s]%s change account"%(g,w,g,w))
	print("   %s[%s0%s] exit setting"%(w,c,w))
	a = raw_input("     ~ magnum : ")
	if a == "":
		print("     %s[%s!%s] please input the number"%(w,r,w))
		return main()
	if a == "1":
		b = raw_input("      [on/off] > ")
		if b == "on":
			o = open("tokenshow.lst","w")
			o.write("on")
			o.close()
			return main()
		if b == "off":
			o = o = open("tokenshow.lst","w")
			o.write("off")
			o.close()
			return main()

	if a == "2":
		b = raw_input("      [on/off] > ")
		if b == "on":
			o = open("emailshow.lst","w")
			o.write("on")
			o.close()
			return main()

		if b == "off":
			o = o = open("emailshow.lst","w")
			o.write("off")
			o.close()
			return main()

	if a == "3":
		b = raw_input("      [on/off] > ")
		if b == "on":
			o = open("phoneshow.lst","w")
			o.write("on")
			o.close()
			return main()

		if b == "off":
			o = o = open("phoneshow.lst","w")
			o.write("off")
			o.close()
			return main()

	if a == "9":
		id()

def id():
	print('%s[%s*%s] login to your %sfacebook%s account'%(w,b,w,b,w))
	id = raw_input('%s[%s?%s] Phone or email : '%(w,c,w))
	pwd = getpass.getpass('%s[%s?%s] Enter the password : '%(w,c,w))
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
   	x.update(sig)

	data.update({'sig':x.hexdigest()})
	get(data)

def get(data):
	b = open('../token.lst','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print "%s[%s+%s] successful generate token"%(w,g,w)
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your email or password or maybe checkpoint'
		os.remove('token.log')
	except requests.exceptions.ConnectionError:
		print '[!] No connection internet'
		os.remove('token.lst')

try:
	main()

except KeyboardInterrupt:
	os.system("clear")
	exit()