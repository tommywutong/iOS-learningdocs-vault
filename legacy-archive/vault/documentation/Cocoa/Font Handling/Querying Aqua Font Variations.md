---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/QueryingAquaFontVary.html
archived_at: '2026-07-15T07:15:49.458082Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Characters%20and%20Glyphs.md)[Previous](Getting%20Font%20Metrics.md)

# Querying Aqua Font Variations

Using the methods of NSFont, you can query all of the Aqua font variations.
To request the default font size for the standard fonts,
you can either explicitly pass in default sizes (obtained from class
methods such as `systemFontSize` and `labelFontSize`),
or pass in 0 or a negative value.

For Objective-C, use the following method invocations:

| Font | Objective-C methods |
| --- | --- |
| System font | `[NSFont systemFontOfSize:[NSFont systemFontSize]]` |
| Emphasized system font | `[NSFont boldSystemFontOfSize:[NSFont systemFontSize]]` |
| Small system font | `[NSFont systemFontOfSize:[NSFont smallSystemFontSize]]` |
| Emphasized small system font | `[NSFont boldSystemFontOfSize:[NSFont smallSystemFontSize]]` |
| Mini system font | `[NSFont systemFontSizeForControlSize: NSMiniControlSize]` |
| Emphasized mini system font | `[NSFont boldSystemFontOfSize:[NSFont systemFontSizeForControlSize: NSMiniControlSize]]` |
| Application font | `[NSFont userFontOfSize:-1.0]` |
| Application fixed-pitch font | `[NSFont userFixedPitchFontOfSize:-1.0]` |
| Label Font | `[NSFont labelFontOfSize:[NSFont labelFontSize]]` |

The equivalent Java invocations are as follows:

| Font | Java methods |
| --- | --- |
| System font | `NSFont.systemFontOfSize(-1.0)` |
| Emphasized system font | `NSFont.boldSystemFontOfSize(-1.0)` |
| Small system font | `NSFont.systemFontOfSize(NSFont.smallSystemFontSize())` |
| Emphasized small system font | `NSFont.boldSystemFontOfSize(NSFont.smallSystemFontSize())` |
| Mini system font | `NSFont.systemFontSizeForControlSize(-1.0)` |
| Emphasized mini system font | `NSFont.boldSystemFontOfSize(NSFont.systemFontSizeForControlSize(-1.0))` |
| Application font | `NSFont.userFontOfSize(-1.0)` |
| Application fixed-pitch font | `NSFont.userFixedPitchFontOfSize(-1.0)` |
| Label font | `NSFont.labelFontOfSize(-1.0)` |

[Next](Characters%20and%20Glyphs.md)[Previous](Getting%20Font%20Metrics.md)

