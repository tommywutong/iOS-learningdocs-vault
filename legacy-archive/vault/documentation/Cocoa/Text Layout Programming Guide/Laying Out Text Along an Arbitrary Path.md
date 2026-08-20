---
title: Text Layout Programming Guide
apple_id: 10000158i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Tasks/ArbitraryTextPath.html
archived_at: '2026-07-15T07:20:24.728194Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Layout Programming Guide](Introduction%20to%20Text%20Layout%20Programming%20Guide.md)


[Next](Drawing%20Strings.md)[Previous](Line%20Fragment%20Generation.md)

# Laying Out Text Along an Arbitrary Path

The Cocoa text system typically lays out text in horizontal lines in a text view. However, it is also possible to use just the text objects needed to store characters and generate glyphs while manually calculating final glyph positions and drawing the glyphs yourself.

To lay out text along an arbitrary path, you need to use the three basic, non-view text objects: `NSTextStorage` to hold the text, `NSTextContainer` to model the region in which the text is laid out, and `NSLayoutManager` to generate the glyphs and layout information. Finally you draw the glyphs in a custom `NSView` object.

First you create and initialize instances of the text storage, text container, and layout manager. You initialize the text container with the string of text to be laid out. Then you hook the objects together: the text storage object retains a reference to the layout manager, and the layout manager retains a reference to the text container. Listing 1, which could reside in the initialization method for the custom `NSView` object that displays the text, illustrates this process.

__Listing 1__  Creating and configuring the non-view text objects

```
NSTextStorage *textStorage;
NSLayoutManager *layoutManager;
NSTextContainer *textContainer;

textStorage = [[NSTextStorage alloc] initWithString:@"This is the string of text in the text storage."];
layoutManager = [[NSLayoutManager alloc] init];
textContainer = [[NSTextContainer alloc] init];
[layoutManager addTextContainer:textContainer];
[textContainer release];
[textStorage addLayoutManager:layoutManager];
[layoutManager release];
```

The reason you “add” these references, rather than “set” them, is because a layout manager can have multiple text containers, and a text storage object can have multiple layout managers. Also note the memory management implications of this procedure: Because the layout manager retains the text container and the text storage retains the layout manager, you can release them as soon as you connect the objects. However, you should explicitly release the text storage object in your `dealloc` method.

Tell the layout manager not to use screen fonts, because they do not scale or rotate properly (by default, screen fonts are allowed):

```
[layoutManager setUsesScreenFonts:NO];
```

Next, force the layout manager to generate glyphs for the characters in the text storage object and have it calculate glyph positions laid out in a simple, rectangular container. You then transform the positions and call the layout manager to draw the glyphs. This can be done in the view’s `drawRect:` method.

The following message forces layout and returns glyphs for the character string in the text storage object:

```
NSRange glyphRange = [layoutManager
                        glyphRangeForTextContainer:textContainer];
```

The code in Listing 2 does the actual drawing.

__Listing 2__  Drawing the string

```
NSGraphicsContext *context = [NSGraphicsContext currentContext];
NSAffineTransform *transform = [NSAffineTransform transform];
[transform rotateByDegrees:30.0];
[context saveGraphicsState];
[transform concat];
[self lockFocus];
[layoutManager drawGlyphsForGlyphRange:glyphRange
                                atPoint:NSMakePoint(50.0, 50.0)];
[self unlockFocus];
[context restoreGraphicsState];
```

This fragment merely rotates the graphic context 30 degrees counterclockwise before it asks the layout manager to draw the glyphs, but another algorithm could be used to calculate a more complex layout path. This discussion simplifies the technique in order to concentrate on interactions with the layout manager.

The _[CircleView](../../../samplecode/CircleView/CircleView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobygi)_ example provides source code for an application that illustrates the technique but does it in a more robust manner. CircleView calculates a position and draws each glyph individually.

[Next](Drawing%20Strings.md)[Previous](Line%20Fragment%20Generation.md)

