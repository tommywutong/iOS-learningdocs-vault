---
title: PostScript Output Filters
apple_id: DTS10000297
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/PostScript_Output_Filters/Listings/SampleFilter_DebugMisc_h.html
archived_at: '2026-07-18T03:19:25.430522Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PostScript Output Filters](PostScript%20Output%20Filters.md)


[Next](SampleFilter-LibraryStuff-Hints.h.md)[Previous](SampleFilter-Debug.h.md)

# SampleFilter/DebugMisc.h

```c
/*
**  File:           DebugMisc.h
**
**  Description:    Debugging assert definitions for use with the
**                  SampleFilter code.
**
**  Version:        1.0     
**
**  Copyright 1999 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "ABC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
**
*/

#if qDebug
#include <Types.h>
#include <Traps.h>
#include <stddef.h>
#include <OSUtils.h>

#define ckLine(line)    #line
#define ckLine2(line)   ckLine(line)
#define ckAssert(cond)      if(!(cond)) DebugStr("\pFailed " #cond ":"__FILE__ " " ckLine2(__LINE__))
#else
#define ckAssert(cond)      ((void)0)           
#endif
```

[Next](SampleFilter-LibraryStuff-Hints.h.md)[Previous](SampleFilter-Debug.h.md)

