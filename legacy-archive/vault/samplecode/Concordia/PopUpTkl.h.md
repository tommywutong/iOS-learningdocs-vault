---
title: Concordia
apple_id: DTS10000181
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-08-28'
source_url: https://developer.apple.com/library/archive/samplecode/Concordia/Listings/PopUpTkl_h.html
archived_at: '2026-07-18T03:04:13.139187Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Concordia](Concordia.md)


[Next](SizeTkl.c.md)[Previous](PopUpTkl.c.md)

# PopUpTkl.h

```c
/*
    File:       PopUpTkl.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1991-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/10/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef _popuptkl_
#define _popuptkl_
/******************************************************************************\
* Header Files
\******************************************************************************/

#ifndef __MENUS__
#include <Menus.h>
#endif

#ifndef __TYPES__
#include <Types.h>
#endif


/******************************************************************************\
* Function Prototypes
\******************************************************************************/

short DoPopUpMsg (MenuHandle, Rect *, short, short, short);


#endif
```

[Next](SizeTkl.c.md)[Previous](PopUpTkl.c.md)

