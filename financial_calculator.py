import tkinter as tk
from tkinter import ttk


def show_frame(frame):
    global current_content_frame
    if current_content_frame:
        current_content_frame.grid_forget()
    frame.grid(row=1,column=0, columnspan=5, sticky="nsew")
    current_content_frame = frame


def show_simple_interest():
    show_frame(simple_interest_frame)


def show_compound_interest():
    show_frame(compound_interest_frame)


def show_loan_payment():
    show_frame(loan_payment_frame)


def show_savings_account():
    show_frame(savings_account_frame)


def calculate_simple_interest():
    # Get the values from the entry fields
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    time_period = float(time_period_entry.get())

    # Calculate the simple interest
    simple_interest = round(principal * interest_rate * time_period, 2)

    # Display the simple interest in the entry field
    simple_interest_entry.delete(0, "end")
    simple_interest_entry.insert(0, simple_interest)


def calculate_compound_interest():
    # Get the values from the entry fields
    compound_principal = float(compound_principal_entry.get())
    interest_rate = float(compound_interest_rate_entry.get()) / 100
    time_period = float(compound_time_period_entry.get())

    # Calculate the simple interest
    compound_interest = round(compound_principal * (1 + interest_rate) ** time_period, 2)

    # Display the simple interest in the entry field
    compound_interest_entry.delete(0, "end")
    compound_interest_entry.insert(0, float(compound_interest))


def calculate_loan_payment():
    loan_principal = float(loan_principal_amount_entry.get())
    loan_interest_rate = float(loan_interest_rate_entry.get()) / 100
    type_period = loan_type_period_entry.get()
    if type_period == str("Months"):
        loan_interest_rate = loan_interest_rate / 12
    number_periods = int(loan_period_entry.get())
    periodic_payment = round((loan_principal * loan_interest_rate) /
                             (1 - (1 + loan_interest_rate) ** -number_periods), 2)

    all_loan_payments = []
    for period in range(1, number_periods + 1):
        period_interest_pmt = loan_principal * loan_interest_rate
        period_principal_pmt = periodic_payment - period_interest_pmt

        all_loan_payments.append([period, period_principal_pmt, period_interest_pmt, periodic_payment])
        loan_principal -= period_principal_pmt

    loan_payment_entry.delete(0, "end")
    loan_payment_entry.insert(0, float(periodic_payment))
    if loan_payment_specific_period_choice_entry.get() == "Yes":
        chosen_period = int(loan_specific_period_payment_entry.get())
        specific_interest = round(all_loan_payments[chosen_period - 1][2], 2)
        specific_principal = round(all_loan_payments[chosen_period - 1][1], 2)
        specific_period_interest_payment_entry.delete(0, "end")
        specific_period_interest_payment_entry.insert(0, specific_interest)
        specific_period_principal_payment_label_entry.delete(0, "end")
        specific_period_principal_payment_label_entry.insert(0, specific_principal)
    loan_payment_plan_output.delete(1.0, "end")
    for idx in range(len(all_loan_payments)):
        string_to_print = f"Period: {all_loan_payments[idx][0]:3d}; Principal Payment: {all_loan_payments[idx][1]:.2f};\
 Interest Payment: {all_loan_payments[idx][2]:.2f}; Loan Payment: {all_loan_payments[idx][3]:.2f}"
        loan_payment_plan_output.insert("end", str(string_to_print) + "\n")

def calculate_future_value_of_savings():
    initial_investment = float(initial_investment_amount_entry.get())
    periodic_investment = float(periodic_investment_amount_entry.get())
    expected_average_annual_return = float(expected_return_entry.get()) / 100
    type_period = savings_type_period_entry.get()
    if type_period == str("Months"):
        expected_average_annual_return = expected_average_annual_return / 12
    number_periods = int(savings_period_entry.get())
    type_annuity = savings_type_entry.get()

    future_value_initial_investment = initial_investment \
                                      * ((1 + expected_average_annual_return) ** number_periods)

    if type_annuity == "Annuity Due":
        future_value_periodic_investment = periodic_investment * \
                                          (((((1 + expected_average_annual_return) ** number_periods)) - 1) / \
                                           expected_average_annual_return) * (1 + expected_average_annual_return)
    else:
        future_value_periodic_investment = periodic_investment * \
                                       (((((1 + expected_average_annual_return) ** number_periods)) - 1) / \
                                        expected_average_annual_return)
    total_future_value = round(future_value_initial_investment + future_value_periodic_investment, 2)
    future_value_savings_entry.delete(0, "end")
    future_value_savings_entry.insert(0, str(total_future_value))

root = tk.Tk()

root.title("Financial Calculator")
root.grid()
root.geometry('1100x650')
root.config(bg='lightblue')
root.grid_rowconfigure(1, weight=1)
root.columnconfigure(0, minsize=23, weight=1)

