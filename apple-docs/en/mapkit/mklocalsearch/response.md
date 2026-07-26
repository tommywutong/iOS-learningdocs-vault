---
title: MKLocalSearch.Response
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/response
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/response.json'
content_hash: 'sha256:b0a976d638fb6822'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# MKLocalSearch.Response

<sub>Class</sub>

The results from a map-based search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Response
```

## Overview

You don’t create instances of this class directly. After initiating a map search using an [MKLocalSearch](../mklocalsearch.md) object, MapKit passes an instance of this class to your completion handler.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Getting the search results

- [mapItems](response/mapitems.md) — An array of map items representing the search results.
- [boundingRegion](response/boundingregion.md) — The map region that encloses the returned search results.
