---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbFilters.html
archived_at: '2026-07-15T07:13:52.932755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Providing%20a%20Filter%20Service.md)[Previous](Reading%20and%20Writing%20RTFD%20Data.md)

# Filter Services

Filter services (see [System Services](../Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)) provide a way to extend the types of data `NSPasteboard` can provide to applications. In addition to the data types explicitly declared for a pasteboard, you can request the data in a type to which a filter service can convert any of the declared types. Files and `NSData` objects can be converted as well using filters.

The `NSPasteboard` class uses filter services when you invoke one of the following methods:

```objc
+ (NSArray *)typesFilterableTo:(NSString *)type
+ (NSPasteboard *)pasteboardByFilteringFile:(NSString *)filename
+ (NSPasteboard *)pasteboardByFilteringData:(NSData *)data ofType:(NSString *)type
+ (NSPasteboard *)pasteboardByFilteringTypesInPasteboard:(NSPasteboard *)pboard
```

The first returns an array of all the data types which can be converted to _type_. The last three return pasteboards with data that is filtered into all types derivable from the current types using available filter services. Filter services are not invoked, and the data converted, until data are requested from the pasteboard, so these methods are reasonably inexpensive.

Because filter services commonly translate data from unknown file formats into known formats, you need a way of dynamically specifying pasteboard types. The filter services and pasteboard facilities define types based on file extensions and HFS file types with these functions:

```
NSString *NSCreateFilenamePboardType(NSString *fileType)
NSString *NSCreateFileContentsPboardType(NSString *fileType)
NSString *NSGetFileType(NSString *pboardType)
NSArray *NSGetFileTypes(NSArray *pboardTypes)
NSString *NSFileTypeForHFSTypeCode(OSType hfsFileTypeCode)
OSType NSHFSTypeCodeFromFileType(NSString *fileTypeString)
```

The _fileType_ argument is either a file extension, minus the period (for example, “`eps`” or “`tiff`”), or an HFS file type encoded with the `NSFileTypeForHFSTypeCode` function (for example, “`‘TEXT’`” or “`‘MooV’`”). You create pasteboard type strings with the first two functions, and get file types (extensions or encoded HFS types) from pasteboard type strings with the second two functions. The last two functions convert between HFS file types (`OSType`) and encoded HFS type strings.

[Next](Providing%20a%20Filter%20Service.md)[Previous](Reading%20and%20Writing%20RTFD%20Data.md)

