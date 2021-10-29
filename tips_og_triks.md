# Tips og triks:

## 1. Navigere i mappestrukturen med *Terminal*:

1. Gå til jupyter.uit.no, trykk på "+" dersom "launcher"-fanen ikke er oppe, og trykk på "Terminal"
2. For å navigere til en bestemt mappe:
```
cd <mappenavn>
```
der du bytter ut \<mappenavn\> med mappen du vil navigere til
    
3. For å navigere opp ett nivå i mappestrukturen:
```
cd ..
```

## 2. Klone dette repositoriet: 
```
git clone https://github.com/uit-sok-1003-h21/notebooks/
```    
 
## 3. Starte Jupyter i bestemt mappe ('D:/myfiles' i dette tilfellet): 
```
jupyter notebook --notebook-dir=D:/myfiles
```        
 
## 4. commit: 
```
git add .
git commit -m "text"
```   
 
## 5. push: 
```  
git push
```
 
## 6. pull: 
```     
git pull
```
1. Om filer er endret, og du ønsker å overskrive endringene:
```
git reset --hard
git pull
```

2. Om filer er endret, og du ønsker å overskrive endringene, men også ta vare på endringer.
```
git stash
```  
 
## 7. Lage git-repositorie:
[Se her for en forklaring på hvordan du skal levere arbeidskrav på github](https://uit-sok-1003-h21.github.io/github.html)

1. Lag en githubkonto (du trenger ikke bruke din uit-mail, det er valgfritt)
2. Logg på `jupyter.uit.no`, og åpne ny Terminal (+), og naviger dit du vil ha repositoriet på jupyter med `cd <mappenavn>`.
3. Konfigurer git med e-posten til kontoen og ditt brukernavn (bytt ut klammeparentesene med e-posten og brukernavnet til githubkontoen):
```
git config --global user.email "<e-post>"
git config --global user.name "<brukernavn>"
```
4. Gå til **Repositories**, trykk **New**, gi repositoriet et navn og velg **Private** eller **Public**. 
5. Hold denne fanen åpen, for du skal bruke html-adressen til denne siden.
6. Sørg for at du har et token. Gå eventuelt til https://github.com/settings/tokens/new for å generere nytt token. *Hold fanen åpen for å ha tokenet tilgjengelig.*
7. kjør `git clone https://<token>@github.com/<sti>` der \<token\> er tokenet er det du fikk i 6. og \<sti\> er det som kommer etter **github.com/**  i html-adressen i 5.

 Du kan nå redigere repositoriet ditt
 
 
## 8. Dytte repositoriet til github:
1. Naviger til repositoriemappen i Terminal (se avsnitt 1.)
2. Kjør i Terminal:
```
git add .
git commit -m "New repository"
git push 
```

Dersom du får en rettighetsfeil kan du forsøke å legge inn, etter `git push`, nettadressen som beskrevet i pkt. 7.7 over. 
      
      
 
 
## 9. Installere stavekontroll for i lokal Jupyter notebook:
```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
```
 
For å installere norsk stavekontroll:
1. gå til https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/spellchecker/README.html
2. kjør
 
```
from jupyter_core.paths import jupyter_data_dir
jupyter_data_dir()
```
 
Resultatet viser stien nenvnt i lenken over. 
3. Lag en mappe `dictionaries` under `spellchecker` i ovvenenvnte sti.
4. Kopier [nb_NO.aff](./dictionaries/nb_NO.aff) og [nb_NO.dic](./dictionaries/nb_NO.dic) fra `/instructions/dictionaries` mappen i dette repositoriet til mappen du nettopp laget.
5. Kopier koden fra nettsiden over til en notebook, bytt ut de_DE med nb_NO, og kjør det.
        
## 10. Fjerne en mappe og alt dets innhold (FARLIG!)

Dersom en mappe har innhold som er vanskelig å fjerne, slik som et git-repositorie, kan det være du må da kjøre en kommando i Terminal for å fjerne mappen. Du må da kjøre en kommando i Terminal for å fjerne mappen. For å fjerne en mappe og alt innholdet, navigerer du til mappen over (se 3.), slik at om du kjører `dir` så ser du navnet på mappen (samme med eventuelt andre filer og mapper). Du kjører så
```
rm -r <navn på mappe du vil ha fjernet>
```
Bytt ut ´<navn på mappe du vil ha fjernet>´ med mappen du vil slette. 

MERK at dette sletter mappen FOR EVIG OG ALLTID! Den kan ikke gjenoprettes, så VÆR HELT SIKKER før du gjør dette. Du må være HELT sikker på hvor du er i mappestrukturen i terminal, slik at du ikke sletter noe uforvarende. 

Når du har kjørt kommandoen, vil du få gjentatte spørsmål om du vil slette hver enkelt fil. Trykk `y` og Enter på hvert spørsmål. 