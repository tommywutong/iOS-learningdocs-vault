---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TextDefaultsBindings/TextDefaultsBindings.html
archived_at: '2026-07-15T07:15:36.421206Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Mouse-Tracking%20and%20Cursor-Update%20Events.md)[Previous](Monitoring%20Events.md)

# Text System Defaults and Key Bindings

This document reveals some tips and tricks about various defaults you can use to customize the behavior of Cocoa’s text system. It also describes how to customize the key bindings supported by the text system.

Heavy-duty subclassers may alter some or all of the text system's functionality, rendering some or all of these features inactive.

The text system uses a generalized key-binding mechanism that is completely re-mappable by the user, although defining custom key bindings dynamically (that is, while the application is running) is not supported. Key bindings are specified in an dictionary file that must have an extension of `.dict`; the format of this file should be an XML [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44), but the text system can also understand old-style (NeXT era) property lists. The standard key bindings are specified in `/System/Library/Frameworks/AppKit.framework/Resources/StandardKeyBinding.dict`. These standard bindings include a large number of Emacs-compatible control key bindings, all the various arrow key bindings, bindings for making field editors and some keyboard UI work, and backstop bindings for many function keys.

To customize bindings, you create a file named `DefaultKeyBinding.dict` in `~/Library/KeyBindings/` and specify bindings to augment or replace the standard bindings. You may use the standard bindings file as a template. It is recommended that you use the Property List Editor application to edit a bindings dictionary. You may use another application such as TextEdit or Xcode, but if you do you must ensure the encoding of the saved file is UTF8.

Key bindings are key-value pairs with the key being a string that specifies a physical key and the value identifying an action method to be invoked when the key is pressed. (Many of these action methods are declared by `NSResponder`.) You can compose physical-key strings using the following elements:

- The alphanumeric character that appears on a US keyboard. For example, "f" or ">". (As noted below, some special characters are reserved for modifier flags.)
- For a few keys, such as Escape, Tab, and backward Delete (BS), the octal number from the ASCII table that identifies the key. For example, the octal number identifying the Escape key (sometimes used as a modifier key) is `\033`.
- An `enum` constant assigned a unique Unicode value that is used to identify a function key. These constants are defined in `NSEvent.h`. Examples of these constants are `NSF7FunctionKey`, `NSHomeFunctionKey`, and `NSHelpFunctionKey`.
- One or more key modifiers, which must precede one of the other key-identifier elements. The following special characters are used for modifier flags:

  - “`^`” for Control
  - “`~`” for Option
  - “`$`” for Shift
  - “`#`” for numeric keypad

  For example, the following string would identify the 0 (zero) key on the numeric keypad when the Control key is pressed simultaneously: "`^#0`".

The text system supports the specification of multiple keystroke bindings through nested binding dictionaries. For instance, Escape could be bound to `cancel:` or it could be bound to a whole dictionary which would then contain bindings for the next keystroke after Escape.

The following sample binding files illustrate how you might customize bindings. The first one adds Option-key bindings for some common Emacs behavior. This might be useful where the Option key bindings are not standard. With these bindings it would be necessary to type “`Control-Q, Option-f`” in order to type a florin character instead of moving forward a word. This sample also explicitly binds Escape to `complete:`. (In OS X, this is the default so this override changes nothing.)

```
/* ~/Library/KeyBindings/DefaultKeyBinding.dict */

{
    /* Additional Emacs bindings */
    "~f" = "moveWordForward:";
    "~b" = "moveWordBackward:";
    "~<" = "moveToBeginningOfDocument:";
    "~>" = "moveToEndOfDocument:";
    "~v" = "pageUp:";
    "~d" = "deleteWordForward:";
    "~^h" = "deleteWordBackward:";
    "~\010" = "deleteWordBackward:";  /* Option-backspace */
    "~\177" = "deleteWordBackward:";  /* Option-delete */

    /* Escape should really be complete: */
    "\033" = "complete:";  /* Escape */
}
```

The following example shows how to have multi-keystroke bindings. It binds a number of Emacs meta bindings using Escape as the meta key instead of the Option modifier. So Escape followed by the "f" key means `moveWordForward:` here. This sample binds Escape-Escape to `complete:`. Note the nested dictionaries

```
/* ~/Library/KeyBindings/DefaultKeyBinding.dict */
{
    /* Additional Emacs bindings */
    "\033" = {
        "\033" = "complete:";  /* ESC-ESC */
        "f" = "moveWordForward:";  /* ESC-f */
        "b" = "moveWordBackward:";  /* ESC-b */
        "<" = "moveToBeginningOfDocument:";  /* ESC-< */
        ">" = "moveToEndOfDocument:";  /* ESC-> */
        "v" = "pageUp:";  /* ESC-v */
        "d" = "deleteWordForward:";  /* ESC-d */
        "^h" = "deleteWordBackward:";  /* ESC-Ctrl-H */
        "\010" = "deleteWordBackward:";  /* ESC-backspace */
        "\177" = "deleteWordBackward:";  /* ESC-delete */
    };
}
```

Once you have completed specifying key bindings, you must save the file and relaunch the application for the bindings to take effect. With the right combination of key bindings and default settings, it should be possible to tailor the text system to your preferences.

The `NSResponder` class declares method prototypes for a number of standard action methods, nearly all related to manipulating selections and editing text. These methods are typically invoked through `doCommandBySelector:` as a result of interpretation by the input manager. They fall into the following general groups:

