---
title: LockFile
apple_id: DTS10000283
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/LockFile/Introduction/Intro.html
archived_at: '2026-07-18T03:13:47.114363Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SetLockBit.c.md)

# LockFile

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Installer 3.2, 3.3 and possibly later |

Sample to demonstrate setting the file lock bit. This action atom code resource must be called through a post installation action atom. In the selector field, pass in the name of the target 'infs' resource id. The code resource gets the resource, converts the partial path name field to a pascal string, then calls, SetFLock. A result of true is always returned so as not to abort the installation. Requirements: Installer 3.2, 3.3 and possibly later Keywords: Installer, file lock bit, LockFile

[Next](SetLockBit.c.md)

