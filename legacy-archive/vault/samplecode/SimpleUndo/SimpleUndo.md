---
title: SimpleUndo
apple_id: DTS40008408
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: Foundation
published: '2013-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleUndo/Introduction/Intro.html
archived_at: '2026-07-18T03:24:26.950169Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SimpleUndo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2013-05-03 Adopted storyboards and ARC. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnbqhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 6.0 SDK or later |
| __Runtime Requirements:__ | iOS 5.0 or later |

The root view controller displays information (title, author, and copyright date) about a book. The user can edit this information by tapping Edit in the navigation bar. When editing starts, the root view controller creates an undo manager to record changes. The undo manager supports up to three levels of undo and redo. When the user taps Done, changes are considered to be committed and the undo manager is disposed of.

[Next](ReadMe.txt.md)

