---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/uint128/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/hashvalue.json'
content_hash: 'sha256:89aefad418664a50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# hashValue

<sub>Instance Property</sub>

The hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hashValue: Int { get }
```

## Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> [!important] Important
> `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.
