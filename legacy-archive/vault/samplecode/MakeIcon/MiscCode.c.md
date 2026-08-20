---
title: MakeIcon
apple_id: DTS10000089
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeIcon/Listings/MiscCode_c.html
archived_at: '2026-07-18T03:14:22.809206Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeIcon](MakeIcon.md)


[Next](MiscCode.h.md)[Previous](MakeIcon.c.md)

# MiscCode.c

```c
/*
    File:       MiscCode.c

    Contains:   

    Written by:     

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#include "MiscCode.h"
#include <QDOffscreen.h>
#include <Resources.h>

void CheckError(Str255 err, short code)
{
    if(code)
    {
        //asm { move.w  code, d0 }
        DebugStr(err);
    }
}

void TryRemoveResource(ResType  type, short ID)
{
    Handle  h;

    h = GetResource(type,ID);
    if(h)
        RemoveResource(h);
}


void DrawImage(WindowPtr wp)
//¥¥¥°°°¥°¥°¥°¥°¥°
// THIS JUST DRAWS THE WINDOW - stolen from PaletteAnimation sample...
// DEPANDANT UPON:  a gWorldPtr being stuffed into the window's refcon field.
//¥¥¥°°°¥°¥°¥°¥°¥°
{
    GWorldPtr   gw;
    WindowPtr   savePort;

    GetPort(&savePort);
    SetPort(wp);
    gw =  (GWorldPtr)GetWRefCon(wp);

    LockPixels (GetGWorldPixMap (gw));
    CopyBits (&((GrafPtr) gw)->portBits, &(wp)-> portBits, 
            &gw->portRect, &wp->portRect, srcCopy, nil);
    UnlockPixels (GetGWorldPixMap (gw));
    SetPort(savePort);
}
```

[Next](MiscCode.h.md)[Previous](MakeIcon.c.md)

