---
title: CommonSample
apple_id: DTS10000108
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CommonSample/Listings/MyErrorHandler_h.html
archived_at: '2026-07-18T03:04:06.422759Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CommonSample](CommonSample.md)


[Next](Document%20Revision%20History.md)[Previous](MyErrorHandler.c.md)

# MyErrorHandler.h

```c
// Quickdraw 3D sample code
//
// Nick Thompson, AppleLink: DEVSUPPORT (devsupport@applelink.apple.com)
//
// ©1994-5 Apple Computer Inc., All Rights Reserved

#ifndef _MYERROR_HANDLER_
#define _MYERROR_HANDLER_

#include "QD3D.h"
#include "QD3DErrors.h"

void MyErrorHandler( TQ3Error error, TQ3Error error2, long  refCon ) ;
void MyWarningHandler( TQ3Warning sticky, TQ3Warning latest, long refCon ) ;

extern const int kErrorHandlerAlertID ; // 21032
#endif
```

[Next](Document%20Revision%20History.md)[Previous](MyErrorHandler.c.md)