- Selection movement and expansion
- Text insertion
- General deletion of elements
- Modifying selected text
- Scrolling a document

In most cases the intent of the action method is clear from its name. The individual method descriptions in this specification also provide detailed information about what such a method should normally do. However, a few general concepts apply to many of these methods, and are explained here.

Some methods refer to spatial directions; left, right, up, down. These are meant to be taken literally, especially in text. To accommodate writing systems with directionality different from Latin script, the terms forward, beginning, backward, and end are used.

Methods that refer to moving, deleting, or inserting imply that some elements in the responder are selected, or that there’s a zero-length selection at some location (the insertion point). These two things must always be treated consistently. For example, the `insertText:` method is defined as replacing the selection with the text provided. The `moveForwardAndModifySelection:` method extends or contracts a selection, even if the selection is merely an insertion point. When a selection is modified for the first time, it must always be extended. So a `moveForward...` message extends the selection from its end, while a `moveBackward...` message extends it from its beginning.

A number of action methods for editing text imitate the Emacs concepts of point (the insertion point), and mark (an anchor for larger operations normally handled by selections in graphical interfaces). The `setMark:` method establishes the mark at the current selection, which then remains in effect until the mark is changed again. The `selectToMark:` method extends the selection to include the mark and all characters between the selection and the mark.

Also like Emacs, deletion methods affecting lines, paragraphs, and the mark implicitly place the deleted text into a buffer, separate from the pasteboard, from which you can later retrieve it. Methods such as `deleteToBeginningOfLine:` add text to this buffer, and `yank:` replaces the selection with the item in the kill buffer.

__Allowed value__: "YES" or "NO".

This default controls whether the text system accepts key events with the Option key down. The default value is `NO`. A value of `YES` means that any key event with the Option bit on will be passed up the responder chain to eventually be treated as a mnemonic instead of being accepted by the text as textual input or a key binding command. If this default is set to NO then the key events with the Option bit set will be passed through the text system's normal key input sequence. This will allow any key bindings involving Option to work (such as Emacs-style bindings like Option-f for word forward) and it allows typing of special international and Symbol font characters.

__Allowed value__: Key-binding style string.

This default controls the numeric argument binding. The default is for numeric arguments not to be supported. If you provide a binding for this default you enable the feature. This allows you to repeat a keyboard command a given number of times. For instance “`Control-U 10 Control-F`” means move forward ten characters.

__Allowed value__: Key-binding style string.

This default controls the quote binding. The default is for this to be “^q” (that's Control-Q). This is the binding that allows you to literally enter characters that would otherwise be interpreted as commands. For instance “`Control-Q Control-F`” would insert a Control-F character into the document instead of performing the command `moveForward:`.

__Allowed value__: "YES" or "NO".

The default controls whether a text object will by default show invisible characters like tab, space, and carriage return using some visible glyph. By default it is `NO`. It only controls the default setting for `NSLayoutManager` objects (which can be modified programmatically). In order for this to work, the rule book generating the glyphs must support the feature. Currently our rule books do not support this feature, so currently this default is not very useful.

__Allowed value__: "YES" or "NO".

The default controls whether a text object will by default show control characters visibly (usually by representing Control-C as “^C” in the text). By default it is `NO`. It only controls the default setting for `NSLayoutManager` objects (which can be modified programmatically). In order for this to work, the rule book(s) generating the glyphs must support the feature. This feature carries a cost. It will increase the memory needed for documents that contain control characters by quite a lot. Use it with care.

__Allowed value__: Color object or specifier.

This default controls the background color of selected text. By default this is light gray. Defaults that accept colors accept them in one of three ways. Either as an archived `NSColor` object, or as three RGB components, or as a string that can be resolved to a factory [selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) on `NSColor` that will return the desired color (for example, “redColor”). Note that NSTextField objects and other controls that use field editors to edit their text control their own selection attributes to conform with the UI.

__Allowed value__: Color object/specifier or "underline".

This default controls the way that marked text is displayed. The `NSMarkedTextAttribute` can be either “`Background`” or “`Underline`”. If it is “`Background`” then `NSMarkedTextColor` indicates the background color to use for marked text. If `NSMarkedTextAttribute` is “`Underline`”, `NSMarkedTextColor` indicates the foreground color to use for marked text (the marked text will be drawn in the indicated color and underlined). By default, marked text is drawn with a yellowish background color. Kit defaults that accept colors accept them in one of three ways. Either as an archived `NSColor` object, or as three RGB components, or as a string that can be resolved to a factory [selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) on `NSColor` that will return the desired color (for example, “redColor”). If the `NSMarkedTextAttribute` default contains a color instead of one of the strings “`Background`” or “`Underline`” then that color is used as the background color for marked text and the `NSMarkedTextColor` attribute is ignored.

__Allowed value__: Number string.

This default controls the size of the kill ring (as in Emacs Control-Y). The default value is 1 (not really a ring at all, just a single buffer). If you set this to a value larger than one, you also need to rebind Control-Y to `yankAndSelect:` instead of `yank:` for things to work properly (note that `yankAndSelect:` is not listed in any headers). See [Key Bindings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq3dqljwgeytambv) for more information about bindings.

[Next](Mouse-Tracking%20and%20Cursor-Update%20Events.md)[Previous](Monitoring%20Events.md)

