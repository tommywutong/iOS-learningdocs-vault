---
title: Cocoa Text Architecture Guide
apple_id: TP40009459
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/UsingCoreText/UsingCoreText.html
archived_at: '2026-07-18T02:08:41.231477Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Cocoa Text Architecture Guide](About%20the%20Cocoa%20Text%20System.md)


[Next](Typographical%20Concepts.md)[Previous](About%20the%20Cocoa%20Text%20System.md)

# Text Handling Technologies in OS X

The Macintosh operating system has provided sophisticated text handling and typesetting capabilities from its beginning. In fact, these features sparked the desktop publishing revolution. Over the years, the text handling facilities of the platform have continued to evolve to become more advanced, more efficient, and easier to use. OS X provides modern text handling capabilities that are available to all applications through the classes of the Cocoa text system and the opaque types and functions of Core Text.

The text-handling component of any application presents one of the greatest challenges to software designers. Even the most basic text-handling system must be relatively sophisticated, allowing for text input, layout, display, editing, copying and pasting, and many other features. But developers and users expect even more than these basic features, expecting even simple editors to support multiple fonts, various paragraph styles, embedded images, spell checking, and other features.

The Cocoa text system provides all these basic and advanced text-handling features, and it also satisfies additional requirements from the ever-more-interconnected computing world: support for the character sets of all of the world’s living languages, powerful layout capabilities to handle various text directionality and nonrectangular text containers, and sophisticated typesetting capabilities such as control of kerning and ligatures. Cocoa’s object-oriented text system is designed to provide all these capabilities without requiring you to learn about or interact with more of the system than is necessary to meet the needs of your application.

Underlying the Cocoa text system is Core Text, which provides low-level, basic text layout and font-handling capabilities to higher-level engines such as AppKit, WebKit, and others. Core Text provides the implementation for many Cocoa text technologies. Application developers typically have no need to use Core Text directly. However, the Core Text API is accessible to developers who must use it directly, such as those writing applications with their own layout engine and those porting ATSUI- or QuickDraw-based codebases to the modern world.

To decide which OS X text technology is right for your application, apply the following guidelines:

- If possible, use Cocoa text. The `NSTextView` class is the most advanced full-featured, flexible text view in OS X. For small amounts of text, use `NSTextField`. For more information about text views, see _[Text System User Interface Layer Programming Guide](../Cocoa/Text%20System%20User%20Interface%20Layer%20Programming%20Guide/Introduction%20to%20Text%20System%20User%20Interface%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4ta2i)_.
- To display web content in your application, use WebKit. For more information about WebKit, see _[WebKit Objective-C Programming Guide](../Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i)_.
- If you have your own page layout engine, you can use Core Text to generate the glyphs and position them relative to each other. For more information about Core Text, see _[Core Text Programming Guide](../Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_.

[Next](Typographical%20Concepts.md)[Previous](About%20the%20Cocoa%20Text%20System.md)

