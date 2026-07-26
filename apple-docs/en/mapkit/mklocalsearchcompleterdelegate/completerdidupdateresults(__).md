---
title: 'completerDidUpdateResults(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalsearchcompleterdelegate/completerdidupdateresults(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/completerdidupdateresults(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleterdelegate/completerdidupdateresults%28_%3A%29.json'
content_hash: 'sha256:fa51932508e681da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleterDelegate](../mklocalsearchcompleterdelegate.md)

# completerDidUpdateResults(_:)

<sub>Instance Method</sub>

Tells the method when the specified search completer updates its array of search completions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func completerDidUpdateResults(_ completer: MKLocalSearchCompleter)
```

## Parameters

- `completer` — The search completer object with updated results.

## Discussion

After receiving results from a query, the search completer updates its [results](../mklocalsearchcompleter/results.md) property with the new [MKLocalSearchCompletion](../mklocalsearchcompletion.md) objects and calls this method. Use this method to update your app’s interface based on the new search results. For example, you might update a table that you use to display search results to the user.

## See Also

### Getting the search results

- [- completer:didFailWithError:](<completer(__didfailwitherror_).md>) — Tells the method when the specified search completer is unable to generate a list of search results.
