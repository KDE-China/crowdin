# crowdin
Crowdin localization workflow (experimental)

1. update: download latest code from SVN
2. upload_sources: upload latest templates to Crowdin
3. download_translations: download latest translations from Crowdin
4. merge: automatically merge Crowdin to SVN
5. commit: commit merged translations to SVN
  a. Automatical: ideal solution, just run commit script.
  b. Manual: use svn command to commit only changed files, need to review
6. update: download and override local translations
7. upload_translations: upload merged translations from SVN to Crowdin

Sync process will take hours. So sync every week is a practical choice.
