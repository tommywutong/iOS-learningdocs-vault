---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/Not_used_in_this_example_GetDriveType_c.html
archived_at: '2026-07-18T03:11:57.268706Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](Not%20used%20in%20this%20example-GetDriveType.h.md)[Previous](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-main.cp.md)

# Not used in this example/GetDriveType.c

```c
#include <Files.h>
#include <Devices.h>
#include "GetDriveType.h"

#define csGetDriveType 96

typedef struct ADriveTypeRec {
    QElemPtr        qLink;
    short           qType;
    short           ioTrap;
    Ptr             ioCmdAddr;
    IOCompletionUPP ioCompletion;
    OSErr           ioResult;
    StringPtr       ioNamePtr;
    short           ioVRefNum;
    short           ioCRefNum;
    short           csCode;
    struct {
            short int driveType;
            short int csParam[10];  // 11 shorts total.
    } csParam;
} ADriveTypeRec;

pascal  OSErr GetDriveType(short ioRefNum, short *Type) 
{
   OSErr           osErr;
   ADriveTypeRec   *pb;

   pb = (ADriveTypeRec *) NewPtrClear(sizeof (*pb));
   osErr = MemError();
   if (0 != pb && noErr == osErr) 
   {
       (*pb).ioCRefNum     = ioRefNum;
       (*pb).ioVRefNum     = 1;     // always define; may have multiple drives
       (*pb).ioCompletion  = nil;
       (*pb).ioNamePtr     = nil;
       (*pb).csCode        = csGetDriveType;
       osErr = PBStatusSync((ParmBlkPtr)pb);    // status, not control call
       if(osErr == noErr)
         *Type = (*pb).csParam.driveType;
       DisposPtr((Ptr) pb);
   }

   return osErr;
}
```

[Next](Not%20used%20in%20this%20example-GetDriveType.h.md)[Previous](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-main.cp.md)

