import random 
from gues import TebakAngka

tebak = TebakAngka()

tebak.jawaban = random.randint(1,10)

tebak.tebakan = int(input('tebak angka 1 s.d 1p: '))

if tebak.cek():
	print("tebakan kamu benar!")
else:
	print("tebakan kamu salah!")
	'