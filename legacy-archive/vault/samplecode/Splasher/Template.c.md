---
title: Splasher
apple_id: DTS10000618
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Splasher/Listings/Template_c.html
archived_at: '2026-07-18T03:25:19.616338Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Splasher](Splasher.md)


[Next](Document%20Revision%20History.md)[Previous](Splasher.md)

# Template.c

```c
/*
    File:       Template.c

    Contains:   splasher:  A very simple application that displays a "modal" window that goes
                away as soon as you click the mouse or press a key.  This is how many splash
                screens behave -- but as long as the window is displayed, the Process Manager
                won't switch your application from being frontmost.

    Written by:     

    Copyright:  Copyright © 1984-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#include <Quickdraw.h>
#include <Fonts.h>
#include <Windows.h>
#include <Dialogs.h>
#include <TextEdit.h>
void main()

{

GrafPort myPort;
WindowPtr myWindow;
EventRecord myEvent;
Boolean doQuit;


    InitGraf((Ptr) &qd.thePort);
    OpenPort(&myPort);
    InitFonts();
    InitWindows();
    InitMenus();
    TEInit();
    InitDialogs(nil);
    InitCursor();

    doQuit = false;
    myWindow = GetNewWindow(128, NULL, (WindowPtr)-1L);
    SetPort(myWindow);
    MoveTo(15,15);
    DrawString("\pThis is our splash screen test of the mouse...");
    while (doQuit == false) {
        if(WaitNextEvent(everyEvent, &myEvent, 10L, NULL)) {
            switch (myEvent.what) {
            case mouseDown:
            case autoKey:
            case keyDown: {
                DisposeWindow(myWindow);
                doQuit = true;
                break;
                }
            };
        }
    }
    ExitToShell();
}
```

[Next](Document%20Revision%20History.md)[Previous](Splasher.md)

