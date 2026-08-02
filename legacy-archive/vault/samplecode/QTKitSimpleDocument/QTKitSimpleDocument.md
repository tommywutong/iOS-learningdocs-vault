---
title: QTKitSimpleDocument
apple_id: DTS10003632
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2005-08-01'
source_url: https://developer.apple.com/library/archive/samplecode/QTKitSimpleDocument/Introduction/Intro.html
archived_at: '2026-07-18T03:20:58.033969Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTKitSimpleDocument

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-08-01 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | XCode 2.1, XCode 2.0 |
| __Runtime Requirements:__ | Mac OS X 10.4, or Mac OS X 10.3.9 and QuickTime 7.0 |

QTKitSimpleDocument shows how to build the simplest document-based Cocoa application that opens and displays QuickTime movies.
This sample code has been updated to include a project that produces a universal binary. No code changes were required for it to run correctly on the Developer Transition Systems.
In the Open panel, files with .mov extensions or 'MooV' file types are selectable. When the user selects a file, it opens in a document window.
This sample does not resize the movie window to conform to the natural size of the movie.
Notice that we use setAttribute:forKey to make the movie editable. The Edit menu items then work automagically to support basic movie editing. We do however need to override saveDocument: to save the edited movie.

[Next](main.m.md)

