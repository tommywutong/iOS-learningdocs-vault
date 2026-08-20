---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CQuickTimeWindow_h.html
archived_at: '2026-07-18T03:25:12.819023Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CSliderControl.cp.md)[Previous](CQuickTimeWindow.cp.md)

# CQuickTimeWindow.h

```c
// ===========================================================================
//  CQuickTimeWindow.h          ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LPane.h>
#include <LPeriodical.h>

#ifndef __MOVIES__
#include <Movies.h>
#endif


class   CQuickTimeWindow : public LWindow,
                           public LPeriodical {
public:
    enum { class_ID = 'qWnd' };
                                CQuickTimeWindow(LStream *inStream);
    virtual                     ~CQuickTimeWindow();

    static Movie                GetMovieFromFile(Str63 movieTitle);
    static CQuickTimeWindow*    CreateQuickTimeWindow(ResIDT inWindowID,
                                    LCommander *inSuperCommander,
                                    Boolean inShow = false,
                                    Movie inMovie = nil);
    static CQuickTimeWindow*    CreateQuickTimeWindowStream(LStream *inStream);

    virtual void                DisplayMovie(Movie inMovie, Str63 inMovieTitle);
    virtual void                SpendTime(const EventRecord &inMacEvent);

    virtual void                ClickInContent(const EventRecord &inMacEvent);

    virtual Boolean             AttemptQuit(Int32 inSaveOption);

    virtual Boolean             HandleKeyPress(const EventRecord &inKeyEvent);


protected:
    Movie                       mMovie;
    MovieController             mMovieController;

    virtual void                DrawSelf();

    virtual Boolean             ObeyCommand(CommandT inCommand, void *ioParam = nil);
    virtual void                FindCommandStatus(CommandT inCommand,
                                    Boolean &outEnabled, Boolean &outUsesMark,
                                    Char16 &outMark, Str255 outName);
};
```

[Next](CSliderControl.cp.md)[Previous](CQuickTimeWindow.cp.md)

