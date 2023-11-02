import customtkinter as tk
import utils

#CRIAR CADA PAGINA EM UMA CLASSE
#CRIAR VARIAVEL CURRENT_PAGE QUE VAI RECEBER A CLASSE DA PÁGINA ATUAL DE ACORDO COM A NECESSIDADE

janela = tk.CTk()
janela.geometry("500x500")
username, password = tk.StringVar(), tk.StringVar()

#Criar função para alterar tema de escuro para claro e vice-versa
bg = "dark"
tk.set_appearance_mode(bg)

top_frame = tk.CTkFrame(janela)
top_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
top_frame.configure(fg_color=janela.cget("fg_color"))

welcome = tk.CTkLabel(top_frame,
                      text="Welcome to ChronosApp",
                      font=("Roboto", 30))
welcome.pack(padx=10, pady=10)

username_entry = tk.CTkEntry(top_frame,
                             placeholder_text="Username",
                             textvariable=username,
                             font=("Roboto", 16))
username_entry.pack(padx=10, pady=5)

password_entry = tk.CTkEntry(top_frame,
                             placeholder_text="Password",
                             textvariable=password,
                             font=("Roboto", 16),
                             show="*")
password_entry.pack(padx=10, pady=5)

botton_frame = tk.CTkFrame(top_frame)
botton_frame.pack(pady=7)
botton_frame.configure(fg_color=janela.cget("fg_color"))


#Criar página de registro e adicionar todas as informações no banco de dados!
def register():
  _frame = tk.CTkFrame(botton_frame)
  print(username.get(), password.get())
  rg = utils.register_user(username.get(), password.get())
  if rg is True:
    tk.CTkLabel(_frame,
                text="User registred!",
                text_color="green",
                font=("Roboto", 12)).pack()


login_button = tk.CTkButton(botton_frame,
                            text="Login",
                            font=("Roboto", 16),
                            width=100)
login_button.pack(side=tk.LEFT, padx=3)

register_button = tk.CTkButton(botton_frame,
                               text="Register",
                               font=("Roboto", 16),
                               width=100,
                               command=register)
register_button.pack(side=tk.LEFT, padx=3)
#organizar páginas em classes provavelmente!

janela.mainloop()
