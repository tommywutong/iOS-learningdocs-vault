---
title: 'max(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/max(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/max(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/max%28by%3A%29.json'
content_hash: 'sha256:25b4baa94cb36cd4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# max(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func max(by areInIncreasingOrder: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher
```

## See Also

### Applying mathematical operations on elements

- [count()](<count()-5rrw2.md>)
- [count()](<count()-5hb52.md>)
- [count()](<count()-b8ct.md>)
- [max()](<max().md>)
- [min()](<min().md>)
- [min(by:)](<min(by_).md>)
