---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_Mac_Classes_TContext_cp.html
archived_at: '2026-07-18T03:11:58.456048Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2MacClasses-TContext.h.md)[Previous](%E2%80%A2MacClasses-TBackGroundApp.h.md)

# •Mac_Classes/TContext.cp

```c
//  TContext.cp - Macintosh Task Context class object
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinne Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
// 

#include "TContext.h"

// CodeWarrior Exception handling

TContext::TContext()
{
//  __new_exception_state(&fExceptionState, fCatchBuffer, sizeof(fCatchBuffer));
}

// ---------------------------------------------------------------------------
//   TContext:Save
// ---------------------------------------------------------------------------
// Save Macintosh Context

void TContext::Save()
{
    // save exception-handling context
//  __switch_exception_state(&fExceptionState, &fExceptionState);
}

// ---------------------------------------------------------------------------
//   TContext:Restore
// ---------------------------------------------------------------------------
// Restore Macintosh Context

void TContext::Restore()
{
    ExceptionState  gone;

    // restore exception-handling context
//  __switch_exception_state(&fExceptionState, &gone);
}
```

[Next](%E2%80%A2MacClasses-TContext.h.md)[Previous](%E2%80%A2MacClasses-TBackGroundApp.h.md)

