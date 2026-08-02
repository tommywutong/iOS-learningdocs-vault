---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html
archived_at: '2026-07-15T07:20:32.233222Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Storage%20Layer-%20The%20NSTextStorage%20Class.md)

# Introduction to Text System Storage Layer Overview

_Text System Storage Layer Overview_ discusses the facilities that the Cocoa text system uses to store the text and geometric shape information used for text layout.

You should read this document if you need to work directly with the text storage layer. For example, you may need to change the text programmatically in a text storage object or extend its capabilities.

To understand this material you should have a general understanding of Cocoa programming conventions. You should also have read _Text System Overview_.

This document contains the following articles:

- [The Storage Layer: The NSTextStorage Class](The%20Storage%20Layer-%20The%20NSTextStorage%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2dmlkdjjbeuschifdq) provides a general introduction to the capabilities of text storage objects.
- [Layout Geometry: The NSTextContainer Class](Layout%20Geometry-%20The%20NSTextContainer%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaydglkdjjbeuschifdq) explains how text containers define the area in which the system lays out text and how they interact with other text system objects.
- [Creating Text Storage](Creating%20Text%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2dslkdjjbeeskbifda) explains how you create and set up text storage objects.
- [Changing Text Storage](Changing%20Text%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2dqlkdjjbeeskbifda) describes the process of editing text in a text storage object programmatically.
- [Displaying a Text Container](Displaying%20a%20Text%20Container.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdilkdjjbeeskbifda) explains how you can display the text in a text storage object in a text view or other NSView object.
- [Calculating Region, Bounding Rectangle, and Inset](Calculating%20Region%2C%20Bounding%20Rectangle%2C%20and%20Inset.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdklkdjjbeeskbifda) discusses how to define a text container’s text layout area.
- [Tracking the Size of a Text View](Tracking%20the%20Size%20of%20a%20Text%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdolkdjjbeeskbifda) explains how you can set up a text container so that its geometry interacts with that of its associated text view.
- [Creating a Subclass of NSTextStorage](Creating%20a%20Subclass%20of%20NSTextStorage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdmlkdjjbeeskbifda) discusses the requirements of NSTextStorage subclasses.

For further reading, refer to the following documents:

- _[Attributed String Programming Guide](../Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztm2i)_ provides information about the attributed string objects on which [NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage) is built. `NSTextStorage` is a subclass of [NSMutableAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSMutableAttributedString).
- _[Text Layout Programming Guide](../Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_ describes the layout process involving text storage, text container, text view, and layout manager objects.
[Next](The%20Storage%20Layer-%20The%20NSTextStorage%20Class.md)

