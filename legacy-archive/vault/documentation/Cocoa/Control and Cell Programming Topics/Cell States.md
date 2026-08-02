---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Concepts/CellStates.html
archived_at: '2026-07-15T07:13:44.853439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Manipulating%20Cells%20and%20Controls.md)[Previous](Represented%20Objects.md)

# Cell States

For some subclasses of NSCell, such as an NSButtonCell, the object’s value is its state. It can have either two states—`NSOnState` and `NSOffState`—or three states—`NSOnState`, `NSOffState`, and `NSMixedState`. A mixed state is useful for a checkbox or radio button that reflects the status of a feature that’s true only for some items in your application or the current selection. For example, suppose a checkbox makes the selected text bold. If all the selected text is bold, it’s on. If none of the selected text is bold, it’s off. If the text has a combination of bold and plain text, it’s mixed. Now suppose you click the checkbox. If you turn it on, all the text becomes bold. If you turn it off, all the text becomes plain. If you select the mixed state, the text remains as it is.

By default, an NSCell has two states. You can allow the third state with the method `setAllowsMixedState:`. To set the button’s state directly, use `setState:`. To cycle through all available states, use `setNextState`.

[Next](Manipulating%20Cells%20and%20Controls.md)[Previous](Represented%20Objects.md)

