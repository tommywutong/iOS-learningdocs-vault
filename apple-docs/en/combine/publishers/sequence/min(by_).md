---
title: 'min(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/min(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/min(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/min%28by%3A%29.json'
content_hash: 'sha256:8e6053bfbcbf4836'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# min(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func min(by areInIncreasingOrder: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher
```

## See Also

### Applying mathematical operations on elements

- [count()](<count()-5rrw2.md>)
- [count()](<count()-5hb52.md>)
- [count()](<count()-b8ct.md>)
- [max()](<max().md>)
- [max(by:)](<max(by_).md>)
- [min()](<min().md>)
