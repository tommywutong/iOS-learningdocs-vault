---
title: X11CallCarbonAndCocoa
apple_id: DTS10000729
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/X11CallCarbonAndCocoa/Listings/Readme_txt.html
archived_at: '2026-07-18T03:28:28.509271Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [X11CallCarbonAndCocoa](X11CallCarbonAndCocoa.md)


[Next](main.c.md)[Previous](X11CallCarbonAndCocoa.md)

# Readme.txt

```
Read Me About X11CallCarbonAndCocoa

1.0

*Description: This sample gives developers a demo of how to create a double clickable X11 application made for MacOSX.  Also, more importantly this program demonstrates how basic X11 code can call directly into native MacOSX Carbon, Cocoa and the low-level CoreFoundation.  

*Important Note for running: To run this program you must have X11 installed and have the application running.

*Notes for X11 programmers: Pay particular attention to the build settings placed in project builder.  Specifically the following settings were added to the default "Carbon Application" project to make the application able to incorporate and use X11 (note these flags are eventually passed onto command line gcc): -I /usr/X11R6/include -L/usr/X11R6/lib  -lXaw -lXext -lXmu -lXt -lX11.  Note you can see _exactly_ what is being passed to gcc by building in project builder and opening the build window once the build is complete.

*What the sample does by default: This sample will display a X11 native window with a group of buttons.  Each button when clicked will perform some native operation in either Carbon, Cocoa or Core Foundation (for example: Putting up alerts or producing system beeps).

*Packing List:
¥ X11CallCarbonAndCocoa.app Ñ The prebuilt X11 application which can be launched simply by double clicking the application bundle.
¥ CarbonCode.h Ñ Header containing the Carbon API's that X11 calls.
¥ CarbonCode.c Ñ Carbon source file containing the implementation of all Carbon functions used in the program.
¥ CocoaCode.h Ñ Header containing the Cocoa API's that X11 calls.
¥ CocoaCode.c Ñ Cocoa source file containing the implementation of all Cocoa functions used in the program.
¥ CFCode.h Ñ Header containing the Core Foundation API's that X11 calls.
¥ CFCode.c Ñ Core Foundation source file containing the implementation of all Core Foundation functions used in the program.
¥ main.c Ñ The main file in the program used to initalize X11 and get things up and running.
¥ X11Code.h Ñ The header file containing the callable X11 functions in the program.  These are the functions which main calls to get the program up and running.
¥ X11Code.c - This file contains all the X11 code in the program.  It initializes X11 displays the dialog and even handles the button clicks which call into native Carbon, Cocoa and Core Foundation.
¥ X11CallCarbonAndCocoa.pbproj Ñ The project builder project file.
¥ Readme.txt Ñ This file.

*Sample Requirements:

For ProjectBuilder users: This project was built with ProjectBuilder Jaguar version as a standard tool.  This project relies on Carbon, CoreFoundation, Cocoa frameworks.  This project also relies on the X11 subsystem being installed (X11R6).

*Building the Sample:

Using Project Builder:  To build the sample simply open the Project builder file and hit the 'build' button.  Similarly the sample can be run simply by clicking the 'run' button.  Note when running the sample you do need to have the X11 application running ahead of time.

*Credits and Version History:

If you find any problems with this sample or have any suggestions, mail <dts@apple.com> with ÒAttn: Chad JonesÓ as the first line of your mail.

Version 1.0 is the first release.

Chad Jones
Apple Developer Technical Support
Networking, Communications, Hardware

Feb 28, 2003

---
```

[Next](main.c.md)[Previous](X11CallCarbonAndCocoa.md)

