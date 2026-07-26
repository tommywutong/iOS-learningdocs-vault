---
title: 'map(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/compactmap/map(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/compactmap/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/compactmap/map%28_%3A%29.json'
content_hash: 'sha256:1bfe30104bb5b465'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CompactMap](../compactmap.md)

# map(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T>(_ transform: @escaping (Output) -> T) -> Publishers.CompactMap<Upstream, T>
```

## See Also

### Mapping elements

- [compactMap(_:)](<compactmap(__).md>)