# create top bar
top_bar_frame = tk.Frame(root)
top_bar_frame.grid(row=0, columnspan=5, sticky=tk.NSEW)
top_bar_frame.columnconfigure(0, minsize=23, weight=1)
top_bar_frame.columnconfigure(1, minsize=23, weight=1)
top_bar_frame.columnconfigure(2, minsize=23, weight=1)
top_bar_frame.columnconfigure(3, minsize=23, weight=1)
top_bar_frame.columnconfigure(4, minsize=23, weight=1)

# create buttons for top bar
button1 = tk.Button(top_bar_frame, text='Simple Interest', bg="sky blue", font="bold",
                    width=25, command=show_simple_interest)
button2 = tk.Button(top_bar_frame, text='Compound Interest', bg="sky blue", font="bold",
                    width=25, command=show_compound_interest)
button3 = tk.Button(top_bar_frame, text='Calc Loan Payment', bg="sky blue", font="bold",
                    width=25, command=show_loan_payment)
button4 = tk.Button(top_bar_frame, text='Future Value of Savings', bg="sky blue", font="bold", width=25,
                    command=show_savings_account)
button5 = tk.Button(top_bar_frame, text='Quit', bg="sky blue", font="bold",
                    width=25, command=root.destroy)

# pack buttons into the top bar
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)
button5.grid(row=0, column=4)

current_content_frame = None

# Create all frames with labels
simple_interest_frame = ttk.LabelFrame(root, text="Simple Interest")
# simple_interest_frame.grid(row=1, column=0, sticky=tk.NSEW)

compound_interest_frame = ttk.LabelFrame(root, text="Compound Interest")
# compound_interest_frame.grid(row=1, column=0, sticky=tk.NSEW)

loan_payment_frame = ttk.LabelFrame(root, text="Loan Payment Calculator")
# loan_payment_frame.grid(row=1, column=0, sticky=tk.NSEW)

savings_account_frame = ttk.LabelFrame(root, text="Savings Account Calculator")
# savings_account_frame.grid(row=4, column=0)

# Add widgets to the simple interest frame
principal_label = ttk.Label(simple_interest_frame, text="Principal Amount:")
principal_entry = ttk.Entry(simple_interest_frame)

interest_rate_label = ttk.Label(simple_interest_frame, text="Interest Rate:")
interest_rate_entry = ttk.Entry(simple_interest_frame)

time_period_label = ttk.Label(simple_interest_frame, text="Time Period (in years):")
time_period_entry = ttk.Entry(simple_interest_frame)

simple_interest_label = ttk.Label(simple_interest_frame, text="Simple Interest:")
simple_interest_entry = ttk.Entry(simple_interest_frame)

simple_interest_button = ttk.Button(simple_interest_frame, text="Calculate",
                                    command=calculate_simple_interest)

# Specify the minimum size of the rows and columns in the simple interest frame
simple_interest_frame.grid_rowconfigure(0, minsize=25)
simple_interest_frame.grid_rowconfigure(1, minsize=25)
simple_interest_frame.grid_rowconfigure(2, minsize=25)
simple_interest_frame.grid_rowconfigure(3, minsize=25)
simple_interest_frame.grid_rowconfigure(4, minsize=25)
simple_interest_frame.grid_columnconfigure(0, minsize=200)
simple_interest_frame.grid_columnconfigure(1, weight=1, minsize=200)

# Place the widgets in the simple interest frame
principal_label.grid(row=0, column=0, sticky=tk.W)
principal_entry.grid(row=0, column=1, sticky=tk.EW)

interest_rate_label.grid(row=1, column=0, sticky=tk.W)
interest_rate_entry.grid(row=1, column=1, sticky=tk.EW)

time_period_label.grid(row=2, column=0, sticky=tk.W)
time_period_entry.grid(row=2, column=1, sticky=tk.EW)

simple_interest_label.grid(row=3, column=0, sticky=tk.W)
simple_interest_entry.grid(row=3, column=1, sticky=tk.EW)

simple_interest_button.grid(row=4, columnspan=2, sticky=tk.EW)
simple_interest_frame.lower()


# Specify the minimum size of the rows and columns in the simple interest frame
compound_interest_frame.grid_rowconfigure(0, minsize=25)
compound_interest_frame.grid_rowconfigure(1, minsize=25)
compound_interest_frame.grid_rowconfigure(2, minsize=25)
compound_interest_frame.grid_rowconfigure(3, minsize=25)
compound_interest_frame.grid_rowconfigure(4, minsize=25)
compound_interest_frame.grid_columnconfigure(0, minsize=200)
compound_interest_frame.grid_columnconfigure(1, weight=1, minsize=200)

