---
title: 'tryReduce(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/tryreduce(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/tryreduce(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/tryreduce%28_%3A_%3A%29.json'
content_hash: 'sha256:9b15b208da3b8b6e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# tryReduce(_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryReduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher
```

## See Also

### Reducing elements

- [collect()](<collect().md>)
- [ignoreOutput()](<ignoreoutput().md>)
- [reduce(_:_:)](<reduce(____).md>)
