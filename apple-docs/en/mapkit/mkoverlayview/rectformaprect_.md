---
title: 'rectForMapRect:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/rectformaprect:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/rectformaprect:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/rectformaprect%3A.json'
content_hash: 'sha256:447228f0dbe64e61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# rectForMapRect:

<sub>Instance Method</sub>

Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGRect) rectForMapRect:(MKMapRect) mapRect;
```

## Parameters

- `mapRect` — A rectangle on the two-dimensional map projection.

## Return Value

The rectangle specified in the receiver’s coordinate system.

## Discussion

Because the bounds and frame rectangles of an overlay view do not change after the view has been created, you may call this method from multiple threads simultaneously. Therefore, you may call this method safely from your view’s [drawMapRect:zoomScale:inContext:](drawmaprect_zoomscale_incontext_.md) method.

## See Also

### Converting points on the map

- [pointForMapPoint:](pointformappoint_.md) — Returns the point in the overlay view that corresponds to specified point on the map. _(deprecated)_
- [mapPointForPoint:](mappointforpoint_.md) — Returns the map point that corresponds to the specified point in the overlay view. _(deprecated)_
- [mapRectForRect:](maprectforrect_.md) — Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system. _(deprecated)_
