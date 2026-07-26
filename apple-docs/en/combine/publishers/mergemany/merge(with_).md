---
title: 'merge(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/mergemany/merge(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/mergemany/merge(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mergemany/merge%28with%3A%29.json'
content_hash: 'sha256:e2dcf6e2533b2c0b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MergeMany](../mergemany.md)

# merge(with:)

<sub>Instance Method</sub>

Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge(with other: Upstream) -> Publishers.MergeMany<Upstream>
```

## Parameters

- `other` — Another publisher of this publisher’s type.

## Return Value

A publisher that emits an event when either upstream publisher emits an event.
