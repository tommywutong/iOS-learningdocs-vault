---
title: MFSLives
apple_id: DTS10004026
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2006-11-09'
source_url: https://developer.apple.com/library/archive/samplecode/MFSLives/Introduction/Intro.html
archived_at: '2026-07-18T03:13:51.328781Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](HashNode.c.md)

# MFSLives

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-11-09 Sample VFS plug-in for the Macintosh File System (MFS) volume format, as used on 400KB floppies. |
| __Build Requirements:__ | Xcode 2.4 |
| __Runtime Requirements:__ | Mac OS X 10.4 |

MFSLives is a sample VFS plug-in that implements read-only access to the Macintosh File System (MFS) volume format. This volume format debuted on the original Macintosh in 1984, and was supplanted by HFS (the predecessor to HFS Plus) with the introduction of the Macintosh Plus in 1986. MFS support was dropped from traditional Mac OS in Mac OS 8.1, and it has never been supported on Mac OS X.
MFS is an excellent volume format for sample code because it's very simple but it allows you to exercise the code paths associated with Macintosh-specific metadata (specifically, Finder info, multi-fork files, and volfs).

[Next](HashNode.c.md)

