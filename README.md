# Rbx-Flip-Sniper
This is a PoC for sniping limited items with a low $/1k robux rate in RBX Flip marketplace. <br/>
This is my first project and a PoC, so please help me improve this code if you can! 
# Requirements
[Python 3.x](https://www.python.org/downloads/release/python-3110/)
# Tutorial
To install this program locally execute the following commands: <br/>
```
git clone https://github.com/tHeFinAlGoaT/Rbx-Flip-Sniper
```
```
cd Rbx-Flip-Sniper
```
Once you've done that, put your auth token in the ```Token = ''``` (Line 11) variable <br/>
Not sure how to get that? i Gotchu <br/> 
<hr>


1. Go into your [RBX Flip](https://www.rbxflip.com/) <br/>
2. Press right click -> inspect or f12 <br/>
3. Head to the network tab <br/>
![here](Sniper_Imgs/network.png) <br/>
If you can't see it, press the 2 arrows ```>>``` and then select it or resize the dev console <br/>
4. Press Fetch/XHR <br/>
![here](Sniper_Imgs/fetch_xhr.png) <br/>
5. Reload the page
6. Press on ```user``` and copy whatever comes after ```Authorization: ``` <br/>
7. ![here](Sniper_Imgs/auth.png) <br/>
8. Paste in in between the ```''``` in the ```main.py``` file <br/>

#FAQ

Nobody actually asked this, but i'll still answer <br/>
1. Is this a logger? <br/>
- Nope, check the source code. It's only 25 lines of simple python <br/>
2. How can I change the rate i want an item to have to buy it? <br/>
- Line 18 of the code. 



