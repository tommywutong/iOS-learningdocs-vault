---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CSliderControl_h.html
archived_at: '2026-07-18T03:25:13.099692Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CSoundboardApp.cp.md)[Previous](CSliderControl.cp.md)

# CSliderControl.h

```c
// ===========================================================================
//  CSliderControl.h            ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LStdControl.h>

enum { sliderCntlProc = 4352 };

class   CSliderControl : public LStdControl {
public:
    enum { 
        class_ID = 'Sldr',
        rSliderBase = 310 
    };

    static void         SetSliderJmpAddress();
    static pascal long  SliderCtl(short varCode, ControlHandle ctl, short msg, long parm);

/*  static LStdControl* CreateFromCNTL(ResIDT inCNTLid,
                            MessageT inValueMessage, ResIDT inTextTraitsID,
                            LView *inSuperView);
*/
    static CSliderControl*  CreateSliderControlStream(LStream *inStream);

                        CSliderControl(Int16 inControlKind);
                        CSliderControl(const CSliderControl &inOriginal);
                        CSliderControl(const SPaneInfo &inPaneInfo,
                            MessageT inValueMessage, Int32 inValue,
                            Int32 inMinValue, Int32 inMaxValue,
                            Int16 inControlKind, ResIDT inTextTraitsID,
                            Str255 inTitle, Int32 inMacRefCon);
                        CSliderControl(const SPaneInfo &inPaneInfo,
                            MessageT inValueMessage, Int32 inValue,
                            Int32 inMinValue, Int32 inMaxValue,
                            Int16 inControlKind, ResIDT inTextTraitsID,
                            ControlHandle inMacControlH);
                        CSliderControl(LStream *inStream);

    virtual             ~CSliderControl();

    virtual void        AdjustSlider(Int32 val, Int32 max);
    virtual long        GetSliderRefCon(void);
    virtual void        SetSliderRefCon(long refCon);

protected:
    Point               mLastClick;
    long                mRefCon;

    void                InitSlider(void);

    virtual void        SliderAction(short newPos);
    virtual void        TrackAndRun(Point *mouseLoc);

    void                UpdateSlider(short hiliteCap = -1);
    virtual void        TrackSlider(Point origMouseLoc);
    void                SliderDrawCIcon(CIconHandle iconHndl, short hloc, short vloc);
    Rect                CalcSliderRect();
    short               CalcSliderValue(Point mouseLoc);
};

// === Inline Functions ===

inline long
CSliderControl::GetSliderRefCon(void)
{
    return mRefCon;
}

inline void
CSliderControl::SetSliderRefCon(long refCon)
{
    mRefCon = refCon;
}
```

[Next](CSoundboardApp.cp.md)[Previous](CSliderControl.cp.md)

