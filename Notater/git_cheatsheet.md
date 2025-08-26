git init                    # Gjør mappa til et git-repo
git add .                   # Legg til alle filer
git commit -m "første commit"
git branch -M main          # Gi hovedbranch navnet "main"
git remote add origin https://github.com/<brukernavn>/<repo>.git
git push -u origin main     # Push til GitHub
git clone https://github.com/<brukernavn>/<repo>.git
git add .                   # Legg til alle endringer
git commit -m "beskriv endringene"
git push                    # Send til GitHub
git pull
git status                  # Sjekk hvilke filer som er endret
git log --oneline           # Kort commit-historikk
