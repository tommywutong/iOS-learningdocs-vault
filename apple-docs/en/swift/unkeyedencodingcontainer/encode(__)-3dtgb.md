---
title: 'encode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encode(_:)-3dtgb'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:)-3dtgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encode%28_%3A%29-3dtgb.json'
content_hash: 'sha256:ad5525ddc3b5fea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: UInt) throws
```

## Parameters

- `value` — The value to encode.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Default Implementations

### UnkeyedEncodingContainer Implementations

- [encode(_:)](<encode(__)-7suq1.md>) — Encodes the given value.
- [encode(_:)](<encode(__)-8m4kj.md>) — Encodes the given value.
