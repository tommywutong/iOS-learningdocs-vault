---
title: 'init(cString:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/init(cstring:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/init(cstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/init%28cstring%3A%29.json'
content_hash: 'sha256:5f56b7c4345a33f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# init(cString:)

<sub>Initializer</sub>

Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(cString nullTerminatedUTF8: UnsafePointer<CChar>)
```

## Parameters

- `nullTerminatedUTF8` — A pointer to a sequence of contiguous, UTF-8 encoded bytes ending just before the first zero byte.
