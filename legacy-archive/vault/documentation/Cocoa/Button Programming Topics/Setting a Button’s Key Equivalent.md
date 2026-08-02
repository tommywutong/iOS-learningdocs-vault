---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Tasks/SettingButtonKeyEquiv.html
archived_at: '2026-07-15T07:11:43.663049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Subclassing%20NSButton.md)[Previous](Making%20a%20Button%20the%20Default%20Button.md)

# Setting a Button’s Key Equivalent

A button can have a key equivalent, so that when the user presses that key, the button responds as though it’s been clicked.

Note that if you set the key equivalent to Return, that button becomes the default button.

You typically set a button’s key equivalent in Interface Builder. To do so, select the button and open the attributes pane of the inspector. Disclose the attributes for the button, click in the Key Equiv. field, and type the key or key combination you want to associate with the button. (You remove the key equivalent by pressing Clear.)

To set the key equivalent programmatically, use `setKeyEquivalent:` with the character. For example, to set it to Return, use:

```
[myButton setKeyEquivalent:@"\r"];
```

To set the button’s key equivalent to non-print character, you can use the key constants defined by `NSResponder`, as in the following example, which sets a button’s key equivalent to the left arrow key.

```
unichar arrowKey = NSLeftArrowFunctionKey;
[button setKeyEquivalent:[NSString stringWithCharacters:&arrowKey length:1]];
```

[Next](Subclassing%20NSButton.md)[Previous](Making%20a%20Button%20the%20Default%20Button.md)

