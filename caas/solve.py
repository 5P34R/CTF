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