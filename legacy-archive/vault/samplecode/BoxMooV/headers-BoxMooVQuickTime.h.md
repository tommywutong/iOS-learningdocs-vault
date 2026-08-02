---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxMooV_QuickTime_h.html
archived_at: '2026-07-18T03:02:13.798013Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxMooVTexture.h.md)[Previous](headers-BoxMooVevent.h.md)

# headers/BoxMooV_QuickTime.h

```c
/*  BoxMooV_QuickTime.h                                                                         

    Rick Evans                                                  
    Robert Dierkes                                                                              
    (c)1994-96 Apple Computer Inc., All Rights Reserved                             

*/
#ifndef _QUICKTIME_H_
#define _QUICKTIME_H_

#include <Movies.h>

#include "BoxMooV_Texture.h"

void        QuickTime_Init( void);
void        QuickTime_Delete(Movie *moviePtr);
Boolean     QuickTime_GetNewMooVTexture(Movie *theMovie);
Boolean     QuickTime_LoadMovie(FSSpec *pFile, Movie *pMovie);
void        QuickTime_LoopMovie(Movie pMovie, GWorldPtr pGWorld);

#endif
```

[Next](headers-BoxMooVTexture.h.md)[Previous](headers-BoxMooVevent.h.md)

