---
title: Text Attribute Programming Topics
apple_id: 10000088i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/TextAttributes.html
archived_at: '2026-07-15T07:20:08.896080Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Text%20Attributes.md)

# Introduction to Text Attributes

_Text Attributes_ describes the text-related attributes maintained by the Cocoa text system. Text attributes provide the distinguishing characteristics of rich text and other formatting information for paragraphs and documents.

You should read this document to understand the different types of text attributes in the text system, especially if you deal directly with attributed strings and need to understand how the text system manages their attributes.

To understand the information in this document, you should have prior general knowledge of the text system’s capabilities and architecture, as well as basic Cocoa programming conventions.

This document includes the following articles:

- [About Text Attributes](About%20Text%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydilkcijbumrkcjbaq) introduces and defines the five types of text-related attributes used in Cocoa. It also provides cross-references to more detailed documentation.
- [Setting Text Attributes](Setting%20Text%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztmlkdjjbeuschifdq) explains how you can programmatically set the attributes of text displayed in a text view object using the methods of NSTextView and its superclass NSText.
- [Accessing Attributes](Accessing%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dclkciffeeqsdijeq) describes the attributes stored with an attributed string and explains how to manipulate them.
- [Changing an Attributed String](Changing%20an%20Attributed%20String.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3delkcijbuer2dirdq) describes the methods available to alter the characters and attributes of an NSMutableAttributedString. This article also discusses attribute fixing.
- [Plain and Rich Text Objects](Plain%20and%20Rich%20Text%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztklkdjjbeuschifdq) discusses text attributes of the rich text format (RTF) standard recognized by text objects.
- [RTF Files and Attributed Strings](RTF%20Files%20and%20Attributed%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dilkcijbuessjijbq) explains how to read and write character and document attributes to RTF files.

For more information, refer to the following documents:

- _[Text System Storage Layer Overview](../Text%20System%20Storage%20Layer%20Overview/Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4do2i)_ provides more information about how the text system stores and manipulates text.
- _[Attributed String Programming Guide](../Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztm2i)_ presents more detailed information about text strings and attributes.
[Next](About%20Text%20Attributes.md)

