---
title: superEncoder()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyedencodingcontainer/superencoder()
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/superencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/superencoder%28%29.json'
content_hash: 'sha256:34638be11474b2e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# superEncoder()

<sub>Instance Method</sub>

Encodes a nested container and returns an `Encoder` instance for encoding `super` into that container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func superEncoder() -> any Encoder
```

## Return Value

A new encoder to pass to `super.encode(to:)`.
