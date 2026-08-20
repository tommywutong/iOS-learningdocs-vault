---
title: Securely Erasing, Accessing and Dismounting a Macintosh Partition
apple_id: DTS10001197
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-01-11'
source_url: https://developer.apple.com/library/archive/qa/fl/fl11.html
archived_at: '2026-07-18T02:29:29.056240Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/Carbon/idxUserExperience-date.html) >

|  |
| --- |
| Technical Q&A FL11Securely Erasing, Accessing and Dismounting a Macintosh Partition |

|  |
| --- |
| ---   Q: I have heard that data from an erased volume can be easily recovered. I am concerned about the confidentially of the data on my disk, and am trying to write code to securely erase the contents of a Macintosh disk partition (and automatically re-initialize it as a Mac OS volume). I plan to write zeros into the data a number of times, but I am not sure how to gain write access to a partition in some absolute manner from the start to end. How can I accomplish this?  A: The first piece of advice I have for you is that the best way to ensure that data stays confidential is to never ever write to a disk in clear-text. The best solution is to use something like [PGPdisk](http://www.nai.com/products/security/pgpdisk/pgpdisk.asp) to encrypt information automatically before it gets written to disk.  The other thing you need to consider is that simply writing an alternating pattern of zeros and ones to a disk is no longer sufficient to "securely erase" a drive. The recent research on the behavior of erase bands of magnetic media recording and the availability of magnetic force microscopy for the analysis of magnetic media suggests the feasibility of a recovery attack on erased data. Further, it has been suggested that the media sanitization guidelines might also be inadequate for the magnetic encoding scheme used by modern disk drives. Knowing what pattern to write is a science in itself. I suggest you read Peter Gutmann's paper, ["Secure Deletion of Data from Magnetic and Solid-State Memory"](http://www.cs.auckland.ac.nz/~pgut001/secure_del.html), for more information on this subject.  Assuming that you do have a pattern in mind, the best way to erase the Mac OS volume is to access the partition itself through the disk driver. Once you know the disk driver's refnum and the length of the volume, you can simply make low level `PBWrite` calls to the disk driver and write your pattern.  Your first step is to familiarize yourself with the data structures used in the Mac OS file system, which are all documented in _Inside Macintosh: Files and Devices_.  You might also consider breaking into MacsBug and typing the '`vol`' and '`drive`' commands to see what I mean. Try dumping the volume table with '`vol`' then taking the VCB address (`xxxxxxxx`) and dumping that by typing '`DM xxxxxxxx VCB`'.  What your code needs to do is as follows:   1. For a given volume, perform a `PBHGetVInfo`    and record the `ioVDRefNum` and the `ioVDrvInfo`    values, which you will need later to talk to the disk driver (read pp.    2-145, Inside Mac: Files). An easy way to do this is to reuse some of the    code from the `MoreFiles` sample code available from the DTS developer CD's.    Specifically, use the `FindDrive` function from MoreFilesExtras.c,    which will give you back the `vRefNum` and the `DrvQElPtr`. 2. You need to then calculate and record the size of the    volume. An easy way to do this is to leverage the `MoreFiles` code,    `GetDiskBlocks` (from MoreFilesExtras.c) by passing in the    `vRefNum` for the volume. 3. Your next task is to attempt    to unmount the volume from the Mac OS files system; you can do this by    calling `PBUnmountVol` passing in the `ioVRefNum`.    Chances are the unmount will fail because some files might be open. You    will know this if the `PBUnmountVol` call returns a    `fBusyErr`. At this point your user will have to close those    files or quit applications that have them open. If you plan    to do it programmatically you _could_ call `PBGetFCBInfo`    passing in the `vRefnum` from the volume and a starting index of    1 (in `ioFCBIndx`) to build a table of open files. You have to then present    the user with a list of possible applications that might have that file    open (look at the file type '`APPL`' to figure out the application name).  Of course, a better alternative would be to ask the Finder    to unmount the volume using an Apple Event (I'd suggest    that). 4. Once the volume is unmounted from the `filesystem`, you can then access    the partition by calling the low level    `PBWrite` function (as documented on pp. 1-73, Inside Mac:    Devices). Remember that you need to not only pass in to    `PBWrite` the drive number (from the `ioVDrvInfo` of the    `PBHGetVInfo`) in the `ioVRefNum` field, but also the driver    reference number (from the `ioVFRefNum` of the `PBHGetVInfo`)    in the `ioRefNum` field. 5. Once you have written your formatting pattern, you can then    attempt to remount the volume with `PBMount`; this will cause the    `filesystem` to query the user to re-initialize the partition as a Mac volume.   You should find that accessing the partition with the device manager is very simple, but I also warn you (from experience) that writing this kind of code can be risky. Make sure that you do your development on a machine other than your everyday production machine; otherwise, you risk losing your own important files. Be careful. |

#### [Jan 11 1999]

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
