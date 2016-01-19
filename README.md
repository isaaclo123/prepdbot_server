# prepdbot_server
Prepdbot is a script that automatically cuts articles for [Prepd](https://prepd.in) from given RSS feeds.

##Server Configuration
* TCP_IP: server IP
* TCP_PORT: server port
* BUFFER_SIZE: server buffer size
* RSSFeeds: An array with the URLs for the RSS feeds used to cut articles.
** In the format [["RSS-URL1", "FOLDERNAME1"], ["RSS-URL2", "FOLDERNAME2"]]

##Client Configuration
* UserName: your Prepd username
* Password: your Prepd password
* FolderName: the folder you want you articles to be cut to
* WaitTime: time to wait for your RSS-given webpage or for Prepd to load
* ChromiumBinary: location of your chromium browser binary
* UserNameLocation: location to click to enter your username
* PasswordLocation: location to click to enter your password
* PrepdButtonLocation: location to click you prepd extension button
* FolderSelectLocation: location to enter your folder name for Prepd
* CatchButtonLocation: location to click the Prepd "Catch" button (after folder is entered)

##Dependacies
* Python 2.7
** feedparser
** socket
** pickle
** pyautogui
* chromium-browser
** Prepd Article Catcher
* (all subdependacies)

##Instructions
1. Run the server script from the server computer/VM.
2. Run the client scripts from the client computer(s)/VM(s).
3. Have fun!
