---
title: Pasteboard Programming Guide
apple_id: TP40008099
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Articles/pbUpdating105.html
archived_at: '2026-07-15T07:17:41.493746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Custom%20Data.md)

# Integrating with OS X v10.5 and Earlier

This article describes the interoperation of pasteboard API from OS X v10.5 and earlier with the APIs introduced in OS X v10.6.

On OS X v10.6, `NSPasteboard` allows you to write multiple items to the pasteboard. If you take advantage of this ability, you may need to consider how your application will interact with others that have not yet adopted this feature.

If you place multiple items on the pasteboard, an application that uses the OS X v10.5 and earlier API will typically retrieve just the best representation of the first item on the pasteboard (using `dataForType:`, -`stringForType:`, or `propertyListForType:`). You should therefore typically ensure that the first item you place on the pasteboard is that likely to be “most interesting” to clients that use the 10.5 and earlier API.

The exception to this pattern is text. If a 10.6-based application writes to the pasteboard multiple items that provide text (strings and attributed strings), then if a 10.5-based application reads text from the pasteboard the text from the items is combined using return characters. (You can think of this as akin to the pasteboard putting the individual strings from the items into an array then joining them with `componentsJoinedByString:"@\r"`.)

You can typically use API from OS X v10.5 and earlier with the APIs introduced in OS X v10.6 together in the same application. This allows you to migrate your code to the new API in a gradual fashion. With any given sequence of interaction, however, you should be consistent in using either the API from OS X v10.5 and earlier or the APIs introduced in OS X v10.6. For example, the following combination will _not_ work:

```
NSArray *fileURLs = <#An array of file URLs#>;
NSPasteboard *pboard = [NSPasteboard generalPasteboard];
NSArray *typeArray = [NSArray arrayWithObject:NSURLPboardType];
[pboard declareTypes:typeArray owner:nil]; // 10.5
[pboard writeObjects:fileURLs]; // 10.6
```


If your application currently defines a public pasteboard type that other applications rely on, you need to perform the following steps to ensure that existing applications will continue to see your pasteboard type even after your application has moved from pboard types to UTIs:

1. Formally declare the new pasteboard type UTI as an exported type declaration.
2. Ensure the declared UTI conforms to the `public.data` type.
3. Add a tag specification for the `com.apple.nspboard-type` tag to the type declaration. The value you provide should be the literal string value of the pboard type, not the name of the constant. The following example shows how to create a tag specification to associate a UTI with a pboard type:

```
<key>UTTypeTagSpecification</key>
    <dict>
        <key>com.apple.nspboard-type</key>
        <string>MyCustomPboardType</string>
    </dict>
```


The [NSPasteboardItem](https://developer.apple.com/documentation/appkit/nspasteboarditem), [NSPasteboardReading](https://developer.apple.com/documentation/appkit/nspasteboardreading), and [NSPasteboardWriting](https://developer.apple.com/documentation/appkit/nspasteboardwriting) APIs introduced in OS X v10.6 use UTIs to specify representation types. Over time, Cocoa will be moving away from the old pboard types, and towards using UTIs exclusively on the pasteboard.

On OS X v10.6 and later, you should use UTIs to identify pasteboard types. Most of the existing pasteboard type constants are not deprecated in OS X v10.6 (the exceptions are PICT and file content types), however they will be deprecated in the future.

The following table shows pasteboard types for which there are new UTIs. The table shows the OS X v10.5 and earlier constant, the OS X v10.6 constant, and the UTI string.

| Old Constant | New Constant | UTI String |
| --- | --- | --- |
| NSColorPboardType | NSPasteboardTypeColor | com.apple.cocoa.pasteboard.color |
| NSSoundPboardType | NSPasteboardTypeSound | com.apple.cocoa.pasteboard.sound |
| NSFontPboardType | NSPasteboardTypeFont | com.apple.cocoa.pasteboard.character-formatting |
| NSRulerPboardType | NSPasteboardTypeRuler | com.apple.cocoa.pasteboard.paragraph-formatting |
| NSTabularTextPboardType | NSPasteboardTypeTabularText | com.apple.cocoa.pasteboard.tabular-text |
| NSMultipleTextSelectionPboardType | NSPasteboardTypeMultipleTextSelection | com.apple.cocoa.pasteboard.multiple-text-selection |
| NSFindPanelSearchOptionsPboardType | NSPasteboardTypeFindPanelSearchOptions | com.apple.cocoa.pasteboard.find-panel-search-options |

The following table shows pasteboard types for which there are existing UTIs. The table shows the OS X v10.5 and earlier constant (where there is one), the OS X v10.6 constant, and the UTI string.

| Old Constant | New Constant | UTI String |
| --- | --- | --- |
| NSStringPboardType | NSPasteboardTypeString | public.utf8-plain-text |
| NSPDFPboardType | NSPasteboardTypePDF | com.adobe.pdf |
| NSRTFPboardType | NSPasteboardTypeRTF | public.rtf |
| NSRTFDPboardType | NSPasteboardTypeRTFD | com.apple.flat-rtfd |
| NSTIFFPboardType | NSPasteboardTypeTIFF | public.tiff |
|  | NSPasteboardTypePNG | public.png |
| NSHTMLPboardType | NSPasteboardTypeHTML | public.html |

Some OS X v10.5 constants do not have corresponding constant definitions on OS X v10.6. The following table shows either their deprecation status or what you should use instead.

| Constant | Replacement/Comments |
| --- | --- |
| NSPICTPboardType | Deprecated in OS X v10.6 |
| NSFilesPromisePboardType | Use `(NSString *)kPasteboardTypeFileURLPromise` instead. |
| NSVCardPboardType | Use `(NSString *)kUTTypeVCard` instead. |
| NSPostScriptPboardType | Use `@"com.adobe.encapsulated-postscript"` instead. |
| NSInkTextPboardType | Use `(NSString *)kUTTypeInkText` instead. |
| NSURLPboardType | Use [writeObjects:](https://developer.apple.com/documentation/appkit/nspasteboard/1525945-writeobjects) to write `NSURL` objects directly to pasteboard. |
| NSFilenamesPboardType | Use [writeObjects:](https://developer.apple.com/documentation/appkit/nspasteboard/1525945-writeobjects) to write file `NSURL` objects directly to pasteboard. |

[Next](Document%20Revision%20History.md)[Previous](Custom%20Data.md)