# Add widgets to the compound interest frame
compound_principal_label = ttk.Label(compound_interest_frame, text="Principal Amount:")
compound_principal_entry = ttk.Entry(compound_interest_frame)

compound_interest_rate_label = ttk.Label(compound_interest_frame, text="Interest Rate:")
compound_interest_rate_entry = ttk.Entry(compound_interest_frame)

compound_time_period_label = ttk.Label(compound_interest_frame, text="Time Period (in years):")
compound_time_period_entry = ttk.Entry(compound_interest_frame)

compound_interest_label = ttk.Label(compound_interest_frame, text="Compound Interest:")
compound_interest_entry = ttk.Entry(compound_interest_frame)

compound_interest_button = ttk.Button(compound_interest_frame,
                                      text="Calculate Compound", command=calculate_compound_interest)

# Place the widgets in the compound interest frame
compound_principal_label.grid(row=0, column=0, sticky=tk.W)
compound_principal_entry.grid(row=0, column=1, sticky=tk.EW)

compound_interest_rate_label.grid(row=1, column=0, sticky=tk.W)
compound_interest_rate_entry.grid(row=1, column=1, sticky=tk.EW)

compound_time_period_label.grid(row=2, column=0, sticky=tk.W)
compound_time_period_entry.grid(row=2, column=1, sticky=tk.EW)

compound_interest_label.grid(row=3, column=0, sticky=tk.W)
compound_interest_entry.grid(row=3, column=1, sticky=tk.EW)

compound_interest_button.grid(row=4, columnspan=2, sticky=tk.EW)


loan_payment_frame.grid_columnconfigure(0, minsize=200)
loan_payment_frame.grid_columnconfigure(1, weight=1, minsize=200)
loan_payment_frame.grid_rowconfigure(0, weight=1)
loan_payment_frame.grid_rowconfigure(1, weight=1)
loan_payment_frame.grid_rowconfigure(2, weight=1)
loan_payment_frame.grid_rowconfigure(3, weight=1)
loan_payment_frame.grid_rowconfigure(4, weight=1)
loan_payment_frame.grid_rowconfigure(5, weight=1)
loan_payment_frame.grid_rowconfigure(6, weight=1)
loan_payment_frame.grid_rowconfigure(7, weight=1)
loan_payment_frame.grid_rowconfigure(8, weight=1)
loan_payment_frame.grid_rowconfigure(9, weight=1)
loan_payment_frame.grid_rowconfigure(10, weight=1)
loan_payment_frame.grid_rowconfigure(11, weight=1)
loan_payment_frame.grid_rowconfigure(12, weight=1)

# Add widgets to the loan payment frame
loan_principal_amount_label = ttk.Label(loan_payment_frame, text="Principal Amount")
loan_principal_amount_entry = ttk.Entry(loan_payment_frame)

loan_interest_rate_annual_label = ttk.Label(loan_payment_frame, text="Annual Interest Rate")
loan_interest_rate_entry = ttk.Entry(loan_payment_frame)

loan_type_period_label = ttk.Label(loan_payment_frame, text="Type Period - Months or Years")
loan_type_period_entry = ttk.Combobox(loan_payment_frame, values=["Months", "Years"])

loan_period_label = ttk.Label(loan_payment_frame, text="Number of Periods")
loan_period_entry = ttk.Entry(loan_payment_frame)

loan_payment_specific_period_choice_label = tk.Label(loan_payment_frame,
                                                     text="Calculate specific payment?")
loan_payment_specific_period_choice_entry = ttk.Combobox(loan_payment_frame, values=["Yes", "No"])

loan_specific_period_payment_label = ttk.Label(loan_payment_frame, text="Enter Payment Period 1 to Final")
loan_specific_period_payment_entry = ttk.Entry(loan_payment_frame)

loan_payment_label = ttk.Label(loan_payment_frame, text="Your loan payment is:")
loan_payment_entry = ttk.Entry(loan_payment_frame)

specific_period_interest_payment_label = ttk.Label(loan_payment_frame, text="Interest Payment for Period")
specific_period_interest_payment_entry = ttk.Entry(loan_payment_frame)

specific_period_principal_payment_label = ttk.Label(loan_payment_frame,
                                                    text="Principal Payment for Period")
specific_period_principal_payment_label_entry = ttk.Entry(loan_payment_frame, style="TEntry", background="light green")

specific_loan_payment_calculate_button = ttk.Button(loan_payment_frame, text="Calculate Payment(s)",
                                                    command=calculate_loan_payment)

loan_payment_plan_label = ttk.Label(loan_payment_frame, text="Loan Payment Plan")
loan_payment_plan_output = tk.Text(loan_payment_frame)
# loan_payment_plan_button = ttk.Button(loan_payment_frame, text="Print Loan Payment Plan", command=print_loan_payment_plan)

