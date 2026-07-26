---
title: 'encode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/singlevalueencodingcontainer/encode(_:)-82sdy'
source_url: 'https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-82sdy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevalueencodingcontainer/encode%28_%3A%29-82sdy.json'
content_hash: 'sha256:bf81846ad04d2bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SingleValueEncodingContainer](../singlevalueencodingcontainer.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes a single value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode(_ value: Int128) throws
```

## Parameters

- `value` — The value to encode.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

> [!info] Precondition
> May not be called after a previous `self.encode(_:)` call.
