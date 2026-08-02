---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CFilterControl_h.html
archived_at: '2026-07-18T03:25:12.448453Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CGrayBox.cp.md)[Previous](CFilterControl.cp.md)

# CFilterControl.h

```c
// ===========================================================================
//  CFilterControl.h            ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LModelObject.h>
#include "CSliderControl.h"


enum {
    SliderAttr_Enabled          = 0x80000000
};

typedef Uint32  ESliderAttr;

const long  ae_SetValue         = 10001;
const long  ae_SetMax           = 10002;

enum {
    cSlider                     = 'Sldr',
    kAESetValue                 = 'sVal',
    kAESetMax                   = 'sMax',
    pValue                      = 'sVal',
    pMaxValue                   = 'sMax',
    pLabel                      = 'sLbl'
};

class   CFilterControl : public CSliderControl,
                         public LModelObject {
public:
    enum { 
        class_ID = 'Filt'
    };
    LCaption            *mLabel;
    unsigned short      mLabelChanges;

    static CFilterControl*  CreateFilterControlStream(LStream *inStream);

                        CFilterControl(LStream *inStream);

    virtual             ~CFilterControl();

    virtual void        SendAESetValue(Int32 value, Boolean inExecute = false);
    virtual void        SendAESetMax(Int32 max);

        // ¥¥ AppleEvent Object Model Support ¥¥

    virtual void        GetAEProperty(DescType inProperty,
                                        const AEDesc &inRequestedType,
                                        AEDesc& outPropertyDesc) const;
    virtual void        SetAEProperty(DescType inProperty,
                                        const AEDesc &inValue,
                                        AEDesc& outAEReply);

    virtual void        HandleAppleEvent(
                                        const AppleEvent    &inAppleEvent,
                                        AppleEvent          &outAEReply,
                                        AEDesc              &outResult,
                                        Int32               inAENumber);
protected:

    virtual void        SliderAction(short newPos);
    virtual void        TrackSlider(Point origMouseLoc);
};
```

[Next](CGrayBox.cp.md)[Previous](CFilterControl.cp.md)

