---
title: QTEffects Explode
apple_id: DTS10000834
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/QTEffects_Explode/Listings/main_h.html
archived_at: '2026-07-18T03:20:51.836622Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTEffects Explode](QTEffects%20Explode.md)


[Next](QTEffects.c.md)[Previous](main.c.md)

# main.h

```
/*
    File:       main.h

    Contains:   Code to generate a QuickTime movie with a QuickTime video effect in it.

    Written by: Scott Kuechle
                (based heavily on QuickTime SDK QTShowEffect sample code by Tim Monroe)

    Copyright:  © 1999 by Apple Computer, Inc. All rights reserved

    Change History (most recent first)

        <1>     9/25/99     srk     first file


*/
#if TARGET_OS_MAC
    static void InitMacToolbox (void);
    static void Macintosh_DisplayMsg(char *msg);
#endif

#if TARGET_OS_WIN32
    static void Win32_DisplayMsg(char *msg);
#endif

static void QuickTimeInit (void);
void CheckError(OSErr error, char *msg);
```

[Next](QTEffects.c.md)[Previous](main.c.md)

