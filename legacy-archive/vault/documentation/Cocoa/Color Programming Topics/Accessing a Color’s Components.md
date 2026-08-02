---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/ColorComponents.html
archived_at: '2026-07-15T07:15:16.067082Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Accessing%20System%20Colors.md)[Previous](Working%20With%20Color%20Spaces.md)

# Accessing a Color’s Components

There’s usually no need to retrieve the individual components of a color, but when needed, you can retrieve either a set of components (using such methods as `getRed:green:blue:alpha:`) or an individual component (using such methods as `redComponent`). However, it’s illegal to ask an NSColor for components that aren’t defined for its color space. You can identify the color space by sending a `colorSpaceName` message to the NSColor object. If you need to ask an NSColor for components that aren’t in its color space (for instance, when you’ve gotten the color from the color panel), first convert the color to the appropriate color space using the `colorUsingColorSpaceName:` method. If the color is already in the specified color space, you get the same color back; otherwise you get a conversion that’s usually lossy or that’s correct only for the current device. You get back `nil` if the specified conversion can’t be done.

[Next](Accessing%20System%20Colors.md)[Previous](Working%20With%20Color%20Spaces.md)

