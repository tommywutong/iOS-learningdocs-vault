---
title: 'initWithPolyline:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkpolylineview/initwithpolyline:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolylineview/initwithpolyline:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolylineview/initwithpolyline%3A.json'
content_hash: 'sha256:65c71ff6928a5e55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolylineView](../mkpolylineview.md)

# initWithPolyline:

<sub>Instance Method</sub>

Initializes and returns a new overlay view using the specified polyline overlay object

> [!warning] Deprecated
> Use an [MKPolylineRenderer](../mkpolylinerenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithPolyline:(MKPolyline *) polyline;
```

## Parameters

- `polyline` — The polyline overlay object containing the information about the path to be stroked. This object must have at least two points defined in order for this view to draw the corresponding path.

## Return Value

A new polyline overlay view.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
