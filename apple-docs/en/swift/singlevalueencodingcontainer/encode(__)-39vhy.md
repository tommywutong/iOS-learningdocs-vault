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
doc_path: '/documentation/swift/singlevalueencodingcontainer/encode(_:)-39vhy'
source_url: 'https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-39vhy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevalueencodingcontainer/encode%28_%3A%29-39vhy.json'
content_hash: 'sha256:9b10b393823429b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SingleValueEncodingContainer](../singlevalueencodingcontainer.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes a single value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: UInt64) throws
```

## Parameters

- `value` — The value to encode.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

> [!info] Precondition
> May not be called after a previous `self.encode(_:)` call.

## Default Implementations

### SingleValueEncodingContainer Implementations

- [encode(_:)](<encode(__)-5lw48.md>) — Encodes a single value of the given type.
- [encode(_:)](<encode(__)-6x0pw.md>) — Encodes a single value of the given type.
- [encode(_:)](<encode(__)-82sdy.md>) — Encodes a single value of the given type.
- [encode(_:)](<encode(__)-wjsd.md>) — Encodes a single value of the given type.
