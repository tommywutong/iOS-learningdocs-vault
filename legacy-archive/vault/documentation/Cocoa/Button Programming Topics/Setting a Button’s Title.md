---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Tasks/SettingButtonTitle.html
archived_at: '2026-07-15T07:11:44.163240Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Setting%20a%20Button%E2%80%99s%20Image.md)[Previous](Setting%20the%20Appearance%20of%20a%20Button%E2%80%99s%20Border.md)

# Setting a Button’s Title

A button can have two titles associated with it: normal and alternate. If the button type is `NSMomentaryPushInButton`, `NSPushOnPushOffButton`, `NSMomentaryLightButton`, or `NSOnOffButton`, only the normal title is ever displayed. If the button type is `NSMomentaryChangeButton` or `NSToggleButton`, the normal title is displayed when the button’s state is off (`NSOffState` )and the alternate title is displayed when the button’s state is on or mixed (`NSOnState`. or `NSMixedState`). If you want a button to display different titles for all three states, you must subclass `NSButton`.

If you want the title to contain plain text, use `setTitle:` to set the normal title and `setAlternateTitle:` to set the alternate title. If you want the title to contain styled text (for example, italics or bold), use `setAttributedTitle:` and `setAttributedAlternateTitle:`.

To set how the title is positioned relative to the button’s image, use `setImagePosition:`, described in [Setting a Button’s Image](Setting%20a%20Button%E2%80%99s%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga4dqlkciffeeq2hindq). If there is no image, the title is centered horizontally and vertically within the button. If the title is above, below, or overlapping the image, the title is centered horizontally within the button. To hide the title, use `setImagePosition:` with an argument of `NSImageOnly`.

To set the title’s font, send `setFont:` to the button’s button cell.

If you want a button to display its title in a tag when the mouse is over it, you need to use Tool Tips.

[Next](Setting%20a%20Button%E2%80%99s%20Image.md)[Previous](Setting%20the%20Appearance%20of%20a%20Button%E2%80%99s%20Border.md)

