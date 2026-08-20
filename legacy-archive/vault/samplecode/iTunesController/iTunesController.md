---
title: iTunesController
apple_id: DTS10003879
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-02-23'
source_url: https://developer.apple.com/library/archive/samplecode/iTunesController/Introduction/Intro.html
archived_at: '2026-07-18T03:29:45.810642Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# iTunesController

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-02-23 iTunesController allows you to control iTunes without having to bring it to the foreground. |
| __Build Requirements:__ | Xcode 2.2, Universal Binary |
| __Runtime Requirements:__ | Mac OS X 10.4 |

iTunesController makes use of the RegisterEventHotKey API which allows you to register to receive hotkey events while in the foreground or background. Registering for a hotkey such as <command>-P causes problems because, once registered for a hotkey, that event does NOT get propagated to the frontmost application, and in this case, would intercept it from printing. We overcome this problem, in the routine PostHotKeyKeyboardEvent, by first unregestering for hotkeys, posting the event to the frontmost application using CGPostKeyboardEvent, and then re-registering for hotkeys. This sample also demonstrates how to communicate with iTunes through an AppleScript in our timer routine, PeriodicTimerAction.
Builds as a Universal Binary

[Next](main.c.md)

