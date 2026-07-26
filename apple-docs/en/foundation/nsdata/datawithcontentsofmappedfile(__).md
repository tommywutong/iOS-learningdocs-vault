---
title: 'dataWithContentsOfMappedFile(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdata/datawithcontentsofmappedfile(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofmappedfile(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithcontentsofmappedfile%28_%3A%29.json'
content_hash: 'sha256:9d51e172dcb63c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithContentsOfMappedFile(_:)

<sub>Type Method</sub>

Creates a data object from the mapped file at a given path.

> [!warning] Deprecated
> Use +dataWithContentsOfURL:options:error: and NSDataReadingMappedIfSafe or NSDataReadingMappedAlways instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func dataWithContentsOfMappedFile(_ path: String) -> Any?
```

## Parameters

- `path` — The absolute path of the file from which to read data.

## Discussion

This method returns `nil` if the data object could not be created

Because of file mapping restrictions, this method should only be used if the file is guaranteed to exist for the duration of the data object’s existence. It is generally safer to use the [dataWithContentsOfFile:](datawithcontentsoffile_.md) method.

This methods assumes mapped files are available from the underlying operating system. A mapped file uses virtual memory techniques to avoid copying pages of the file into memory until they are actually needed.

## See Also

### Reading Data from a File

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
