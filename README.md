# Translate-Files-to-different-languages

### To use the bulk File translator

1. Go to the Bulk file translator directory
2. Open up the terminal and type/copy paste the following command: 

   ```
   python3 translatorr.py to_translate translated
   ```
3. To translate your own files:

   `python3 translatorr.py {your_file_to_be_translated} {the_name_of_directory_you_want_to_store_the_translated_files_in}`

### Changing the languages

The translatorr will by default translate to Japanese.

To change the language:

1. Navigate to [line 5](https://github.com/adrinorosario/Translate-Files-to-different-languages/blob/main/Bulk%20File%20Translator/translatorr.py) and change the `to_lang('ja')` to any other language code. `ja` is the code of Japanese language.

2. You can check the different language codes [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
