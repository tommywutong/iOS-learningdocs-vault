---
title: PBAllocate
apple_id: DTS10000040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBAllocate/Listings/Alloc_c.html
archived_at: '2026-07-18T03:18:19.594553Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBAllocate](PBAllocate.md)


[Next](Document%20Revision%20History.md)[Previous](PBAllocate.md)

# Alloc.c

```c
#include    <Files.h>
#include    <Quickdraw.h>
#include    <Windows.h>
#include    <dialogs.h>
#include    <OSEvents.h>
#include    <StandardFile.h>
#include    <Memory.h>
#include    <StdIO.h>

#define TRUE            0xFF
#define FALSE           0

main()
{
    ParmBlkPtr          myRecPtr;
    HParmBlkPtr         myVRecPtr;
    OSErr               err;
    Point               where = {20,20};
    SFReply             reply;
    short               refnum;
    char*               string;

    InitGraf(&qd.thePort);
    FlushEvents(everyEvent, 0);
    InitWindows();
    InitDialogs(nil);
    InitCursor();

/* does not work version */

    string = (char*) "\pWhere is junk file";

    SFGetFile (where, (Str255) string, nil, -1, (SFTypeList) nil, nil, &reply);
    err = FSOpen(reply.fName, reply.vRefNum, &refnum);
    if (err != noErr)
        Debugger();

    myRecPtr = (ParmBlkPtr) NewPtrClear(sizeof(ParamBlockRec));;
    myRecPtr->ioParam.ioRefNum = refnum;
    myRecPtr->ioParam.ioReqCount = 0x7fffffff;

    err = PBAllocate (myRecPtr, FALSE);

    printf("error = %d, Actual count = %d\n",err, myRecPtr->ioParam.ioActCount);

    err = FSClose(refnum);
    if (err != noErr)
        Debugger();

/* The method which works - work around to above bug */

    string = (char*) "\pWhere is File";

    SFGetFile (where, (Str255) string, nil, -1, (SFTypeList) nil, nil, &reply);
    err = FSOpen(reply.fName, reply.vRefNum, &refnum);
    if (err != noErr)
        Debugger();

    myVRecPtr = (HParmBlkPtr) NewPtrClear(sizeof(HParamBlockRec));;
    myVRecPtr->volumeParam.ioVRefNum = reply.vRefNum;

    err = PBHGetVInfo(myVRecPtr, FALSE);
    if (err != noErr)
        Debugger();

    printf("# of blocks = %d\n Size of blocks = %d\n",myVRecPtr->volumeParam.ioVNmAlBlks, myVRecPtr->volumeParam.ioVAlBlkSiz);

    myRecPtr = (ParmBlkPtr) NewPtrClear(sizeof(ParamBlockRec));;
    myRecPtr->ioParam.ioRefNum = refnum;
    myRecPtr->ioParam.ioReqCount = (myVRecPtr->volumeParam.ioVNmAlBlks) * 
                                    (myVRecPtr->volumeParam.ioVAlBlkSiz);

    err = PBAllocate (myRecPtr, FALSE);

    printf("error = %d, Actual count = %d\n",err, myRecPtr->ioParam.ioActCount);

    err = FSClose(refnum);
    if (err != noErr)
        Debugger();
}
```

[Next](Document%20Revision%20History.md)[Previous](PBAllocate.md)

