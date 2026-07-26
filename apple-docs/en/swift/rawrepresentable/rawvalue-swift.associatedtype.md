---
title: RawValue
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rawrepresentable/rawvalue-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable/rawvalue-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable/rawvalue-swift.associatedtype.json'
content_hash: 'sha256:dad93f73cf59f046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawRepresentable](../rawrepresentable.md)

# RawValue

<sub>Associated Type</sub>

The raw type that can be used to represent all values of the conforming type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype RawValue
```

## Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

### Accessing the Raw Value

- [rawValue](rawvalue-swift.property.md) — The corresponding value of the raw type.
