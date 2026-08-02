---
title: GetHWEthernetAddr
apple_id: DTS10000696
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GetHWEthernetAddr/Listings/GetHWEthernetAddr_c.html
archived_at: '2026-07-18T03:10:46.961784Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GetHWEthernetAddr](GetHWEthernetAddr.md)


[Next](Document%20Revision%20History.md)[Previous](Carbon.r.md)

# GetHWEthernetAddr.c

```c
/*
    File:   GetHWEthernetAddr.c     

    Contains:   A Simple app to get and display the Hardware Ethernet Address

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
                6/28/00     Created 


*/

#ifdef __APPLE_CC__
#include <Carbon/Carbon.h>
#else
#include <Carbon.h>
#endif

int main(int argc, char* argv[])
{
    IBNibRef        nibRef;
    WindowRef       window;
    ControlRef      HWEnetField;
    InetInterfaceInfo   myInetInterfaceInfo;
    Rect        fieldRect;
    CFMutableStringRef  HWEnetAddr;
    int         i;

    /*setup interface from nib file*/
    CreateNibReference(CFSTR("main"), &nibRef);
    SetMenuBarFromNib(nibRef, CFSTR("MainMenu"));
    CreateWindowFromNib(nibRef, CFSTR("MainWindow"), &window);
    DisposeNibReference(nibRef);

    OTInetGetInterfaceInfo(&myInetInterfaceInfo,kDefaultInetInterface);
    //create a mutable string to store our Ethernet Address
    HWEnetAddr=CFStringCreateMutable(NULL,0);
    //loop through hex bytes and append them as characters to our string.
    for(i=0;i<myInetInterfaceInfo.fHWAddrLen;i++)
        CFStringAppendFormat(HWEnetAddr,NULL,CFSTR("%02x "),myInetInterfaceInfo.fHWAddr[i]);

    GetWindowPortBounds(window,&fieldRect);
    InsetRect(&fieldRect,96,4);
    CreateStaticTextControl(window,&fieldRect,HWEnetAddr,NULL,&HWEnetField);

    /*show the window*/
    ShowWindow(window);

    RunApplicationEventLoop();

    return 0;
}
```

[Next](Document%20Revision%20History.md)[Previous](Carbon.r.md)

