---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Tasks/RespondingToFontChanges.html
archived_at: '2026-07-15T07:15:49.952905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Converting%20Fonts%20Manually.md)[Previous](Creating%20a%20Font%20Manager.md)

# Responding to Font Changes

The font manager responds to a font-changing action method
by sending a `changeFont` action
message up the responder chain. A text-bearing object that receives
this message should have the font manager convert the fonts in its
selection by invoking `convertFont` for each
font and using the NSFont object returned. The `convertFont` method
uses the information recorded by the font-changing action method,
such as `addFontTrait`, modifying
the font provided appropriately. (There’s no way to explicitly
set the font-changing action or trait; instead, you use the methods
described in [Converting Fonts Manually](Converting%20Fonts%20Manually.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2delkdjjbeoqsbivdq).)

This simple Objective-C example assumes there’s only one
font in the selection:

```objc
- (void)changeFont:(id)sender
{
    NSFont *oldFont = [self selectionFont];
    NSFont *newFont = [sender convertFont:oldFont];
    [self setSelectionFont:newFont];
    return;
}
```

Most text-bearing objects have to scan the selection for ranges
with different fonts and invoke `convertFont` for
each one.

[Next](Converting%20Fonts%20Manually.md)[Previous](Creating%20a%20Font%20Manager.md)

