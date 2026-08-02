---
title: QTSimpleApplet
apple_id: DTS10000982
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/samplecode/QTSimpleApplet/Introduction/Intro.html
archived_at: '2026-07-18T03:21:20.663183Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# QTSimpleApplet

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-06-28 Support for XCode 2. Modified project layout for platform independent distribution and compilation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydaojygiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

Demonstrates how to display QuickTime content inside a java.awt.Applet. By implementing init, start, stop, and destroy methods enables the applet to be reloaded, suspended and resumed. For example the user leaving and returning to the page with the applet. The use of the init/destroy and start/stop methods are reciprocal in their activities.

This introductory sample uses QTFile, on a local filesystem resource, in lieu of invoking a File Open dialogue. Please see QTStreamingApplet for an example that uses a remote server resource.

[Next](README.txt.md)

