from tkinter import *
import Caesar
import Vernam
import matplotlib.pyplot as plt
import Base_64


class encryption_gui():
    def __init__(self,master):
      
        #root ----------------#
        self.master = master
        self.master.config(bg="white")
        self.master.title("Encryption Software")
        self.master.option_add("*Background", "white")
        self.master.option_add("*Foreground", "black")
        self.master.geometry("800x650+100+100")

        #frames ---------------#

        self.master_frame = Frame(master, borderwidth= 0)
        self.master_frame.pack(expand = True, fill = "both")
        
        frame1 = Frame(self.master_frame, borderwidth= 0, relief = GROOVE)
        frame1.pack(fill= "both", pady= 10)
        
        frame2 = Frame(self.master_frame, borderwidth= 0, relief = GROOVE)
        frame2.pack(fill = "both")
        frame2a = Frame(frame2, borderwidth= 4, relief = GROOVE)
        frame2a.pack(padx=10,pady=10, expand = True, fill = "both")
        
        frame3 = Frame(self.master_frame, borderwidth= 0, relief = GROOVE)
        frame3.pack(fill = "both")
        frame3a = Frame(frame3, borderwidth=4, relief = GROOVE)
        frame3a.pack(expand = True, fill = "both", padx=10, pady=10)
        
        frame4 = Frame(self.master_frame, borderwidth= 0, relief = GROOVE)
        frame4.pack(fill = "both")
        frame4a = Frame(frame4, borderwidth=4, relief = GROOVE)
        frame4a.pack(expand = True, padx=10, pady=10, side = LEFT, fill= "both")
        frame4b = Frame(frame4, borderwidth= 4, relief = GROOVE)
        frame4b.pack(fill="both", expand = True, padx = 10, pady=10, side = RIGHT)
        
        frame5 = Frame(self.master_frame, borderwidth= 0, relief = GROOVE)
        frame5.pack(fill = "both")
        frame5a = Frame(frame5, relief = GROOVE, borderwidth = 4)
        frame5a.pack(fill = "both", padx=10, pady=10, expand = True)

        frame6 = Frame(self.master_frame)
        frame6.pack(fill = "both")
        frame6a = Frame(frame6, borderwidth=4, relief = GROOVE)
        frame6a.pack( fill = "both", padx=10, pady=10, expand = True)
        
        #label 1 ---------------#

        
        
        icon = PhotoImage(file = "GetImage_40x40.gif")
        logo = Label(frame1)
        logo.config(image = icon)
        logo.image = icon
        logo.pack(side = LEFT, padx=10)

    

        label = Label(frame1, text = "File Encryption", fg = "black", font = ("helvitica 12 bold"))
        label.pack(side = LEFT, padx= 10)

        #label2 ---------------#
        
        

        label2 = Label(frame2a, text = "Parameters:")
        label2.pack(side=LEFT, padx=10)

        icon = PhotoImage(file = "padlock_black_20.png")
        logo = Label(frame2a)
        logo.config(image = icon)
        logo.image = icon
        logo.pack(side = LEFT, padx=10)
        

        
        
                           

        self.radio_choice = IntVar(master)
        self.radio_choice.set(2)
        radio_1 = Radiobutton(frame2a, text = "Encrypt", variable = self.radio_choice, value = 1)
        radio_2 = Radiobutton(frame2a,text= "Decrypt", variable = self.radio_choice, value = 2)
        radio_1.pack(side= LEFT, padx= 100 , pady=20)
        radio_2.pack(side= LEFT, padx=100, pady=20)

    

        #label 3 ---------------------#
        
        label3 = Label(frame3a, text = "Text:")
        label3.pack(side = LEFT, padx=10,pady=10)
        
        image_text = PhotoImage(file = "text_20.png")
        text_label = Label(frame3a)
        text_label.image = image_text
        text_label.config(image = image_text)
        text_label.pack(side = LEFT)
        
        self.field = Text(frame3a, height =6, width =75, borderwidth =2, relief = GROOVE)
        self.field.pack(side = LEFT, padx=10,pady=10)

        clear_button_3  = Button(frame3a, borderwidth = 2, relief = RAISED, fg = "black", bg = "white", command = self.clear_text, text = "Clear", width =10)
        clear_button_3.pack(side = RIGHT, padx=5)
        

        # label 4 --------------------#

        Label4= Label(frame4a, text = "Cipher:")
        Label4.pack(side = LEFT, pady=20, padx=10)

        #https://www.bing.com/images/search?view=detailV2&ccid=xX9nQj%2b7&id=73D1A5A9458185D61E824C3A8563C791321C92D0&thid=OIP.xX9nQj-7UFNDTd621uVGtQHaJO&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.c57f67423fbb5053434ddeb6d6e546b5%3frik%3d0JIcMpHHY4U6TA%26riu%3dhttp%253a%252f%252fcdn.onlinewebfonts.com%252fsvg%252fimg_77572.png%26ehk%3ddLPGMIXHaVNYrps5QE79mfkLT2RjzeZnG%252b85AuTMkgE%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=980&expw=786&q=Binary+Icon&simid=607999320464379563&FORM=IRPRST&ck=9AC24CF72E6229A5E5C9AD66B6D1EA7F&selectedIndex=1&adlt=strict%2cstrict&ajaxhist=0&ajaxserp=0
        

        bin_icon = PhotoImage(file ="binary_icon_20.png")
        bin_label = Label(frame4a)
        bin_label.image = bin_icon
        bin_label.config(image = bin_icon)
        bin_label.pack(side= LEFT)
        
        self.radio_choice_4 = IntVar(master)
        self.radio_choice_4.set(3)
        radio_1_4 = Radiobutton(frame4a, text = "Caesar", variable = self.radio_choice_4, value= 1)
        radio_2_4 = Radiobutton(frame4a, text = "Vernam", variable = self.radio_choice_4, value= 2)
        radio_3_4 = Radiobutton(frame4a, text = "Base 64", variable = self.radio_choice_4, value= 3)
        radio_1_4.pack(side = LEFT, padx=20)
        radio_2_4.pack(side = LEFT, padx=20)
        radio_3_4.pack(side = LEFT, padx=20)

        key= Label(frame4b, text = "Key:", fg= "black")
        key.pack(side = LEFT, padx=10)
        image_key =  PhotoImage(file = "key_20.png")
        key_label = Label(frame4b)
        key_label.image = image_key
        key_label.config(image = image_key)
        key_label.pack(side = LEFT)
   
        self.field_4b = Text(frame4b, width =20, height=2)
        self.field_4b.pack(side = RIGHT, padx=10, pady=10)

        # label 5 ---------------------#

        label5a = Label(frame5a, text = "Output:", fg =  "black")
        label5a.pack(padx=10,pady=10, side = LEFT)

        icon5 = PhotoImage(file = "text_20.png")
        i_label5 = Label(frame5a)
        i_label5.image = icon5
        i_label5.config(image = icon5)
        i_label5.pack(side= LEFT, padx=5)

        frame5b = Frame(frame5a, relief= GROOVE, borderwidth = 2, height = 100)
        frame5b.pack(padx=10,pady=10, side = RIGHT)

        
        self.out5 = Text(frame5a, fg = "black", width = 80, height = 6)
        self.out5.pack(side = RIGHT)
        

        # label 6 --------------------- #

        label6 = Label(frame6a, text = "Command:", fg = "black")
        label6.pack(side = LEFT, padx=10)
        button6 = Button(frame6a, relief = RAISED, borderwidth=2, command = self.generate, text = "Start", width = 20)
        button6.pack(side = LEFT, pady = 20,padx=30)
        button6b = Button(frame6a, fg= "black", bg = "white", relief = RAISED, borderwidth=2, text = "Information", width =20, command = self.info)
        button6b.pack(side = LEFT, padx=30)

        button6a = Button(frame6a, relief = RAISED, borderwidth=2, command= master.destroy, text= "Close", width=10)
        button6a.pack(side = LEFT, padx=30)
        
    
        
    def clear_text(self):
        self.field.delete("1.0", END)
        
    def info(self):
        
        # unpack master ------------- #
        
        self.master_frame.pack_forget()

        # create frames ------------- #
        
        self.frame1_info = Frame(self.master)
        self.frame1_info.pack(fill = "both")
        self.frame2_info = Frame(self.frame1_info, borderwidth = 2, relief = GROOVE)
        self.frame2_info.pack(expand = True, fill = "both")

        # labels -------------------- #
        
        texter = "Symmetric Key Encryption: \nEncryption is a process to change the form of any message in order to protect it from reading by anyone. In Symmetric-key encryption the message is encrypted by using a key and the same key is used to decrypt the message which makes it easy to use but less secure. It also requires a safe method to transfer the key from one party to another.\n\nAsymmetric Key Encryption: \nAsymmetric Key Encryption is based on public and private key encryption techniques. It uses two different key to encrypt and decrypt the message. It is more secure than the symmetric key encryption technique but is much slower."      
        text = Text(self.frame2_info)
        text.insert(END, texter)
        text.pack(padx =10, pady=10)
        button = Button(self.frame2_info, text = "Back", command = self.repack)
        button.pack()
        
    def repack(self):
        self.frame1_info.pack_forget()
        self.frame2_info.pack_forget()
        self.master_frame.pack()
        
        
            
    



    def generate(self):

        # gets all inputs ---------------- #

        actual = []
        self.out5.delete("1.0", END)
        key = self.field_4b.get("1.0", "end-1c")
        cipher = self.radio_choice_4.get()
        input_ = self.field.get("1.0", "end-1c")
        method = self.radio_choice.get()

        # looks to see what cipher ------------- #

        if cipher == 1 and method == 1:
            actual = (Caesar.encrypt(key, input_))
            self.out5.insert(END, actual)
        elif cipher == 1 and method == 2:
            
            actual = (Caesar.decrypt(key, input_))
            self.out5.insert(END, actual)
        elif cipher == 2:
        
            actual = (Vernam.encrypt(key, input_))
            self.out5.insert(END, actual)
        elif cipher == 3 and method ==1:
            actual = (Base_64.encrypt(input_))
            self.out5.insert(END, actual)
            actual = str(actual)
            actual = actual[2:(len(actual)-1)]
        elif cipher ==3 and method ==2:
            actual = (Base_64.decrypt(input_))
            self.out5.insert(END, actual)
            actual = str(actual)
            actual = actual[2:(len(actual)-1)]
            

        # performs frequency analysis --------------#

        data = []
        letters = []
        actual = actual.upper()
        for i in range(0,26):
            letters.append(chr(65+i))
            data.append(0)
        for a in range(0, len(letters)):
            char = letters[a]

            for x in range(0, len(actual)):
                
                if char == actual[x]:
                    data[a] = data[a] + 1

        # graphs for frequency analysis -----------#

        plt.clf()
        plt.bar(letters, data)
        plt.show()
        
               

def main():
    root = Tk()
    app = encryption_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
