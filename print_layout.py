#Toto jsem napsal po nekolika nocich, kdy jsem skoro nespal
#Uprimne, takhle hnusny kod jsem dlouho nenapsal
#Pozor, muze zpusobovat paleni oci, nevolnosti

#Pouzil jsem velmi enefektivne seznam, kde bych moh mit cislo...

#K certu s blbou knihou keya
#si to sazejte sami


#pocet stranek
pages = 56

if(pages%4):
	raise(Exception("stranky musi byt delitelne ctyrmi"))

major_pages=pages//4

p_beg = 1
p_end = pages


left=p_beg
right=p_end//2 + 1

print("rozdeleni do leve a prave casti: ")
print(left)
print(right)

print("poradi stranek")

def quadruple(left, right):
	A= left
	left +=1

	B = right
	right+=1

	C= right
	right+=1

	D = left
	left+=1

	print("{}, {}, {}, {}, ".format(A, B, C, D), end="")
	return(left, right)



for i in range(major_pages):
	left, right = quadruple(left,right)


print()