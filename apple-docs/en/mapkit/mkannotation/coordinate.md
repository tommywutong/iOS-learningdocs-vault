---
title: coordinate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotation/coordinate
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotation/coordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotation/coordinate.json'
content_hash: 'sha256:2d391c75c52a7727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotation](../mkannotation.md)

# coordinate

<sub>Instance Property</sub>

The center point (specified as a map coordinate) of the annotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var coordinate: CLLocationCoordinate2D { get }
```

## Discussion

Your implementation of this property must be key-value observing (KVO) compliant. For more information on how to implement support for KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
