---
title: Text Attachment Programming Topics
apple_id: 10000094i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2006-12-05'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttachments/Tasks/AddingAttachments.html
archived_at: '2026-07-15T07:20:04.356152Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Attachment Programming Topics](Introduction%20to%20Text%20Attachments.md)


[Next](Document%20Revision%20History.md)[Previous](Text%20Attachments.md)

# Adding Attachments to Text

You can embed graphics or other
attachments in text in either of two ways: programmatically or directly
through user actions. In the programmatic approach, you can add
graphic objects using the `NSText` method [replaceCharactersInRange:withRTFD:](https://developer.apple.com/documentation/appkit/nstext/1525846-replacecharacters) or through a more specific method defined by a subclass.

An alternate means of adding an image or other attachment
to the text is for the user to drag an image or other file directly
into the text object. The text object automatically creates an `NSTextAttachment` object to manage
the display of the image. This feature requires a rich text object
that has been configured to receive dragged images using the `NSText` method [setImportsGraphics:](https://developer.apple.com/documentation/appkit/nstext/1531887-importsgraphics). (`NSTextView` and `NSTextField` also have implementations of this method.)

Images that have been imported can be written as part of an
RTFD document.
RTFD documents use a file package, or directory,
to store the components of the document (the “D” stands for
“directory”). The file package has the name of the document
plus an `.rtfd` extension.
The file package always contains a file called `TXT.rtf` for
the text of the document, and one or more TIFF or EPS files for
the images, plus the files for other attachments. A text object
can transfer information in an RTFD document to a file and read it
from a file using the `NSText` methods [writeRTFDToFile:atomically:](https://developer.apple.com/documentation/appkit/nstext/1527085-writertfd) and [readRTFDFromFile:](https://developer.apple.com/documentation/appkit/nstext/1532564-readrtfdfromfile).

[Next](Document%20Revision%20History.md)[Previous](Text%20Attachments.md)

