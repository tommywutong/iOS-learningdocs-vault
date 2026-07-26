---
title: collect()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/sequence/collect()
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/collect()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/collect%28%29.json'
content_hash: 'sha256:a599f398ac3a9d86'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# collect()

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher
```

## See Also

### Reducing elements

- [ignoreOutput()](<ignoreoutput().md>)
- [reduce(_:_:)](<reduce(____).md>)
- [tryReduce(_:_:)](<tryreduce(____).md>)
