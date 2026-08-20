---
title: SoundSprocketTest
apple_id: DTS10000060
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundSprocketTest/Listings/TS3Menu_h.html
archived_at: '2026-07-18T03:25:09.461216Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundSprocketTest](SoundSprocketTest.md)


[Next](TS3Message.c.md)[Previous](TS3Menu.c.md)

# TS3Menu.h

```
/*
 *  File:       TS3Menu.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __TS3Menu__
#define __TS3Menu__

void Menu_Init(
    void);

void Menu_Exit(
    void);

void Menu_Select(
    short           inMenuID,
    short           inItem);

short Menu_GetInterpolation(
    void);

#endif /* __TS3Menu__ */
```

[Next](TS3Message.c.md)[Previous](TS3Menu.c.md)

