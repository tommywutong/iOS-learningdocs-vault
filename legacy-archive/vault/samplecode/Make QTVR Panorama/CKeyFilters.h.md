---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CKeyFilters_h.html
archived_at: '2026-07-18T03:14:24.940913Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CLogConsole.cp.md)[Previous](CKeyFilters.cp.md)

# CKeyFilters.h

```c
/*
    A key filter for edit fields that contain numbers that allow decimals and 
    the minus sign.

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#pragma once

#include <UKeyFilters.h>

class CKeyFilters : public UKeyFilters
{
public:

    static EKeyStatus RealNumberField(const EventRecord &inKeyEvent);

    static EKeyStatus RealNumberFieldPositive(const EventRecord &inKeyEvent);
};
```

[Next](CLogConsole.cp.md)[Previous](CKeyFilters.cp.md)

