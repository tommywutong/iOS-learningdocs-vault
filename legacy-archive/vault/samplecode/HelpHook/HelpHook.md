---
title: HelpHook
apple_id: DTS10003493
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-04-12'
source_url: https://developer.apple.com/library/archive/samplecode/HelpHook/Introduction/Intro.html
archived_at: '2026-07-18T03:11:53.928760Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Document%20Revision%20History.md)

Current information on this Developer Library topic can be found here:

- [Java > Design Guidelines](https://developer.apple.com/referencelibrary/Java/idxDesignGuidelines-date.html)

# HelpHook

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-04-12 Updated compiler options to generate 1.4 compatible bytecode. |
| __Build Requirements:__ | Xcode 1.5 or later, Java 1.4.2 or later |
| __Runtime Requirements:__ | Mac OS X 10.3 or later, Java 1.4.2 or later |

This is a very simple example of integrating a J2SE application with the Apple Help Viewer application. A simple Cocoa library calls [NSApplication showHelp], which allows HelpViewer to inspect the application bundle for help content. Also critical are the CFBundleHelpBookFolder and CFBundleHelpBookName keys, added to the application's Info.plist dictionary. (see the HelpHook target in Xcode).

The call to [NSApplication showHelp] is made asynchronously to prevent deadlocks between AWT and AppKit. A badShowHelp function is also written that blocks AWT against this call and under certain circumstances can lead to a deadlock. See the comments in JavaHelpHook.m and Technical Note 2147 for more details.

This sample code has been updated to include a project that produces a universal binary. No code changes were required for it to run correctly on Intel-based Macintosh computers.

[Next](Document%20Revision%20History.md)

