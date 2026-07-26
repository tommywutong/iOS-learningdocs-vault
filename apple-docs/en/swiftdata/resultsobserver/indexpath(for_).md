---
title: 'indexPath(for:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultsobserver/indexpath(for:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/indexpath(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/indexpath%28for%3A%29.json'
content_hash: 'sha256:cea28924afe2027e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# indexPath(for:)

<sub>Instance Method</sub>

Returns the index path of the given element within the sectioned results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func indexPath(for element: Element) -> IndexPath?
```

## Parameters

- `element` — An element to locate within the sectioned results.

## Return Value

An index path where `[0]` is the section index and `[1]` is the item index, or `nil` if the object is not found or [sections](sections.md) is `nil`.

## See Also

### Accessing observer results

- [results](results.md) — The current collection of fetched models matching the fetch criteria. _(beta)_
- [element(at:)](<element(at_).md>) — Returns the element at the given index path in the sectioned results. _(beta)_
