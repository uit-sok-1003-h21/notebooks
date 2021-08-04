# Tips and tricks:
 1. clone this repository: 
 
         git clone https://github.com/uit-sok-1003-h21/notebooks/
     
 2. Start jupyter notebook in a custom directory (D:/myfiles here): 
 
         jupyter notebook --notebook-dir=D:/myfiles
         
 3. commit: 
 
         git add .
         git commit -m "text"
     
 4. push: 
         
         git push
 
 5. pull: 
     
         git pull
         
     a) If files have changed, and you want discard those changes:
         
         git reset --hard
         git pull
     
     b) If files have changed, and you want discard those changes, but also stash the changes in a dirty working directory.
     
         git stash
 
 5. Install spell check for Jupyter notebook, in console:
 
        pip install jupyter_contrib_nbextensions
        jupyter contrib nbextension install --user
        jupyter nbextension enable spellchecker/main
        
    To install Norwegian dictionary:
    1. go to https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/spellchecker/README.html
    2. run
    
        from jupyter_core.paths import jupyter_data_dir
        jupyter_data_dir()
        
        The result will show the location of the data directory with the directory structure mentioned on the web-page above. 
    3. Crate a folder `dictionaries`under `spellchecker` adn copy [nb_NO.aff](./dictionaries/nb_NO.aff) and [nb_NO.dic](./dictionaries/nb_NO.dic) from the `dictionaries` folder here to the newly created folder.
    4. Copy the code from the wepage above to a notebook, replace de_DE with nb_NO, and run it.. 
        