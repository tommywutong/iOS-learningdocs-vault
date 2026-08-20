---
title: CWCocoaComponent
apple_id: DTS10003596
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-04-12'
source_url: https://developer.apple.com/library/archive/samplecode/CWCocoaComponent/Introduction/Intro.html
archived_at: '2026-07-18T03:02:46.989700Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ColorSelectionEvent.java.md)

# CWCocoaComponent

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-04-12 Updated compiler options to generate 1.4 compatible bytecode. |
| __Build Requirements:__ | Xcode 2.0 or later |
| __Runtime Requirements:__ | Mac OS X 10.4 or later, Java 1.4.2 or later |

This sample uses Apple's CocoaComponent feature to embed an NSColorWell inside a Swing JFrame in place of the standard JColorChooser. An integration layer is set up where changes to the system NSColorPanel are converted to Java AWT events, allowing Java code to utiilize the native color picker for AWT or Swing components. Note the use of EventQueue.invokeLater when firing AWT events to ensure thread safety between Java and Cocoa.
This sample code has been updated to include a project that produces a universal binary. No code changes were required for it to run correctly on Intel-based Macintosh computers. See Technical Note 2147 for more details on using CocoaComponent.

[Next](ColorSelectionEvent.java.md)

