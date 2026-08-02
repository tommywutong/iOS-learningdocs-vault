---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/TextEditing.html
archived_at: '2026-07-15T07:20:17.088279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Text%20Editing.md)

# Introduction to Text Editing Programming Guide for Cocoa

_Text Editing Programming Guide for Cocoa_ describes ways in which you can control the behavior of the Cocoa text system as it performs text editing. Text editing is the modification of text characters or attributes by interacting with text objects. Usually, editing is performed by direct user action with a text view, but it can also be accomplished by programmatic interaction with a text storage object. This document also discusses the text input system that translates keyboard events into commands and text input.

You should read this programming topic if you need to understand how text editing in Cocoa works and how to modify that behavior.

To understand the information in this programming topic you should have prior general knowledge of the Cocoa text system’s capabilities and architecture, as well as basic Cocoa programming conventions.

This programming topic contains the following articles:

- [Overview of Text Editing](Overview%20of%20Text%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdslkcijbumrkcjbaq) provides a high-level view of the text editing mechanism and explains the message sequence that occurs when a text view receives a key event.
- [About Key Bindings](About%20Key%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dsmbqfvbecssdirdemsi) describes the key-binding mechanism by which keyboard events are mapped to method names or processed as text input.
- [Intercepting Key Events](Intercepting%20Key%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaytglkdjjbeoqsjijba) explains how to catch key events received by an `NSTextView` object so that you can modify their effect.
- [Delegate Messages and Notifications](Delegate%20Messages%20and%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztelkdjjbeuschifdq) describes the messages the text view delegate and registered observers of the text system can receive.
- [Subclassing NSTextView](Subclassing%20NSTextView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztolkdjjbeuschifdq) explains the responsibilities an `NSTextView` subclass must fulfill to interact successfully with the text system.
- [Creating Custom Views](Creating%20Custom%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dqojzfvbegskdivdeori) describes how to implement a custom text view that interacts with the text input system, in case `NSTextView` does not provide the support required by your application.
- [Synchronizing Editing](Synchronizing%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaytelkdjjbeoqsjijba) explains the batch editing concept and shows how to force the end of editing, which sends notifications and leaves the text backing store in a consistent state.
- [Setting Focus and Selection Programmatically](Setting%20Focus%20and%20Selection%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztglkdjjbeoqsjijba) explains how to make a text view the first responder and how to manipulate the selection programmatically.
- [Working With the Field Editor](Working%20With%20the%20Field%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaytklkdjjbeuschifdq) explains how the text system uses the field editor and how you can modify that behavior.
- [Handling Drops in a Text Field](Handling%20Drops%20in%20a%20Text%20Field.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhaytilkdjjbeoqsjijba) explains how to add drag-and-drop support to a text field, which includes providing a custom field editor for the text view.

- _Text System Overview_ provides an overview of the Cocoa text system, introducing its important features and describing aspects of the text system as a whole.
- _[Text System User Interface Layer Programming Guide](../Text%20System%20User%20Interface%20Layer%20Programming%20Guide/Introduction%20to%20Text%20System%20User%20Interface%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4ta2i)_ provides more information about the primary interface to the text system, the `NSTextView` class.
- _[TextLayoutDemo](../../../samplecode/TextLayoutDemo/TextLayoutDemo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzuge)_ sample code illustrates customizing `NSTextView` with `NSLayoutManager` and a custom `NSTextContainer` object.
- _[NSFontAttributeExplorer](../../../samplecode/NSFontAttributeExplorer/NSFontAttributeExplorer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojwga)_ sample code demonstrates how to gather and display font metric information for installed fonts using `NSFont`.
- _TextInputView_ sample code, in /Developer/Examples/AppKit, explains how to implement the `NSTextInputClient` protocol for custom views.

The other guides and programming topics in the text system area also have information related to text editing. In addition, please refer to the other text-related code samples installed with Xcode Tools in /Developer/Examples/AppKit, including complete source code for the TextEdit application that ships with OS X.

[Next](Overview%20of%20Text%20Editing.md)

