---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/main_c.html
archived_at: '2026-07-18T03:11:57.603668Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](Not%20used%20in%20this%20example-CheckEjectability.c.md)[Previous](How%20to%20Detect%20a%20CD.md)

# main.c

```c
#include <stdio.h>
#include <types.h>
#include <Files.h>
#include <Devices.h>

#include "WhereCDs.h"

/* 
 * use this version of a Control structure for a ReadTOC call
 */
typedef struct {
    struct QElem *qLink;
    short qType;
    short ioTrap;
    Ptr ioCmdAddr;
    ProcPtr ioCompletion;
    OSErr ioResult;
    char *ioNamePtr;
    short ioVRefNum;
    short ioCRefNum;
    short csCode;
    unsigned long   discID;
    char    unused[18];
} CDTOCParam;

enum {
    kReadTOC = 100,
    kDiskIsLocked = 0x80,
    kDiskEjectableFlag = 0x08
};

#define kDriverName "\p.AppleCD"

void main(void);
Boolean DriveIsEjectable(DrvQEl *queueElementPtr);
Boolean DriveIsHardwareLocked(DrvQEl *queueElementPtr);
OSErr IDDisc(short refNum, unsigned long *discID);
void TechNoteCDs(void);


/************************************************************************
 *
 *  Function:   main
 *  
 *  Purpose:    for testing only
 *
 *  Returns:    nothing
 *
 *  Side Effects: prints list of available CD-ROM drives (best guess)
 *
 *  Description: scan drive queue.  Call PBControl with a csCode 100
 *               ReadTOC call. See tech note DV 22 for details.
 *
 ************************************************************************/
void main(void)
{
    OSErr   err;
    short   refNum;
    UInt32  discID = 0L;
    QHdrPtr driveQueuePtr;
    DrvQEl  *queueElementPtr;

    printf("Test of identifying a disc\n"); // initializes toolbox

    driveQueuePtr = GetDrvQHdr();
    queueElementPtr = (DrvQEl *)driveQueuePtr -> qHead;

    do 
    {
        refNum = queueElementPtr->dQRefNum;

        if ( DriveIsEjectable(queueElementPtr) && 
                DriveIsHardwareLocked(queueElementPtr) )
            printf("drive with refNum %d (0x%x) is ejectable and hardware locked\n", 
                        refNum, refNum);

        err = IDDisc(refNum, &discID);      // If we don't get an error from
                                            // calling ReadTOC, assume it's a CD.
        if (!err)
            printf("I think this is a CD-ROM disc.\n");


        queueElementPtr = (DrvQEl *)queueElementPtr->qLink;
    } while (queueElementPtr != nil);

    TechNoteCDs();
    printf("Finished!\n");
}


/************************************************************************
 *
 *  Function:       DriveIsEjectable
 *
 *  Purpose:        determine if drive is ejectable
 *
 *  Returns:        true if ejectable, false if not
 *
 *  Side Effects:   none
 *
 *  Description:    look at the 4 bytes preceeding the drive queue
 *                  element.
 *
 ************************************************************************/
Boolean DriveIsEjectable(DrvQEl *queueElementPtr)
{
    UInt8 * bytePtr;

    bytePtr = (UInt8 *)queueElementPtr;
    bytePtr -= 4;
    return ( (bytePtr[1] & kDiskEjectableFlag) != kDiskEjectableFlag );

}


/************************************************************************
 *
 *  Function:       DriveIsHardwareLocked
 *
 *  Purpose:        determine if drive is HardwareLocked
 *
 *  Returns:        true if HardwareLocked, false if not
 *
 *  Side Effects:   none
 *
 *  Description:    look at the 4 bytes preceeding the drive queue
 *                  element.
 *
 ************************************************************************/
Boolean DriveIsHardwareLocked(DrvQEl *queueElementPtr)
{
    UInt8 * bytePtr;

    bytePtr = (UInt8 *)queueElementPtr;
    bytePtr -= 4;
    return ( (bytePtr[0] & kDiskIsLocked) == kDiskIsLocked );

}


/************************************************************************
 *
 *  Function:       IDDisc
 *
 *  Purpose:        return total time on this disc as unique ID
 *
 *  Returns:        OSErr
 *                  either noErr if everything was okay
 *                  or some parameter error from driver call.
 *
 *  Side Effects:   fills in discID
 *
 *  Description:    call the driver ReadTOC call to get lead-out time.
 *                  Return this time as the unique id for this disc.
 *
 ************************************************************************/
OSErr IDDisc(short refNum, unsigned long *discID)
{
    CDTOCParam  myPB;
    OSErr   result;

    myPB.ioCompletion = 0;
    myPB.ioNamePtr = (char *) 0;
    myPB.ioVRefNum = 0;
    myPB.ioCRefNum = refNum;
    myPB.csCode = kReadTOC;
    myPB.discID = 0x00020000;   /* request lead-out time */

    result = PBControlSync((ParmBlkPtr)&myPB);

    if (result == noErr)
        *discID = myPB.discID >> 8;
    else
        *discID = 0;
    return result;
}


/************************************************************************
 *
 *  Function:       TechNoteCDs 
 *
 *  Purpose:        use the technique in DV 22 to find CD-ROM drives
 *
 *  Returns:        nothing
 *
 *  Side Effects:   prints a list of found CDs
 *
 *  Description:    call the routine documented in DV 22 and print 
 *                  the result
 *
 ************************************************************************/
void TechNoteCDs(void)
{
    UInt8   locations;
    short   i;

    locations = WhereCDs();
    printf("The WhereCDs() procedure reports there are CDs at SCSI IDs: ");
    for (i = 0; i < 7; i++)
        if (locations & (1 << i))
            printf("%d ", i);
    putchar('\n');
}
```

[Next](Not%20used%20in%20this%20example-CheckEjectability.c.md)[Previous](How%20to%20Detect%20a%20CD.md)

