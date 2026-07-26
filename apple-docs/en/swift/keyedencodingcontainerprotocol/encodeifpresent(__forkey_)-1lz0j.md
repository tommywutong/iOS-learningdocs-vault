---
title: 'encodeIfPresent(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1lz0j'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1lz0j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent%28_%3Aforkey%3A%29-1lz0j.json'
content_hash: 'sha256:4500f63a7c864110'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# encodeIfPresent(_:forKey:)

<sub>Instance Method</sub>

Encodes the given value for the given key if it is not `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeIfPresent(_ value: UInt16?, forKey key: Self.Key) throws
```

## Parameters

- `value` — The value to encode.

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.
