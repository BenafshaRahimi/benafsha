
set_word1= [ ]
 #ابتدا برای ذخیره کلمات چند لیست میسازیم تا بعدا از آن استفاده نمايیم
exit_words = [ ]
non_exit_words = [ ]
txt = open("C:\\Users\\Aria Computer\\Downloads\How.I.Met.your.Mother.S01E01.srt","r") 
# متن و لغات خود را باز میکنیم
given_words = open("C:\\Users\\Aria Computer\\Downloads\Longman Communication 3000.txt","r")
txt_count = txt.read() 
#دستور خواندن متن و بعد دستور خواندن لغات را می دهیم.
words_count= given_words.read()
words = txt_count.split(" ") 
#برای جدا سازی کلمات متن از دستور اسپلیت استفاده می کنیم.
for word in words:
    #حلقه تشکیل می دهم که یک کلمه را از میان کلمات بگیرده 
   if word.isalpha(): 
    # شرط گذاشتم تا کلمات حروف الفبا را از متن جدا کند 
    set_word1.append(word)
    #کلمات را در ست ذخیره کند 
for x in set_word1:
    #برو کلمه را از لیست کلمات بگیر بشرط اینکه در لیست لغات بود در لیست کلمات موجوده اصافه کن
    if x  in  words_count:
        exit_words.append(x)
    # در غیر این صورت اگر کلمه متن در لیست لغات نبود در ست اضافه کن 
    else:   
        non_exit_words.append(x)
        non_exit_words1 = set (non_exit_words)
print(non_exit_words1)
 # ست لغات غیر موجودی را پرنت کن 

