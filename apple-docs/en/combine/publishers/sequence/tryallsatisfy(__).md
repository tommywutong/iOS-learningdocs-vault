---
title: 'tryAllSatisfy(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/tryallsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/tryallsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/tryallsatisfy%28_%3A%29.json'
content_hash: 'sha256:3c1711a92cb06dfe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# tryAllSatisfy(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryAllSatisfy(_ predicate: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>)
- [contains(where:)](<contains(where_).md>)
- [tryContains(where:)](<trycontains(where_).md>)
- [allSatisfy(_:)](<allsatisfy(__).md>)
