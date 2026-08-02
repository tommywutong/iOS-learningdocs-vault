---
title: Text Layout Programming Guide
apple_id: 10000158i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/TextLayout.html
archived_at: '2026-07-15T07:20:26.231178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Layout%20Manager.md)

# Introduction to Text Layout Programming Guide

_Text Layout Programming Guide_ describes how the Cocoa text system lays out text. Text layout is the process of converting a string of text characters, font information, and page specifications into lines of glyphs placed at specific locations on a page, suitable for display and printing.

You should read this document if you need to understand how the text system layout mechanism works and how to work directly with an [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) object to accomplish the programming goals described in the articles.

To understand the information in this document, you should have read _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_. You should also understand basic Cocoa programming conventions, such as delegation.

This programming topic contains the following articles:

- [The Layout Manager](The%20Layout%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydklkcijbumrkcjbaq) introduces the [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) class, describing its features and explaining how it performs text layout.
- [Typesetters](Typesetters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydmlkcijbumrkcjbaq) describes the responsibilities of the typesetter object, instantiated from a concrete subclass of [NSTypesetter](https://developer.apple.com/documentation/appkit/nstypesetter), which generates the line fragments and glyph positions on behalf of the layout manager.
- [Line Fragment Generation](Line%20Fragment%20Generation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2dolkdjjbeeskbifda) explains how the typesetter and text container work together to create line fragment rectangles.
- [Drawing Strings](Drawing%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydqlkdjjbeoqsjijba) explains how to use the layout manager, rather than `NSString` convenience methods, to draw strings of text efficiently.
- [Laying Out Text Along an Arbitrary Path](Laying%20Out%20Text%20Along%20an%20Arbitrary%20Path.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydolkdjjbeoqsjijba) shows how to use the layout manager without a text view to lay out glyphs along a calculated path.
- [Calculating Text Height](Calculating%20Text%20Height.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydslkdjjbeoqsjijba) shows how to determine the height of a block of text laid out in a fixed-width area.
- [Counting Lines of Text](Counting%20Lines%20of%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaytalkdjjbeoqsjijba) explains how you can programmatically count the number of lines in a string of text, whether the lines are defined by hard line-break characters or laid out in a text container.
- [Using Text Tables](Using%20Text%20Tables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmbqfvjvooa) explains how you can add text table support to your application in OS X version 10.4 and later.

For further reading, refer to the following documents:

- _[Text System Storage Layer Overview](../Text%20System%20Storage%20Layer%20Overview/Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4do2i)_ discusses the facilities that the Cocoa text system uses to store the text and geometric shape information used for text layout.
- _[Text Attribute Programming Topics](../Text%20Attribute%20Programming%20Topics/Introduction%20to%20Text%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dq2i)_ describes the text-related attributes maintained by the Cocoa text system, which provide the distinguishing characteristics of rich text and other formatting information for paragraphs and documents.
[Next](The%20Layout%20Manager.md)

