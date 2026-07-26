---
title: 'dataWithContentsOfFile:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithcontentsoffile:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsoffile:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithcontentsoffile%3A.json'
content_hash: 'sha256:97b14ba1edb9774f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithContentsOfFile:

<sub>Type Method</sub>

Creates a data object by reading every byte from the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithContentsOfFile:(NSString *) path;
```

## Parameters

- `path` — The absolute path of the file from which to read data.

## Discussion

This method returns `nil` if the data object could not be created. If you need to know the reason for failure, use [dataWithContentsOfFile:options:error:](datawithcontentsoffile_options_error_.md).

This method is equivalent to calling [dataWithContentsOfFile:options:error:](datawithcontentsoffile_options_error_.md) and passing no options.

A sample using this method can be found in [Working With Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## See Also

### Reading Data from a File

- [dataWithContentsOfFile:options:error:](datawithcontentsoffile_options_error_.md) — Creates a data object by reading every byte from the file at a given path.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
