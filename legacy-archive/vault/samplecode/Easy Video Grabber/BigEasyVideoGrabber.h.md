---
title: Easy Video Grabber
apple_id: DTS10000320
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Easy_Video_Grabber/Listings/BigEasyVideoGrabber_h.html
archived_at: '2026-07-18T03:07:32.583788Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Easy Video Grabber](Easy%20Video%20Grabber.md)


[Next](EasyGrabberTest.c.md)[Previous](BigEasyVideoGrabber.c.md)

# BigEasyVideoGrabber.h

```c
/*
  File:         BigEasyVideoGrabber.h
  Contains:     Header Files for the Application.
  Written by:   David Van Brink / QT Engineering
  Copyright:    © 1991-1994 by Apple Computer, Inc., all rights reserved.
  Change History (most recent first):
  <2>       12/4/94     khs     changed the format of the file to the new look and feel
  <1>       12/12/91    dvb     Started with 1.0
  To Do:
*/


// INCLUDES
#include <QuickTimeComponents.h>


// TYPES
typedef struct
{
    ComponentInstance sg;                       /* Sequence Grabber */
    ComponentInstance vc;                       /* Video Channel */
    Rect preferredRect;                         /* Size of digitizing area */
} EasyVideoGrabberRecord, * EasyVideoGrabber;


// FUNCTION PROTOTYPES
EasyVideoGrabber NewEasyVideoGrabber(Rect* outputSize); /* returns the biggest it'll draw */
Boolean GrabEasyVideoGrabber(EasyVideoGrabber evg,
                             Rect* r);                  /* draws into current port */
void DisposeEasyVideoGrabber(EasyVideoGrabber evg);     /* close everything down */
```

[Next](EasyGrabberTest.c.md)[Previous](BigEasyVideoGrabber.c.md)

