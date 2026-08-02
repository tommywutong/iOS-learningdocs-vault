---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbDataTypes.html
archived_at: '2026-07-15T07:13:52.433452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Reading%20and%20Writing%20Font%20Data.md)[Previous](Named%20Pasteboards.md)

# Data Types

Data can be placed in the pasteboard server in more than one representation. For example, an image might be provided both in Tag Image File Format (TIFF) and as encapsulated PostScript code (EPS). Multiple representations give pasting applications the option of choosing which data type to use. In general, an application taking data from the pasteboard should choose the richest representation it can handle—rich text over plain ASCII, for example. An application putting data in the pasteboard should promise to supply it in as many data types as possible, so that as many different applications as possible can use it.

Filtering services (see [Filter Services](Filter%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dmlkcijbuorkdiraq)) transform the data from one representation to another. Typically, these services are not invoked until data are read from a pasteboard.

Data types are identified by string objects containing the full type name. These global variables identify the string objects for the standard pasteboard types:

|  |  |
| --- | --- |
| `NSColorPboardType` |  |
| `NSInkTextPboardType` |  |
| `NSFileContentsPboardType` |  |
| `NSFilesPromisePboardType` |  |
| [NSCreateFileContentsPboardType](https://developer.apple.com/documentation/appkit/1525733-nscreatefilecontentspboardtype) |  |
| [NSCreateFilenamePboardType](https://developer.apple.com/documentation/appkit/1528662-nscreatefilenamepboardtype) |  |
| `NSFilenamesPboardType` |  |
| [NSFindPanelSearchOptionsPboardType](https://developer.apple.com/documentation/appkit/nsfindpanelsearchoptionspboardtype) |  |
| `NSFontPboardType` |  |
| `NSHTMLPboardType` |  |
| `NSPDFPboardType` |  |
| `NSPICTPboardType` |  |
| `NSPostScriptPboardType` |  |
| `NSRTFPboardType` |  |
| `NSRTFDPboardType` |  |
| `NSRulerPboardType` |  |
| `NSSoundPboardType` |  |
| `NSStringPboardType` |  |
| `NSTabularTextPboardType` |  |
| `NSTIFFPboardType` |  |
| `NSURLPboardType` |  |
| `NSVCardPboardType` |  |
| `WebArchivePboardType` |  |

Typically, data is written to the pasteboard using `setData:forType:` and read using `dataForType:`. Some of these types can only be written with certain methods. For instance, `NSFilenamesPboardType`’s form is an array of `NSString` objects and requires special handling. Use these methods to write these types:

| Type | Writing Method | Reading Method |
| --- | --- | --- |
| `NSColorPboardType` | `NSColor` class methods | `NSColor` class methods |
| `NSFileContentsPboardType` | `writeFileContents:` | `readFileContentsType:toFile:` |
| `NSFilenamesPboardType` | `setPropertyList:forType:` | `propertyListForType:` |
| `NSStringPboardType` | `setString:forType:` | `stringForType:` |
| `NSURLPboardType` | `writeToPasteboard:` (`NSURL`) | `URLFromPasteboard:` (`NSURL`) |
| NSFontPboardType | See [Writing Font Data](Reading%20and%20Writing%20Font%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjwfvjvomq) | See [Reading Font Data](Reading%20and%20Writing%20Font%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjwfvjvomy) |

Types other than those listed above can also be used. For example, your application may keep data in a private format that is richer than any of the existing types. That format can also be used as a pasteboard type.

[Next](Reading%20and%20Writing%20Font%20Data.md)[Previous](Named%20Pasteboards.md)

