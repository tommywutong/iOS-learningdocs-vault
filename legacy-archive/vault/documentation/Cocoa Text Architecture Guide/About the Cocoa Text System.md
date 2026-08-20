---
title: Cocoa Text Architecture Guide
apple_id: TP40009459
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html
archived_at: '2026-07-18T02:08:08.879220Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Text%20Handling%20Technologies%20in%20OS%20X.md)

# About the Cocoa Text System

The Cocoa text system is the primary text-handling system in OS X, responsible for the processing and display of all visible text in Cocoa. It provides a complete set of high-quality typographical services through the text-related AppKit classes, which enable applications to create, edit, display, and store text with all the characteristics of fine typesetting, such as kerning, ligatures, line-breaking, and justification.

![../Art/text_system_architecture_2x.png](attachments/Art/text_system_architecture_2x.png)

The Cocoa text system provides text editing and layout for most applications. The object-oriented design of the system provides flexibility and ease of use.

If your application needs to display text, and especially if its users need to enter and edit text, then you should use the Cocoa text system. The Cocoa text system is one of two text-handling systems in OS X. The other is Core Text, which provides low-level, basic text layout and font-handling capabilities to higher-level engines such as the AppKit.

The Cocoa text system encodes characters as Unicode values. It translates characters into glyphs, including ligatures and other contextual forms, and handles typefaces, styles, fonts, and families. The system does text layout, placing glyphs horizontally or vertically in either direction, using font metric information, and uses kerning when appropriate. It performs high-quality line breaking and hyphenation to create lines of text with proper alignment or justification.

The Cocoa text system is abstracted as a set of classes that represent modular, layered functional areas reflecting the Model-View-Controller design paradigm. The top layer of the system is the user-interface layer of various views, the bottom layer stores the data models, and the middle layer consists of controllers that interpret keyboard input and arrange text for display.

The four primary text system classes—`NSTextView`, `NSLayoutManager`, `NSTextContainer`, and `NSTextStorage`—can be configured in various ways to accomplish different text-handling goals.

The Cocoa text system handles five kinds of attributes: character attributes, such as font and size; temporary attributes used during processing or display, such as underlining of misspelled words; paragraph attributes, such as alignment and tab stops; glyph attributes that may control special handling of particular glyphs; and document attributes, such as margins and paper size.

The Font panel, also called the _Fonts window_, is a user interface object that displays a list of available font families and styles, letting the user preview them and change the font used to display text. Text views work with `NSFontPanel` and `NSFontManager` objects to implement the font-handling system. You can create font objects using the `NSFont` class and query them for font metrics and detailed glyph layout information.

Usually, text editing is performed by direct user action with a text view, but it can also be accomplished by programmatic interaction with a text storage object. The text input system translates keyboard events into commands and text input. You can customize editing behavior using many methods of text system objects, through the powerful Cocoa mechanisms of notification and delegation, or, in extreme cases, by replacing the text view itself with a custom subclass.

To understand the information in this document, you should understand the material in _[Text System User Interface Layer Programming Guide](../Cocoa/Text%20System%20User%20Interface%20Layer%20Programming%20Guide/Introduction%20to%20Text%20System%20User%20Interface%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4ta2i)_. In addition, you should have a general knowledge of Cocoa programming paradigms and, to understand the code examples, familiarity with the Objective-C language.

The following documents describe other aspects of the Cocoa text system:

_[Text System User Interface Layer Programming Guide](../Cocoa/Text%20System%20User%20Interface%20Layer%20Programming%20Guide/Introduction%20to%20Text%20System%20User%20Interface%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4ta2i)_ describes the high-level interface to the Cocoa text system, which is sufficient for most applications.

_[Text System Storage Layer Overview](../Cocoa/Text%20System%20Storage%20Layer%20Overview/Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4do2i)_ discusses the lower-level facilities that the Cocoa text system uses to store text.

_[Text Layout Programming Guide](../Cocoa/Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_ describes how the Cocoa text system lays out text on a page, suitable for display and printing.

The following sample code projects illustrate how to use many of the APIs of the Cocoa text system:

_[CircleView](../../samplecode/CircleView/CircleView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobygi)_ is a small application with a demonstration subclass of `NSView` that draws text in a circle.

_[NSFontAttributeExplorer](../../samplecode/NSFontAttributeExplorer/NSFontAttributeExplorer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojwga)_ demonstrates how to gather and display various metric information for installed fonts using `NSFont`.

_[TextInputView](../../samplecode/TextInputView/TextInputView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobuga)_ demonstrates how a view can implement the `NSTextInputClient` protocol.

_[TextViewDelegate](../../samplecode/TextViewDelegate/TextViewDelegate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbrge)_ demonstrates using a text view's delegate to control selection and user input.

[Next](Text%20Handling%20Technologies%20in%20OS%20X.md)

