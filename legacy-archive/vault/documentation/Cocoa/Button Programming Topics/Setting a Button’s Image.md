---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Tasks/SettingButtonImage.html
archived_at: '2026-07-15T07:11:39.643431Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Hiding%20a%20Button.md)[Previous](Setting%20a%20Button%E2%80%99s%20Title.md)

# Setting a Button’s Image

A button can have two images associated with it: normal and alternate. If the button type is `NSMomentaryPushInButton`, `NSPushOnPushOffButton`, `NSMomentaryLightButton`, or `NSOnOffButton`, only the normal image is ever displayed. If the button type is `NSMomentaryChangeButton` or `NSToggleButton`, the normal image is displayed when the button’s state is off (`NSOffState`) and the alternate image is displayed when the button’s state is on or mixed (`NSOnState`. or `NSMixedState`). If you want a button to display different image for all three states, you must subclass `NSButton`. (Although switch and radio buttons can display different images for all three states, there is no public interface for this feature.)

To set the normal image, use `setImage:`. To set the alternate image, use `setAlternateImage:`.

To set the position for a button’s image, use `setImagePosition:`, with one of the following values below. The default is `NSNoImage`

|  |  |  |
| --- | --- | --- |
| `NSNoImage`NSNoImage | `NSImageOnly`NSImageOnly | `NSImageOverlaps`NSImageOverlaps |
| `NSImageLeft`NSImageLeft | `NSImageRight`NSImageRight |  |
| `NSImageBelow`NSImageBelow | `NSImageAbove`NSImageAbove |  |

[Next](Hiding%20a%20Button.md)[Previous](Setting%20a%20Button%E2%80%99s%20Title.md)

