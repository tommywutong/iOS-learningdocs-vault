---
title: Text Layout Programming Guide
apple_id: 10000158i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Tasks/StringHeight.html
archived_at: '2026-07-15T07:20:26.222462Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Layout Programming Guide](Introduction%20to%20Text%20Layout%20Programming%20Guide.md)


[Next](Counting%20Lines%20of%20Text.md)[Previous](Drawing%20Strings.md)

# Calculating Text Height

There may be times when you need to know the height of a block of text formed by a text string after it is laid out in a fixed-width area. The `NSLayoutManager` class can do this very simply. This article illustrates the technique implemented in a single function.

The basic technique for calculating text height uses the three basic non-view components of the text system: `NSTextStorage`, `NSTextContainer`, and `NSLayoutManager`. The text storage object holds the string to be measured; the text container specifies the width of the layout area; and the layout manager does the layout and returns the height.

To set up the text system for the calculation, you need the text string to be measured, a font for the string, and a width for the area modeled by the text container. You can pass these values into a function with a declaration such as the following:

```
float heightForStringDrawing(NSString *myString, NSFont *myFont,
    float myWidth);
```

The argument names in the function declaration appear as variables in the following code fragments that define the method body.

First, you instantiate the needed text objects and hook them together. You use the designated initializer for the text storage object, which takes the string pointer as an argument. Likewise, the text container’s designated initializer takes the container size as its argument. You set the container width to your desired width and set the height to an arbitrarily large value, as shown in the following code fragment:

```
NSTextStorage *textStorage = [[[NSTextStorage alloc]
        initWithString:myString] autorelease];
NSTextContainer *textContainer = [[[NSTextContainer alloc]
        initWithContainerSize: NSMakeSize(myWidth, FLT_MAX)] autorelease];
NSLayoutManager *layoutManager = [[[NSLayoutManager alloc] init]
        autorelease];
```

Once the text objects are created, you can hook them together:

```
[layoutManager addTextContainer:textContainer];
[textStorage addLayoutManager:layoutManager];
```

You don’t need to release the text container and layout manager because you added them to the autorelease pool at initialization time. Next, set the font by adding the font attribute to the range of the entire string in the text storage object. Set the line fragment padding to `0` to get an accurate width measurement. (Padding is used in page layout to prevent the text in a text container from abutting too closely other elements on a page, such as graphics.)

```
[textStorage addAttribute:NSFontAttributeName value:myFont
        range:NSMakeRange(0, [textStorage length])];
[textContainer setLineFragmentPadding:0.0];
```

Finally, because the layout manager performs layout lazily, on demand, you must force it to lay out the text, even though you don’t need the glyph range returned by this function. Then you can simply ask the layout manager for the height of the rectangle occupied by the laid-out text and, assuming this code is in a function implementation, return the value:

```
(void) [layoutManager glyphRangeForTextContainer:textContainer];
return [layoutManager
        usedRectForTextContainer:textContainer].size.height;
```

[Next](Counting%20Lines%20of%20Text.md)[Previous](Drawing%20Strings.md)

