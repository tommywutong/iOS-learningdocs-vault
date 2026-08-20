---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Articles/MakingaButtontheDefaultButton.html
archived_at: '2026-07-15T07:11:30.383113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Setting%20a%20Button%E2%80%99s%20Key%20Equivalent.md)[Previous](Hiding%20a%20Button.md)

# Making a Button the Default Button

If button has the `NSRoundedBezelStyle` bezel type, you can mark it as the default button. A default button pulses, and its action message is invoked when the user presses Return. It looks like this:

![Default button](attachments/Art/defaultpushbutton.gif)

To mark a button as the default, set its key equivalent to Return with `setKeyEquivalent:`, like this:

```
[myButton setKeyEquivalent:@"\r"];
```

You can also set the button’s key equivalent in Interface Builder, as described in [Setting a Button’s Key Equivalent](Setting%20a%20Button%E2%80%99s%20Key%20Equivalent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga4tclkdjjbegrckifca).

The default button has a thick outline drawn around it, outside the button’s border; your interface design should account for that extra space.

[Next](Setting%20a%20Button%E2%80%99s%20Key%20Equivalent.md)[Previous](Hiding%20a%20Button.md)

