---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:adcbeed71a1d674e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initializes a data object with the content of the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfFile path: String)
```

## Parameters

- `path` — The absolute path of the file from which to read data.

## Return Value

A data object initialized by reading into it the data from the file specified by `path`.

## Discussion

This method is equivalent to [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) with no options.

## See Also

### Reading Data from a File

- [- initWithContentsOfFile:options:error:](<init(contentsoffile_options_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
