---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TSetupPane_h.html
archived_at: '2026-07-18T03:18:34.428210Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](Document%20Revision%20History.md)[Previous](sources-TSetupPane.cp.md)

# sources/TSetupPane.h

```c
//  TSetupPane.h -  AppleShare IP Dialog Pane Object
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinnie Moscaritolo
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

#pragma once 

#include "TPane.h"
#include "TPGPUAMPrefs.h"



// ---------------------------------------------------------------------------
//   TSetupPane  - base class for Dialog Pane Object
// ---------------------------------------------------------------------------
// 
class TSetupPane : public TPane
{
public:

//  CONSTRUCTORS AND DESTRUCTORS
              TSetupPane( DialogPtr dialog, SInt16 origItems, TPGPUAMPrefs* prefs);

    virtual  ~TSetupPane(); 

// MAIN INTERFACE
    virtual void Refresh();
    virtual void ItemHit(SInt16 item);
    virtual void Idle() ;

// PRIVATE FIELDS
protected:
    TPGPUAMPrefs*  fPrefs;
    ControlHandle  fCachePassPhrase;
    ControlHandle  fCacheTimeLimit;
    ControlHandle  fTick1;
    ControlHandle  fTick2;
    ControlHandle  fTick3;
    ControlHandle  fTickLast;

    ControlHandle  fAuthServer;
    ControlHandle  fOption1;
    ControlHandle  fOption2;

 };
```

[Next](Document%20Revision%20History.md)[Previous](sources-TSetupPane.cp.md)

