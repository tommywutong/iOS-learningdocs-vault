---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_podium_h.html
archived_at: '2026-07-18T03:27:23.240529Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerprototypes.h.md)[Previous](TumblerSource-Tumblerpodium.c.md)

# TumblerSource/Tumbler_podium.h

```c
// Tumbler_podium.h -- this contains the podium specific routines for the Tumbler app
//
//


#ifndef _Tumbler_PODIUM_H_
#define _Tumbler_PODIUM_H_

#include <Events.h>
#include "Tumbler_Document.h"

#define LeftTopHandle       1
#define RightTopHandle      2
#define LeftBottomHandle    3
#define RightBottomHandle   4

void Podium_DoContent(DocumentPtr theDocument, EventRecord *theEvent) ;
void Podium_DoBackgroundContent(DocumentPtr theDocument, EventRecord *theEvent) ;
void Podium_DoIdle(EventRecord *theEvent) ;
void Podium_Init(void) ;

#endif
```

[Next](TumblerSource-Tumblerprototypes.h.md)[Previous](TumblerSource-Tumblerpodium.c.md)

