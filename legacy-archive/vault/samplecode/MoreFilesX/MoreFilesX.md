---
title: MoreFilesX
apple_id: DTS10000474
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-05-13'
source_url: https://developer.apple.com/library/archive/samplecode/MoreFilesX/Introduction/Intro.html
archived_at: '2026-07-18T03:15:13.636484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MoreFilesX.c.md)

# MoreFilesX

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.2, 2005-05-13 rdar://problem/3510800 Changed FSMoveRenameObjectUnicode to handle source and destination directories being the same, and to make sure the destination actually is a directory. rdar://problem/3926695 Replaced FSLockRange and FSUnlockRange with FSLockRangeCompat and FSUnlockRangeCompat. rdar://problem/4012003 Fixed casting and comparison warnings when -Werror -Wmissing-declarations -Wmissing-prototypes -Wall -W -Wcast-qual -Wpointer-arith -Wno-four-char-constants -Wno-unknown-pragmas are used with XCode 2.0. |
| __Build Requirements:__ | Mac OS 9.0 |
| __Runtime Requirements:__ | Carbon Mac OS 9.0 or later, or Mac OS X |

MoreFilesX is a collection of useful high-level File Manager routines that use the HFS Plus APIs introduced in Mac OS 9.0 wherever possible.

While many of the routines in MoreFilesX are based on the older MoreFiles sample code (which used the older File Manager APIs), by using the HFS Plus APIs, the routines in MoreFilesX have several advantages over the older MoreFiles code:

\* The routines are simpler to understand because the high-level HFS Plus APIs are more powerful.

\* The routines support the features of the HFS Plus volume format such as long Unicode filenames and files larger than 2GB.

\* In many cases, the routines execute more efficiently than code that uses the older File Manager APIs -- especially on non-HFS volumes.

\* The routines use Apple's standard exception and assertion macros (the require, check, and verify macros) which improves readability and error handling, and which provides easy debug builds -- just add #define DEBUG 1 and every exception causes an assertion.

\* The routines are thread safe. There are no global or static variables so multiple program threads can use MoreFilesX routines safely.

If you are writing new Carbon applications for Mac OS X that call the File Manager, you should use MoreFilesX -- not MoreFiles. If you're porting existing applications to Mac OS X and those applications use routines from MoreFiles, you should consider switching to the routines in MoreFilesX. The routines were designed for applications running in the Mac OS X Carbon environment. All of the routines will work under Mac OS 9 if you define BuildingMoreFilesXForMacOS9 to 1. Doing that removes code that calls Mac OS X only APIs. MoreFilesX cannot be used in pre-Mac OS 9 system releases. The routines in MoreFilesX have been tested (but not stress-tested) and are fully documented. Requirements: Mac OS 9.0 or later, or Mac OS X Keywords: File Manager Sample Code

[Next](MoreFilesX.c.md)

