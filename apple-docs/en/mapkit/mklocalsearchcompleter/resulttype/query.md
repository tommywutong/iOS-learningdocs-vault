---
title: query
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/resulttype/query
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/resulttype/query'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/resulttype/query.json'
content_hash: 'sha256:54fa99b2f1a27da9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearchCompleter](../../mklocalsearchcompleter.md) · [ResultType](../resulttype.md)

# query

<sub>Type Property</sub>

A value that indicates that the search completer includes query completions in the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var query: MKLocalSearchCompleter.ResultType { get }
```

## Discussion

For example, the search string `cof` yields a completion for _coffee_.

## See Also

### Type properties

- [MKLocalSearchCompleterResultTypeAddress](address.md) — A value that indicates that the search completer includes address completions in the result.
- [MKLocalSearchCompleterResultTypePointOfInterest](pointofinterest.md) — A value that indicates that the search completer includes point-of-interest completions in the result.
- [MKLocalSearchCompleterResultTypePhysicalFeature](physicalfeature.md) — A value that indicates that the search completer includes physical feature completions in the result.
