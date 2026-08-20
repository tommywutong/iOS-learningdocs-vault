---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TAboutBoxPane_h.html
archived_at: '2026-07-18T03:18:33.513227Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TASIPKeyPane.cp.md)[Previous](sources-TAboutBoxPane.cp.md)

# sources/TAboutBoxPane.h

```c
//  TAboutBoxPane.h -  AppleShare IP Dialog Pane Object
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


// ---------------------------------------------------------------------------
//   TAboutBoxPane  - base class for Dialog Pane Object
// ---------------------------------------------------------------------------
// 
class TAboutBoxPane : public TPane
{
public:

//  CONSTRUCTORS AND DESTRUCTORS
              TAboutBoxPane( DialogPtr dialog, SInt16 origItems);

    virtual  ~TAboutBoxPane();  

// MAIN INTERFACE
    virtual void Refresh();
    virtual void ItemHit(SInt16 item);
    virtual void Idle() ;

// PRIVATE FIELDS
protected:
    ControlHandle  fItem1;

 };
```

[Next](sources-TASIPKeyPane.cp.md)[Previous](sources-TAboutBoxPane.cp.md)

