---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_teutilities_h.html
archived_at: '2026-07-18T03:27:23.419527Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblertraps.c.md)[Previous](TumblerSource-Tumblerteutilities.c.md)

# TumblerSource/Tumbler_teutilities.h

```
// Tumbler_teutilities.h
//
// offscreen related function prototypes for the the Tumbler application
//
// Modification History
//
//  11/26/94        nick        added in stuff from symantec proto_helper app, add defines
//                              actually we can propably get rid of this stuff.
//
//  to do:
//          dump obselete stuff


#ifndef _Tumbler_TEUTILITIES_H_
#define _Tumbler_TEUTILITIES_H_

/* Tumbler_teutilities.c */
short TEICut(TEHandle theTE);
short TEIPaste(TEHandle theTE, short *spaceBefore, short *spaceAfter);
short TEIsFrontOfLine(short offset, TEHandle theTE);
short TEGetLine(short offset, TEHandle theTE);

#endif
```

[Next](TumblerSource-Tumblertraps.c.md)[Previous](TumblerSource-Tumblerteutilities.c.md)

