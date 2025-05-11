from tkinter import *

class PasswordManagerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("500x500")

        # Padding
        self.root.config(padx = 50 , pady = 50)

        # Logo Image
        self.canvas = Canvas(height=200, width= 200)
        try:
            self.logo_img = PhotoImage(file="logo.png")
            self.canvas.create_image(100, 100, image=self.logo_img)
        except Exception as e:
            print("Logo not Loaded:", e)
        self.canvas.grid(row=0, column=1)

        # Labels
        self.website_label = Label(text= "Website:")
        self.website_label.grid(row = 1, column=0) 

        self.email_label = Label(text= "Email/Username:")
        self.email_label.grid(row=2, column = 0)
    
        self.password_label = Label(text= "Password:")
        self.password_label.grid(row=3, column = 0)

        # Entries(input fields)
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row = 1, column = 1, columnspan = 2 )
        self.website_entry.focus() #it will focus the cursor on a particular entry.
        
        self.email_entry = Entry(width = 35)
        self.email_entry.grid(row = 2, column = 1, columnspan = 2 )
        self.email_entry.insert(0, "you@example.com") #it being pre populated 
        
        self.password_entry = Entry(width = 21)
        self.password_entry.grid(row = 3, column = 1)
        
        # Buttons
        
        self.generate_button = Button(text = "Generate Password")
        self.generate_button.grid(row = 3, column = 2 )
        
        self.add_button = Button(text = "Add", width = 36, command= self.save)
        self.add_button.grid(row = 4, column = 1, columnspan = 2)
    
    def save(self):
        pass #placeholder for save functionality

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = PasswordManagerApp(root)
    root.mainloop()



