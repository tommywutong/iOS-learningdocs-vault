---
title: 'reduce(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/reduce(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/just/reduce(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/reduce%28_%3A_%3A%29.json'
content_hash: 'sha256:b2d290903872476c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# reduce(_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reduce<T>(_ initialResult: T, _ nextPartialResult: (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher
```

## See Also

### Reducing elements

- [collect()](<collect().md>)
- [ignoreOutput()](<ignoreoutput().md>)
- [tryReduce(_:_:)](<tryreduce(____).md>)
