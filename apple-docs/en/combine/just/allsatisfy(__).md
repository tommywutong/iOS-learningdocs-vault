---
title: 'allSatisfy(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/allsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/allsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/allsatisfy%28_%3A%29.json'
content_hash: 'sha256:5c6110ae0cf633da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# allSatisfy(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allSatisfy(_ predicate: (Output) -> Bool) -> Just<Bool>
```

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>)
- [contains(where:)](<contains(where_).md>)
- [tryContains(where:)](<trycontains(where_).md>)
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>)
