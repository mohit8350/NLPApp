import tkinter as tk
from mydb_code import Database
from tkinter import messagebox
from myapi import API
from classifier import classifiers as clf
class NLPApp:


    def __init__(self, root):
        self.root = root
        # creating database, classifiers and API objects so we can use there methods
        self.dbo = Database()
        self.clfo = clf()
        self.apio = API()        
        self.root.title("NLPApp")
        self.root.geometry("600x500")
        self.root.configure(bg="#34495e")
        self.login_gui()

        self.root.mainloop()
    
    def login_gui(self):
        self.clear_gui()
        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,50))
        heading.configure(font=('verdana',46, 'bold'))


        email_lebel = tk.Label(self.root, text = 'Enter Your Email', bg = '#34495e')
        email_lebel.pack(pady=(25,2), ipady = 2)
        email_lebel.configure(font=('verdana', 12))

        # taking emali input
        self.email_input = tk.Entry(self.root, width=35   ) #, bg = '#FFFDD0')       
        self.email_input.pack(pady=(3,3), ipady = 3)


        password_lebel = tk.Label(self.root, text = 'Enter Your Password',  bg = '#34495e')
        password_lebel.pack(pady=(25,3), ipady = 2)
        password_lebel.configure(font=('verdana', 12))


        # taking password input
        self.password_input = tk.Entry(self.root, width=35, show='*') #, bg = '#FFFDD0')       
        self.password_input.pack(pady=(2,2), ipady= 3)


        # creating login button
        login_button = tk.Button(self.root, text = 'Login', width=15, height= 1, command=self.perform_login)
        login_button.pack(pady = (20,10))
        

        NM_lebel = tk.Label(self.root, text = 'Not a member?',  bg = '#34495e')
        NM_lebel.pack(pady=(10,3), ipady = 2)
        NM_lebel.configure(font=('verdana', 8))

        
        # creating register button
        register_button = tk.Button(self.root, text = 'Register Now', width=15, height= 1, command=self.register_gui)
        register_button.pack(pady = (3,10))
    
    def register_gui(self):
        self.clear_gui()

        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,50))
        heading.configure(font=('verdana',46, 'bold'))

        name_lebel = tk.Label(self.root, text = 'Enter Your Name', bg = '#34495e')
        name_lebel.pack(pady=(25,2), ipady = 2)
        name_lebel.configure(font=('verdana', 12))

        # taking name from user
        self.name_input = tk.Entry(self.root, width=35   ) #, bg = '#FFFDD0')       
        self.name_input.pack(pady=(3,3), ipady = 3)

        email_lebel = tk.Label(self.root,text = 'Enter Your Email', bg = '#34495e')
        email_lebel.pack(pady=(25,2), ipady = 2)
        email_lebel.configure(font=('verdana', 12))

        # taking emali input
        self.email_input = tk.Entry(self.root, width=35   ) #, bg = '#FFFDD0')       
        self.email_input.pack(pady=(3,3), ipady = 3)

        password_lebel = tk.Label(self.root, text = 'Enter Your Password',  bg = '#34495e')
        password_lebel.pack(pady=(25,3), ipady = 2)
        password_lebel.configure(font=('verdana', 12))

        # taking password input
        self.password_input = tk.Entry(self.root, width=35, show='*') #, bg = '#FFFDD0')       
        self.password_input.pack(pady=(2,2), ipady= 3)

        # creating register button
        register_button = tk.Button(self.root, text = 'Register', width=15, height= 1, command = self.perform_registeration)
        register_button.pack(pady = (20,10))
        
        AM_lebel = tk.Label(self.root, text = 'Already a member?',  bg = '#34495e') 
        AM_lebel.pack(pady=(10,3), ipady = 2)
        AM_lebel.configure(font=('verdana', 8))
        
        # creating login button
        login_button = tk.Button(self.root, text = 'Login Now', width=15, height= 1, command=self.login_gui)
        login_button.pack(pady = (3,10))

    def sentiment_gui(self):
        self.clear_gui()

        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,20))
        heading.configure(font=('verdana',46, 'bold'))

        heading = tk.Label(self.root, text= 'Sentiment Analysis')
        heading.pack(pady = (10,20))
        heading.configure(font=('verdana', 20), bg = '#34495e')

        name_lebel = tk.Label(self.root, text = 'Enter The Text', bg = '#34495e')
        name_lebel.pack(pady=(25,2), ipady = 2)
        name_lebel.configure(font=('verdana', 12))

        self.sentence = tk.Text(self.root,height=10, width=50, font=("verdana", 10))
        self.sentence.pack(pady=(3,3), ipady = 5)
        self.sentence.configure(font=('verdana', 10))

