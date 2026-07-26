---
title: 'completer(_:didFailWithError:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalsearchcompleterdelegate/completer(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/completer(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleterdelegate/completer%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:8c89e68e961b8d0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleterDelegate](../mklocalsearchcompleterdelegate.md)

# completer(_:didFailWithError:)

<sub>Instance Method</sub>

Tells the method when the specified search completer is unable to generate a list of search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func completer(_ completer: MKLocalSearchCompleter, didFailWithError error: any Error)
```

## Parameters

- `completer` — The search completer object reporting the error.

- `error` — The error object containing the reason for the failure.

## Discussion

Use this object to process any errors that occur while generating search results. Even when an error occurs, the search completer starts a new search if it already has a new search string. Depending on the error, you might do nothing or let the user know that you were unable to obtain a list of search completions.

## See Also

### Getting the search results

- [- completerDidUpdateResults:](<completerdidupdateresults(__).md>) — Tells the method when the specified search completer updates its array of search completions.
