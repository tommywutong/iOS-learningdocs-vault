---
title: qtfullscreen.win
apple_id: DTS10000862
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtfullscreen.win/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.422071Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtfullscreen.win

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Defines functions that illustrate how to play QuickTime movies full screen. |
| __Build Requirements:__ | QTWindows SDK |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample code has been updated for QuickTime 5.0 README - QTFullScreen QTFullScreen.c defines functions that illustrate how to play QuickTime movies full screen. The key elements to displaying full screen movies are the calls BeginFullScreen and EndFullScreen, introduced in QuickTime 2.5. Here we open a QuickTime movie, configure it to play full screen, associate a movie controller, and then let the controller handle events. Your application should call the function QTFullScreen_EventLoopAction in its event loop (on Mac OS) or when it gets idle events (on Windows).

[Next](README.txt.md)

