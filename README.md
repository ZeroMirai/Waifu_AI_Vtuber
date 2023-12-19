# Waifu_AI_Vtuber

Waifu_AI_Vtuber is a Python-based AI virtual YouTuber chatbot. The chatbot interacts with live YouTube chat, processes the messages, generates responses using the OpenAI GPT-3.5 model, and provides text-to-speech audio output for responses using VoiceVox engine.

![Example Image](guide/example.gif)
---
## Table of Contents

- [Waifu_AI_Vtuber](#waifu_ai_vtuber)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [File Structure](#file-structure)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Contributing](#contributing)
    - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
    - [Pull Requests](#pull-requests)
  - [Note](#note)
  - [License](#license)
  - [Credits](#credits)
    
## Features

- Real-time interaction with YouTube live chat.
- Utilizes OpenAI GPT-3.5 model for generating chat responses.
- Converts generated responses into Japanese text-to-speech audio.
- Creates subtitle files in any language that can be used in obs.
- Customizable character names and their prompt.

## Prerequisites

- **Python** Version 3.11. Download it [here](https://www.python.org/downloads/).
- **API keys** from OpenAI and AssemblyAI, you can get it from here [OpenAI](https://platform.openai.com/api-keys), [AssemblyAI](https://www.assemblyai.com/app/account).
- **VoiceMeeter banana** Download it [here](https://vb-audio.com/Voicemeeter/banana.htm), installed and running
- **Voicevox software** Version 0.14.7 or higher. Download it [here](https://voicevox.hiroshiba.jp/), installed and running
- **EarTrumpet** Download it [here](https://eartrumpet.app/), installed and running.
- **Open Broadcaster Software**. Download it [here](https://obsproject.com/).
- **Vtuber Studio**. Download it [here](https://denchisoft.com/)

## Installation

1. Download [OBS](https://obsproject.com/), [Vtuber studio](https://denchisoft.com/), [EarTrumpet](https://eartrumpet.app/), [VoiceMeeter banana](https://vb-audio.com/Voicemeeter/banana.htm)(after you install VoiceMeeter banana you'll also need to restart your PC) and open VoiceVox.
2. For VoiceMeeter banana, we need to change voice output and voice input first.
   1. Open the Control Panel by pressing the `Windows key` and typing `Control Panel`. In the upper right corner, click on `View by` and select `Large icon`.
      
      ![guide_1](guide/1.png)
      ![guide_2](guide/2.png)
      
   2. Click on `Sound`, scroll down until you see `VoiceMeeter Input`, and then click on it. Finally, click `Set Default`.
      
      ![guide_3](guide/3.png)
      ![guide_4](guide/4.png)
      
   3. Click on `Recording` at the top, scroll down until you see `VoiceMeeter Aux Output`, click on it, and then click `Set Default`.
      
      ![guide_5](guide/5.png)
      ![guide_6](guide/6.png)
      
   4. The first time the program is opened, it would look like this.
      
      ![guide_7](guide/7.png)
      
   5. Click on each `A1` to deselect them on all five panels. Similarly, do the same with `B1`. It should now look like this.

      ![guide_8](guide/8.png)
      ![guide_9](guide/9.png)
      
   6. On the upper right corner, click on `A1` and select your speaker output (WDM is recommended).
       
      ![guide_10](guide/10.png)
      ![guide_11](guide/11.png)

   7. Now, click on `A1` for all VIRTUAL INPUTS. However, for VOICEMEETER AUX, you'll also need to click on `B1`.
       
      ![guide_12](guide/12.png)

3. For Vtuber Studio.
   1. Open the settings by double-clicking on the screen and then click on the gear icon located on the left side.
      
      ![guide_13](guide/13.png)
      
   3. Scrolldown until you see `Microphone Setting` check `Use microphone` and select `VoiceMeeter Output (VB-Audio VoiceMeeter VAIO)` by clicking on the `Microphone`.
      
      ![guide_14](guide/14.png)
      ![guide_15](guide/15.png)
      
   3. Go to Model setting at the top left corner(a people icon with a gear). Scroll down until you see `Mouth Open`. Click on `input` and select or type `VoiceVolumePlusMouthOpen`.
      
      ![guide_16](guide/16.png)
      ![guide_17](guide/17.png)
      ![guide_18](guide/18.png)
      
   4. **Optional**: In `Microphone Setting`, I recommend setting `Volume gain` to 20 and everything else is set to 0.
4. For OBS, we'll add subtitles to display the text, and for Vtuber studio, we'll use it to show Live2D.
   1. To add a subtitle, press `+` in the source, select `Text(GDI+)`, and name it as `Subtitle`.
      
      ![guide_19](guide/19.png)
      ![guide_20](guide/20.png)
      
   2. After adding the text source, a window will appear like this. You'll need to check `Read from file` and then click `Browse`.
      
      ![guide_21](guide/21.png)
      ![guide_22](guide/22.png)
      
   3. Navigate to `subtitle.txt`, which is located inside the `text_log` folder, and select it.
      
      ![guide_23](guide/23.png)
      
   4. Customize and configure the subtitle file according to your preferences, (For my recommendation, I suggest reducing the size of the text, setting `Alignment` to center and `Verticle alignment` to center, right-clicking on the text, navigating to `Tranform` and selecting `Center Horizontally`. Also, check `Outline`, set the outline size to 10-14, and change the outline color to black by clicking on `Select color`).
      
      ![guide_24](guide/24.png)
      ![guide_25](guide/25.png)
      ![guide_26](guide/26.png)

   5. To add Vtuber Studio, press `+` in the source, select `Window Capture` and name it as `Live2D`
       
      ![guide_27](guide/27.png)
      ![guide_28](guide/28.png)
      
   6. After adding the video source, a window will appear like this. Click on `Window`, select `[VTube Studio.exe]: VTube Studio`, on `Capture Method` choose `Windows 10 (1903 and up)`, and then click `OK`.
       
       ![guide_29](guide/29.png)
       ![guide_30](guide/30.png)
       
   7. Right-click on the preview screen, choose `Windowed Projector (Preview)`, and resize it as your desire.
       
       ![guide_31](guide/31.png)
5. Running the code, open EarTrumpet and scroll down to the bottom you'll see `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)`, right click on `Python 3.11.xx` and click on `change` icon, select `VoiceMeeter Aux Input (VB-Audio VoiceMeeter AUX VAIO)`.
   
   ![guide_33](guide/33.png)
   ![guide_34](guide/34.png)
   ![guide_35](guide/35.png)
   
6. Change your `playback/output device` by clicking on the speaker icon on the taskbar (or go to `window setting` -> `System` -> `Sound` -> `Choose your output device`). Select `VoiceMeeter Aux Input (VB-Audio VoiceMeeter AUX VAIO)` first and then selcet `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` (we need to do this process to let Python recognize these playback devices).
   
   ![guide_36](guide/36.png)
   ![guide_37](guide/37.png)
   
7. In Vtuber Studio, open the settings, navigate to `Microphone Setting` and click on `Reload`.
8. Download the project zip file from GitHub or Clone this repository by typing these in terminal or command prompt (but if you choose to download the project as a zip file you'll also need to extract the zip file).
   ```
   git clone https://github.com/ZeroMirai/VirtuAI-Helper.git
   ```
    
9. Open a terminal or command prompt and change the directory to the project folder by typing `cd` followed by where this folder is located for example `cd C:\Git_hub\VirtuAI Helper`.
10. Install all necessary library by typing.
   ```
   pip install -r requirements.txt
   ```
11. Configure the necessary API keys and other config in config.txt.

## File Structure

- 📁`functions`: Contains modular components of the project.
  - 📁`keys`: folder to contain API keys.
    - 📝`api_key_chat`: File to store configuration for chatGPT's API keys.
  - 📝`chatbot.py`: Code to interact with the OpenAI GPT-3.5 model to create responses.
  - 📝`create_subtitle.py`: Code to generate subtitle files to use in obs.
  - 📝`tts.py`: Code for text-to-speech using Voicevox.
- 📝`main.py`: Main code for the AI virtual YouTuber chatbot.
- 📝`youtube_chat.py`: Code to read and process YouTube live chat messages.

## Configuration

Before running the program, Ensure you have changed all the configurations and **pasted them right after the : in the file**. The file must have the following format.

- Configure API keys and settings in the code files as specified in the comments in `api_key_chat.py` to generate chat responses and `youtube_chat.py` to capture a youtube live chat.
- Update `main.py` with the character's name.
- Update `youtube_chat.py`, in `video_id` get your video id at your youtube live url and paste it here. For example `https://www.youtube.com/watch?v=CSdEsXa` your video id is `CSdEsXa`.
- you can create your own AI personality by changing the prompt in the `RoleAndStory.txt` **but don't change the rule part** (if you are too lazy to write your own prompt you can also ask chatGPT to make your own one by asking).
  ```
  Generate me a prompt so I can use with my AI assistant "that's a ..(personality,gender,traits).., ..(other personality,gender,traits).."
  ```

## Usage

1. Open VoiceVox engine.
2. Open `run.bat`.
   
---
## Contributing

Actually, this is a project that's made just for fun but if you are interested to contribute in this project here is how you can make this project better for everyone:

### Bug Reports and Feature Requests

If you found a bug or have an idea for a new feature, feel free to requests and reports by [open an issue](https://github.com/ZeroMirai/Waifu_AI_Vtuber/issues) on GitHub and post it if it's a bug please give as much detail as possible or suggest an idea please include a step or a clear description.

### Pull Requests

If you have suggestions or improvements.

1. Fork the repository and create your own branch from `main`.
2. Work on your changes.
3. Write clear, concise commit messages that describe the purpose of your changes.
4. Open a pull request and provide a detailed description of your changes.

I'm primarily looking for code improvements and bug fixes. Once your changes are approved, they will be merged into the main project.

### ⭐ Share and Give a Star ⭐

**If you find this project useful I would be really grateful if you could consider sharing this small project with others and giving it a star on GitHub.**

---

## Note

- Running **main.py** and **youtube_chat.py** simultaneously is necessary for the chatbot to function correctly.
- Make sure you have the required dependencies and API keys set up before running the code.
- If text in obs is not showing, make sure  you place the Subtitle source above the Live2D source.
- Ensure that you have the required dependencies and configuration set up before running the code.
- Running the program and VoiceVox engine simultaneously is necessary for proper program functionality.
- You need to redo steps 5-8 every time the program is opened.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- **Pytchat** - Used for real-time YouTube chat interaction. For more information, visit [Pytchat](https://github.com/taizan-hokuto/pytchat)
- **OpenAI** - Used to generate responses with the chatGPT model. For more information, visit [OpenAI API](https://openai.com/)
- **Voicevox** by Hiroshiba - Used to synthesize speech in Japanese. For more information, visit [VoiceVox Engine](https://voicevox.hiroshiba.jp/)

Special thanks to [Neuro-sama](https://www.twitch.tv/vedal987), who inspired me to start learning how to code and create my own waifu.

