---
title: HTML5VideoOverlays
apple_id: DTS40010109
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-06-23'
source_url: https://developer.apple.com/library/archive/samplecode/HTML5VideoOverlays/Introduction/Intro.html
archived_at: '2026-07-18T03:11:36.200288Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# HTML5VideoOverlays

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2010-06-23 Added a fullscreen button, which is shown if the browser supports triggering fullscreen mode programmatically for HTML5 <video>. |
| __Build Requirements:__ | Safari 5.0 or later, or Safari on iPhone OS 3.2 or later |
| __Runtime Requirements:__ | Safari 5.0 or later, or Safari on iPhone OS 3.2 or later |

This sample uses layered HTML elements, media events, and CSS transitions to optimize the user experience.

An image and a semi-opaque "Click To Play" button are initially laid over the video. When the "Click To Play" button is clicked, a progress spinner is shown until the video can be played all the way through. At this point, CSS transitions are used to fade out the progress spinner and overlay image, as the video is loaded and begins to play. Two buttons appear when the video begins playing - a simple play/pause button, and a button that triggers fullscreen video display. The fullscreen button is only shown in browsers that support programmatically switching to fullscreen mode.

This sample also uses touch events on iPhone OS/iOS to provide immediate feedback when buttons are touched.

[Next](ReadMe.txt.md)

