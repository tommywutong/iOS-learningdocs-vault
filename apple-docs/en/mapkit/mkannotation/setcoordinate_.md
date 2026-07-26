---
title: 'setCoordinate:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkannotation/setcoordinate:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotation/setcoordinate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotation/setcoordinate%3A.json'
content_hash: 'sha256:433b422aee6a32aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotation](../mkannotation.md)

# setCoordinate:

<sub>Instance Method</sub>

Sets the new center point of the annotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setCoordinate:(CLLocationCoordinate2D) newCoordinate;
```

## Parameters

- `newCoordinate` — The new center point for the annotation.

## Discussion

Annotations that support dragging should implement this method to update the position of the annotation.

If you implement this method, you must update the value of the coordinate in a key-value observing (KVO) compliant way. For more information on how to implement support for KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Position attributes

- [coordinate](coordinate.md) — The center point (specified as a map coordinate) of the annotation.
