---
title: DirectSetEntries
apple_id: DTS10000142
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DirectSetEntries/Listings/DirectSetEntries_c.html
archived_at: '2026-07-18T03:06:58.884134Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DirectSetEntries](DirectSetEntries.md)


[Next](Document%20Revision%20History.md)[Previous](DirectSetEntries.md)

# DirectSetEntries.c

```c
#include    <Resources.h>
#include    <Memory.h>
#include    <Video.h>
#include    <Quickdraw.h>
#include    <Files.h>
#include    <Devices.h>

#define TRUE            0xFF
#define FALSE           0

struct myVDEntryRecord {
        CSpecArray *csTable;
        short   csStart;
        short   csCount;
    };
typedef struct myVDEntryRecord myVDEntryRecord;

main()
{
    ColorSpec           myTable[0xFF];
    short               i;
    OSErr               result;
    myVDEntryRecord     *VDPtr, **sickHack;
    GDHandle            curdev, olddev;
    CntrlParam          pRecord;

    VDPtr = (myVDEntryRecord *) NewPtr (sizeof (myVDEntryRecord));
    if (VDPtr == nil || MemError() != noErr)
        Debugger();

    olddev = GetGDevice();

    curdev = GetDeviceList();
    do {
        if ((**curdev).gdType == 2) {
            for (i=0;i<=0xFE;i++) {
                myTable[i].value = i;
                myTable[i].rgb.red = 0xffff - i*0xff;
                myTable[i].rgb.green = 0x0 + i*0xff;
                myTable[i].rgb.blue = 0x0 + i*0xff;
                }

            VDPtr->csTable = (CSpecArray *)&myTable;
            VDPtr->csStart = 0;
            VDPtr->csCount = 0xfe;

            pRecord.ioCompletion = nil;
            pRecord.ioVRefNum = 0;
            pRecord.ioCRefNum = (**curdev).gdRefNum;
            pRecord.csCode = 8;
            sickHack = (myVDEntryRecord **)&pRecord.csParam;
            *sickHack = VDPtr;

            if (result = PBControl((ParmBlkPtr)&pRecord, false) )
                Debugger();
            }

        curdev = GetNextDevice(curdev);
        } while (curdev != nil);

    SetGDevice(olddev);
}
```

[Next](Document%20Revision%20History.md)[Previous](DirectSetEntries.md)

