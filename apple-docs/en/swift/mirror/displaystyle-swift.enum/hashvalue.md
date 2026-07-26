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
doc_path: /documentation/swift/mirror/displaystyle-swift.enum/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/mirror/displaystyle-swift.enum/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/displaystyle-swift.enum/hashvalue.json'
content_hash: 'sha256:213b38f3cbeda2aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Mirror](../../mirror.md) · [DisplayStyle](../displaystyle-swift.enum.md)

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
