---
title: results
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/results
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/results'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/results.json'
content_hash: 'sha256:b4ba2c1949369256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# results

<sub>Instance Property</sub>

The most recently received search completions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var results: [MKLocalSearchCompletion] { get }
```

## Discussion

This property is `nil` initially. After a successful query, the search completer sets this property to the array of [MKLocalSearchCompletion](../mklocalsearchcompletion.md) objects that the query returns. Each new successful query replaces the previous value of this property.
