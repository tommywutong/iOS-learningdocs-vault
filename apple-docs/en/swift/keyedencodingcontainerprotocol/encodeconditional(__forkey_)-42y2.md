---
title: 'encodeConditional(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/encodeconditional(_:forkey:)-42y2'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encodeconditional(_:forkey:)-42y2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/encodeconditional%28_%3Aforkey%3A%29-42y2.json'
content_hash: 'sha256:d0f4d79d1db51a5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# encodeConditional(_:forKey:)

<sub>Instance Method</sub>

Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeConditional<T>(_ object: T, forKey key: Self.Key) throws where T : AnyObject, T : Encodable
```

## Parameters

- `object` — The object to encode.

- `key` — The key to associate the object with.

## Discussion

For encoders which don’t support this feature, the default implementation encodes the given object unconditionally.

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.
