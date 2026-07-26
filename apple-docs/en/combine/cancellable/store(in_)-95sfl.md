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
doc_path: '/documentation/combine/cancellable/store(in:)-95sfl'
source_url: 'https://developer.apple.com/documentation/combine/cancellable/store(in:)-95sfl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/cancellable/store%28in%3A%29-95sfl.json'
content_hash: 'sha256:78ce16e61a329142'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Cancellable](../cancellable.md)

# store(in:)

<sub>Instance Method</sub>

Stores this cancellable instance in the specified set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func store(in set: inout Set<AnyCancellable>)
```

## Parameters

- `set` — The set in which to store this [Cancellable](../cancellable.md).

## See Also

### Storing instances

- [store(in:)](<store(in_)-35vnt.md>) — Stores this cancellable instance in the specified collection.
