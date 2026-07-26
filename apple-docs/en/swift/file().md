---
title: file()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/file()
source_url: 'https://developer.apple.com/documentation/swift/file()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/file%28%29.json'
content_hash: 'sha256:a3f497553750eb04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# file()

<sub>Macro</sub>

Produces the path to the file in which it appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro file<T>() -> T where T : ExpressibleByStringLiteral
```

## Overview

The string value from `#file` depends on the language version, to enable migration from the old `#filePath` behavior to the new `#fileID` behavior. Currently, `#file` has the same value as `#filePath`. In a future version of Swift, `#file` will have the same value as `#fileID` instead. To adopt the future behavior, replace `#file` with `#fileID` or `#filePath` as appropriate.

This macro’s value can be changed by `#sourceLocation`, as described in [Line Control Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements#Line-Control-Statement) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## See Also

### Getting Source Location Information

- [fileID()](<fileid().md>) — Produces a unique identifier for the source file in which the macro appears.
- [filePath()](<filepath().md>) — Produces the complete path to the file in which the macro appears.
- [function()](<function().md>) — Produces the name of the declaration in which it appears.
- [line()](<line().md>) — Produces the line number on which it appears.
- [column()](<column().md>) — Produces the column number in which the macro begins.
