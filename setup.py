import os, time

print("""
                [About]
magnum project adalah alat untuk mempermudah
facebook script ini ANTI LOGGER (aman) jika
anda merasa tidak nyaman uninstall aja :D
jangan lupa subscribe channel saya
        []	Mr4fun YT  []
jika anda ingin merevisi ini mohon cantumkan
nama saya bahwa anda tidak copyright
	""")
time.sleep(5)

print("ketik [i] untuk install atau [u] untuk uninstall")
op = raw_input("magnum@setup $ ")
if op == "i" or op == "I":
	os.system("""
pip2 install requests
pip2 install bs4
pip2 install mechanize
	""")
if op == "u" or op == "U":
	os.system("""
cd ..
rm -rf Magnum_project
""")