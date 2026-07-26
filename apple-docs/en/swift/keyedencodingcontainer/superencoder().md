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
doc_path: /documentation/swift/keyedencodingcontainer/superencoder()
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/superencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/superencoder%28%29.json'
content_hash: 'sha256:838d9bbf0bc7ad47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# superEncoder()

<sub>Instance Method</sub>

Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func superEncoder() -> any Encoder
```

## Return Value

A new encoder to pass to `super.encode(to:)`.

## Discussion

Equivalent to calling `superEncoder(forKey:)` with `Key(stringValue: "super", intValue: 0)`.
