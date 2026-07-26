---
title: delegate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/delegate
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/delegate.json'
content_hash: 'sha256:21d62ed3067c7455'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# delegate

<sub>Instance Property</sub>

The object that receives the completion results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any MKLocalSearchCompleterDelegate)? { get set }
```

## Discussion

You must provide a delegate object to receive completion results and to handle any errors that might occur. For more information about the methods of the delegate protocol, see [MKLocalSearchCompleterDelegate](../mklocalsearchcompleterdelegate.md).

## See Also

### Receiving the search results

- [MKLocalSearchCompleterDelegate](../mklocalsearchcompleterdelegate.md) — Methods the delegate calls with search completion data.
