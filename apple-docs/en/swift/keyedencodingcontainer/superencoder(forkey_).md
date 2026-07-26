---
title: 'superEncoder(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/superencoder(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/superencoder(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/superencoder%28forkey%3A%29.json'
content_hash: 'sha256:8aa9b897ea305567'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# superEncoder(forKey:)

<sub>Instance Method</sub>

Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func superEncoder(forKey key: KeyedEncodingContainer<K>.Key) -> any Encoder
```

## Parameters

- `key` — The key to encode `super` for.

## Return Value

A new encoder to pass to `super.encode(to:)`.
