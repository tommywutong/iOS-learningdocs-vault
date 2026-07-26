---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/range/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/range/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/hashvalue.json'
content_hash: 'sha256:79aa25533e74ece1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

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

## See Also

### Infrequently Used Functionality

- [init(uncheckedBounds:)](<init(uncheckedbounds_).md>) — Creates an instance with the given bounds.
