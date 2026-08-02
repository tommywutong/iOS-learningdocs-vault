---
title: Notification Hacks
apple_id: DTS10000194
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Notification_Hacks/Listings/GestaltTalk_GestaltTalk_h.html
archived_at: '2026-07-18T03:17:05.675336Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Notification Hacks](Notification%20Hacks.md)


[Next](GestaltTalk-GestaltTalkCommands.c.md)[Previous](Notification%20Hacks.md)

# GestaltTalk/GestaltTalk.h

```c
#pragma once

#include <Processes.h>

#define gestaltTalkSelector 'GTLK'

typedef enum { ginit, gstatus, gread, 
                gwrite, gregister, gunregister, 
                ggetapp, guserinit } gcmd;

typedef struct {
    long                    buffCount;
    Ptr                     dataBuffer;
    long                    appRegistered;
    ProcessSerialNumber     appPSN;
} gtg, *gtp;

typedef struct {
    gcmd    command;
    long    datalength;
    Ptr     data;
    gtp     gtData;
} GestaltTalkPB;


#define bufferSize (Size)(300)

OSErr GestaltTalk(GestaltTalkPB *gpb);
pascal OSErr GestaltTalkGestalt(long selector, long *resp);
```

[Next](GestaltTalk-GestaltTalkCommands.c.md)[Previous](Notification%20Hacks.md)

