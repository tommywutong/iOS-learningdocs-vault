---
title: Cocoa Drawing Guide
apple_id: TP40003290
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Text/Text.html
archived_at: '2026-07-15T07:12:35.068413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Drawing Guide](Introduction%20to%20Cocoa%20Drawing%20Guide.md)


[Next](Paths.md)[Previous](Advanced%20Drawing%20Techniques.md)

# Text

Text rendering is a special type of drawing that is an important part of most applications. Cocoa provides a range of options for rendering text that should satisfy the needs of most developers. The following sections cover these options briefly. For more detailed information, you should see the documents in [Reference Library > Cocoa > Text & Fonts](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000416-TP30000461).

Cocoa provides support for programmatically getting font information using the [NSFont](https://developer.apple.com/documentation/appkit/nsfont) class. You can apply fonts as attributes to strings or use them to set the default font in the current context. The Cocoa text system also uses font objects for formatting text. You request `NSFont` objects from Cocoa using the name and size of the font you want, as shown in the following example.

```
NSFont* font1= [NSFont fontWithName:@"Helvetica" size:9.0];
NSFont* font2 = [NSFont fontWithName:@"Helvetica Bold"  size:10.0];
```

The `NSFont` class does not provide a programmatic way to modify other text attributes, such as the character spacing and text drawing mode. Cocoa does, however, provide a system Font panel that you can display to the user. From this panel, the user can make changes to the current font attributes. You can also set most text options using the Cocoa text system, which is described in [Advanced Text Drawing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqhewueq2jincuuq2k).

Although you usually specify font attributes directly when drawing [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) and [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) objects, you can also change the font and font size information in the current graphics state. To change these values, you create an `NSFont` object and invoke its `set` method.

For information about working with fonts and font objects, see _[Font Handling](../Font%20Handling/Introduction%20to%20Font%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4tg2i)_. For information about how to display the Font panel, see [Creating a Font Panel](../../Cocoa%20Text%20Architecture%20Guide/Font%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjzfvbuqnjnknltg).

If you need to draw a small amount of text quickly, the simplest way to do it is using the methods of [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) and [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString). The Application Kit defines methods on these classes that support drawing the string in the current context. For an `NSString` object, you can apply basic attributes (such as font, color, and style settings) to the entire string during drawing. For an `NSAttributedString` object, you can apply multiple sets of attributes to different parts of the string.

Prior to OS X v10.4, the `NSString` and `NSAttributedString` classes were intended for rendering text occasionally in your program. The performance of these drawing methods was not as good as the performance you could get by rendering text using the Cocoa text system. Also, the layout for strings is limited to a simple rectangular area in the current view. In OS X v10.4, performance of the string drawing methods improved significantly and is useful in many situations; of course, you should always measure the performance yourself and see if it is adequate for your program. If you need to do more complex text layout, you should still consider using the Cocoa text system.

For information on string drawing methods, see NSString Application Kit Additions Reference or NSAttributedString Application Kit Additions Reference in _[Application Kit Framework Reference](https://developer.apple.com/documentation/appkit)_.

If your program displays a lot of text or needs to arrange text in complex ways, you should use the Cocoa text system. This system provides advanced text-handling capabilities on top of basic features such as text input, layout, display, editing, copying, and pasting. The system supports multiple fonts and paragraph styles, embedded images, spell checking, nonrectangular text containers, and sophisticated typesetting features, among many other features.

Text layout is one of the most expensive drawing-related operations you can do and the Cocoa text system is optimized for the best possible performance. The text system manages a sophisticated set of caches and optimizes the times at which it performs layout to reduce the impact on your program’s drawing cycle. Of course, these optimizations work only if your program reuses its text objects, but doing so is relatively simple.

The simplest way to use the Cocoa text system is to place an [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) object in one of your windows. A text view object creates and maintains the text layout objects it needs to draw text and responds to user events to modify the text.

If you want to have more control over the text layout and editing behavior, you can tie into the Cocoa text system at several places. The text engine at the heart of the Cocoa text system is highly customizable. You can subclass several text system classes to provide custom layout and typesetting behavior. You can also create your own text-based views to provide features beyond what the default `NSTextView` offers.

For information about the Cocoa text system, you should start by reading _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_. That document describes the basic concepts of the text system and introduces you to many of the classes involved in text layout and management. It also provides simple tutorials to get you started and pointers to other text-related documents.

[Next](Paths.md)[Previous](Advanced%20Drawing%20Techniques.md)