# Generate sentiment button
        genrate = tk.Button(self.root, text = 'Generate', height=1, command= self.do_sentiment_analyze )
        genrate.pack(pady=(5,15))
        genrate.configure(font=('None', 12, 'bold') )

# Back button
        back = tk.Button(self.root, text = 'Back', width=15, height=1, command= self.home_gui )
        back.pack(pady=(55,15))
        back.configure(font=('verdana', 10) )

    def ner_gui(self):
        self.clear_gui()

        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,20))
        heading.configure(font=('verdana',46, 'bold'))

        heading = tk.Label(self.root, text= 'NER Analysis')
        heading.pack(pady = (10,20))
        heading.configure(font=('verdana', 20), bg = '#34495e')

        name_lebel = tk.Label(self.root, text = 'Enter The Text', bg = '#34495e')
        name_lebel.pack(pady=(25,2), ipady = 2)
        name_lebel.configure(font=('verdana', 12))

        self.sentence = tk.Text(self.root,height=10, width=50, font=("verdana", 10))
        self.sentence.pack(pady=(3,3), ipady = 5)
        self.sentence.configure(font=('verdana', 10))

# Generate sentiment button
        back = tk.Button(self.root, text = 'Generate', height=1, command= self.do_ner_analyze )
        back.pack(pady=(5,15))
        back.configure(font=('None', 12, 'bold') )

# Back button
        back = tk.Button(self.root, text = 'Back', width=15, height=1, command= self.home_gui )
        back.pack(pady=(55,15))
        back.configure(font=('verdana', 10) )

    def emotion_gui(self):
        
        self.clear_gui()

        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,20))
        heading.configure(font=('verdana',46, 'bold'))

        heading = tk.Label(self.root, text= 'Emotion Analysis')
        heading.pack(pady = (10,20))
        heading.configure(font=('verdana', 20), bg = '#34495e')

        name_lebel = tk.Label(self.root, text = 'Enter The Text', bg = '#34495e')
        name_lebel.pack(pady=(25,2), ipady = 2)
        name_lebel.configure(font=('verdana', 12))

        self.sentence = tk.Text(self.root,height=10, width=50, font=("verdana", 10))
        self.sentence.pack(pady=(3,3), ipady = 5)
        self.sentence.configure(font=('verdana', 10))
# Generate sentiment button
        back = tk.Button(self.root, text = 'Generate', height=1, command= self.do_emotion_analyze )
        back.pack(pady=(5,15))
        back.configure(font=('None', 12, 'bold') )

