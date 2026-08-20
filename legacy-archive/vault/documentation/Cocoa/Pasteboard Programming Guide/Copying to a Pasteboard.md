---
title: Pasteboard Programming Guide
apple_id: TP40008099
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Articles/pbCopying.html
archived_at: '2026-07-15T07:17:41.382894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Guide](Introduction.md)


[Next](Reading%20from%20a%20Pasteboard.md)[Previous](Pasteboard%20Concepts.md)

# Copying to a Pasteboard

You perform a copy operation by first clearing the existing contents of, then writing the copied objects to, a pasteboard.

There are three steps to performing a copy operation:

1. Get a pasteboard.

   Typically, you just use the general pasteboard:

```
NSPasteboard *pasteboard = [NSPasteboard generalPasteboard];
```
2. Clear the contents of the pasteboard.

   Typically, you just use the general pasteboard:

```
NSInteger changeCount = [pasteboard clearContents];
```

   The method returns the change count of the pasteboard; you usually don’t need this value.
3. Write the objects being copied to the pasteboard.

   You pass the objects to write in an array—objects in the array must adopt the [NSPasteboardWriting Protocol Reference](https://developer.apple.com/documentation/appkit/nspasteboardwriting) protocol:

```
NSArray *objectsToCopy = <#An array of objects#>;
BOOL OK = [pasteboard writeObjects:objectsToCopy];
```

   The method returns `NO` if the items were not successfully added to the pasteboard.

In many cases, this is as much as you need to do. Note, though, the important prerequisite that objects you write to the pasteboard must adopt the `NSPasteboardWriting` [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45). Classes that implement the protocol include `NSString`, `NSImage`, `NSURL`, `NSColor`, `NSAttributedString`, and `NSPasteboardItem`. If you want to write an instance of a custom class, either it must adopt the `NSPasteboardWriting` protocol or you can wrap it in an instance of an [NSPasteboardItem](https://developer.apple.com/documentation/appkit/nspasteboarditem)—see [Custom Data](Custom%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmrsfvjvomi).

[Next](Reading%20from%20a%20Pasteboard.md)[Previous](Pasteboard%20Concepts.md)

