---
title: 'tryFilter(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/filter/tryfilter(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/filter/tryfilter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/filter/tryfilter%28_%3A%29.json'
content_hash: 'sha256:aa168ac3e4f3e03b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Filter](../filter.md)

# tryFilter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryFilter(_ isIncluded: @escaping (Publishers.Filter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>)
