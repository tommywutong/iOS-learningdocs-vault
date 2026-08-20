---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CPict2VRWindow_h.html
archived_at: '2026-07-18T03:14:25.802820Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CPreferences.cp.md)[Previous](CPict2VRWindow.cp.md)

# CPict2VRWindow.h

```c
/*
    A window that provides the a interface for creating QTVR movies.

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#pragma once

#ifndef __MOVIES__
#include <Movies.h>
#endif

#include <LDialogBox.h>

class CPict2VRWindow :
    public LDialogBox,
    public LBroadcaster
{
public:

    enum { class_ID = 'p2vr' };

    static CPict2VRWindow *CreatePict2VRWindowWindowStream(
        LStream *inStream);

    CPict2VRWindow(
        LStream *inStream);

    virtual ~CPict2VRWindow();

    virtual void FinishCreateSelf();

    virtual void ListenToMessage(
        MessageT inMessage,
        void *ioParam);

    void SetPictFile(
        FSSpec *inMacFSSpec);

    void SetCompText();

private:

    FSSpec mSrcSpec;
    FSSpec mTileSpec;
    FSSpec mDestSpec;
    PaneIDT mCreate;
    Int16 mWidth;
    Int16 mHeight;
    CodecType mCodec;
    CodecQ mSpatialQuality;
    Int16 mDepth;
    Rect mPictFrame;
};
```

[Next](CPreferences.cp.md)[Previous](CPict2VRWindow.cp.md)

