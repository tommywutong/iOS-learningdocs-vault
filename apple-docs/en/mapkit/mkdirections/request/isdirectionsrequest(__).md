---
title: 'isDirectionsRequest(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdirections/request/isdirectionsrequest(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/isdirectionsrequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/isdirectionsrequest%28_%3A%29.json'
content_hash: 'sha256:7a400c0dd05b4591'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# isDirectionsRequest(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the specified URL contains a directions request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isDirectionsRequest(_ url: URL) -> Bool
```

## Parameters

- `url` — The URL the system provides  to your app.

## Return Value

[true](../../../swift/true.md) if the URL contains a directions request that your app needs to display to the user, or [false](../../../swift/false.md) if it doesn’t.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a directions request object

- [init(contentsOfURL:)](<init(contentsofurl_).md>) — Creates and returns a directions request object using the specified URL.
