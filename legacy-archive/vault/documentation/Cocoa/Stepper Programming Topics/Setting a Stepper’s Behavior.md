---
title: Stepper Programming Topics
apple_id: 10000108i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Steppers/Tasks/SettingStepperBehavior.html
archived_at: '2026-07-15T07:19:24.655791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Stepper Programming Topics](Introduction%20to%20Steppers.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Steppers.md)

# Setting a Stepper’s Behavior

To set the minimum and maximum values for a stepper, use `setMinValue:` and `setMaxValue:`. To choose how much the stepper changes its value when an arrow is pressed, use `setIncrement:`. Pressing the upper arrow increments the value by `increment`. Pressing the bottom arrow decrements the value by `increment`.

To choose what happens when the user presses the mouse button and holds it down, use `setAutoRepeat:`. If `autoRepeat` is `YES`, the stepper changes its value at a regular interval. If `autoRepeat` is `NO`, the stepper changes its value once after the mouse button is released.

To choose what happens when the user continues to press the stepper after its value has reached its minimum or maximum value, use `setValueWraps:`. If `valueWraps` is `YES`, the stepper wraps around to the minimum or maximum value. If `valueWraps` is `NO`, the stepper doesn’t change its value.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Steppers.md)

