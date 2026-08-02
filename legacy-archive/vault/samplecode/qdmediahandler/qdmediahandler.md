---
title: qdmediahandler
apple_id: DTS10000820
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qdmediahandler/Introduction/Intro.html
archived_at: '2026-07-18T03:29:55.528479Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](dllmain.c.md)

# qdmediahandler

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Illustrates one way to write a derived media handler. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This sample code has been updated for QuickTime 5.0 README - QDrawMHdlr ABOUT QDrawMHdlr This sample code illustrates one way to write a derived media handler. It's based on the code described in the article "Somewhere in QuickTime: Derived Media Handlers" in develop, issue 14. That article shows how to store QuickDraw pictures as the media in a track. The current sample expands on the original code by making it PowerPC-savvy and cross-platform. Mac OS Build Instructions: Build either the PPC or 68K project using CodeWarrior; then install the resulting extension in the Extensions folder in the System folder and reboot. Alternatively, just drop the extension onto a utility like Reinstaller to make the media handler immediately available. Windows Build Instructions: Build the Windows DLL using CodeWarrior; then copy the DLL to a Windows machine, along with the files QDrawHandler.r, QDMediaCommon.h, and QDrawMHdlr.rez.bat. Once all these files are on a Windows machine, run the batch file QDrawMHdlr.rez.bat, which should create the file QDrawMHdlr.qtx. Move that .qtx file into the System folder in the Windows folder. (You may need to edit the .bat file if the Rez and RezWack utilities are not located in the folder QuickTimeSDKQTDevWinTools.) If you are using MS-Dev, just build the project and then run the batch file QDrawMHdlr.rez.bat; move the .qtx file as described in the preceding paragraph. Enjoy!

[Next](dllmain.c.md)

