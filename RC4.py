# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:20:10 2020

@author: Enab
"""
import array as a
#KeyScheduling Algorithm. Restricting The Key to 4 bytes and S and T vectors to 8 Bytes
PlainText=a.array('i',[1,2,2,2])
CipherText=a.array('i',[])
DeText=a.array('i',[])
Key=a.array('i',[1,2,3,6])
#Generating S-Vector and T-vector. Here we consider Size of keystream-T to be 8 instead of 256. Sizes of  S-vector and T-vector are Same  
T=a.array('i',[])
j=0
i=0
while i < 8:
    while j < len(Key): 
        T.append(Key[j])
        j=j+1
        i=i+1
    j=0      
print('The KeyStream is: ',T)
S=[0,1,2,3,4,5,6,7]
#Pseudo-Random Number Generation
j=0
i=0
while i < 8:
 j=((j+S[i]+T[i]) % 8 )
 temp=S[i]
 S[i]=S[j]
 S[j]=temp
 i=i+1
print('The S vector is ',S)    
#Generating The Cipher Text Now
i=0
j=0
count=0
while i<len(PlainText):
    i=((i+1) % 8) 
    j=((j+S[i]) % 8) 
    S[i],S[j]=S[j],S[i]
    print('New S after Iteration',i,S)
    K=((S[i]+S[j]) % 8)
    x=S[K]
    CipherText.append((PlainText[count]) ^ (x))
    count+=1
print('Ciphertext = ',CipherText)
print('------------------------Now Decrypting-------------------------')
count=0
S=[0,1,2,3,4,5,6,7]
j=0
i=0
while i < 8:
 j=((j+S[i]+T[i]) % 8 )
 S[i],S[j]=S[j],S[i]
 i=i+1
print('The S vector is ',S)   
i=j=0
while i<len(PlainText):
    i=((i+1) % 8) 
    j=((j+S[i]) % 8) 
    S[i],S[j]=S[j],S[i]
    print('New S after Iteration',i,S)
    K=((S[i]+S[j]) % 8) 
    x=S[K]
    DeText.append((CipherText[count]) ^ (x))
    count+=1   
print('De',DeText)  

    