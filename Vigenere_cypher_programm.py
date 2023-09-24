# first_question=input("Do you want encrypt or decrypt message ?(encrypt/decrypt)")
# if first_question=="encrypt":
#     key_name=str(input("Enter the Key name: "))
#     messagecode = str(input("Enter the decrypted message: "))
#     alphabet=("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
#     key_name1=""
#     messagecode1=""
#     result=""
#     result1=""
#     for i in range(0,len(key_name)) :
#         d=alphabet.find(key_name[i])
#         key_name1=(key_name1+alphabet[d])
#     key_name1=key_name1*25
#     key_name1=key_name1[:25]
#     for s in range(0,len(messagecode)):
#         q=alphabet.find(messagecode[s])
#         messagecode1=(messagecode1+alphabet[q])


#     def cut(a, b):                 
#         if len(a) > len(b):     
#             result = ""
#             a = a[:len(b)]
#             result = a 
#             return result  

#     result = cut(key_name1, messagecode1)

#     def addvarriables(e,f):
#         result1=""
#         for i in range(min(len(e), len(f))):
#             m=alphabet.find(e[i])
#             n=alphabet.find(f[i])
#             o=alphabet[(m+n+1)%25]
#             result1+=o
#         return result1
#     alphabet=("abcdefghijklmnopqrstuvwxyz")
#     result1 = addvarriables(key_name1, messagecode1)
#     print(result1)
# elif first_question=="decrypt":
    
#     key_name=str(input("Enter the Key name: "))
#     decryptmessage = str(input("Enter the decrypted message: "))
#     alphabet=("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
#     key_name1=""
#     decryptmessage1=""
#     o=""
#     result=""
#     result1=""
#     for i in range(0,len(key_name)) :
#         d=alphabet.find(key_name[i])
#         key_name1=(key_name1+alphabet[d])
#     key_name1=key_name1*25
#     key_name1=key_name1[:25]
#     for s in range(0,len(decryptmessage)):
#         q=alphabet.find(decryptmessage[s])
#         decryptmessage1=(decryptmessage1+alphabet[q])


#     def cut(a, b):                 
#         if len(a) > len(b):     
#             result = ""
#             a = a[:len(b)]
#             result = a 
#             return result  

#     result = cut(key_name1, decryptmessage1)

#     def addvarriables(e,f):
#         result1=""
#         for i in range(min(len(e), len(f))):
#             m=alphabet.find(e[i])
#             n=alphabet.find(f[i])
#             o=alphabet[(n-m-1)%25]
#             result1+=o
#         return result1
#     alphabet=("abcdefghijklmnopqrstuvwxyz")
#     result1 = addvarriables(key_name1, decryptmessage1)
#     print(result1)
# else:
#     print('Error')
    


while True:
    first_question=input("Do you want encrypt or decrypt message ?(encrypt/decrypt)")
    if first_question=="encrypt":
        key_name=str(input("Enter the Key name: "))
        messagecode = str(input("Enter the decrypted message: "))
        alphabet=("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        key_name1=""
        messagecode1=""
        result=""
        result1=""
        for i in range(0,len(key_name)) :
            d=alphabet.find(key_name[i])
            key_name1=(key_name1+alphabet[d])
        key_name1=key_name1*25
        key_name1=key_name1[:25]
        for s in range(0,len(messagecode)):
            q=alphabet.find(messagecode[s])
            messagecode1=(messagecode1+alphabet[q])


        def cut(a, b):                 
            if len(a) > len(b):     
                result = ""
                a = a[:len(b)]
                result = a 
                return result  

        result = cut(key_name1, messagecode1)

        def addvarriables(e,f):
            result1=""
            for i in range(min(len(e), len(f))):
                m=alphabet.find(e[i])
                n=alphabet.find(f[i])
                o=alphabet[(m+n+1)%25]
                result1+=o
            return result1
        alphabet=("abcdefghijklmnopqrstuvwxyz")
        result1 = addvarriables(key_name1, messagecode1)
        print(result1)
        break
    elif first_question=="decrypt":
    
        key_name=str(input("Enter the Key name: "))
        decryptmessage = str(input("Enter the decrypted message: "))
        alphabet=("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        key_name1=""
        decryptmessage1=""
        o=""
        result=""
        result1=""
        for i in range(0,len(key_name)) :
            d=alphabet.find(key_name[i])
            key_name1=(key_name1+alphabet[d])
        key_name1=key_name1*25
        key_name1=key_name1[:25]
        for s in range(0,len(decryptmessage)):
            q=alphabet.find(decryptmessage[s])
            decryptmessage1=(decryptmessage1+alphabet[q])


        def cut(a, b):                 
            if len(a) > len(b):     
                result = ""
                a = a[:len(b)]
                result = a 
                return result  

        result = cut(key_name1, decryptmessage1)

        def addvarriables(e,f):
            result1=""
            for i in range(min(len(e), len(f))):
                m=alphabet.find(e[i])
                n=alphabet.find(f[i])
                o=alphabet[(n-m-1)%25]
                result1+=o
            return result1
        alphabet=("abcdefghijklmnopqrstuvwxyz")
        result1 = addvarriables(key_name1, decryptmessage1)
        print(result1)
        break

    else: #first_question!="decrypt" and first_question!="encrypt":
        print("Error")



