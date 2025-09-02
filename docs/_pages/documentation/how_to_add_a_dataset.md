---
title: How to add a data set
layout: single
permalink: /documentation/how_to_add_a_dataset/
---

TODO: Explain how to add a dataset

Step by Step guide to adding your dataset to the DLAB organization
--

#  1) Create repository in organization

1. Go to the **DLAB organization** page on GitHub.
2. Click the **"Repositories"** tab.
3. Click the green **"New"** button (top right).
4. Make the repo **public**. 
5. Give the repo a descriptive name and create it.

***

#  2) Metadata.json file follows schema 1 file template

1. Go to the datalake repository.
2. Locate the file `schema_1.0.json` — this is your metadata **template**.
3. In your own dataset repo:
   - Click the **"Add File"** dropdown near the green **"<> Code"** button.
   - Select **"Create new file"**.
   - Name it `metadata.json`.
5. Copy the contents of `schema_1.0.json` into your new `metadata.json`.
6. Replace the placeholder values with your dataset’s real information.
7. Click **"Commit new file"** to save it to the repo.

***

# 3) Steps to set up git sub modular repo

1. Platform to run git commands
   - CMD
   - Git Bash
   - Github Desktop
   - VS Code
2. GUIDE FOR: Open terminal or Powershell in VS Code
3. Clone your main repo to your local devices
4. Run these commands:
   - git clone URL
   - cd REPONAME
   - ex) git clone https://github.com/sadak2004/gitsubmodulerepo.git
   - cd gitsubmodulerepo
5. Now add the second repo as a submodule repo inside a folder.
6. Run these commands:
   - Git submodule add URLSUBREPO
   - ex) git submodule add https://github.com/sadak2004/subrepo.git
   - For adding inside a folder:
   - ex) git submodule add https://github.com/sadak2004/subrepo.git FOLDERNAME/REPONAME
7. Commit and push the changes.
8. Run these commands:
   - git add .gitmodules REPONAME
   - git commit -m "COMMIT MESSAGE"
   - git push origin main
9. For further help/information: visit this link https://gist.github.com/gitaarik/8735255


***

