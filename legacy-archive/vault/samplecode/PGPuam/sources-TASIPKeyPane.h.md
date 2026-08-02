---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TASIPKeyPane_h.html
archived_at: '2026-07-18T03:18:33.329966Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TASIPPGPkey.cp.md)[Previous](sources-TASIPKeyPane.cp.md)

# sources/TASIPKeyPane.h

```c
//  TASIPKeyPane.h -  AppleShare IP Dialog Pane Object
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

#ifndef _H_TASIPKEYPANE
#define _H_TASIPKEYPANE

#include <TPane.h>
#include "TASIPPGPkey.h"



// ---------------------------------------------------------------------------
//   TPane  - base class for Dialog Pane Object
// ---------------------------------------------------------------------------
// 
class TASIPKeyPane : public TPane
{
public:

//  CONSTRUCTORS AND DESTRUCTORS
              TASIPKeyPane( DialogPtr dialog, SInt16 origItems, TASIPPGPkey* serverKey);

    virtual  ~TASIPKeyPane();   

// MAIN INTERFACE
    virtual void Refresh();
    virtual void ItemHit(SInt16 item);
    virtual void Idle();
    virtual Boolean HandleMouseDown(EventRecord *) ;

// PRIVATE FIELDS
protected:
    TASIPPGPkey*    fKey;


    ControlHandle  fKeyDragBox;
    ControlHandle  fKeyExpiresTitle;
    ControlHandle  fKeyCreateDate;
    ControlHandle  fKeyExpiredDate;
    ControlHandle  fKeySize;
    ControlHandle  fKeyType;
    ControlHandle  fKeyName;
    ControlHandle  fFingerPrint;
    ControlHandle  fKeyValidValue;
    ControlHandle  fKeyTrustValue;
    ControlHandle  fKeyExpiredIcon;
    ControlHandle  fKeyInfoBox;
    ControlHandle  fKeyTrustBox;
    ControlHandle  fKeyFPBox;
    ControlHandle  fKeyDetailsBox;


};

#endif
```

[Next](sources-TASIPPGPkey.cp.md)[Previous](sources-TASIPKeyPane.cp.md)

