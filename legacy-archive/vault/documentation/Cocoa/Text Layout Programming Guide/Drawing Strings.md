---
title: Text Layout Programming Guide
apple_id: 10000158i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Tasks/DrawingStrings.html
archived_at: '2026-07-15T07:20:25.758144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Layout Programming Guide](Introduction%20to%20Text%20Layout%20Programming%20Guide.md)


[Next](Calculating%20Text%20Height.md)[Previous](Laying%20Out%20Text%20Along%20an%20Arbitrary%20Path.md)

# Drawing Strings

There are three ways to draw text programmatically in Cocoa: using methods of `NSString` or `NSAttributedString`, using those of `NSCell`, and using `NSLayoutManager` directly. `NSLayoutManager` is the most efficient.

The `NSString` class has two convenience methods for drawing string objects directly in an `NSView` object: `drawAtPoint:withAttributes:` and `drawInRect:withAttributes:`. For strings that have multiple attributes associated with ranges and individual characters, you must use `NSAttributedString`. You can draw a string (in a focused `NSView`) with either the `drawAtPoint:` or `drawInRect:` method. These methods are designed for drawing small amounts of text or text that must be drawn rarely. They create and dispose of various supporting text objects, including `NSLayoutManager`, every time you call them.

For repeated drawing of text, however, the string drawing convenience methods are not efficient because they do a lot of work behind the scenes. For example, to draw Unicode text, you must first convert the characters into glyphs, the elements of a font. Glyph generation is complicated because several characters may produce a single glyph and vice versa, depending on the context and other factors. In addition, the system does a lot of work setting up for glyph conversion, and the string drawing convenience methods do this work each time they draw a string. Using the layout manager directly provides significant performance improvements because it caches glyph layout and size information.

The `NSCell` class also provides primitives for displaying and editing text. `NSCell` text drawing methods are used by `NSBrowser` and `NSTableView`. Text drawing by `NSCell` is more efficient than using the string convenience methods because it caches some information, such as the size of the text rectangle. So, for displaying the same text repeatedly, `NSCell` works well, but for the most efficient display of an arbitrary text string, use `NSLayoutManager` directly.

If you use the `NSTextView` class to display text, either by dragging a text view object from the Interface Builder Data palette or creating a text view programmatically using the `NSTextView` method `initWithFrame:` method, Cocoa automatically creates an `NSLayoutManager` instance to draw your text. If you create a text view using the `NSTextView` `initWithFrame:textContainer:` method, however, or if you need to draw text directly into a different type of `NSView` object, you must create the `NSLayoutManager` explicitly.

To use `NSLayoutManager` to draw a text string directly into a view, you must create and initialize the three basic non-view components of the text system. First create an `NSTextStorage` object to hold the string. Then create an `NSTextContainer` object to describe the geometric area for the text. Then create the `NSLayoutManager` object and hook the three objects together by adding the layout manager to the text storage object and adding the text container to the layout manager. The code in Listing 1, which could reside in the view’s `initWithFrame:` method, illustrates this procedure.

__Listing 1__  Creating and configuring the non-view text objects

```
NSTextStorage *textStorage = [[NSTextStorage alloc]
    initWithString:@"This is the text string."];
NSLayoutManager *layoutManager = [[NSLayoutManager alloc] init];
NSTextContainer *textContainer = [[NSTextContainer alloc] init];
[layoutManager addTextContainer:textContainer];
[textContainer release];
[textStorage addLayoutManager:layoutManager];
[layoutManager release];
```

You can release the text container because the layout manager retains it, and you can release the layout manager because the text storage object retains it.

To draw glyphs directly in a view, you can use the `NSLayoutManager` method `drawGlyphsForGlyphRange:` in the view’s `drawRect:` method. However, you must first convert the character range you want to draw into a glyph range. If you need to select a subrange of the text in the text storage object, you can use the `glyphRangeForCharacterRange:actualCharacterRange:` method. If you want to draw the entire string in the text storage object, use the `glyphRangeForTextContainer:` method as in Listing 2 (which uses the `layoutManager` variable name from Listing 1).

__Listing 2__  Drawing glyphs directly in a view

```
NSRange glyphRange = [layoutManager
    glyphRangeForTextContainer:textContainer];
[self lockFocus];
[layoutManager drawGlyphsForGlyphRange: glyphRange atPoint: rect.origin];
[self unlockFocus];
```


There are differences among Cocoa’s three ways to draw text with regard to typesetter behavior, which is described in [Typesetter Behaviors and Versions](Typesetters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydmljvge4dini). By default, the string-drawing convenience methods and `NSCell` objects supplied by the Application Kit use [NSTypesetterBehavior_10_2_WithCompatibility](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior/behavior_10_2_withcompatibility), whereas `NSLayoutManager` objects use [NSTypesetterLatestBehavior](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior/latestbehavior). It is important to use the same typesetter behavior when both measuring and rendering text, to avoid differences in paragraph spacing, line spacing, and head indent handling.

In cases where you must measure text one way and render it another, set the typesetter behavior to match using the [setTypesetterBehavior:](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403199-typesetterbehavior) method defined by `NSLayoutManager` and `NSTypesetter`. For example, if you need to use an `NSLayoutManager` object to measure text and convenience string drawing methods to draw it, change the layout manager’s typesetter behavior to `NSTypesetterBehavior_10_2_WithCompatibility`.

[Next](Calculating%20Text%20Height.md)[Previous](Laying%20Out%20Text%20Along%20an%20Arbitrary%20Path.md)

