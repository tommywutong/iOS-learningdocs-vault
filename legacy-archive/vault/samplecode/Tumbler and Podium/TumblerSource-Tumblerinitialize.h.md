---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_initialize_h.html
archived_at: '2026-07-18T03:27:22.526920Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblermain.c.md)[Previous](TumblerSource-Tumblerinitialize.c.md)

# TumblerSource/Tumbler_initialize.h

```
// Tumbler_initialize.h
//
// Initialization function prototypes for the 
// Tumbler application
//
// Modification History
//
//  11/26/94        nick        initial cut - symantec proto_helper app, add defines


#ifndef _Tumbler_INITIALIZE_H_
#define _Tumbler_INITIALIZE_H_

/* Tumbler_initialize.c */
void InitializeToolbox(void);
void InitializeAppStuff( short  numMoreMasters ) ;


void InitializeGlobals(void);
void DeallocateGlobals(void);
void SetupMenus(void);

void    SplashSetUp( void ) ;
void    SplashTearDown( void ) ;

#endif
```

[Next](TumblerSource-Tumblermain.c.md)[Previous](TumblerSource-Tumblerinitialize.c.md)

