---
title: 'encode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encode(_:)-4ehqa'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:)-4ehqa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encode%28_%3A%29-4ehqa.json'
content_hash: 'sha256:f1da2f3c5abf7d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: UInt128) throws
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
