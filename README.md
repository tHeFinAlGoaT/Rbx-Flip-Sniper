# Rbx-Flip-Sniper
Made this for a friend because we coudln't find one online. <br/>
I haven't tested this myself, but since the code is theoretically right and doesn't throw any kind of error i suppose it works. <br/>
Feel free to test and lmk in the issues <br/>
Consider this a Proof of Concept 
# Tutorial
If you already have python installed, clone this repo with git clone https://github.com/tHeFinAlGoaT/Rbx-Flip-Sniper and do cd  Rbx-Flip-Sniper<br/>
Then put your auth token in the token = ' ' variable. (inside the main.py file). <br/>
To find it go into bloxflip, press f12 and on the network tab select Fetch/XHR. Now select the balance request  <br/>
(or any other POST request if you know what they are) and scroll down a bit. You will see a very long string, that's your token.  <br/>
Copy the Bearer part to. Your token should look like: 'Bearer eyJhbGciOenfhnejfnubdhswfnuwnfinufwidnsbfusnfudhfudjfudh'<-not a real token <br/>
Once done save the edited main.py with ctrl + s and execute the following command: pip install -r requirements.txt <br/>
Finally, launch the main file with python main.py
# Objective 
If this gets to 5 stars i'll make a better readme and improve the sniper
# Notes
This thing chooses to buy an item by its rate $/1k robux. You can change it in the 18th line, just modify the 1.8 to the rate an item should have for the bot to snipe it
