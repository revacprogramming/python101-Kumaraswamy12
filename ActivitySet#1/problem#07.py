text = "X-DSPAM-Confidence:    0.8475"
index=text.find('0.8475')
tt=float(text[index:])
print(tt) 
#file present in py4e