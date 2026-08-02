---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CKeyFilters_cp.html
archived_at: '2026-07-18T03:14:24.893242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CKeyFilters.h.md)[Previous](CBeachBall.h.md)

# CKeyFilters.cp

```c
/*
    A key filter for edit fields that contain numbers that allow decimals and 
    the minus sign.

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#include "CKeyFilters.h"

EKeyStatus CKeyFilters::RealNumberFieldPositive(
    const EventRecord &inKeyEvent)
{
    EKeyStatus theKeyStatus = keyStatus_PassUp;
    Char16 theKey = inKeyEvent.message;
    Char16 theChar = theKey & charCodeMask;

    if (theChar == '.')
        theKeyStatus = keyStatus_Input;
    else
        theKeyStatus = IntegerField(inKeyEvent);

    return theKeyStatus;
}

EKeyStatus CKeyFilters::RealNumberField(
    const EventRecord &inKeyEvent)
{
    EKeyStatus theKeyStatus = keyStatus_PassUp;
    Char16 theKey = inKeyEvent.message;
    Char16 theChar = theKey & charCodeMask;

    if (theChar == '.')
        theKeyStatus = keyStatus_Input;
    else if (theChar == '-')
        theKeyStatus = keyStatus_Input;
    else
        theKeyStatus = IntegerField(inKeyEvent);

    return theKeyStatus;
}
```

[Next](CKeyFilters.h.md)[Previous](CBeachBall.h.md)

