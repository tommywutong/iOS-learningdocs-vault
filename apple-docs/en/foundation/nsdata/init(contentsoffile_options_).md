---
title: 'init(contentsOfFile:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(contentsoffile:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(contentsoffile:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28contentsoffile%3Aoptions%3A%29.json'
content_hash: 'sha256:d24fb113d4f6ae2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(contentsOfFile:options:)

<sub>Initializer</sub>

Initializes a data object with the content of the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOfFile path: String, options readOptionsMask: NSData.ReadingOptions = []) throws
```

## Parameters

- `path` — The absolute path of the file from which to read data.

- `readOptionsMask` — A mask that specifies options for reading the data. Constant components are described in [ReadingOptions](readingoptions.md).

## Return Value

A data object initialized by reading into it the data from the file specified by `path`.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading Data from a File

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a data object with the content of the file at a given path.
- [ReadingOptions](readingoptions.md) — Options for methods used to read data objects.
- [- initWithContentsOfMappedFile:](<init(contentsofmappedfile_).md>) — Initializes a data object with the contents of the mapped file specified by a given path. _(deprecated)_
- [+ dataWithContentsOfMappedFile:](<datawithcontentsofmappedfile(__).md>) — Creates a data object from the mapped file at a given path. _(deprecated)_
