---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_utility_c.html
archived_at: '2026-07-18T03:27:23.524247Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerutility.h.md)[Previous](TumblerSource-Tumblertraps.h.md)

# TumblerSource/Tumbler_utility.c

```c
//
//
//      utility.c
//
//      Utility routines.
//      
//
//      Author:     Nick Thompson & Pablo Fernicola, with thanks to the QuickDraw 3D team
//
//      Copyright © 1992-95 Apple Computer, Inc., All Rights Reserved
//
//


#include "Tumbler_prototypes.h"

#include "Tumbler_utility.h"
//
//  PStrCmp returns true if the two given pascal strings are equal.
//

short PStrCmp(char *s1, char *s2)

{   short       size, index;

    size = s1[0] + 1;

    while (size--) {
        if (*(s1++) != *(s2++))
            return(false);
    }

    return(true);
}




//--------------------------------------------------------------------------------
// Given two rects, this function centers the second one within the first. 

void    CenterRectInRect(Rect *outerRect, Rect *innerRect)
{
    PositionRectInRect(outerRect, innerRect, FixRatio(1, 2), FixRatio(1, 2));
}

//-------------------------------------------------------------------------------------------
// Given two rectangles, this function positions the second within the first
// one so that it maintains the spacing specified by the horzRatio and
// vertRatio parameters.  In other words, to center an inner rectangle
// hoizontally, but have its center be 1/3 from the top of the outer rectangle,
// call this function with horzRatio = FixRatio(1, 2), vertRatio =
// FixRatio(1, 3).  We use Fixed rather than floating point to avoid
// complications when mixing MC68881/non-MC68881 versions of Utilities. 

void    PositionRectInRect(Rect *outerRect, Rect *innerRect, Fixed horzRatio, Fixed vertRatio)
{
    short   outerRectHeight;
    short   outerRectWidth;
    short   innerRectHeight;
    short   innerRectWidth;
    short   yLocation;
    short   xLocation;

    outerRectHeight = outerRect->bottom - outerRect->top;
    outerRectWidth = outerRect->right - outerRect->left;

    innerRectHeight = innerRect->bottom - innerRect->top;
    innerRectWidth = innerRect->right - innerRect->left;
        yLocation = Fix2Long(FixMul(Long2Fix(outerRectHeight - innerRectHeight), vertRatio))
            + outerRect->top;
        xLocation = Fix2Long(FixMul(Long2Fix(outerRectWidth - innerRectWidth), horzRatio))
            + outerRect->left;

    innerRect->top = yLocation;
    innerRect->left = xLocation;
    innerRect->bottom = yLocation + innerRectHeight;
    innerRect->right = xLocation + innerRectWidth;
}
```

[Next](TumblerSource-Tumblerutility.h.md)[Previous](TumblerSource-Tumblertraps.h.md)

