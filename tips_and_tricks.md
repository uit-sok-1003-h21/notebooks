# Tips and tricks:
 1. Klone dette repositoriet: 
 
         git clone https://github.com/uit-sok-1003-h21/notebooks/
     
 2. Starte Jupyter i bestemt mappe (D:/myfiles here): 
 
         jupyter notebook --notebook-dir=D:/myfiles
         
 3. commit: 
 
         git add .
         git commit -m "text"
     
 4. push: 
         
         git push
 
 5. pull: 
     
         git pull
         
     a) Om filer er endret, og du ønsker å overskrive endringene:
         
         git reset --hard
         git pull
     
     b) Om filer er endret, og du ønsker å overskrive endringene, men også ta vare på endringer.
     
         git stash
         
 6. Lage git-repositorie:

     1. Lag en githubkonto (du trenger ikke bruke din uit-mail, det er valgfritt)
     2. Logg på `jupyter.uit.no`, og åpne ny Terminal (+), og naviger dit du vil ha repositoriet på jupyter.
     3. Konfigurer git med e-posten til kontoen og ditt brukernavn (bytt ut klammeparentesene med e-posten og brukernavnet til githubkontoen):
        ```
        git config --global user.email "<e-post>"
        git config --global user.name "<brukernavn>"
        ```
     4. Gå til **Repositories**, trykk **New**, gi repositoriet et navn og velg **Private** eller **Public**. 
     5. Kopier html-lenken
     6. Sørg for at du har et token. Gå eventuelt til https://github.com/settings/tokens/new for å generere nytt token.
     7. kjør `git clone https://<token>@github.com/<sti>` der <token> er tokenet du fikk i g) og <sti> er det som står i adressen etter **github.com/**  når du trykker "html"-knappen i repositoriet ditt på github
 
      Du kan nå redigere repositoriet ditt
 
 7. Dytte repositoriet til github:
    a) Naviger til repositoriemappen i Terminal
    b) Kjør i Terminal:
       ```
       git add .
       git commit -m "New repository"
       git push 
        ```
      
      
 
 5. Installere stavekontroll for i lokal Jupyter notebook:
 
        pip install jupyter_contrib_nbextensions
        jupyter contrib nbextension install --user
        jupyter nbextension enable spellchecker/main
        
    For å installere norsk stavekontroll:
    1. gå til https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/spellchecker/README.html
    2. kjør
    
        from jupyter_core.paths import jupyter_data_dir
        jupyter_data_dir()
        
        Resultatet viser stien nenvnt i lenken over. 
    3. Lag en mappe `dictionaries` under `spellchecker` i ovvenenvnte sti.
    4. Kopier [nb_NO.aff](./dictionaries/nb_NO.aff) og [nb_NO.dic](./dictionaries/nb_NO.dic) fra `/instructions/dictionaries` mappen i dette repositoriet til mappen du nettopp laget.
    5. Kopier koden fra nettsiden over til en notebook, bytt ut de_DE med nb_NO, og kjør det.
        
