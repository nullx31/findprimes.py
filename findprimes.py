#!/usr/bin/env python
# Schnellerer Primzahlensucher
# unter Verwendung des "Sieb des Eratosthenes"
# or just use http://www.wolframalpha.com/input/?i=factor%2815%29&dataset=&asynchronous=false&equal=Submit
# @pirate_security

import math

n = 2065107859

def eratosthenesSieb(n):
	sieb = [True] * n # Erstelle eine Liste und markiere alle Zahlen als True
	sieb[0] = sieb[1] = False # Null und Eins sind kein Primzahlen.

	# Den Sieb bauen.
	for i in range(2, int(math.sqrt(n)) + 1): # Für Zahlen zwischen 2 und sqrt(n)
		pointer = i * 2 # Multipliziere die Zahl mit 2
		while pointer < n: # Wenn das Ergebnis kleiner als n ist 
			sieb[pointer] = False # Markiere den Pointer als False
			pointer += i # Addiere 1 zur Zahl und beginne von vorne.

	# Teste die Primzahlen auf restlose Teilbarkeit mit n
	primes = []
	for i in range(n):
		if sieb[i] == True:
			print (i)
			if sieb[i] == True and n%i == 0:
				print ("p: %r\nq: %r" %(i,int(n/i)))
				break

eratosthenesSieb(n)
