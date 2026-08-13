caption=input("Enter the caption: ")
if len(caption)>100:
        caption = caption[0:100]

if caption.startswith("#"):
       print( "caption starts with #")
    
words=caption.split()
words[0]=words[0].capitalize()
caption=" ".join(words)
    
if caption.count("#")<3:
        print("Add more hashtags")
print(caption)

