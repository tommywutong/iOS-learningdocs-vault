---
title: 'init(contentsOfURL:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdirections/request/init(contentsofurl:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/init(contentsofurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/init%28contentsofurl%3A%29.json'
content_hash: 'sha256:ec877d3f23ec5657'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# init(contentsOfURL:)

<sub>Initializer</sub>

Creates and returns a directions request object using the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOfURL url: URL)
```

## Parameters

- `url` — The URL provided to your app.

## Return Value

An initialized directions request object.

## Discussion

You should use the [+ isDirectionsRequestURL:](<isdirectionsrequest(__).md>) method to verify that the specified URL is of the correct format before calling this method to initialize the object.

## See Also

### Creating a directions request object

- [+ isDirectionsRequestURL:](<isdirectionsrequest(__).md>) — Returns a Boolean value that indicates whether the specified URL contains a directions request.
