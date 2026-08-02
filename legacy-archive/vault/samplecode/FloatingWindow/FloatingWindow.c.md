---
title: FloatingWindow
apple_id: DTS10000633
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-24'
source_url: https://developer.apple.com/library/archive/samplecode/FloatingWindow/Listings/FloatingWindow_c.html
archived_at: '2026-07-18T03:08:46.818846Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FloatingWindow](FloatingWindow.md)


[Next](Document%20Revision%20History.md)[Previous](FloatingWindow.md)

# FloatingWindow.c

```c
/*
    File:   FloatingWindow.c    

    Contains:   A trivial sample on how to create a floating window

    Written by: Karl Groethe

    Copyright:  Copyright © 2000 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                6/28/00     created


*/
#include<Carbon/Carbon.h>

int main(int argc, char* argv[])
{
    IBNibRef        nibRef;
    WindowRef       window;
    WindowRef       floatingWindow;
    WindowRef       floatingSidebar;

    /*setup interface from nib file*/
    CreateNibReference(CFSTR("Main"), &nibRef);
    SetMenuBarFromNib(nibRef, CFSTR("MainMenu"));
    CreateWindowFromNib(nibRef, CFSTR("MainWindow"), &window);
    CreateWindowFromNib(nibRef, CFSTR("FloatingWindow"),&floatingWindow);
    CreateWindowFromNib(nibRef, CFSTR("FloatingSidebar"),&floatingSidebar);
    DisposeNibReference(nibRef);

    /*show the windows*/
    ShowWindow(window);
    ShowWindow(floatingWindow);
    ShowWindow(floatingSidebar);

    RunApplicationEventLoop();

    return 0;
}
```

[Next](Document%20Revision%20History.md)[Previous](FloatingWindow.md)

