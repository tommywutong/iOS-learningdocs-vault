---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SubclassingNSColor.html
archived_at: '2026-07-15T07:15:17.576772Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Storing%20NSColor%20in%20User%20Defaults.md)[Previous](Adding%20Custom%20Color%20Pickers%20to%20a%20Color%20Panel.md)

# Subclassing NSColor

Subclasses of NSColor need to implement the `colorSpaceName` and `set` methods, as well as the methods that return the components for that color space and the methods in the NSCoding protocol. Some other methods—such as `colorWithAlphaComponent:`, `isEqual:`, and `colorUsingColorSpaceName:device:`—may also be implemented if they make sense for the color space. Mutable subclasses (if any) should additionally implement `copyWithZone:` to provide a true copy.

[Next](Storing%20NSColor%20in%20User%20Defaults.md)[Previous](Adding%20Custom%20Color%20Pickers%20to%20a%20Color%20Panel.md)

