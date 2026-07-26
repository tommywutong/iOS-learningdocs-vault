---
title: 'pointForMapPoint:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/pointformappoint:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/pointformappoint:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/pointformappoint%3A.json'
content_hash: 'sha256:6f7002dcbc20e58f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# pointForMapPoint:

<sub>Instance Method</sub>

Returns the point in the overlay view that corresponds to specified point on the map.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGPoint) pointForMapPoint:(MKMapPoint) mapPoint;
```

## Parameters

- `mapPoint` — A point on the two-dimensional map projection. If you have a coordinate value (latitude and longitude), you can use the [MKMapPointForCoordinate](<../mkmappoint/init(__).md>) function to convert that coordinate to a map point.

## Return Value

The point in the receiver’s coordinate system that corresponds to the map point.

## Discussion

Because the bounds and frame rectangles of an overlay view do not change after the view has been created, you may call this method from multiple threads simultaneously. Therefore, you may call this method safely from your view’s [drawMapRect:zoomScale:inContext:](drawmaprect_zoomscale_incontext_.md) method.

## See Also

### Converting points on the map

- [mapPointForPoint:](mappointforpoint_.md) — Returns the map point that corresponds to the specified point in the overlay view. _(deprecated)_
- [rectForMapRect:](rectformaprect_.md) — Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map. _(deprecated)_
- [mapRectForRect:](maprectforrect_.md) — Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system. _(deprecated)_
