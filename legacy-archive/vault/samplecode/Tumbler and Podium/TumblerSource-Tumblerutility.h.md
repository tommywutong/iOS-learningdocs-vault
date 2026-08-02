---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_utility_h.html
archived_at: '2026-07-18T03:27:23.573982Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerwindows.c.md)[Previous](TumblerSource-Tumblerutility.c.md)

# TumblerSource/Tumbler_utility.h

```
// Tumbler_utility.h
//
// utility related function prototypes for the the Tumbler application
//
// Modification History
//
//  11/26/94        nick        added in stuff from symantec proto_helper app, add defines


#ifndef _Tumbler_UTILITY_H_
#define _Tumbler_UTILITY_H_

/* Tumbler_utility.c */
short   PStrCmp(char *s1, char *s2);
void    PositionRectInRect(Rect *outerRect, Rect *innerRect, Fixed horzRatio, Fixed vertRatio) ;
void    CenterRectInRect(Rect *outerRect, Rect *innerRect);
#endif
```

[Next](TumblerSource-Tumblerwindows.c.md)[Previous](TumblerSource-Tumblerutility.c.md)

