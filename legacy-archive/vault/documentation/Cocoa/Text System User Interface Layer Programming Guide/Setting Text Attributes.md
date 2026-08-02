---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Tasks/SetTextAttributes.html
archived_at: '2026-07-15T07:20:38.243353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System User Interface Layer Programming Guide](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)


[Next](Setting%20Text%20Margins.md)[Previous](Plain%20and%20Rich%20Text%20Objects.md)

# Setting Text Attributes

NSTextView allows you to change the attributes of its text programmatically through various methods, most inherited from the superclass, NSText. NSTextView adds its own methods for setting the attributes of text that the user types, for setting the baseline offset of text as an absolute value, and for adjusting kerning and use of ligatures. Most of the methods for changing attributes are defined as action methods and apply to the selected text or typing attributes for a rich text view, or to all of the text in a plain text view.

An NSTextView maintains a set of typing attributes (font, size, color, and so on) that it applies to newly entered text, whether typed by the user or pasted as plain text. It automatically sets the typing attributes to the attributes of the first character immediately preceding the insertion point, of the first character of a paragraph if the insertion point is at the beginning of a paragraph, or of the first character of a selection. The user can change the typing attributes by choosing menu commands and using utilities such as the Font panel (Fonts window). You can also set the typing attributes programmatically using `setTypingAttributes:`, though you should rarely find need to do so unless creating a subclass.

NSText defines the action methods `superscript:`, `subscript:`, and `unscript:`, which raise and lower the baseline of text by predefined increments. NSTextView gives you much finer control over the baseline offset of text by defining the `raiseBaseline:` and `lowerBaseline:` action methods, which raise or lower text by one point each time they’re invoked.

NSTextView provides convenient action methods for adjusting the spacing between characters. By default, an NSTextView object uses standard kerning (as provided by the data in a font’s AFM file). A `turnOffKerning:` message causes this kerning information to be ignored and the selected text to be displayed using nominal widths. The `loosenKerning:` and `tightenKerning:` methods adjust kerning values over the selected text and `useStandardKerning:` reestablishes the default kerning values.

Kerning information is a character attribute that’s stored in the text view’s NSTextStorage object. If your application needs finer control over kerning than the methods of this class provide, you should operate on the NSTextStorage object directly through methods defined by its superclass, NSMutableAttributedString. See the reference documentation for NSAttributedString Additions for information on setting attributes.

NSTextView’s support for ligatures provides the minimum required ligatures for a given font and script. The required ligatures for a specific font and script are determined by the mechanisms that generate glyphs for a specific language. Some scripts may well have no ligatures at all—English text, as an example, doesn’t require ligatures, although certain ligatures such as “fi” and “fl” are desirable and are used if they’re available. Other scripts, such as Arabic, demand that certain ligatures must be available even if a `turnOffLigatures:` message is sent to the NSTextView. Other scripts and fonts have standard ligatures that are used if they’re available. The `useAllLigatures:` method extends ligature support to include all possible ligatures available in each font for a given script.

Ligature information is a character attribute that’s stored in the text view’s NSTextStorage object. If your application needs finer control over ligature use than the methods of this class provide, you should operate on the NSTextStorage object directly through methods defined by its superclass, NSMutableAttributedString. See the reference documentation for NSAttributedString Additions for information on setting attributes.

[Next](Setting%20Text%20Margins.md)[Previous](Plain%20and%20Rich%20Text%20Objects.md)

