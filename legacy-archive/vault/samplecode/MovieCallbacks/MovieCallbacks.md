---
title: MovieCallbacks
apple_id: DTS10000966
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/MovieCallbacks/Introduction/Intro.html
archived_at: '2026-07-18T03:16:04.753397Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-MovieCallbacks.java.md)

# MovieCallbacks

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-05-11 Support for XCode 2. Modified project layout for platform independent distribution and compilation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydaojwgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

Call-backs provide the facility for QuickTime to invoke your Java application code, at specific points, during program execution. Call-backs are provided in many parts of QuickTime including the MovieController, Movie and QuickTimeVR APIs.

The user to chooses a movie using the standard open file dialogue, that also shows a preview. Afterwards, a number of call-backs are installed. Depending on the type of movie opened, different callbacks are installed:

(1) Movie - DrawingComplete proc is used to notify the Java program whenever QuickTime draws to the screen.

(2) MovieController - ActionFilter procs are used - this subclass overides those actions that pass no parameters or a float parameter.

(3) If the Movie contains QuickTime VR content then a number of QTVR callbacks are installed and invoked when panning, tilting, hot-spot entering and leaving.

[Next](src-MovieCallbacks.java.md)

