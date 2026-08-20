---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Concepts/UILayer.html
archived_at: '2026-07-15T07:20:32.725877Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System User Interface Layer Programming Guide](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)


[Next](Creating%20an%20NSTextView%20Object.md)[Previous](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)

# The User-Interface Layer: NSTextView Class

The vast majority of applications interact with the text system through one class: NSTextView. An NSTextView object provides a rich set of text-handling features and can:

- Display text in various fonts, colors, and paragraph styles
- Display images
- Read text and images from (and write them to) disk or the pasteboard
- Let users control text attributes such as font, superscripting and subscripting, kerning, and the use of ligatures
- Cooperate with other views to enable scrolling and display of the ruler
- Cooperate with the Font panel (Fonts window) and Spelling panel
- Support various key bindings, such as those used in Emacs

The interface that this class declares (and inherits from its superclass NSText) lets you programmatically:

- Control the size of the area in which text is displayed
- Control the editability and selectability of the text
- Select and act on portions of the text

NSTextView objects are used throughout the Cocoa user interface to provide standard text input and editing features.

An NSTextView object is a convenient package of the most generally useful text-handling features. If the features of the NSTextView class satisfy your application’s requirements and you need more programmatic control over the characters and attributes that make up the text, you’ll have to learn something about the object that stores this data, NSTextStorage.

One of the design goals of NSTextView is to provide a comprehensive set of text-handling features so that you should rarely need to create a subclass. In its standard incarnation, NSTextView creates the requisite group of objects that support the text system—NSTextContainer, NSLayoutManager, and NSTextStorage objects. Here are the major features that NSTextView adds to those of NSText:

- _Rulers._ NSTextView works with the NSRulerView class to let users control paragraph formatting, in addition to using commands in the Text menu provided by Interface Builder, which is available as a submenu of the Format menu as well as a menu in the menu bar.
- _Input management and key binding._ Certain key combinations are bound to specific NSTextView methods so that the user can, for example, move the insertion point without using the mouse.
- _Marked text attributes._ NSTextView defines a set of text attributes that support special display characteristics during input management. Marked text attributes affect only visual aspects of text—color, underline, and so on—they don’t include any attributes that would change the layout of text.
- _File and graphic attachments._ The extended text system provides programmatic access to text attachments as instances of NSTextAttachment, through the NSTextView and NSTextStorage classes.
- _Delegate messages and notifications._ NSTextView adds several delegate messages and notifications to those used by NSText. The delegate and observers of an NSTextView can receive any of the messages or notifications declared by either class.

[Next](Creating%20an%20NSTextView%20Object.md)[Previous](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)

