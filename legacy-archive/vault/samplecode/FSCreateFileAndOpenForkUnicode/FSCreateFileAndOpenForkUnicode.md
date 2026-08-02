---
title: FSCreateFileAndOpenForkUnicode
apple_id: DTS10003677
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/FSCreateFileAndOpenForkUnicode/Introduction/Intro.html
archived_at: '2026-07-18T03:08:08.609211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# FSCreateFileAndOpenForkUnicode

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2005-06-01 Demonstartes the use of FSCreateFileAndOpenForkUnicode to create a file with restricted access on disk and a read/write access path. |
| __Build Requirements:__ | Tiger |
| __Runtime Requirements:__ | Tiger |

This sample is a tool which shows the use of FSCreateFileAndOpenForkUnicode to create a file on disk with restricted access from the outset while allowing the creating process to have a read/write access path to the item. The sample creates the file with a POSIX mode of 000 (no access) and an access control list with a single access control entry which grants the current user read access to the file data. It then writes out some data to the file on the fsRdWrPerm access path it requested. The target volume needs to have extended security enabled since the sample depends on ACLs (the tool checks for this support). FSCreateFileAndOpenForkUnicode enables the creation of files with restricted access on disk while allowing the creator to have less restricted access (a file can be created with no access or read only access and the fork opened with read/write access. Once the inital write path is closed, a subsequent attempt to open the file for writing would fail).

[Next](main.c.md)

