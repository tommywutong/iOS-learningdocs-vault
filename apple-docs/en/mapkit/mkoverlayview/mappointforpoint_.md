---
title: 'mapPointForPoint:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/mappointforpoint:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/mappointforpoint:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/mappointforpoint%3A.json'
content_hash: 'sha256:ebefb4790cdc0922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# mapPointForPoint:

<sub>Instance Method</sub>

Returns the map point that corresponds to the specified point in the overlay view.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (MKMapPoint) mapPointForPoint:(CGPoint) point;
```

## Parameters

- `point` — The point in the view’s coordinate system that you want to convert.

## Return Value

The point on the two-dimensional map projection corresponding to the specified point.

## Discussion

Because the bounds and frame rectangles of an overlay view do not change after the view has been created, you may call this method from multiple threads simultaneously. Therefore, you may call this method safely from your view’s [drawMapRect:zoomScale:inContext:](drawmaprect_zoomscale_incontext_.md) method.

## See Also

### Converting points on the map

- [pointForMapPoint:](pointformappoint_.md) — Returns the point in the overlay view that corresponds to specified point on the map. _(deprecated)_
- [rectForMapRect:](rectformaprect_.md) — Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map. _(deprecated)_
- [mapRectForRect:](maprectforrect_.md) — Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system. _(deprecated)_
