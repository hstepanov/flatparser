https://api-docs-v2.readthedocs.io/ - api documentation.  
Before start bot, you should register at https://developers.ria.com/account and get your own API key (`apikey` variable).  
After that register your own Telegram bot and get bot token (`tg_token` variable).  
`user_id` variable stores your ID, which you can find using one of bots in telegram.  
All sensitive data stores as OS environment variables (`MY_TG_USER_ID`, etc.) and exports via .bashrc, for example.  
Example of sending message using curl:  
`curl 'https://api.telegram.org/bot<tg_token>/sendMessage?chat_id=<yours_tg_user_id>&text=test'`
