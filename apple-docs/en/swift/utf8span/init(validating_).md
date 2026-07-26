---
title: 'init(validating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/init(validating:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/init(validating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/init%28validating%3A%29.json'
content_hash: 'sha256:6934d8de84c9f5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# init(validating:)

<sub>Initializer</sub>

Creates a UTF8Span containing `codeUnits`. Validates that the input is valid UTF-8, otherwise throws an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(validating codeUnits: consuming Span<UInt8>) throws(UTF8.ValidationError)
```

## Discussion

The resulting UTF8Span has the same lifetime constraints as `codeUnits`.

> [!abstract] Complexity
> O(n)
