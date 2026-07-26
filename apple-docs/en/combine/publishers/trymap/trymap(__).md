---
title: 'tryMap(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/trymap/trymap(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/trymap/trymap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trymap/trymap%28_%3A%29.json'
content_hash: 'sha256:85587a670a51f2ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryMap](../trymap.md)

# tryMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryMap<T>(_ transform: @escaping (Output) throws -> T) -> Publishers.TryMap<Upstream, T>
```
