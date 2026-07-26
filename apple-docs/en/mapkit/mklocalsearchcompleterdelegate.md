---
title: MKLocalSearchCompleterDelegate
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleterdelegate
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleterdelegate.json'
content_hash: 'sha256:f37d020aafc43f8a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalSearchCompleterDelegate

<sub>Protocol</sub>

Methods the delegate calls with search completion data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MKLocalSearchCompleterDelegate : NSObjectProtocol
```

## Overview

You use this protocol when implementing an autocomplete solution for a map in your app. As the user types search terms, use an [MKLocalSearchCompleter](mklocalsearchcompleter.md) object to start searching for valid completions. The delegate you assign to that object needs to conform to this protocol. As it receives completions, the local search completer calls the methods of this protocol to deliver the results.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the search results

- [- completerDidUpdateResults:](<mklocalsearchcompleterdelegate/completerdidupdateresults(__).md>) — Tells the method when the specified search completer updates its array of search completions.
- [- completer:didFailWithError:](<mklocalsearchcompleterdelegate/completer(__didfailwitherror_).md>) — Tells the method when the specified search completer is unable to generate a list of search results.

## See Also

### Receiving the search results

- [delegate](mklocalsearchcompleter/delegate.md) — The object that receives the completion results.
