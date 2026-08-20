---
title: CDROMDriveCheck
apple_id: DTS10000010
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CDROMDriveCheck/Listings/CDROMDriveCheck_c.html
archived_at: '2026-07-18T03:02:24.710310Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CDROMDriveCheck](CDROMDriveCheck.md)


[Next](Document%20Revision%20History.md)[Previous](CDROMDriveCheck.md)

# CDROMDriveCheck.c

```
/*
File: CDROMDriveCheck.c

What's this?
An MPW c tool that checks to see which SCSI IDs are AppleCD SC drives.  It
makes a status call(97) to the AppleCD SC driver (only works with this 
driver).  On exit from the status call, the byte at csParam+1 contains a 
bit field with bits 7 - 0 corresponding to SCSI IDs 7 - 0.  That is, a 
value of 10000010 means there are two AppleCD SCs attached, with SCSI 
IDs 7 and 1.

Code notes:
```
| ``` As the Blue
yster Cult says, I'm making a career of evil:  the refnum is  ``` |
```c
hard-coded, which would cause Clarus to commence to bitin' on my kneecaps 
(dogcows aren't very tall) were s/he to find out.

Further references:
Apple CD SCª Developers Guide, Revised Edition, Macintosh CD-ROM device 
driver status calls section.   It's available from APDA.

Mark Baumwell 4/1/92

*/

#include    <types.h>
#include    <stdio.h>
#include    <files.h>
#include    <osutils.h>
#include    <strings.h>
#include    <devices.h>
#include    <sane.h>

main()

{
   CntrlParam
   pb;

   OSErr
   err;

   /*Debugger();*/

   pb.ioCompletion = nil;
   pb.ioVRefNum = 1;
   pb.ioCRefNum = -39; /*Don't hard code refnum!!!*/
   pb.ioNamePtr = nil;
   pb.csCode = 97; // checks bit for a CD ROM

   err = PBStatus ((ParmBlkPtr) &pb, false);
   if (err == noErr)
   {
   char byte2; /*in c, char is an 8 bit value*/
   byte2 = ((char*) pb.csParam)[1];
   printf ("the csParam (in decimal) = %i\n",(short)byte2);
   }
   else
   {
   printf ("error = %i\n",err);
   }
}
```

[Next](Document%20Revision%20History.md)[Previous](CDROMDriveCheck.md)

