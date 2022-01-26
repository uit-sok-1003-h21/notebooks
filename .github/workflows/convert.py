import nbformat as nbf
import nbconvert as nb
import os


def main():
	for file in os.listdir('../../'):
		filename = os.fsdecode(file)
		if filename.endswith(".ipynb"):
			convert('../../'+filename)




def convert(file):
	html,res=nb.HTMLExporter(template_name='Classic').from_filename(file)
	html=html.replace('.ipynb">','.html">')
	f=open(file.replace('.ipynb','.html'),'w',encoding="utf-8")
	f.write(html)
	f.close()
	
	
	
main()
