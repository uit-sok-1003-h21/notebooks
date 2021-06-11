# Tips and tricks:
 1. clone this repository: git clone https://github.com/uit-sok-1003-h21/notebooks/
 2. Start jupyter notebook in a custom directory (D:/myfiles here): 
         jupyter notebook --notebook-dir=D:/myfiles
 3. commit: 
     1. git add .
     1. git commit -m "text"
 4. push: git push
 
 5. pull: git pull
     a) If files have changed, and you want discard those changes:
         
         git reset --hard
         git pull
     
     b) If you want stash the changes in a dirty working directory away
     
         git stash
 
 5. Install spell check for Jupyter notebook, in console:
        pip install jupyter_contrib_nbextensions
        jupyter contrib nbextension install --user
        jupyter nbextension enable spellchecker/main
        
    To install Norwegian dictionary: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/spellchecker/README.html#dictionaries
    Replace "de_DE" with "no_NO", and download the dictionaries from the linked chromium site. Convert the files to "UTF-8", and change the encoding in the first line of the no_NO.aff file to "UTF-8"