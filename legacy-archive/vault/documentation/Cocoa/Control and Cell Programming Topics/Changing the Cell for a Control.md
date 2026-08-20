---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/ChangingCellClass.html
archived_at: '2026-07-15T07:13:47.873664Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Using%20a%20Continuous%20Control.md)[Previous](Displaying%20Cell%20Values.md)

# Changing the Cell for a Control

Because NSControl uses objects derived from the NSCell class to implement most of its functionality, you can usually implement a unique user interface device by creating a subclass of NSCell rather than NSControl. As an example, let’s say you want all your application’s NSSliders to have a type of cell other than the generic NSSliderCell. First, you create a subclass of NSCell, NSActionCell, or NSSliderCell. (Let’s call it MyCellSubclass.) Then, you can simply invoke NSSlider’s `setCellClass` class method:

```
[NSSlider setCellClass:[MyCellSubclass class]];
```

All NSSliders created thereafter will use MyCellSubclass, until you call `setCellClass:` again.

If you want to create generic NSSliders (ones that use NSSliderCell) in the same application as the customized NSSliders that use MyCellSubclass, there are two possible approaches. One is to invoke `setCellClass:` as above whenever you’re about to create a custom NSSlider, resetting the cell class to NSSliderCell afterwards. The other approach is to create a custom subclass of NSSlider that automatically uses MyCellSubclass, as explained in the [NSControl](https://developer.apple.com/documentation/appkit/nscontrol) class reference.

[Next](Using%20a%20Continuous%20Control.md)[Previous](Displaying%20Cell%20Values.md)

