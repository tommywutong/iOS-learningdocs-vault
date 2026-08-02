---
title: PlayMovie
apple_id: DTS10001042
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/PlayMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:19:06.960684Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-FileMenu.java.md)

# PlayMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-05-11 Support for XCode 2. Modified project layout for platform independent distribution and compilation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcmbugiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

Excellent if you are just getting started with QuickTime for Java! A Simple example demonstrating QuickTime content playback.

The user is shown a sample movie and is able to open another QuickTime Movie file through the File menu. The opened movie is presented in its own window with the standard movie controller. The window is initially sized to fit the movie but resizing the window will scale the movie. The MovieController is displayed on screen using a QTComponent. The QTComponent is created using QTFactory.makeQTComponent(MovieController mc).

[Next](src-FileMenu.java.md)

