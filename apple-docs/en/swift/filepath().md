---
title: filePath()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/filepath()
source_url: 'https://developer.apple.com/documentation/swift/filepath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/filepath%28%29.json'
content_hash: 'sha256:810ea6e75759f57a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# filePath()

<sub>Macro</sub>

Produces the complete path to the file in which the macro appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro filePath<T>() -> T where T : ExpressibleByStringLiteral
```

## Overview

Because `#fileID` doesn’t embed the full path to the source file, unlike `#filePath`, it gives you better privacy and reduces the size of the compiled binary. Avoid using `#filePath` outside of tests, build scripts, or other code that doesn’t become part of the shipping program.

This macro’s value can be changed by `#sourceLocation`, as described in [Line Control Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements#Line-Control-Statement) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## See Also

### Getting Source Location Information

- [file()](<file().md>) — Produces the path to the file in which it appears.
- [fileID()](<fileid().md>) — Produces a unique identifier for the source file in which the macro appears.
- [function()](<function().md>) — Produces the name of the declaration in which it appears.
- [line()](<line().md>) — Produces the line number on which it appears.
- [column()](<column().md>) — Produces the column number in which the macro begins.
