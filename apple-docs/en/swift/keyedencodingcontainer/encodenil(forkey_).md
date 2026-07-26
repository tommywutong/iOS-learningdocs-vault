---
title: 'encodeNil(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encodenil(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodenil(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encodenil%28forkey%3A%29.json'
content_hash: 'sha256:35c8e7a93019d1cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encodeNil(forKey:)

<sub>Instance Method</sub>

Encodes a null value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeNil(forKey key: KeyedEncodingContainer<K>.Key) throws
```

## Parameters

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if a null value is invalid in the current context for this format.
