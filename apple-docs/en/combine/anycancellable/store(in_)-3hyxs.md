---
title: 'store(in:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/anycancellable/store(in:)-3hyxs'
source_url: 'https://developer.apple.com/documentation/combine/anycancellable/store(in:)-3hyxs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anycancellable/store%28in%3A%29-3hyxs.json'
content_hash: 'sha256:a1b0cdc5628b0d47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AnyCancellable](../anycancellable.md)

# store(in:)

<sub>Instance Method</sub>

Stores this type-erasing cancellable instance in the specified set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func store(in set: inout Set<AnyCancellable>)
```

## Parameters

- `set` — The set in which to store this [AnyCancellable](../anycancellable.md).

## See Also

### Storing instances

- [store(in:)](<store(in_)-6cr9i.md>) — Stores this type-erasing cancellable instance in the specified collection.
