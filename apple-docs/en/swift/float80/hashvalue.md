---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/float80/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/hashvalue.json'
content_hash: 'sha256:b3b0ff8985d334ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# hashValue

<sub>Instance Property</sub>

The hash value.

<sub>macOS</sub>

```swift
var hashValue: Int { get }
```

## Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> [!important] Important
> `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.
