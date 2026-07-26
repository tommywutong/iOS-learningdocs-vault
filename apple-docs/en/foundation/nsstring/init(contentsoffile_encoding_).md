---
title: 'init(contentsOfFile:encoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(contentsoffile:encoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(contentsoffile:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28contentsoffile%3Aencoding%3A%29.json'
content_hash: 'sha256:9844a7a9df3a4be3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(contentsOfFile:encoding:)

<sub>Initializer</sub>

Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(contentsOfFile path: String, encoding enc: UInt) throws
```

## Parameters

- `path` — A path to a file.

- `enc` — The encoding of the file at `path`. For possible values, see [NSStringEncoding](../nsstringencoding.md).

## Return Value

An `NSString` object initialized by reading data from the file named by `path` using the encoding, `enc`. The returned object may be different from the original receiver. If the file can’t be opened or there is an encoding error, returns `nil`.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating and Initializing a String from a File

- [- initWithContentsOfFile:usedEncoding:error:](<init(contentsoffile_usedencoding_).md>) — Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.
