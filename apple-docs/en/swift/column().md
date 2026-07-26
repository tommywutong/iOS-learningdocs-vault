---
title: column()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/column()
source_url: 'https://developer.apple.com/documentation/swift/column()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/column%28%29.json'
content_hash: 'sha256:dc5c5d115f6a66cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# column()

<sub>Macro</sub>

Produces the column number in which the macro begins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro column<T>() -> T where T : ExpressibleByIntegerLiteral
```

## See Also

### Getting Source Location Information

- [file()](<file().md>) — Produces the path to the file in which it appears.
- [fileID()](<fileid().md>) — Produces a unique identifier for the source file in which the macro appears.
- [filePath()](<filepath().md>) — Produces the complete path to the file in which the macro appears.
- [function()](<function().md>) — Produces the name of the declaration in which it appears.
- [line()](<line().md>) — Produces the line number on which it appears.
