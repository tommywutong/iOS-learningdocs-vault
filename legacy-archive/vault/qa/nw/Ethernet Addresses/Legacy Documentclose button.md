---
title: Ethernet Addresses
apple_id: DTS10001417
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw05.html
archived_at: '2026-07-18T02:29:44.169366Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW05Ethernet Addresses |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: How can I obtain an Ethernet address programmatically? I can get correct Ethernet addresses for RAM-based drivers, but this does not appear to work for all drivers. For example, addresses for PowerBooks with DaynaPort connections are not available. I am using the following code to obtain Ethernet addresses:   |  | | --- | | ```     myErr = OpenDriver("\p.ENET", &myRefNum);     theEPB.EParms1.ioRefNum = myRefNum;      theEPB.EParms1.ePointer = NewPtrClear(78);     theEPB.EParms1.eBuffSize = 78;     theEPB.EParms1.ioNamePtr = NULL;     myErr = EGetInfo(&theEPB,false); ``` |   How can I scan through all the installed Ethernet drivers for the one that's active and obtain information about that one?  A: Your approach for obtaining Ethernet address information seems appropriate. Here are a few pieces of information that may help:   1. OpenDriver("\p.ENET", &myRefNum) only opens the first Ethernet driver. If the system has more than one Ethernet card installed, you have to open them explicitly. 2. Machines such as the SE and PowerBooks that have the Ethernet hardware connected via the SCSI port are accessed through ENET0 (most machines have this ability).   The following is a code fragment that you can use:   |  | | --- | | ``` /* check internal non slotted card    check if enet0 driver is installed */  short     saveRes;     saveRes = LMGetResLoad();     LMSetResLoad(0)     GetNamedResource('DRVR',"\p.ENET0");   // check if ENET0 is in ROM     LMSetResLoad(saveRes)     if(!ResError()) {  /* Setup Open PB */     PB.slotDevParam.ioNamePtr  = "\p.ENET0";   // Attempt to open it     PB.slotDevParam.ioVRefNum    = 0;     PB.slotDevParam.csCode        = 0;     PB.slotDevParam.ioSlot        = 0;     PB.slotDevParam.ioID        = 0;  /* try and open the internal non slotted enet card */     ErrNo = PBOpenSync(&PB);   // notice I do a regular open call $A000     refnum = PB.ioRefNum; ``` |  3. For NuBus and SE30 devices (and PCI slots), you have to use the Slot Manager to scan for available Ethernet cards, per this example:  |  | | --- | | ``` /* Setup Open PB  for sloted device */     PB.slotDevParam.ioNamePtr  = "\p.ENET";     PB.slotDevParam.ioVRefNum    = 0;     PB.slotDevParam.csCode        = 0; /* try Slotmanger Call */     if(!OSTrapAvailable (_SlotManager)) return(Error);     SPB.spExtDev     = 0;     SPB.spCategory    = 4;        /* Network     */     SPB.spCType        = 1 ;        /* EtherNet */     SPB.spTBMask    = 0x3;  /* loop on each card */     while((ErrNo = SNextTypeSRsrc(&SPB)) == noErr){         PB.slotDevParam.ioSlot        = SPB.spSlot;         PB.slotDevParam.ioID        = SPB.spID; /* try and open the enet card */         ErrNo = PBOpenImmed(&PB);       // Notice I Do an OpenImmed $A200         refnum = PB.ioRefNum;      } ``` |  4. An important point to consider: `OpenDriver` calls fail when Ethernet devices are not cabled or hooked up, so it's not possible to get the address of Ethernet cards that aren't hooked up. |

#### [May 01 1995]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
