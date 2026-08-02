---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/About_h.html
archived_at: '2026-07-18T02:59:27.182995Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](AEGestalt.r.md)[Previous](About.cp.md)

# About.h

```c
//  About.h
//  Copyright © 1992 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the About box code including any adorners/behaviors
//  The resources are placed in the project .r file
//  Version Info (latest first):
//
//  <1>     khs     1.0     First final version


#ifndef __UABOUT__
#define __UABOUT__

#ifndef __MACAPP__
#include <MacApp.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif


//  CONSTANTS

const unsigned short phAboutBox = 12000;        // our resource which resides in the .r file
const ResType kVersInfoType = 'vers';           // for getting out the version info from the binary
const ResNumber kVers1InfoID = 1;
const IDType kBlueMetalLook = 'blmt';           // our AboutBox adorner ID


//  FUNCTION PROTOTYPES

void CreateAboutBox();                          // the one and only function, place this inside the
// TApplication->DoAboutBox(), and you are up and running!


//  CLASSES
//  Our adorner used inside the About Box resource
DeclareClassDesc(TMetalBlueFill);

class TMetalBlueFill : public TAdorner
{

    DeclareClass(TMetalBlueFill);

public:
    TMetalBlueFill();
    virtual void Draw(TView* itsView,
                             const VRect&       /*area*/);
};



#endif
```

[Next](AEGestalt.r.md)[Previous](About.cp.md)

