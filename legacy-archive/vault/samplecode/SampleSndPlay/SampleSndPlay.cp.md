---
title: SampleSndPlay
apple_id: DTS10000350
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SampleSndPlay/Listings/SampleSndPlay_cp.html
archived_at: '2026-07-18T03:23:04.987800Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleSndPlay](SampleSndPlay.md)


[Next](Document%20Revision%20History.md)[Previous](SampleSndPlay.md)

# SampleSndPlay.cp

```c
#include    <Quickdraw.h>
#include    <Windows.h>
#include    <dialogs.h>
#include    <OSEvents.h>
#include    <Packages.h>
#include    <Sound.h>

#define TRUE            0xFF
#define FALSE           0

main()
{
    Point               where = {20,20};
    OSErr               err;
    SFReply             reply;
    short               refnum;
    char*               string;

    InitGraf(&qd.thePort);
    FlushEvents(everyEvent, 0);
    InitWindows();
    InitDialogs(nil);
    InitCursor();

    string = (char*) "\pPick a SND File";

    SFGetFile (where, (Str255) string, nil, -1, (SFTypeList) nil, nil, &reply);
    err = FSOpen(reply.fName, reply.vRefNum, &refnum);
    if (err != noErr)
        Debugger();

    err = SndStartFilePlay (nil, refnum, 0, 74000, nil, nil, nil, FALSE);
    if (err != noErr)
        Debugger();

}
```

[Next](Document%20Revision%20History.md)[Previous](SampleSndPlay.md)

