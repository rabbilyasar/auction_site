# auction_site
An auction site like ebay.



# Setup
Step 1. clone the repository <br/>
Step 2. Source the env file using `source env/bin/activate` <br/>
step 4. install from requirements `pip install -r requirements.txt`
Step 3. start the django server `cd auction_site && python manage.py runserver 0.0.0.0:8000`
Step 4. run all the test cases `python manage.py test`


# Signup
- visit url `http://0.0.0.0:8000/accounts/signup/`

# Login to the page
- visit url `http://0.0.0.0:8000/accounts/login/`

# Welcome to dashboard
- This is where all the auctions are listed from all the users
- A user can create a new auction by clicking the button "Add new auction"


# Todo
- feature to bid 
- expire auction after the elapsed time and notify the winner of the auction
