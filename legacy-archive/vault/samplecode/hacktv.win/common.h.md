---
title: hacktv.win
apple_id: DTS10000804
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/hacktv.win/Listings/common_h.html
archived_at: '2026-07-18T03:29:28.133278Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [hacktv.win](hacktv.win.md)


[Next](globals.c.md)[Previous](common.c.md)

# common.h

```c
/*
    File:       Common.h

    Contains:   HackTV common routines

    Copyright:  © 1992-1998 by Apple Computer, Inc.
*/

#ifndef _APP_COMMON_
#define _APP_COMMON_

#include <QTML.h>
#include <Menus.h>
#include <Printing.h>
#include <QuickTimeComponents.h>

void InitializeSequenceGrabber(void);
void DoRecord(void);
void DoAboutDialog(void);
void DoPageSetup(void);
void DoPrint(void);
void DoCopyToClipboard(void);
void DoVideoSettings(void);
void DoSoundSettings(void);
void DoResize(short divisor);

// CreateMonitorWindow is implemented platform-specific
void CreateMonitorWindow(void);
#endif
```

[Next](globals.c.md)[Previous](common.c.md)

