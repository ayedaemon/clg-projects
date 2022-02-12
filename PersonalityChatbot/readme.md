Simple Personality based chatbot in python and tensorflow



##Usage

Step 1: create a data folder in your project directory, download the Cornell Movie-Dialogs Corpus from https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html Unzip it

Step 2: update config.py file
Change DATA_PATH to where you store your data

Step 3: python3 data.py
This will do all the pre-processing for the Cornell dataset.

Step 4: python3 chatbot.py --mode [train/chat]
If mode is train, then you train the chatbot. By default, the model will restore the previously trained weights (if there is any) and continue training up on that.

If you want to start training from scratch, please delete all the checkpoints in the checkpoints folder.

If the mode is chat, you'll go into the interaction mode with the bot.

By default, all the conversations you have with the chatbot will be written into the file output_convo.txt in the processed folder. If you run this chatbot.
