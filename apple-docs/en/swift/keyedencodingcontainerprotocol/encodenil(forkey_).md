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
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/encodenil(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encodenil(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/encodenil%28forkey%3A%29.json'
content_hash: 'sha256:b75fd2265fb37829'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# encodeNil(forKey:)

<sub>Instance Method</sub>

Encodes a null value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeNil(forKey key: Self.Key) throws
```

## Parameters

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if a null value is invalid in the current context for this format.
