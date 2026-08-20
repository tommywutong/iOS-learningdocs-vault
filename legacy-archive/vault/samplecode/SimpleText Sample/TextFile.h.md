---
title: SimpleText Sample
apple_id: DTS10000736
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleText_Sample/Listings/TextFile_h.html
archived_at: '2026-07-18T03:24:21.736574Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleText Sample](SimpleText%20Sample.md)


[Next](TextFile.r.md)[Previous](TextFile.c.md)

# TextFile.h

```c
/*
    File:       TextFile.h

    Contains:   Text file support for simple text application

** Copyright 1993, 1995-1996 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.

*/

#include "SimpleText.h"

#define kTextStrings            kTextBaseID
#define iSpeakSelection             1
#define iSpeakAll                   2
#define iStationeryHelp             3
#define iStationerySelectedHelp     4
#define iDocumentHelp               5
#define iDocumentSelectedHelp       6
#define iPictureMarker1             7
#define iPictureMarker2             8

#define kTextSaveAsDialogID     kTextBaseID+1
#define iTextDocumentItem       14
#define iStationeryDocumentItem 15
#define iTextUserItem           16
#define iStationeryUserItem     17

#define kMaxLength              31*1024


#ifndef REZ
    struct TextDataRecord
        {
        WindowDataRecord        w;

        Boolean                 insideClickLoop;    // inside the click loop
        TEClickLoopUPP          docClick;           // old click loop value
        TEHandle                hTE;                // text editing area
        Handle                  soundHandle;        // sound associated with this machine

        // undo support items
        short                   prevCommandID;
        Handle                  prevText;
        Handle                  prevStyle;
        short                   prevLength;
        short                   prevSelStart;
        short                   beforeSelStart, beforeSelEnd;
        };
    typedef struct TextDataRecord TextDataRecord, *TextDataPtr; 
#endif
```

[Next](TextFile.r.md)[Previous](TextFile.c.md)

