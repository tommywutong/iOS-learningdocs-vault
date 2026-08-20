---
title: Font Panel Programming Topics
apple_id: 10000116i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontPanel/Tasks/UsingFontPanel.html
archived_at: '2026-07-15T07:15:52.461344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Panel Programming Topics](Introduction%20to%20Font%20Panel.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20a%20Font%20Panel.md)

# Using the Font Panel

You can enable the interaction between a text object and the font panel using the [setUsesFontPanel:](https://developer.apple.com/documentation/appkit/nstextview/1449534-usesfontpanel) method. Doing so is recommended for a text view that serves as a field editor, for example.

You can use the Font panel on objects other than standard text fields. The NSFontManager method [setAction:](https://developer.apple.com/documentation/appkit/nsfontmanager/1462349-action) sets the action (specified by a selector) that is sent up the responder chain when a new font is selected. The default selector is [changeFont:](https://developer.apple.com/documentation/objectivec/nsobject/1462311-changefont):. Any object that receives this message from the responder chain should send a [convertFont:](https://developer.apple.com/documentation/appkit/nsfontmanager/1462293-convertfont): message back to the NSFontManager to convert the font in a manner the user has specified.

This example assumes there is only one font selected:

```
– (void)changeFont:(id)sender
{
    NSFont *oldFont = [self font];
    NSFont *newFont = [sender convertFont:oldFont];
    [self setFont:newFont];
    return;
}
```

If multiple fonts are selected, `changeFont:` must send conversion messages for each selected font. This is useful for objects such as table views, which do not inherently respond to messages from the font panel.

[Next](Document%20Revision%20History.md)[Previous](Creating%20a%20Font%20Panel.md)

