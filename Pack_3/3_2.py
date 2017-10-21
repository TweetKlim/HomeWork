class int_rim(int):
    def rToI(self,s):
        R={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        c=0
        for i in range(len(s)):
            if i>0 and R[s[i]]>R[s[i-1]]:
                c+=R[s[i]]-2*R[s[i-1]]
            else:
                c+=R[s[i]]
        print (c)
        pass
    def iToR(self,s):
        I=[[1000,'M'], [900,'CM'],[500,'D'], [400,'CD'], [100,'C'],[90,'XC'], [50,'L'], [40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        c=''
        while s:
        	for r in range(0, 13):
        		if s - I[r][0] >= 0:
        			s-= I[r][0]
        			c += I[r][1]
        			break
        print(c)
        pass

a=int_rim()
s=input('Введите число ')
if s.isnumeric() and int(s) < 4000:
    a.iToR(int(s))
else:
	a.rToI(s)