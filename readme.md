# What

Generic account objects that can be used and shared in
arbitrary ways. 

# Setup

This is a Python/Django project. 

* make sure you have the following python tools installed: pip (the python package manager), virtualenv, and virtualenvwrapper
  * these will install new commands accessible from the command line, so make sure you have re-sourced your `.bashrc`/`.zshrc` file as directed in the above installation process, or the commands won't be accessible. 
* create a virtual environment for this project, eg, `mkvirtualenv bank`, then "enter" the virtual env: `workon bank`. 
* install the project requirements: `pip install -r requirements.txt`
* set up the database and run migrations with the command: `./manage.py migrate`. you will see some output confirming various tables created.  
* create a superuser so you can login: `./manage.py createsuperuser`
* runserver: `./managy.py runserver <port>`
* go to `/admin` and set up a few things:
  * create a currency
    * this automatically creates system DEBIT and CREDIT accounts for that currency. 
  * create one or more additional user accounts
  * still in the admin interface, create an initial balance in one or more user accounts by creating a transaction _from_ the system DEBIT account of the appropriate currency, _to_ the user account. 
  (system DEBIT accounts are constrained to have a balance < 0. I am not convinced this is 100% necessary but we can revisit later if needed). 

* visit `/accounts/list` to see your accounts. 
* transfer money between accounts on the `list` page
* view account transactions on the account detail page.

# Basics

* currencies
* system accounts
* owners, admins
* transfers

# Use Cases

* Liability tracking
* Solidarity Fund
* Savings Pool
* Pooling money for a purchase (using promises)
* A custom mutual credit system
* Time bank
* RV Food/maintenance account
* Event costs tracking and transparency
* Reimbursement Management
* 
