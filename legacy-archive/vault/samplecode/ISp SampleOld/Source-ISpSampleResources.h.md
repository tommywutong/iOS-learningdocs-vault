---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_ISp_SampleResources_h.html
archived_at: '2026-07-18T03:12:09.279550Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-main.c.md)[Previous](Source-ISpSample.h.md)

# Source/ISp_SampleResources.h

```
/*
    File:       ISp_SampleResources.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __ISP_SAMPLERESOURCES__
#define __ISP_SAMPLERESOURCES__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types

#define     kISpSampleCreator           '????'
#define     kISpSampleNeedsVersion      'isps'

enum
{
    kSTRn_NeedNames     =   1000,
    kSTRn_WeaponNames   =   1001
};

enum
{
    kisap_ISpSample         =   128,

    ksetl_ISpSample         =   128,

    ktset_DefaultKeyboard   =   200,
    ktset_LeftyKeyboard     =   201,

    ktset_DefaultMouse      =   300,
    ktset_YawMouse          =   301
};

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-main.c.md)[Previous](Source-ISpSample.h.md)

