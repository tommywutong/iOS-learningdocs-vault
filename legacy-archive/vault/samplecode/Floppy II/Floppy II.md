---
title: Floppy II
apple_id: DTS10000016
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Floppy_II/Introduction/Intro.html
archived_at: '2026-07-18T03:08:46.921320Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](FloppytestII.c.md)

# Floppy II

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This application (Floppy II) uses the sony driver calls to get the format list of a super drive disk. It then steps through the list to find if the disk supports MFM 720 disk and if so, it reformats the disk to be that type. The usefullness of this app is to see how to use the status and control calls in the sony driver and how to search the data which is returned. Warning: When you run this app, don't have a disk you want in drive 1. The data on the disk will get blown away and there are no warnings. Requires: floppy disk drive, SuperDrive Keywords: floppy disk, Sony, return format list, format, MFM

[Next](FloppytestII.c.md)

