---
title: CustomWindow
apple_id: DTS10000566
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/CustomWindow/Listings/main_c.html
archived_at: '2026-07-18T03:05:43.673407Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CustomWindow](CustomWindow.md)


[Next](CustomWindow.c.md)[Previous](CustomWindow.md)

# main.c

```c
/*
    File:       main.c  

    Contains:   The main program for the custom window sample

    Written by:     Karl Groethe

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
#include "CustomWindow.h"

int main(int argc, char* argv[])
{
    IBNibRef        nibRef;
    WindowRef       customWindow;
    Rect        windowRect={100,100,411,335};

    const WindowDefSpec customWindowDefSpec={kWindowDefProcPtr,
                                            {NewWindowDefUPP(myWindowDef)}
                                            };
    /*setup interface from nib file*/
    CreateNibReference(CFSTR("main"), &nibRef);
    SetMenuBarFromNib(nibRef, CFSTR("MainMenu"));
    DisposeNibReference(nibRef);

    CreateCustomWindow( &customWindowDefSpec,
                        kDocumentWindowClass,
                        kWindowStandardDocumentAttributes |
                        kWindowStandardHandlerAttribute,
                        &windowRect,
                        &customWindow);
    SetWTitle(customWindow,"\pmyCustomWindow");
    ShowWindow(customWindow);
    RunApplicationEventLoop();

    return 0;
}
```

[Next](CustomWindow.c.md)[Previous](CustomWindow.md)

