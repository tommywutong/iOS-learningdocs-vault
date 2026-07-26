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
doc_path: '/documentation/swift/singlevalueencodingcontainer/encode(_:)-5kf5u'
source_url: 'https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-5kf5u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevalueencodingcontainer/encode%28_%3A%29-5kf5u.json'
content_hash: 'sha256:8ab96b33bfa2349d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SingleValueEncodingContainer](../singlevalueencodingcontainer.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes a single value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: UInt128) throws
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
