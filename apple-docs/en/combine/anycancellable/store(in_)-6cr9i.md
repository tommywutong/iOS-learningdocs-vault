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
doc_path: '/documentation/combine/anycancellable/store(in:)-6cr9i'
source_url: 'https://developer.apple.com/documentation/combine/anycancellable/store(in:)-6cr9i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anycancellable/store%28in%3A%29-6cr9i.json'
content_hash: 'sha256:47212d38600f78a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AnyCancellable](../anycancellable.md)

# store(in:)

<sub>Instance Method</sub>

Stores this type-erasing cancellable instance in the specified collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func store<C>(in collection: inout C) where C : RangeReplaceableCollection, C.Element == AnyCancellable
```

## Parameters

- `collection` — The collection in which to store this [AnyCancellable](../anycancellable.md).

## See Also

### Storing instances

- [store(in:)](<store(in_)-3hyxs.md>) — Stores this type-erasing cancellable instance in the specified set.
