---
title: vrflattenmovie
apple_id: DTS10001023
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrflattenmovie/Introduction/Intro.html
archived_at: '2026-07-26T19:52:57.115104Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](VRFlatten.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# vrflattenmovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates calling the QTVR (Virtual Reality) Flattener directly. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

QuickTime VR (Virtual Reality) is a compelling technology for delivering interactive object and panorama movies. QTVR has always been well-suited for web delivery because of its compact size. But over low-bandwidth connections, large movies take time to download. A Streaming VR movie compensates for slow-bandwidth connections in one of two ways: either by first rapidly downloading a low-resolution preview of the VR movie, or by resequencing the data so that the panorama data loads in and displays a tile at a time. Either way, users on slow-bandwidth connections are quickly presented with data they can use to determine if they want to continue the download. This flattening is accomplished using the QTVR Flattener extension. Currently (as of QuickTime version 4.1.2) this extension is not automatically installed when you install QuickTime; it is likely however that it will be included in some future version. Your application can call the QTVR Flattener directly. That's what is sample code snippet illustrates. Requires: QuickTime 5 Keywords: QuickTime, QTVR, flattener, extension

[Next](VRFlatten.c.md)

