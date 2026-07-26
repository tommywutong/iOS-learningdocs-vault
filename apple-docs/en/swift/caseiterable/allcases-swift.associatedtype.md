---
title: AllCases
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/caseiterable/allcases-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swift/caseiterable/allcases-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/caseiterable/allcases-swift.associatedtype.json'
content_hash: 'sha256:470d3a40d84ca22d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CaseIterable](../caseiterable.md)

# AllCases

<sub>Associated Type</sub>

A type that can represent a collection of all values of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype AllCases : Collection = [Self] where Self == Self.AllCases.Element
```

## See Also

### Accessing Cases

- [allCases](allcases-swift.type.property.md) — A collection of all values of this type.
