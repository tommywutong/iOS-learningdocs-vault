---
title: 'warning(_:)'
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/warning(_:)'
source_url: 'https://developer.apple.com/documentation/swift/warning(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/warning%28_%3A%29.json'
content_hash: 'sha256:25370b3de019c9c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# warning(_:)

<sub>Macro</sub>

Produces the given warning message during compilation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro warning(_ message: String)
```

## Overview

Compilation proceeds after emitting the message as a nonfatal warning.

## See Also

### Generating Compile-Time Diagnostics

- [error(_:)](<error(__).md>) — Emits the given message as a fatal error and terminates the compilation process.
