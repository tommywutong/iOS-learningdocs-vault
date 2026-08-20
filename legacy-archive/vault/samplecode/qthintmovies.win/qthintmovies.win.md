---
title: qthintmovies.win
apple_id: DTS10000866
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qthintmovies.win/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.587158Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qthintmovies.win

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Illustrates how to add hint tracks to a QuickTime movie. |
| __Build Requirements:__ | MW CodeWarrior |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

A QuickTime movie that is to be streamed should contain a "hint track" for each media track in the movie. A hint track contains information that assists the streaming server in the process of forming and timing network packets. These hint tracks essentially free the server from having to know the details of network protocols or media-specific codecs, thereby reducing run-time processing. This mechanism also allows the server to stream new codec and network protocol types without modification (once they can be hinted). This sample code illustrates how to add hint tracks to a QuickTime movie. It illustrates several methods of doing this, and shows how to either display or not display the settings dialog box. Requires: QuickTime 5 Keywords: QuickTime, hint track, movie

[Next](README.txt.md)

