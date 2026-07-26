---
title: 'encode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encode(_:forkey:)-99z4'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encode(_:forkey:)-99z4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encode%28_%3Aforkey%3A%29-99z4.json'
content_hash: 'sha256:d37fd0d1f7d811d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes the given value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: Int8, forKey key: KeyedEncodingContainer<K>.Key) throws
```

## Parameters

- `value` — The value to encode.

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.
