---
title: 'tryContains(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/trycontains(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/trycontains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/trycontains%28where%3A%29.json'
content_hash: 'sha256:0be6495203da10bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# tryContains(where:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryContains(where predicate: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>)
- [contains(where:)](<contains(where_).md>)
- [allSatisfy(_:)](<allsatisfy(__).md>)
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>)
