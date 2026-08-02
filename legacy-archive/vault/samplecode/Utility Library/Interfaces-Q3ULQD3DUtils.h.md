---
title: Utility Library
apple_id: DTS10000113
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Utility_Library/Listings/Interfaces_Q3UL_QD3DUtils_h.html
archived_at: '2026-07-18T03:27:38.721067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Utility Library](Utility%20Library.md)


[Next](Source-Q3UL.c.md)[Previous](Interfaces-Q3UL.h.md)

# Interfaces/Q3UL_QD3DUtils.h

```c
/*
 *
 * QuickDraw 3D code for a utility library.
 *
 * This file contains interfaces to an amalgamation of code 
 * that has been useful for QuickDraw 3D sample apps.
 *
 * Nick Thompson, nickt@apple.com
 * Send bug reports and feedback to devsupport@apple.com.
 *
 * ©1997 Apple Computer Inc, All Rights Reserved 
 *
 * Modification History:
 *
 */

#ifndef _Q3UL_UTILS_
#define _Q3UL_UTILS_

#include "Q3UL.h"
#include "QD3D.h"
#include "QD3DCamera.h"
#include "QD3DGroup.h"
#include "QD3DView.h"

TQ3ViewObject           Q3UL_NewView( TQ3UL_WindowRef theWindow ) ;
TQ3DrawContextObject    Q3UL_NewMacintoshDrawContext( TQ3UL_WindowRef theWindow ) ;
TQ3CameraObject         Q3UL_NewCamera( TQ3UL_WindowRef theWindow ) ;
TQ3GroupObject          Q3UL_NewDefaultLightGroup( void ) ;

#endif
```

[Next](Source-Q3UL.c.md)[Previous](Interfaces-Q3UL.h.md)

