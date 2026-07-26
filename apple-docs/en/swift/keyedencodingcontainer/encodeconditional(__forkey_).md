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
doc_path: '/documentation/swift/keyedencodingcontainer/encodeconditional(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodeconditional(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encodeconditional%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:552980de3d3f0e16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encodeConditional(_:forKey:)

<sub>Instance Method</sub>

Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeConditional<T>(_ object: T, forKey key: KeyedEncodingContainer<K>.Key) throws where T : AnyObject, T : Encodable
```

## Parameters

- `object` — The object to encode.

- `key` — The key to associate the object with.

## Discussion

For encoders which don’t support this feature, the default implementation encodes the given object unconditionally.

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.
