---
title: Font Handling
apple_id: 10000093i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/FontHandling/Concepts/InitiatingFontChanges.html
archived_at: '2026-07-15T07:15:43.426133Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Font Handling](Introduction%20to%20Font%20Handling.md)


[Next](Creating%20a%20Font%20Manager.md)[Previous](Recording%20the%20Font%20in%20a%20Selection.md)

# Initiating Font Changes

The user normally
changes the font of the selection by manipulating the Font panel (also called
the Fonts window) and the Font menu. These objects initiate the
intended change by sending an action message to the font manager. There
are four font-changing action methods:

- `addFontTrait`
- `removeFontTrait`
- `modifyFont`
- `modifyFontViaPanel`

The first three cause the font manager to query the sender
of the message in order to determine which trait to add or remove,
or how to modify the font. The last causes the font manager to use
the settings in the Font panel to modify the font. The font manager
records this information
and uses it in later requests to convert fonts, as described in [Responding to Font Changes](Responding%20to%20Font%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2dclkdjjbeqqsdi5ba).

When the font manager receives an `addFontTrait` or `removeFontTrait` message,
it queries the sender with a `tag` message,
interpreting the return value as a trait mask for use with `convertFontToHaveTrait` or `convertFontToNotHaveTrait`,
as described in [Converting Fonts Manually](Converting%20Fonts%20Manually.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2delkdjjbeoqsbivdq).
The Font menu commands Italic and Bold, for example, have trait mask
values of `ItalicMask` and `BoldMask`,
respectively. See the section “Constants” in the NSFontManager
reference documentation for a list of trait mask values.

When the font manager receives a `modifyFont` message,
it queries the sender with a `tag` message
and interprets the return value as a particular kind of conversion
to perform, via the various conversion methods described in [Converting Fonts Manually](Converting%20Fonts%20Manually.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq2delkdjjbeoqsbivdq).
For example, a button whose tag value is `SizeUpFontAction` causes
the font manager’s `convertFont` method
to increase the size of the NSFont passed as the argument. See the NSFontManager
method `modifyFont` for
a list of conversion tag values.

For `modifyFontViaPanel`,
the font manager sends the application’s Font panel a `panelConvertFont` message.
The Font panel in turn uses the font manager to convert the font
provided according to the user’s choices. For example, if the
user selects only the font family in the Font panel (perhaps Helvetica),
then for whatever fonts are provided to `panelConvertFont`,
only the family is changed: Courier Medium 10.0 point becomes Helvetica
Medium 10.0 point, and Times Italic 12.0 point becomes Helvetica
Oblique 12.0 point.

[Next](Creating%20a%20Font%20Manager.md)[Previous](Recording%20the%20Font%20in%20a%20Selection.md)

