original_msg="Anurag Pandey"
key= 5
text_list = {
     "A" : 0,"B" : 2,"C" : 3,"D" : 4,"E" : 5,"F" : 6,"G" : 7,"H" : 8,"I" : 9,"J" : 10,"k" : 11,"L" : 12,"M" : 13,"N" : 14,"O" : 15,"P" : 16,"Q" : 17,"R" : 18,"S" : 19,"T" : 20,"U" : 21,"V" : 22,"W" : 23,"X" : 24,"Y" : 25,"Z" : 26
   }
Enc_Msg=""
for char in original_msg.upper():
  found=False
  for a in range (26):
    if char==text_list[0][a]:
      Enc=(text_list[1][a]+key)%26
      Enc_Msg=Enc_Msg+text_list[0][Enc]
      found=True
      break
  if not found:
    Enc_Msg=Enc_Msg+char
print("Encrypted message:",Enc_Msg)
   