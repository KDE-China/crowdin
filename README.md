# crowdin
Crowdin localization workflow (experimental)

1. update: download latest code from SVN
2. upload_sources: upload latest templates to Crowdin
3. download_translations: download latest translations from Crowdin
4. Manually sync from crowdin to upstream folder with Lokalize. Each changed string should be reviewed. Changed files can be found in Crowdin recent activities.
5. commit: commit merged translations to SVN
6. update: download and override local translations
7. upload_translations: upload merged translations from SVN to Crowdin

The process can be simplified by 3 steps:

1. before_merge: step 1, 2, 3
2. Manually merge
3. after_merge: step 5, 6, 7
