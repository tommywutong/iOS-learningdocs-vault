---
title: MovieAssembler
apple_id: DTS10004133
resource_type: Sample Code
platform: macOS
topic: Apple Applications
technology: null
published: '2007-11-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieAssembler/Introduction/Intro.html
archived_at: '2026-07-18T03:16:03.575206Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# MovieAssembler

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2007-11-14 Updated FCP_AppleEvents.h to include revised event definitions and documentation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimjtgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.4.0 or later, Xcode 2.1 or later. |
| __Runtime Requirements:__ | Mac OS X 10.4.0 or later, Final Cut Pro 5.1.2 or later. |

The MovieAssembler sample application demonstrates the use of several new developer features in Final Cut Pro 5.1.2. It demonstrates how to communicate with Final Cut Pro using AppleEvents, how to modify FCP project files using XML and how to use the QuickTime metadata APIs to provide media file identification for FCP.

- AppleEvent commands to communicate with and control Final Cut Pro.

- QuickTime metadata to identify and process movie files.

- Version 3 of the Final Cut Pro XML Interchange Format to access and modify the contents of sequences in Final Cut Pro project files.

Once configured properly, MovieAssembler monitors a watch folder for newly copied media files, using ID tag(s) stored as metadata to specify if and where a particular media file should be inserted into a selected sequence. All of these operations, while performed in Final Cut Pro, are initiated and configured from the MovieAssembler application.

[Next](main.m.md)

