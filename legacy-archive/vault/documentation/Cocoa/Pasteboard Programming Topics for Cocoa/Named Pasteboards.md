---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbNamedPasteboards.html
archived_at: '2026-07-15T07:13:54.938808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Data%20Types.md)[Previous](Implementing%20Copy%20and%20Paste.md)

# Named Pasteboards

Data in the pasteboard server is associated with a name (a string) that indicates how it is to be used. Each set of data and its associated name is, in effect, a separate pasteboard, distinct from the others. An application keeps a separate `NSPasteboard` object for each named pasteboard that it uses. There are five standard pasteboards in common use, each named by a global string variable:

| Pasteboard Name | Description |
| --- | --- |
| `NSGeneralPboard` | The pasteboard that is used for ordinary cut, copy, and paste operations. It holds the contents of the last selection that has been cut or copied. |
| `NSFontPboard` | The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor. |
| `NSRulerPboard` | The pasteboard that holds information about paragraph formats in support of the Copy Ruler and Paste Ruler commands that may be implemented in a text editor. |
| `NSFindPboard` | The pasteboard that holds information about the current state of the active application’s Find panel. This information permits users to enter a search string into the Find panel, then switch to another application to conduct another search. |
| `NSDragPboard` | The pasteboard that stores data to be moved as the result of a drag operation. For additional information on working with the drag pasteboard, see [Drag and Drop](../Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i). |

You can create private pasteboards by asking for an `NSPasteboard` object with any name other than those listed above. Data in a private pasteboard may then be shared by passing its name between applications.

The `NSPasteboard` class makes sure there is never more than one object for each named pasteboard on the computer for each user. If you ask for a new object when one has already been created for the pasteboard with that name, the existing object is returned.

[Next](Data%20Types.md)[Previous](Implementing%20Copy%20and%20Paste.md)

