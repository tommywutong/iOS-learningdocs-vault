---
title: 'init(naturalLanguageQuery:region:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalsearch/request/init(naturallanguagequery:region:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request/init(naturallanguagequery:region:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request/init%28naturallanguagequery%3Aregion%3A%29.json'
content_hash: 'sha256:3efe76ece668cc20'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Request](../request.md)

# init(naturalLanguageQuery:region:)

<sub>Initializer</sub>

Initializes and returns a local search request based on the provided string and region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(naturalLanguageQuery: String, region: MKCoordinateRegion)
```

## Parameters

- `naturalLanguageQuery` — A string containing the desired search item.

- `region` — A map region that provides a hint as to where to search.

## See Also

### Initializing a natural language search request

- [- initWithNaturalLanguageQuery:](<init(naturallanguagequery_).md>) — Initializes and returns a local search request based on the provided string.
