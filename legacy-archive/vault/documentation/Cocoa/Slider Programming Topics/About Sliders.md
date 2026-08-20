---
title: Slider Programming Topics
apple_id: 10000025i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Slider/Concepts/AboutSliders.html
archived_at: '2026-07-15T07:19:08.980661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Slider Programming Topics](Introduction%20to%20Sliders.md)


[Next](Using%20Slider%20Tick%20Marks.md)[Previous](Introduction%20to%20Sliders.md)

# About Sliders

A slider is a control that displays a range of values and has an indicator, or knob, which indicates the current setting. Optionally, it can have tick marks at regularly spaced intervals. A slider can be a bar or a dial. The user moves the knob along the slider’s bar, or around the dial, to change the setting.

A slider’s behavior and appearance is controlled by the class [NSSliderCell](https://developer.apple.com/documentation/appkit/nsslidercell). An `NSSliderCell` object must be contained within a subclass of NSControl. If you need one slider, use an `NSSlider` object that contains a single `NSSliderCell` object. If you need a group of related sliders, use an [NSMatrix](https://developer.apple.com/documentation/appkit/nsmatrix) object that contains several `NSSliderCell` objects. Most `NSSliderCell` methods have covers in `NSSlider`, which simply call the `NSSliderCell` equivalent. For more information, see the `NSSliderCell` and `NSSlider` class specifications.

To set the slider’s minimum and maximum values, use `setMinValue:` and `setMaxValue:`. To read the slider’s value, as represented by the knob’s current position, use an `NSControl` “get” method, such as `floatValue`;. To set the slider’s value, use an `NSControl` “set” method, such as `setFloatValue:`.

You should use text fields to display the slider’s name, minimum value, maximum value, and tick-mark value. Although you can set a title for a slider that’s displayed automatically, it’s displayed right in the slider’s bar and is easily obscured by the knob. There is no way for a slider to display automatically its minimum, maximum, and tick-mark values.

[Next](Using%20Slider%20Tick%20Marks.md)[Previous](Introduction%20to%20Sliders.md)

