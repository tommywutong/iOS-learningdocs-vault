---
title: 'write(toFile:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/write(tofile:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/write(tofile:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/write%28tofile%3Aoptions%3A%29.json'
content_hash: 'sha256:8fbace463615a90f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# write(toFile:options:)

<sub>Instance Method</sub>

Writes the data object’s bytes to the file specified by a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(toFile path: String, options writeOptionsMask: NSData.WritingOptions = []) throws
```

## Parameters

- `path` — The location to which to write the receiver’s bytes.

- `writeOptionsMask` — A mask that specifies options for writing the data. Constant components are described in [WritingOptions](writingoptions.md).

## Discussion

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [FileHandle](../filehandle.md) instead. For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Writing Data to a File

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [- writeToURL:options:error:](<write(to_options_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [WritingOptions](writingoptions.md) — Options for methods used to write data objects.
