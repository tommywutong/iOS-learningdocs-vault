---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbFundamentals.html
archived_at: '2026-07-15T07:13:53.944446Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Implementing%20Copy%20and%20Paste.md)[Previous](Introduction%20to%20Pasteboards%20Programming%20Topics.md)

# Pasteboard Fundamentals

On Mac OS X, copy and paste operations are supported by a pasteboard server process. In Cocoa, you access the pasteboard server through an `NSPasteboard` object. This article describes how the pasteboard process works.

The basic operations you want to perform when implementing copy and paste are (a) to write data to a pasteboard and (b) to read data from a pasteboard. These operations are conceptually very simple, but mask a number of important details. In practical terms for you as an application developer, the main underlying complicating issue is that there may be a number of ways to represent data—this leads in turn to considerations of efficiency. From the systems perspective, there are additional issues to consider.

Whether the data is transferred between objects in the same application or two different applications, in a Cocoa application the interface is the same—an `NSPasteboard` object accesses a shared repository where writers and readers meet to exchange data. The writer, referred to as the pasteboard owner, deposits data on a pasteboard instance and moves on. The reader then accesses the pasteboard asynchronously, at some unspecified point in the future. By that time, the writer object may not even exist anymore. For example, a user may have closed the source document or quit the application.

Consequently, when moving data between two different applications, and therefore two different address spaces, a third memory space gets involved so the data persists even in the absence of the source. `NSPasteboard` provides access to a third address space—a pasteboard server process (`pbs`)—that is always running in the background. The pasteboard server maintains an arbitrary number of individual pasteboards to distinguish among several concurrent data transfers.

There are several standard pasteboards provided for well-defined operations system-wide:

- `NSGeneralPboard`—for cut, copy, and paste
- `NSRulerPboard`—for copy and paste of rulers
- `NSFontPboard`—for cut, copy, and paste of `NSFont` objects
- `NSFindPboard`—application-specific find panels can share a sought after text value
- `NSDragPboard`—for graphical drag and drop operations

These are described in more detail in [Named Pasteboards](Named%20Pasteboards.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqzdqlkciffessscivda). Typically you use one of the system-defined pasteboards, but if necessary you can create your own pasteboard for exchanges that fall outside the predefined set using [pasteboardWithName:](https://developer.apple.com/documentation/appkit/nspasteboard/1531026-init) Lastly, if you invoke [pasteboardWithUniqueName](https://developer.apple.com/documentation/appkit/nspasteboard/1528936-withuniquename), the pasteboard server will provide you with a uniquely-named pasteboard.

The pasteboard owner declares the data types it can write. Pasteboard data generally refer to an object instance whether a string, an arbitrarily complex object graph such as a dictionary of arrays, an instance of `NSData`, or an object wrapper for an arbitrary block of data. You can name your own pasteboard types for special-purpose data types.

Any object written to an `NSPasteboard` must conform to the `NSCoding` protocol—it must be able to archive and unarchive itself. Generally, pasteboard data consists of a value class object or a collection containing such objects.

Like the standard named pasteboards used for common operations, there are several commonly used system-defined data types, including:

- `NSStringPboardType`
- `NSTabularTextPboardType`
- `NSFilenamesPboardType`
- `NSTIFFPboardType`
- `NSFontPboardType`
- `NSRulerPboardType`
- `NSColorPboardType`

These and others are described in detail in [Data Types](Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqzdslkcineuuskkifdq).

Pasteboard operations are often carried out between two different applications. For example, an editor, capable of handling rich text format, may allow a user to select a region of text and copy it to the general pasteboard. Another application provides a simple `NSTextView` instance configured to provide ASCII text. It allow the user to paste from the general pasteboard. Neither application has knowledge about the other and the kinds of data each can handle. It is impossible for the owner to determine which of several applications might show up as the next reader of pasteboard data.

To maximize the potential for sharing, a pasteboard can hold multiple representations of the same data, each identified by a different pasteboard type string. Pasteboard owners should provide as many different representations as possible. In the previous example, the rich text editor might provide RTFD, RTF, and `NSString` representations of the copied data. A reader, on the other hand, must find the data type that best suits its capabilities. Generally, this means selecting the richest type available.

The change count is a computer-wide variable that increments every time the contents of the pasteboard changes (a new owner is declared). An independent change count is maintained for each named pasteboard. By examining the change count, an application can determine whether the current data in the pasteboard is the same as the data it last received.

The `changeCount`, `addTypes:owner:`, and `declareTypes:owner:` methods return the change count. A `types` or `availableTypeFromArray:` message should be sent by the pasteboard before reading data so the change count is valid.

Except where errors are specifically mentioned in the `NSPasteboard` method descriptions, any communications error with the pasteboard server raises an`NSPasteboardCommunicationException`.

[Next](Implementing%20Copy%20and%20Paste.md)[Previous](Introduction%20to%20Pasteboards%20Programming%20Topics.md)

