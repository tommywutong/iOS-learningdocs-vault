---
title: 'initWithPolygon:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkpolygonview/initwithpolygon:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygonview/initwithpolygon:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygonview/initwithpolygon%3A.json'
content_hash: 'sha256:4e9c0c9f79fe2d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolygonView](../mkpolygonview.md)

# initWithPolygon:

<sub>Instance Method</sub>

Initializes and returns a new overlay view using the specified polygon overlay object.

> [!warning] Deprecated
> Use an [MKPolygonRenderer](../mkpolygonrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithPolygon:(MKPolygon *) polygon;
```

## Parameters

- `polygon` — The polygon overlay containing the information about the area to be drawn. This object must have at least three points defining the polygon in order for this view to draw the corresponding path.

## Return Value

A new polygon overlay view.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
