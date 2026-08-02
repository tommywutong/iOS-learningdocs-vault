---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/SystemColors.html
archived_at: '2026-07-15T07:15:18.077430Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Using%20the%20System%20Control%20Tint.md)[Previous](Accessing%20a%20Color%E2%80%99s%20Components.md)

# Accessing System Colors

[NSColor](https://developer.apple.com/documentation/appkit/nscolor) has a number of methods that return system colors that you can use to create custom controls or subclass existing controls while honoring the user's color preferences.

System colors are implemented as named colors in a special color list named “`Developer`.” You can examine this color list in the color panel of any application that supports colors. For more on named colors and color lists, see [About Color Lists](About%20Color%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tolkciffeqssfireq).

To extract the components of a system color, you must use the `NSColor` method [colorUsingColorSpaceName:](https://developer.apple.com/documentation/appkit/nscolor/1534332-usingcolorspacename) to convert the color to a color space known to respond to the component accessor methods you need; see [Creating and Converting Colors Using Color Spaces](Working%20With%20Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbxfu4tmobugy) for more about color conversion.

An `NSSystemColorsDidChangeNotification` is sent when the system colors have been changed (such as through a system control panel interface). If you have any non-system colors that depend on the system colors, you can change them when you receive this notification.

[Next](Using%20the%20System%20Control%20Tint.md)[Previous](Accessing%20a%20Color%E2%80%99s%20Components.md)

