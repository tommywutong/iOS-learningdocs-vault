---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CSoundboardWindow_h.html
archived_at: '2026-07-18T03:25:13.497706Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](GWLayers.c.md)[Previous](CSoundboardWindow.cp.md)

# CSoundboardWindow.h

```c
// ===========================================================================
//  CSoundboardWindow.h         ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#pragma once

#include <LWindow.h>

class   CSoundboardWindow : public LWindow {
public:
    enum { class_ID = 'sWnd' };
                        CSoundboardWindow(LStream *inStream);
    virtual             ~CSoundboardWindow();

    static CSoundboardWindow*   CreateSoundboardWindow(ResIDT inWindowID,
                                    LCommander *inSuperCommander);
    static CSoundboardWindow*   CreateSoundboardWindowStream(LStream *inStream);

    virtual void        AttemptClose();
    virtual void        DoClose();

    virtual Boolean     ObeyCommand(CommandT inCommand, void *ioParam = nil);
    virtual void        FindCommandStatus(CommandT inCommand,
                            Boolean &outEnabled, Boolean &outUsesMark,
                            Char16 &outMark, Str255 outName);
    virtual void        Show();
    virtual void        ClickInContent(const EventRecord &inMacEvent);
};
```

[Next](GWLayers.c.md)[Previous](CSoundboardWindow.cp.md)

