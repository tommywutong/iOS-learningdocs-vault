---
title: 'init(contentsOfMappedFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdata/init(contentsofmappedfile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(contentsofmappedfile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28contentsofmappedfile%3A%29.json'
content_hash: 'sha256:73d03a5099d99c0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(contentsOfMappedFile:)

<sub>Initializer</sub>

Initializes a data object with the contents of the mapped file specified by a given path.

> [!warning] Deprecated
> Use -initWithContentsOfURL:options:error: and NSDataReadingMappedIfSafe or NSDataReadingMappedAlways instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfMappedFile path: String)
```

## Parameters

- `path` — The absolute path of the file from which to read data.

## Return Value

A data object initialized by reading into it the mapped file specified by `path`.

## See Also

### Reading Data from a File

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
