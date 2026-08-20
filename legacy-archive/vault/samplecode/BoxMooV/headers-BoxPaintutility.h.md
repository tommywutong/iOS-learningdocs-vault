---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxPaint_utility_h.html
archived_at: '2026-07-18T03:02:14.512695Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](sources-BoxMooVdocument.c.md)[Previous](headers-BoxPaintSupport.h.md)

# headers/BoxPaint_utility.h

```c
/*  BoxPaint_utility.h                                                                          

    Nick Thompson
    Michael Bishop - August 21 1996                                                 
    (c)1994-96 Apple Computer Inc., All Rights Reserved                             

*/

#ifndef _UTILITY_H_
#define _UTILITY_H_

#include "QD3D.h"

short       Utility_HiWrd(long aLong) ;
short       Utility_LoWrd(long aLong) ;

void        Utility_MyGetMouse(TQ3Point2D *thePoint);
int         Utility_MyStillDown(void);


#endif
```

[Next](sources-BoxMooVdocument.c.md)[Previous](headers-BoxPaintSupport.h.md)

