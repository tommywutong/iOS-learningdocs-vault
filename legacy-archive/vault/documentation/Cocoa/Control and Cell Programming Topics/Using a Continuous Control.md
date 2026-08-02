---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/UsingContControl.html
archived_at: '2026-07-15T07:13:50.929248Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Subclassing%20NSCell.md)[Previous](Changing%20the%20Cell%20for%20a%20Control.md)

# Using a Continuous Control

A continuous control sends its action message at regular intervals as the user holds the mouse button down. For example, a continuous slider sends its action message repeatedly as the user moves the knob, and a continuous button sends its action message repeatedly as the user presses the button. If a control isn’t continuous, it sends its action message only after the user releases the mouse.

To find out or change whether a control is continuous: send `isContinuous` or `setContinuous:` to its cell. By default, sliders are continuous and other controls are not.

To find out how often a continuous control sends its action message, use the method `getPeriodicDelay:interval:`., which returns the following:

- The periodic delay is the amount of time (in seconds) that a continuous control will pause before starting to periodically send action messages to the target object. It’s taken from the user’s defaults. If the user hasn’t set it, it’s 0.4 seconds.
- The interval is the amount of time (in seconds) between messages. By default, it’s taken from the user’s defaults. If the user hasn’t set it, it’s 0.075 seconds.

(In Java, use the two methods `periodicDelay` and `interval`.)

If you’re using a button, use `setPeriodicDelay:interval:` to change these values programmatically. If you’re using another type of control, you must subclass the control’s cell class to change them programmatically.

[Next](Subclassing%20NSCell.md)[Previous](Changing%20the%20Cell%20for%20a%20Control.md)

