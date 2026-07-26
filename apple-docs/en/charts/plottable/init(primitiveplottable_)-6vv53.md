---
title: 'init(primitivePlottable:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/plottable/init(primitiveplottable:)-6vv53'
source_url: 'https://developer.apple.com/documentation/charts/plottable/init(primitiveplottable:)-6vv53'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottable/init%28primitiveplottable%3A%29-6vv53.json'
content_hash: 'sha256:8caf4f251b190af2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Plottable](../plottable.md)

# init(primitivePlottable:)

<sub>Initializer</sub>

Creates the plottable value for the underlying type, if any, that corresponds to the primitive plottable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init?(primitivePlottable: Self.PrimitivePlottable)
```

## Discussion

This initializer fails if there is no corresponding plottable value.
