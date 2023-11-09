from ctypes import alignment
import customtkinter as tk
from utils import verify_if_user_exists
import getpass
from database import UserDatabase

bg = "dark"
tk.set_appearance_mode(bg)


class LoginPage(tk.CTk):

	def __init__(self):
		super().__init__()
		self.geometry("500x500")
		self.grid()

		def Login():
			db = UserDatabase()

			username = self.username_entry.get()
			password = getpass.getpass(self.password_entry.get())

			db.cursor.execute(
					'SELECT * FROM users WHERE username = ? AND password = ?',
					(username, password))
			user_data = db.cursor.fetchone()

			if user_data:
				sucess_label = tk.CTkLabel(self,
																 text="User Logged",
																 font=("Roboto", 14),
																 text_color="green")
				sucess_label.grid(row=2, column=1, columnspan=2, sticky="n")
				return True, username
			else:
				sucess_label = tk.CTkLabel(self,
																 text="Login Failed",
																 font=("Roboto", 14),
																 text_color="red")
				sucess_label.grid(row=2, column=1, columnspan=2, sticky="n")
				return False
		def Register():
			db = UserDatabase()

			username = self.username_entry.get()
			password = getpass.getpass(self.password_entry.get())

			user_boolean_value = verify_if_user_exists(username)
			if user_boolean_value is True:
				fail_label = tk.CTkLabel(self,
																 text="Register Failed!",
																 font=("Roboto", 14),
																 text_color="red")
				fail_label.grid(row=2, column=1, columnspan=2, sticky="n")
				return False
			else:
				db.register_user(username=username, password=password)
				sucess_label = tk.CTkLabel(self,
																	 text="User Registered",
																	 font=("Roboto", 14),
																	 text_color="green")
				sucess_label.grid(row=2, column=1, columnspan=2, sticky="n")
				return True

		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=3)
		self.rowconfigure((2, 3), weight=1)
		self.rowconfigure(4, weight=5)
		self.columnconfigure((0, 4), weight=1)
		self.welcome_text = tk.CTkLabel(self,
																		text="Welcome to ChronosApp",
																		font=("Roboto", 30))
		self.welcome_text.grid(row=1, column=1, columnspan=2, sticky="s", ipady=20)

		self.username_entry = tk.CTkEntry(self,
																			placeholder_text="Username",
																			font=("Roboto", 16))
		self.username_entry.grid(row=2, column=1, columnspan=2, sticky="s", pady=3)

		self.password_entry = tk.CTkEntry(self,
																			placeholder_text="Password",
																			font=("Roboto", 16),
																			show="*")
		self.password_entry.grid(row=3, column=1, columnspan=2, sticky="n", pady=3)

		self.login_button = tk.CTkButton(self,
																		 text="Login",
																		 font=("Roboto", 16),
																		 command=Login,
																		 width=100)
		self.login_button.grid(row=4, column=1, sticky="ne", padx=3)

		self.register_button = tk.CTkButton(self,
																				text="Register",
																				font=("Roboto", 16),
																				command=Register,
																				width=100)
		self.register_button.grid(row=4, column=2, sticky="nw", padx=3)


class Tabs(tk.CTkTabview):

	def __init__(self, master):
		super().__init__(master)

		# create tabs
		self.add("Taks")
		self.add("Finances")

		# add widgets on tabs
		self.label = tk.CTkLabel(master=self.tab("Finances"))
		self.label.grid(row=0, column=0, padx=20, pady=10)


class MainPage(tk.CTk):

	def __init__(self):
		super().__init__()

		self.welcome = tk.CTkLabel(self, text="ChronosApp", font=("Roboto", 30))
		self.welcome.pack(padx=10, pady=10)

		self.tab_view = Tabs(master=self)
		self.tab_view.pack(padx=5, pady=5)


app = LoginPage()
app.mainloop()
