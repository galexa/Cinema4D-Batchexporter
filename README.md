## What?
This is based on [joppevos/Cinema4D-FBX-Batchexporter: Batch FBX-exporter for Cinema4D](https://github.com/joppevos/Cinema4D-FBX-Batchexporter). 

I couldn't get it to work on my Mac. I suspect it's fine on Windows (since it specifies a Windows location for the scripts folder).

## Why?
I have a lot of **pre-r19 files** that I needed to save out from r19 so I could open them in later versions. I also thought it might useful to have alternate formats in case I stopped using c4d. 

This will ask for a folder of .c4d files and export into folders for .obj, .fbx  and .c4d. Saving to .c4d also seems to allow you to close all files without having to confirm with a save / not save dialogue but there may be a better way around that if you want to change it back to just exporting fbx.


## How?
Place in the Cinema4D scripts folder and restart (You can find your scripts folder by clicking the 'Open Preferences Folder' at the bottom of the Preferences dialogue) or just run it straight in Cinema's script-manager - Script > User Scripts > Run Script... (in r19). It's fairly simple and opening Script > Console should show up any problems.

This was tested in Cinema4D r19 on a Mac running Monterey (OS 12). I'm no expert so make copies and use those if you're worried.



