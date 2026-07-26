---
title: 'encodeConditional(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encodeconditional(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodeconditional(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encodeconditional%28_%3A%29.json'
content_hash: 'sha256:df8204f5d9ac2a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encodeConditional(_:)

<sub>Instance Method</sub>

Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeConditional<T>(_ object: T) throws where T : AnyObject, T : Encodable
```

## Parameters

- `object` — The object to encode.

## Discussion

For encoders which don’t support this feature, the default implementation encodes the given object unconditionally.

For formats which don’t support this feature, the default implementation encodes the given object unconditionally.

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Default Implementations

### UnkeyedEncodingContainer Implementations

- [encodeConditional(_:)](<encodeconditional(__)-4trvc.md>) — Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
