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
doc_path: '/documentation/combine/cancellable/store(in:)-35vnt'
source_url: 'https://developer.apple.com/documentation/combine/cancellable/store(in:)-35vnt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/cancellable/store%28in%3A%29-35vnt.json'
content_hash: 'sha256:1a66b31f4ac6c151'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Cancellable](../cancellable.md)

# store(in:)

<sub>Instance Method</sub>

Stores this cancellable instance in the specified collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func store<C>(in collection: inout C) where C : RangeReplaceableCollection, C.Element == AnyCancellable
```

## Parameters

- `collection` — The collection in which to store this [Cancellable](../cancellable.md).

## See Also

### Storing instances

- [store(in:)](<store(in_)-95sfl.md>) — Stores this cancellable instance in the specified set.
