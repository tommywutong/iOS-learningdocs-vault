---
title: SpotlightFortunes
apple_id: DTS40007773
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2008-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/SpotlightFortunes/Introduction/Intro.html
archived_at: '2026-07-18T03:25:21.958541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](FortuneCookie-GetMetadataForFile.m.md)

# SpotlightFortunes

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2008-06-06 Demonstrates how to provision a Spotlight importer plug-in for a custom UTI, and how to use a NSMetadataQuery with bindings to display live query results in a table view. |
| __Build Requirements:__ | Xcode 3.1 and later, Mac OS X v10.5 and later |
| __Runtime Requirements:__ | Mac OS X v10.5 and later |

This sample was inspired by the classic Unix fortune program. Instead of reading entries from a monolithic .fortunes file, it uses Spotlight to find all files with the com.example.fortune-file UTI and displays them in a Cocoa table view. Since the focus of this sample is Spotlight's live query support, only minimal support for creating new fortune files is provided. Support for deleting, editing, etc. is left as an exercise for the reader.

[Next](FortuneCookie-GetMetadataForFile.m.md)

