---
title: results
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/resultsobserver/results
source_url: 'https://developer.apple.com/documentation/swiftdata/resultsobserver/results'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultsobserver/results.json'
content_hash: 'sha256:e5560ba4632ef6fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsObserver](../resultsobserver.md)

# results

<sub>Instance Property</sub>

The current collection of fetched models matching the fetch criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var results: FetchResultsCollection<Element> { get set }
```

## Discussion

This property is updated automatically when relevant changes occur in the model context. As an `@Observable` property, SwiftUI views that read this value will automatically refresh when the results change.

## See Also

### Accessing observer results

- [element(at:)](<element(at_).md>) — Returns the element at the given index path in the sectioned results. _(beta)_
- [indexPath(for:)](<indexpath(for_).md>) — Returns the index path of the given element within the sectioned results. _(beta)_
