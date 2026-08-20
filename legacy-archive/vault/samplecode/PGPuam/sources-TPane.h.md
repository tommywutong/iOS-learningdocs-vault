---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TPane_h.html
archived_at: '2026-07-18T03:18:34.186364Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TPGPException.h.md)[Previous](sources-TMemPGPkey.h.md)

# sources/TPane.h

```c
//  TPane.h - base class for Dialog Pane Object
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

#ifndef _H_TPANE
#define _H_TPANE

#include <Dialogs.h>

extern pascal OSErr AppendDialogItemList( DialogPtr dialog, SInt16 ditlID, DITLMethod method )
 THREEWORDINLINE(0x303C, 0x0412, 0xAA68);


// ---------------------------------------------------------------------------
//   TPane  - base class for Dialog Pane Object
// ---------------------------------------------------------------------------
// 
class TPane
{
public:

//  CONSTRUCTORS AND DESTRUCTORS
              TPane( DialogPtr dialog, SInt16 origItems) :
                    fDialog(dialog), fOrigItems(origItems) { };

    virtual  ~TPane() { };      

// MAIN INTERFACE
    virtual void Refresh() { };
    virtual void ItemHit(SInt16 item) { };
    virtual void Idle()     { };
    virtual Boolean HandleMouseDown(EventRecord *) { return false; };

// PRIVATE FIELDS
protected:
    DialogPtr   fDialog;
    SInt16      fOrigItems;

};

#endif
```

[Next](sources-TPGPException.h.md)[Previous](sources-TMemPGPkey.h.md)

