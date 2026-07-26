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
doc_path: '/documentation/combine/publishers/map/map(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/map/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/map/map%28_%3A%29.json'
content_hash: 'sha256:f2f160c398038bce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Map](../map.md)

# map(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T>(_ transform: @escaping (Output) -> T) -> Publishers.Map<Upstream, T>
```

## See Also

### Mapping elements

- [tryMap(_:)](<trymap(__).md>)
