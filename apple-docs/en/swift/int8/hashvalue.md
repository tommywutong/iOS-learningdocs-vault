---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/int8/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/hashvalue.json'
content_hash: 'sha256:ef212ae1000bc472'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

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
