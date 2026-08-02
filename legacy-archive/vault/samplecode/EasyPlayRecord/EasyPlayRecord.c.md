---
title: EasyPlayRecord
apple_id: DTS10000345
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/EasyPlayRecord/Listings/EasyPlayRecord_c.html
archived_at: '2026-07-18T03:07:32.409120Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EasyPlayRecord](EasyPlayRecord.md)


[Next](Document%20Revision%20History.md)[Previous](EasyPlayRecord.md)

# EasyPlayRecord.c

```c
#include    <Quickdraw.h>
#include    <Windows.h>
#include    <dialogs.h>
#include    <OSEvents.h>
#include    <Memory.h>
#include    <StandardFile.h>
#include    <Sound.h>
#include    <SoundInput.h>
#include    <OSUtils.h>

#define TRUE            0xFF
#define FALSE           0

#ifdef powerc
   QDGlobals    qd;
#endif


main()
{
    Point               where = {20,20};
    Point               whereto = {100,100};
    OSErr               err;
    StandardFileReply   reply;
    short               refnum;
    Handle              SNDHand;
    SndChannelPtr       chan;

    InitGraf(&qd.thePort);
    FlushEvents(everyEvent, 0);
    InitWindows();
    InitDialogs(nil);
    InitCursor();

    StandardGetFile (nil, -1, nil, &reply);

    err = HOpen(reply.sfFile.vRefNum, reply.sfFile.parID, reply.sfFile.name, fsRdPerm, &refnum);

    if (err != noErr)
      Debugger();

    err = SndStartFilePlay (nil, refnum, 0, 74000, nil, nil, nil, TRUE);
    if (err != noErr)
        Debugger();

    SNDHand = NewHandle (0xc9000);
    if (MemError() != noErr || SNDHand == nil)
        Debugger();

    err = SndRecord (nil, whereto, siBestQuality, &SNDHand);
    if (err != noErr)
        Debugger();

    FSClose (refnum);

    chan = nil;
    err = SndNewChannel (&chan, 0, 0, nil);
    if (err != noErr)
        Debugger();

    err = SndPlay (chan, SNDHand, FALSE);
    if (err != noErr)
        Debugger();

    err = SndDisposeChannel (chan,FALSE);
    if (err != noErr)
        Debugger();
}
```

[Next](Document%20Revision%20History.md)[Previous](EasyPlayRecord.md)

