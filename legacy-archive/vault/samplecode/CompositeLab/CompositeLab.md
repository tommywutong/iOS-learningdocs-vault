---
title: CompositeLab
apple_id: DTS40008846
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2011-04-25'
source_url: https://developer.apple.com/library/archive/samplecode/CompositeLab/Introduction/Intro.html
archived_at: '2026-07-18T03:04:07.449617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CompositeLabmain.m.md)

# CompositeLab

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-04-25 Updated for Mac OS X 10.6 and for Xcode 4. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6.x or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

CompositeLab is a simple application useful for interactively demonstrating compositing modes in the Quartz display system.

Two separate images, source and destination, whose colors (and opacity) are chosen through the use of NSColorWells & the NSColorPanel, are composited together using a compositing mode specified by the user. The images are kept instances of NSImage. One subclass of NSView, CompositeView, manages all target/action methods and drawing.

[Next](CompositeLabmain.m.md)

