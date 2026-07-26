---
title: forCurrentLocation()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/forcurrentlocation()
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/forcurrentlocation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/forcurrentlocation%28%29.json'
content_hash: 'sha256:64ed689419b21513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# forCurrentLocation()

<sub>Type Method</sub>

Creates and returns a singleton map item object representing the user’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func forCurrentLocation() -> MKMapItem
```

## Return Value

An `MKMapItem` object representing the user’s location.

## Discussion

For privacy reasons, and because the user’s location can change, the map item that this method returns doesn’t contain any coordinate data. When you need the actual location of the user, use the Core Location framework to retrieve it.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating map items

- [- initWithPlacemark:](<init(placemark_).md>) — Creates and returns a map item object using the specified placemark object. _(deprecated)_
