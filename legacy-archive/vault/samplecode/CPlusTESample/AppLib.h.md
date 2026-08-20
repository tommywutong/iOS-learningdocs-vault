---
title: CPlusTESample
apple_id: DTS10000730
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CPlusTESample/Listings/AppLib_h.html
archived_at: '2026-07-18T03:02:42.993007Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CPlusTESample](CPlusTESample.md)


[Next](AppLib.r.md)[Previous](CPlusTESample.md)

# AppLib.h

```
/*------------------------------------------------------------------------------------------

    Program:    CPlusTESample 2.0
    File:       AppLib.h

    by Andrew Shebanow
    of Apple Macintosh Developer Technical Support

    Copyright © 1989-1990 Apple Computer, Inc.
    All rights reserved.

------------------------------------------------------------------------------------------*/

#ifndef __APPLIB__
#define __APPLIB__

/*
    These definitions are shared by Rez and C++. We use #define statements
    instead of constants in this file because Rez doesn't support constants.
 */

/* Some constants for resource ID's */
#define kErrStrings         128             /* error string list */
#define kBuzzwordStrings    129             /* list of buzzwords */
#define kSysErrStrings      130             /* system error strings */
#define rUserAlert          129             /* user error alert */
#define rSaveAlert          130             /* do you wanna save? alert */

/* The following are indicies into our error STR# resource. */
#define eWrongMachine       1
#define eSmallSize          2
#define eCannotOpenDoc      3
#define eCannotReadDoc      4

/* indices into buzzwords string resource */
#define bQuitting           1
#define bClosing            2

#endif
```

[Next](AppLib.r.md)[Previous](CPlusTESample.md)

