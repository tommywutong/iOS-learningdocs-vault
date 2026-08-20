---
title: SoundSprocketTest
apple_id: DTS10000060
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundSprocketTest/Listings/TS3Window_h.html
archived_at: '2026-07-18T03:25:11.395052Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundSprocketTest](SoundSprocketTest.md)


[Next](Document%20Revision%20History.md)[Previous](TS3Window.c.md)

# TS3Window.h

```c
/*
 *  File:       TS3Window.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __TS3Window__
#define __TS3Window__

#include <Windows.h>

typedef enum WindowMethod {
    kWindowMethod_FIRST,
    kWindowMethod_GetSleep = kWindowMethod_FIRST,
    kWindowMethod_ConsumeEvent,
    kWindowMethod_MouseDown,
    kWindowMethod_KeyDown,
    kWindowMethod_Update,
    kWindowMethod_Activate,
    kWindowMethod_Deactivate,
    kWindowMethod_COUNT
} WindowMethod;

typedef void (*WindowMethodPtr)(WindowPtr, ...);

void Window_Init(
    void);

void Window_Exit(
    void);

void Window_New(
    WindowPtr           inWindow,
    WindowMethodPtr     (*inMetaHandler)(WindowMethod inMethod));

void Window_Dispose(
    WindowPtr           inWindow);

Boolean Window_IsMine(
    WindowPtr           inWindow);

void Window_GetSleep(
    WindowPtr           inWindow,
    UInt32*             outSleep);

void Window_ConsumeEvent(
    WindowPtr           inWindow,
    const EventRecord*  inEvent,
    Boolean*            outConsumed);

void Window_MouseDown(
    WindowPtr           inWindow,
    Point               inWhere);

void Window_KeyDown(
    WindowPtr           inWindow,
    char                inChar,
    char                inKeyCap,
    short               inModifiers,
    Boolean             inAutoKey);

void Window_Update(
    WindowPtr           inWindow);

void Window_Activate(
    WindowPtr           inWindow);

void Window_Deactivate(
    WindowPtr           inWindow);

#endif /* __TS3Window__ */
```

[Next](Document%20Revision%20History.md)[Previous](TS3Window.c.md)

