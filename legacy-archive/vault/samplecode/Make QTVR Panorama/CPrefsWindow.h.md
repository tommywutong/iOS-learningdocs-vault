---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CPrefsWindow_h.html
archived_at: '2026-07-18T03:14:26.324062Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CUtils.cp.md)[Previous](CPrefsWindow.cp.md)

# CPrefsWindow.h

```c
/*
    A window that provides the user interface for editing preferences.

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#pragma once

#include <Movies.h>

#include <LDialogBox.h>

#include "CApp.h"

class CPrefsWindow :
    public LDialogBox,
    public LBroadcaster
{
public:

    enum { class_ID = 'pref' };

    static CPrefsWindow *CreatePrefsWindowWindowStream(
        LStream *inStream);

    CPrefsWindow(
        LStream *inStream);

    virtual ~CPrefsWindow();

    virtual void FinishCreateSelf();

    virtual void ListenToMessage(
        MessageT inMessage,
        void *ioParam);

    void SetCompText();

protected:

    virtual void FindCommandStatus(
        CommandT inCommand,
        Boolean &outEnabled,
        Boolean &outUsesMark,
        Char16 &outMark,
        Str255 outName);

private:

    CodecType mCodec;
    CodecQ mSpatialQuality;
    Int16 mDepth;

    P2VRPrefsHdl mPrefsHdl;
};
```

[Next](CUtils.cp.md)[Previous](CPrefsWindow.cp.md)

