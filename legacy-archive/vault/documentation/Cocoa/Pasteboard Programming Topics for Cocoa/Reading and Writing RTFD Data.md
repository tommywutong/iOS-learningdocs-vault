---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbReadWriteRTFD.html
archived_at: '2026-07-15T07:13:55.438195Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Filter%20Services.md)[Previous](Reading%20and%20Writing%20Font%20Data.md)

# Reading and Writing RTFD Data

The `NSRTFDPboardType` is used for the contents of an RTFD file package (a directory containing an RTF text file and one or many image files). There are several ways to work with RTFD data. If you have an `NSFileWrapper` object that represents an RTFD file wrapper, you can send it a `serializedRepresentation` message to return the RTFD data and write that to the pasteboard as follows:

```
NSFileWrapper *tempRTFDData = [[[NSFileWrapper alloc]
    initWithPath:@"/tmp/MyTemporaryRTFDDocument.rtfd"] autorelease];
[pboard setData:[tempRTFDData serializedRepresentation]
    forType:NSRTFDPboardType];
```

In addition to `NSFileWrapper`, instances of classes such as `NSAttributedString` and `NSText` can return RTFD data. If you are using one of these classes, you can write an RTFD representation of their contents to the pasteboard as follows:

```
NSAttributedString *attrString = /* get an attributed string */;
NSRange wholeStringRange = NSMakeRange(0, [attrString length]);
NSData *rtfdData = [attrString RTFDFromRange:wholeStringRange
                                documentAttributes:nil];
[pboard setData:rtfdData forType:NSRTFDPboardType];
```

Note that the `NSText` method does not require the `documentAttributes` parameter.

[Next](Filter%20Services.md)[Previous](Reading%20and%20Writing%20Font%20Data.md)

