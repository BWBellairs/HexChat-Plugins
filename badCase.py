import hexchat
import random

__module_name__ = 'badcase'
__module_author__ = 'BWBellairs'
__module_version__ = '0.1.0'
__module_description__ = 'Makes messages you send annoying'

enabled = False

def toggle(words, word_eols, userdata):
    global enabled

    enabled = not enabled

    if enabled:
        hexchat.prnt("badcase text is now enabled")

    else:
        hexchat.prnt("badcase text is now disabled")

def converter(key, data, userdata):
    global enabled
    
    if not enabled:
        return hexchat.EAT_NONE
    
    if key[0] == "65293":
        if (hexchat.get_info("inputbox").startswith("/")):
            return hexchat.EAT_NONE
        
        output = ""
        lower = random.choice([False, True])
        for word in hexchat.get_info("inputbox").strip(" ").split(" "):
            newWord = ""
            for letter in word:
                if not lower:
                    letter = letter.upper()

                else:
                    letter = letter.lower()

                newWord = newWord + letter

                lower = not lower
                
            output = output + " " + newWord if output else output + newWord

        hexchat.command("say " + output)
        hexchat.command("settext  ")

        return hexchat.EAT_ALL

    return hexchat.EAT_NONE

hexchat.hook_print("Key Press", converter)
hexchat.hook_command("badcase", toggle)
