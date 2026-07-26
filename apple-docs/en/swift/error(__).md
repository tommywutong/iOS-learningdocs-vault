---
title: 'error(_:)'
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/error(_:)'
source_url: 'https://developer.apple.com/documentation/swift/error(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/error%28_%3A%29.json'
content_hash: 'sha256:e71235db91df9407'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# error(_:)

<sub>Macro</sub>

Emits the given message as a fatal error and terminates the compilation process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro error(_ message: String)
```

## Parameters

- `message` — The error message.

## See Also

### Generating Compile-Time Diagnostics

- [warning(_:)](<warning(__).md>) — Produces the given warning message during compilation.
