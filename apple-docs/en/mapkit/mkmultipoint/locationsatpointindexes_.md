---
title: 'locationsAtPointIndexes:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmultipoint/locationsatpointindexes:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint/locationsatpointindexes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint/locationsatpointindexes%3A.json'
content_hash: 'sha256:6601c56923aa771f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMultiPoint](../mkmultipoint.md)

# locationsAtPointIndexes:

<sub>Instance Method</sub>

Returns a set of unit distance values that correspond to the point indexes along the shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSArray<NSNumber *> *) locationsAtPointIndexes:(NSIndexSet *) indexes;
```

## Parameters

- `indexes` — A set of map point indexes associated with the shape.

## Return Value

An [NSIndexSet](../../foundation/nsindexset.md) that corresponds to the point indexes along the shape.

## See Also

### Accessing the points in the shape

- [- points](<points().md>) — Returns an array of map points associated with the shape.
- [pointCount](pointcount.md) — The number of points associated with the shape.
- [- locationAtPointIndex:](<location(atpointindex_).md>) — Translates a point index into a unit distance along the shape.
