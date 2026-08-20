---
title: PIDFromBSDProcessName
apple_id: DTS10000741
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2003-02-13'
source_url: https://developer.apple.com/library/archive/samplecode/PIDFromBSDProcessName/Listings/Readme_txt.html
archived_at: '2026-07-18T03:18:34.862004Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIDFromBSDProcessName](PIDFromBSDProcessName.md)


[Next](main.c.md)[Previous](PIDFromBSDProcessName.md)

# Readme.txt

```
Read Me About PIDFromBSDProcessName

1.0

*Description: This sample gives developers an simple API which allows lookup of Process PID based on BSD process name.  This also allows developers at the UNIX level to determine if a process is running or not.

*What the sample does by default: Returns a list of PIDs for predefined processes like the Finder and init

*Packing List:
¥ GetPID.h Ñ Header to the PID lookup API. 
¥ GetPID.c Ñ Source to the PID lookup API.  This does all the work of looking up the process in the process list and returning the PID for the process.
¥ main.c Ñ The main file in the program and a demonstration file showing how to lookup processes PIDs based on Process Name.       
¥ PIDFromBSDProcessName.pbproj Ñ The project builder project file.
¥ Readme.txt Ñ This file.

*Sample Requirements:

For ProjectBuilder users: This project was built with ProjectBuilder Jaguar version as a standard tool.  This project relies on no frameworks and only the underlying BSD subsystem.

*Building the Sample:

Using Project Builder:  To build the sample simply open the Project builder file and hit the 'build' button.  Similary the sample can be run simply by clicking the 'run' button.

*Credits and Version History:

If you find any problems with this sample or have any suggestions, mail <dts@apple.com> with ÒAttn: Chad JonesÓ as the first line of your mail.

Version 1.0 is the first release.

Chad Jones
Apple Developer Technical Support
Networking, Communications, Hardware

Feb 10, 2003
```

[Next](main.c.md)[Previous](PIDFromBSDProcessName.md)

