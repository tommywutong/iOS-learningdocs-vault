---
title: fileID()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/fileid()
source_url: 'https://developer.apple.com/documentation/swift/fileid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fileid%28%29.json'
content_hash: 'sha256:b55e32e198206127'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# fileID()

<sub>Macro</sub>

Produces a unique identifier for the source file in which the macro appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro fileID<T>() -> T where T : ExpressibleByStringLiteral
```

## Overview

The unique identifier has the form _module_/_file_, where _file_ is the name of the file in which the expression appears and _module_ is the name of the module that this file is part of.

Because `#fileID` doesn’t embed the full path to the source file, unlike `#filePath`, it gives you better privacy and reduces the size of the compiled binary.

Note: To parse a `#fileID` expression, read the module name as the text before the first slash (`/`) and the filename as the text after the last slash. In future versions of Swift, the string might contain multiple slashes, such as `MyModule/some/disambiguation/MyFile.swift`.

This macro’s value can be changed by `#sourceLocation`, as described in [Line Control Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements#Line-Control-Statement) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## See Also

### Getting Source Location Information

- [file()](<file().md>) — Produces the path to the file in which it appears.
- [filePath()](<filepath().md>) — Produces the complete path to the file in which the macro appears.
- [function()](<function().md>) — Produces the name of the declaration in which it appears.
- [line()](<line().md>) — Produces the line number on which it appears.
- [column()](<column().md>) — Produces the column number in which the macro begins.
