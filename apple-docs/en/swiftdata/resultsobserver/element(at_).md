---
title: 'element(at:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultsobserver/element(at:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/element(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/element%28at%3A%29.json'
content_hash: 'sha256:e9dac2a561ed4e7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# element(at:)

<sub>Instance Method</sub>

Returns the element at the given index path in the sectioned results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func element(at indexPath: IndexPath) -> Element?
```

## Parameters

- `indexPath` — An index path where `indexPath[0]` is the section index and `indexPath[1]` is the item index within that section.

## Return Value

The element at the given index path, or `nil` if [sections](sections.md) is `nil` or the index path is out of bounds.

## See Also

### Accessing observer results

- [results](results.md) — The current collection of fetched models matching the fetch criteria. _(beta)_
- [indexPath(for:)](<indexpath(for_).md>) — Returns the index path of the given element within the sectioned results. _(beta)_
