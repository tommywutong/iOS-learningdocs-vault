---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_ErrorHandler_h.html
archived_at: '2026-07-18T03:27:20.888041Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerevent.c.md)[Previous](TumblerSource-TumblerErrorHandler.c.md)

# TumblerSource/Tumbler_ErrorHandler.h

```c
#ifndef _MYERROR_HANDLER_
#define _MYERROR_HANDLER_

#include "QD3D.h"
#include "QD3DErrors.h"

void MyErrorHandler( TQ3Error error, TQ3Error error2, long  refCon ) ;
void MyWarningHandler( TQ3Warning sticky, TQ3Warning latest, long refCon ) ;

extern const int kErrorHandlerAlertID ; // 21032
#endif
```

[Next](TumblerSource-Tumblerevent.c.md)[Previous](TumblerSource-TumblerErrorHandler.c.md)

