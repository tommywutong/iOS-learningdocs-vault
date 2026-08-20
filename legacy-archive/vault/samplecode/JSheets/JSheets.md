---
title: JSheets
apple_id: DTS10003595
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-07-11'
source_url: https://developer.apple.com/library/archive/samplecode/JSheets/Introduction/Intro.html
archived_at: '2026-07-18T03:13:14.246217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](JSheetDelegate.h.md)

# JSheets

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-07-11 Updated compiler options to generate 1.4 compatible bytecode. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.0 or later |
| __Runtime Requirements:__ | Mac OS X 10.4 or later, Java 1.4.2 or later |

This sample demonstrates a mechanism for displaying document-modal sheets, a feature specific to Mac OS X applications, inside a Java application. It uses the AWT Native Interface (JAWT) to obtain a JFrame's underlying NSWindow (Cocoa) peer, and displays an NSOpenPanel or NSSavePanel using the beginSheetForDirectory:... method. Note the combination of performSelectorOnMainThread and EventQueue.invokeLater to prevent threading problems when communicating between AppKit and AWT.

[Next](JSheetDelegate.h.md)

