---
title: 'canDrawMapRect:zoomScale:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/candrawmaprect:zoomscale:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/candrawmaprect:zoomscale:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/candrawmaprect%3Azoomscale%3A.json'
content_hash: 'sha256:7f5a73cf0f686843'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# canDrawMapRect:zoomScale:

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the overlay view is ready to draw its content.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) canDrawMapRect:(MKMapRect) mapRect zoomScale:(MKZoomScale) zoomScale;
```

## Parameters

- `mapRect` — The map rectangle that needs to be updated.

- `zoomScale` — The current scale factor applied to the map.

## Return Value

[true](../../swift/true.md) if this view is ready to draw its contents or [false](../../swift/false.md) if it is not.

## Discussion

Overlay views can override this method in situations where they may depend on the availability of other information to draw their contents. For example, an overlay view showing traffic information might want to delay drawing until it has all of the traffic data it needs. In such a case, it can return [false](../../swift/false.md) from this method to indicate that it is not ready.

If you return [false](../../swift/false.md) from this method, your application is responsible for calling the [setNeedsDisplayInMapRect:zoomScale:](setneedsdisplayinmaprect_zoomscale_.md) method when the overlay view subsequently becomes ready to draw its contents.

The default implementation of this method returns [true](../../swift/true.md).

## See Also

### Drawing the overlay

- [drawMapRect:zoomScale:inContext:](drawmaprect_zoomscale_incontext_.md) — Draws the contents of the overlay view. _(deprecated)_
- [setNeedsDisplayInMapRect:](setneedsdisplayinmaprect_.md) — Invalidates the view in the given map rectangle at all zoom scales. _(deprecated)_
- [setNeedsDisplayInMapRect:zoomScale:](setneedsdisplayinmaprect_zoomscale_.md) — Invalidates the view in the given map rectangle but only at the specified zoom scale. _(deprecated)_
