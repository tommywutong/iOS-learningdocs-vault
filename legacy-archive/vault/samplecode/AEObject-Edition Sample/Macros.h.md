---
title: AEObject-Edition Sample
apple_id: DTS10000204
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEObject-Edition_Sample/Listings/Macros_h.html
archived_at: '2026-07-18T02:59:29.826143Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEObject-Edition Sample](AEObject-Edition%20Sample.md)


[Next](Menu.c.md)[Previous](Initialize.c.md)

# Macros.h

```swift
/*------------------------------------------------------------------------------
 *
 *  Apple Developer Technical Support
 *
 *  
 *
 *  Program:    AEObject-Edition Sample
 *  File:       Macros.h -    C Source
 *
 *  by:         C.K. Haun <TR>
 *
 *  Copyright © 1991-1992 Apple Computer, Inc.
 *  All rights reserved.
 *
 *------------------------------------------------------------------------------
 * This file contains all the C Macros I use in this program.  If you find 
 * the macros hard to read (instead of easier, which is the reason for the 
 * macro) do a global search and replace with the values here 
 * all macros start with a small 'm' 
 * I don't use many, never trusted macros..... 
*----------------------------------------------------------------------------*/
#ifndef __MACROS__
#define __MACROS__
#define mDispatch(handle,routine,paramter) (ProcPtr)((*handle)->routine)(paramter)
#define mAEErrorDisplay(A,B) if(B){AddAEText("\p \nAppleEvent error ");AddAEText(A);AddAENum(B);AEErrorText(B);}
#define mVerboseOutput(A)   if(gPreferences.verboseAE)AddAEText(A);
#endif
```

[Next](Menu.c.md)[Previous](Initialize.c.md)

