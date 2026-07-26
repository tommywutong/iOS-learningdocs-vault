---
title: 'dataWithContentsOfFile:options:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithcontentsoffile:options:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsoffile:options:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithcontentsoffile%3Aoptions%3Aerror%3A.json'
content_hash: 'sha256:3cc48807e54562a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithContentsOfFile:options:error:

<sub>Type Method</sub>

Creates a data object by reading every byte from the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithContentsOfFile:(NSString *) path options:(NSDataReadingOptions) readOptionsMask error:(NSError **) errorPtr;
```

## Parameters

- `path` — The absolute path of the file from which to read data.

- `readOptionsMask` — A mask that specifies options for reading the data. Constant components are described in [ReadingOptions](readingoptions.md).

- `errorPtr` — If an error occurs, upon return contains an error object that describes the problem.

## Discussion

This method returns `nil` if the data object could not be created. In this case, `errorPtr` will contain an [NSError](../nserror.md) indicating the problem.

## See Also

### Reading Data from a File

- [dataWithContentsOfFile:](datawithcontentsoffile_.md) — Creates a data object by reading every byte from the file at a given path.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
