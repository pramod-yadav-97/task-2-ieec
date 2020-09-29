#!/usr/bin/python3
print("content-type:text/html\n")

import cgi
import subprocess
import pyttsx3

form=cgi.FieldStorage()
cmd=form.getvalue("query")

p = cmd.upper()


    if "DONT" in p or "NEVER" in p or "DO NOT" in p or "NEGATIVE" in p  :     # In case of Negative Input
        
        pyttsx3.speak(" => Ok as you wish")                           # discussed module so used for more user friendly and flexibility . 
                                                                #Thinking of how google respond
        
    elif(("RUN" in p) or ("LAUNCH" in p) or ("EXECUTE" in p) or ("START" in p) or ("OPEN" in p)):      # In open the software 
        if (("CODE" in p) or ("VS CODE" in p) or ( "VISUAL STUDIO CODE" in p) ):                      # launching software
            subprocess.getoutput("Code")
        elif (("CHROME" in p) or ("CHROME BROWSER" in p) or ( "GOOGLE CHROME" in p)):                  # launching software
            subprocess.getoutput("chrome")
        elif (("VLC" in p) or ("VLC PLAYER" in p) or ( "VLC MEDIA PLAYER" in p)):                  # launching software
            subprocess.getoutput("vlc")
        elif (("FIREFOX" in p) or ("FIREFOX BROWSER" in p)):                  # launching software
            subprocess.getoutput("firefox")
        elif (("PICASA" in p) or ("PICASA3" in p) or ("PICASA 3" in p)):                  # launching software
            subprocess.getoutput("picasa3")
        elif (("KMPLAYER" in p) or ("KM PLAYER" in p) or ("KM" in p)):                  # launching software
            subprocess.getoutput("KMPlayer")
        elif (("NOTEPAD" in p) or ("NOTEPAD EDITOR" in p) or ("NOTE" in p) ):                  # launching software
            subprocess.getoutput("notepad")
        elif (("CALC" in p) or ("CALCULATOR" in p) or ("CAL" in p)):                  # launching software
            subprocess.getoutput("CALC")
        elif(("WINDOWS FAX AND SCAN" in p) or ("WFS" in p) or ("WINDOWS FAX" in p) or ("WINDOWS SCAN" in p)):                     # launching software
            subprocess.getoutput("wfs")
        elif(("PAINT" in p) or ("MSPAINT" in p) or ("MS PAINT" in p) or ("MICROSOFT PAINT" in p)):                                            # launching software
            subprocess.getoutput("mspaint")
        elif(("QUICKASSIST" in p) or ("QUICK ASSIST" in p)):                                                              # launching software
            subprocess.getoutput("quickassist")
        elif("SNIPPING TOOL" in p):                                                                       # launching software
            subprocess.getoutput("snippingtool")
        else:
            pyttsx3.speak("Please launch only supported softwares \nMake sure you have the software file location in your user environment variable in case of any launching issue\n ")
    