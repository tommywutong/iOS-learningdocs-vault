---
title: 'filter(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/filter/filter(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/filter/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/filter/filter%28_%3A%29.json'
content_hash: 'sha256:28b5712e5378910b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Filter](../filter.md)

# filter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: @escaping (Publishers.Filter<Upstream>.Output) -> Bool) -> Publishers.Filter<Upstream>
```

## See Also

### Filtering elements

- [tryFilter(_:)](<tryfilter(__).md>)
