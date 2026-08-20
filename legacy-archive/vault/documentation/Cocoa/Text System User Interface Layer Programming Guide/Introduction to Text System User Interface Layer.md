---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/TextUILayer.html
archived_at: '2026-07-15T07:20:39.773321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20User-Interface%20Layer-%20NSTextView%20Class.md)

# Introduction to Text System User Interface Layer

_Text System User Interface Layer_ describes the high-level user interface to the Cocoa text system through the `NSTextView` class.

You should read this document if your application needs to present a user interface to the full capabilities of the text system, that is, if your users need to edit substantial amounts of text.

To understand this material you should have a general understanding of Cocoa programming conventions, and you should have read _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_.

This document contains the following articles:

- [The User-Interface Layer: NSTextView Class](The%20User-Interface%20Layer-%20NSTextView%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdqlkdjjbeuschifdq) describes the capabilities and features of the NSTextView class, through which most applications interact with the text system.
- [Creating an NSTextView Object](Creating%20an%20NSTextView%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztclkdjjbeeskbifda) explains how to instantiate an `NSTextView` object using Interface Builder.
- [Creating an NSTextView Programmatically](Creating%20an%20NSTextView%20Object%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztalkdjjbeeskbifda) explains how to create an `NSTextView` object in code and cause it to create its supporting web of text-handling objects.
- [Putting an NSTextView Object in an NSScrollView](Putting%20an%20NSTextView%20Object%20in%20an%20NSScrollView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztqlkdjjbeeskbifda) shows how to programmatically configure an `NSTextView` object with scroll bars.
- [Using Multiple NSTextViews](Using%20Multiple%20NSTextViews.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztilkdjjbeuschifdq) describes the attributes held in common by multiple text views configured to share a single layout manager.
- [Plain and Rich Text Objects](Plain%20and%20Rich%20Text%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztklkdjjbeuschifdq) explains the difference between plain text and rich text and lists the RTF control words that any text object recognizes.
- [Setting Text Attributes](Setting%20Text%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztmlkdjjbeuschifdq) discusses text attributes and the action methods you can use to control them programmatically.
- [Setting Text Margins](Setting%20Text%20Margins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydelkdjjbeuschifdq) describes the values, maintained by various text system objects, that affect the apparent margins surrounding text on a printed page or display.

For more information, refer to the following documents:

- _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_ provides an overview of the Cocoa text system. It also explains how the text system supports entering and modifying text and attributes through user interaction with the user interface layer.
- _[Text System Storage Layer Overview](../Text%20System%20Storage%20Layer%20Overview/Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4do2i)_ describes the facilities that the Cocoa text system uses to store the text and geometric shape information used for text layout.
[Next](The%20User-Interface%20Layer-%20NSTextView%20Class.md)

