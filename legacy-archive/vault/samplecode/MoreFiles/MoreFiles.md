---
title: MoreFiles
apple_id: DTS10000473
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreFiles/Introduction/Intro.html
archived_at: '2026-07-18T03:15:08.407735Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CHeaders-DirectoryCopy.h.md)

# MoreFiles

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Shows various File Manager operations (file copy, etc.) through a collection of high-level routines. |
| __Build Requirements:__ | Mac OS X Carbon |
| __Runtime Requirements:__ | Carbon |

MoreFiles is a collection of high-level routines written over the years to answer File Manager questions developers have sent to Apple Developer Technical Support, and to answer questions on various online services and the internet. The routines have been tested (but not stress-tested), documented, code-reviewed, and used in both my own programs, the Macintosh OS, and in many commercial products. Important Note These routines are meant to be used from an application environment. In particular, some routines use static variables, which require an A5 world (if you're building 68K code), and almost all routines make calls that are unsafe at interrupt time (i.e., synchronous File Manager calls and Memory Manager calls). If you plan to use these routines from stand-alone 68K code modules, you may need to make some modifications to the code that uses static variables. Don't even think about using most of these routines from code that executes at interrupt time. Note: If you need to use the routines in FSpCompat in stand-alone 68K code, set GENERATENODATA to 1 in FSpCompat.c (or pass it in) so globals (static variables) are not used. Some routines in Search.c also use static variables. Build Environments MoreFiles is built using the latest development environments I have access to and Universal Interfaces v3.4. You might have to make some minor changes to compile or link with MoreFiles. Keywords: File Manager Sample Code

[Next](CHeaders-DirectoryCopy.h.md)

