---
title: SimpleHIMovieViewPlayer
apple_id: DTS10003662
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-07-15'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleHIMovieViewPlayer/Introduction/Intro.html
archived_at: '2026-07-18T03:24:03.073007Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# SimpleHIMovieViewPlayer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-07-15 Added Xcode 2.1 project & universal binary target |
| __Build Requirements:__ | Xcode 2.1+, Xcode 2.0, CodeWarrior 9.5 |
| __Runtime Requirements:__ | Mac OS X 10.4+, QuickTime 7+ |

SimpleHIMovieViewPlayer is an application demonstrating how to use an HIMovieView to play back QuickTime Movies. It allows some manipulation of the view's attributes and displays the views optimum bounds and current bounds as the window size changes.
Xcode 2.1 project builds universal binary.
What Is HIMovieView?
HIMovieView is similar to the older Carbon Movie Control in that it is a higher level interface to the QuickTime Movie Controller Component. This view however is a first class HIObject and not simply a custom control. The advantage of using this view over both the lower level control and the Carbon Movie Control is that it uses Core Video and Visual Contexts to render Movies providing higher performance, live resizing and a much simpler client interface.
Availability:
HiMovieView was added in QuickTime 7 and is available only on Mac OS X 10.4 and greater.
What Is HIView?
HIView is a object-oriented view system available for implementing Carbon user interface elements.

[Next](main.c.md)

