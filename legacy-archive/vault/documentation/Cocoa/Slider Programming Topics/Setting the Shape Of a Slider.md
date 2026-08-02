---
title: Slider Programming Topics
apple_id: 10000025i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Slider/Tasks/SettingShape.html
archived_at: '2026-07-15T07:19:09.985267Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Slider Programming Topics](Introduction%20to%20Sliders.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Slider%20Tick%20Marks.md)

# Setting the Shape Of a Slider

Sliders come in three shapes: horizontal bar, vertical bar, and circular dial. To determine whether a slider is a bar or a dial, use `setSliderType:`. For a dial, set the slider type to `NSCircularSlider` (that is, call `[[slider cell] setSliderType:NSCircularSlider];`). If you are using Interface Builder, you can drag a circular slider widget into your design window, or select the circular slider checkbox in the slider’s info window.

The following figure shows circular dial sliders.

__Figure 1__  Circular Sliders

![Circular Sliders](attachments/Tasks/art/circularsliders.gif)

A bar-shaped slider automatically determines whether it’s horizontal or vertical by the shape of its containing rectangle. If the slider is wider than it is tall, it’s horizontal. Otherwise, it’s vertical. Use the `initWithFrame:` method to initialize a slider, passing in an NSRect with the size and shape you want.

For a circular slider, you must pass an NSRect at least large enough to contain the control. For a regular circular slider, the NSRect must be at least 28 by 30 pixels. For a small circular slider, it must be at least 18 by 20 pixels. Add 4 pixels in each dimension if your slider has tick marks.

If you specify a larger NSRect, the slider will be centered in the rectangle. If you specify a smaller rectangle, the control will be clipped.

A vertical slider has its minimum on the bottom; a horizontal slider has its minimum on the left; a circular slider has its minimum at the top.

[Next](Document%20Revision%20History.md)[Previous](Using%20Slider%20Tick%20Marks.md)

