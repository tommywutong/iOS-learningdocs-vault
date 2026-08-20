---
title: qtcustombutton
apple_id: DTS10000855
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcustombutton/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.187754Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](QTCustomButton.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtcustombutton

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Display a pop-up menu when the user clicks on the custom button in the movie controller bar. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This code snippet shows one way to display a pop-up menu when the user clicks on the custom button in the movie controller bar (just like the QuickTime web browser plug-in does for its custom button). The basic idea is very simple: just call PopUpMenuSelect when the user clicks the custom button. Before we do that, however, we need to obtain a MenuHandle to the desired pop-up menu. Here we use NewMenu and MacAppendMenu to create the menu on the fly; we do this mainly so that we don't need to drag a resource file around. A real application would just call MacGetMenu to read the menu from its resource file. Requires: QuickTime 5 Keywords: QuickTime, custom button, movie controller, pop-up

[Next](QTCustomButton.c.md)