# place widgets in the loan payment frame
loan_principal_amount_label.grid(row=0, column=0, sticky=tk.W)
loan_principal_amount_entry.grid(row=0, column=1, sticky=tk.EW)

loan_interest_rate_annual_label.grid(row=1, column=0, sticky=tk.W)
loan_interest_rate_entry.grid(row=1, column=1, sticky=tk.EW)

loan_type_period_label.grid(row=2, column=0, sticky=tk.W)
loan_type_period_entry.grid(row=2, column=1, sticky=tk.EW)

loan_period_label.grid(row=3, column=0, sticky=tk.W)
loan_period_entry.grid(row=3, column=1, sticky=tk.EW)

loan_payment_specific_period_choice_label.grid(row=4, column=0, sticky=tk.W)
loan_payment_specific_period_choice_entry.grid(row=4, column=1, sticky=tk.EW)

loan_specific_period_payment_label.grid(row=5, column=0, sticky=tk.W)
loan_specific_period_payment_entry.grid(row=5, column=1, sticky=tk.EW)

loan_payment_label.grid(row=6, column=0, sticky=tk.W)
loan_payment_entry.grid(row=6, column=1, sticky=tk.EW)

specific_period_interest_payment_label.grid(row=7, column=0, sticky=tk.W)
specific_period_interest_payment_entry.grid(row=7, column=1, sticky=tk.EW)

specific_period_principal_payment_label.grid(row=8, column=0, sticky=tk.W)
specific_period_principal_payment_label_entry.grid(row=8, column=1, sticky=tk.EW)

loan_payment_plan_label.grid(row=9, columnspan=2, sticky=tk.W)
loan_payment_plan_output.grid(row=10, columnspan=2, sticky=tk.NSEW)

specific_loan_payment_calculate_button.grid(row=11, columnspan=2, sticky=tk.EW)
# loan_payment_plan_button.grid(row=12, columnspan=2, sticky=tk.EW)

# Add widgets to savings account frame:
initial_investment_amount_label = ttk.Label(savings_account_frame, text="Initial Investment:")
initial_investment_amount_entry = ttk.Entry(savings_account_frame)

periodic_investment_amount_label = ttk.Label(savings_account_frame, text="Periodic Investment:")
periodic_investment_amount_entry = ttk.Entry(savings_account_frame)

expected_return_label = ttk.Label(savings_account_frame, text="Expected Annual Return:")
expected_return_entry = ttk.Entry(savings_account_frame)

savings_type_period_label = ttk.Label(savings_account_frame, text="Select Period Type:")
savings_type_period_entry = ttk.Combobox(savings_account_frame, values=["Months", "Years"])

savings_period_label = ttk.Label(savings_account_frame, text="Number of Periods:")
savings_period_entry = ttk.Entry(savings_account_frame)

savings_type_label = ttk.Label(savings_account_frame, text="Ordinary or Annuity Due:")
savings_type_entry = ttk.Combobox(savings_account_frame, values=["Ordinary Annuity", "Annuity Due"])

future_value_savings_label = ttk.Label(savings_account_frame, text="Future value of your savings:")
future_value_savings_entry = ttk.Entry(savings_account_frame)

future_value_savings_calc_button = ttk.Button(savings_account_frame, text="Calculate Payment(s)",\
                                              command=calculate_future_value_of_savings)
# Place the widgets in the savings account frame
savings_account_frame.grid_columnconfigure(0, minsize=200)
savings_account_frame.grid_columnconfigure(1, weight=1, minsize=200)

initial_investment_amount_label.grid(row=0, column=0, sticky=tk.W)
initial_investment_amount_entry.grid(row=0, column=1, sticky=tk.EW)

periodic_investment_amount_label.grid(row=1, column=0, sticky=tk.W)
periodic_investment_amount_entry.grid(row=1, column=1, sticky=tk.EW)

expected_return_label.grid(row=2, column=0, sticky=tk.W)
expected_return_entry.grid(row=2, column=1, sticky=tk.EW)

savings_type_period_label.grid(row=3, column=0, sticky=tk.W)
savings_type_period_entry.grid(row=3, column=1, sticky=tk.EW)

savings_period_label.grid(row=4, column=0, sticky=tk.W)
savings_period_entry.grid(row=4, column=1, sticky=tk.EW)

savings_type_label.grid(row=5, column=0, sticky=tk.W)
savings_type_entry.grid(row=5, column=1, sticky=tk.EW)

future_value_savings_label.grid(row=6, column=0, sticky=tk.W)
future_value_savings_entry.grid(row=6, column=1, sticky=tk.EW)

future_value_savings_calc_button.grid(row=7, columnspan=2, sticky=tk.EW)

root.mainloop()