# Back button
        back = tk.Button(self.root, text = 'Back', width=15, height=1, command= self.home_gui )
        back.pack(pady=(55,15))
        back.configure(font=('verdana', 10) )

    def home_gui(self):
        self.clear_gui()
        heading = tk.Label(self.root, text = 'NLPApp', fg = 'Black', bg = '#34495e')
        heading.pack(pady=(55,50))
        heading.configure(font=('verdana',46, 'bold'))

        sentiment_btn = tk.Button(self.root, text = 'Sentiment Analysis', width=25, height=2, command = self.sentiment_gui )
        sentiment_btn.pack(pady=(10,10))
        sentiment_btn.configure(font=('verdana', 10) )

        ner_btn = tk.Button(self.root, text = 'Named Entity Recognition', width=25, height=2, command= self.ner_gui )
        ner_btn.pack(pady=(10,10))
        ner_btn.configure(font=('verdana', 10) )

        emotion_btn = tk.Button(self.root, text = 'Emotion Prediction', width=25, height=2, command= self.emotion_gui )
        emotion_btn.pack(pady=(10,10))
        emotion_btn.configure(font=('verdana', 10) )
        self.perform_logout()


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)
        if response:
            self.home_gui()
            messagebox.showinfo('Success', 'Login successful')
        
        else:
            messagebox.showerror('Error', 'Incorrect email or password. Try again.')

    def perform_registeration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.adddata(name,email,password)

        if response:
            self.clear_gui()
            self.login_gui
            messagebox.showinfo('Success', 'Registraion successfull. Now you can login.')
        
        else:
            messagebox.showerror('Error', 'Email already exists.')

    def perform_logout(self):
        logout = tk.Button(self.root, text = 'Logout', width=15, height=1, command= self.login_gui )
        logout.pack(pady=(15,15))
        logout.configure(font=('verdana', 10) )


    def do_sentiment_analyze(self):
        
        text = self.sentence.get("1.0", tk.END)
        self.response = self.cflo.analyze_polarity(text)
        message_to_show= self.response["Polarity Label"]

        # Check if output_frame already exists and destroy it
        if hasattr(self, "output_frame") and self.output_frame:
            self.output_frame.destroy()

        # Create a new Frame for the result output
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=(25, 2), fill=tk.BOTH, expand=True)

        # Create a Scrollbar
        scrollbar = tk.Scrollbar(self.output_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Text widget (read-only)
        result_text = tk.Text(self.output_frame, height=5, width=50, wrap=tk.WORD, bg='#f0f0f0', fg='black', font=('verdana', 12))
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insert the sentiment analysis result into the Text widget
        result_text.insert(tk.END, message_to_show)

        # Make the Text widget read-only
        result_text.config(state=tk.DISABLED)

        # Link the scrollbar to the Text widget
        result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result_text.yview)

    def do_ner_analyze(self):
        
        text = self.sentence.get("1.0", tk.END)
        self.response = self.apio.perform_NER(text)
        message_to_show= self.response

        # Check if output_frame already exists and destroy it
        if hasattr(self, "output_frame") and self.output_frame:
            self.output_frame.destroy()

        # Create a new Frame for the result output
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=(25, 2), fill=tk.BOTH, expand=True)
        
            # Create a Scrollbar for the Text widget
        scrollbar = tk.Scrollbar(self.output_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Create the Text widget to display NER results
        result_text = tk.Text(self.output_frame, height=5, width=50, wrap=tk.WORD, bg='#f0f0f0', fg='black', font=('verdana', 12))
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)

        # Insert the NER results into the Text widget
        for i in message_to_show:

            if i["score"] > 0.7 and 'entity_group' in i:

                formatted_text = '{} {} {}\n'.format(
                    i['word'],
                    "-->",
                    self.clfo.ner_labels_full_names(i['entity_group'])
                    
                )
                result_text.insert(tk.END, formatted_text)
        
        # Make the Text widget read-only (non-editable)
        result_text.config(state=tk.DISABLED)
        
        # Link the scrollbar to the Text widget
        result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result_text.yview)
        
    def do_emotion_analyze(self):
        
        text = self.sentence.get("1.0", tk.END)
        message_to_show = self.apio.analyze_emotion(text)

        # Check if output_frame already exists and destroy it
        if hasattr(self, "output_frame") and self.output_frame:
            self.output_frame.destroy()

        # Create a new Frame for the result output
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=(25, 2), fill=tk.BOTH, expand=True)

        # Create a Scrollbar
        scrollbar = tk.Scrollbar(self.output_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Text widget (read-only)
        result_text = tk.Text(self.output_frame, height=5, width=50, wrap=tk.WORD, bg='#f0f0f0', fg='black', font=('verdana', 12))
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insert the sentiment analysis result into the Text widget
        result_text.insert(tk.END, message_to_show)

        # Make the Text widget read-only
        result_text.config(state=tk.DISABLED)

        # Link the scrollbar to the Text widget
        result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result_text.yview)

    def clear_gui(self):        
        for widget in self.root.winfo_children():
            widget.destroy()  # Destroy each widget



root = tk.Tk()
app = NLPApp(root)
root.mainloop()
