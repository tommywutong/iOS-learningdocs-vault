---
title: 'setNeedsDisplayInMapRect:zoomScale:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/setneedsdisplayinmaprect:zoomscale:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/setneedsdisplayinmaprect:zoomscale:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/setneedsdisplayinmaprect%3Azoomscale%3A.json'
content_hash: 'sha256:7ba54dd8ddb89b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# setNeedsDisplayInMapRect:zoomScale:

<sub>Instance Method</sub>

Invalidates the view in the given map rectangle but only at the specified zoom scale.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setNeedsDisplayInMapRect:(MKMapRect) mapRect zoomScale:(MKZoomScale) zoomScale;
```

## Parameters

- `mapRect` — The portion of the overlay that needs to be updated. This value is specified using a map rectangle and not view coordinates. You can convert from a view rectangle to a map rectangle using the [mapRectForRect:](maprectforrect_.md) method.

- `zoomScale` — The zoom scale for which you want to invalidate the overlay.

## Discussion

Marking a rectangle as invalid causes that portion of the view to be redrawn during the next update cycle. This method invalidates the overlay only when it is drawn at the specified zoom scale.

## See Also

### Drawing the overlay

- [canDrawMapRect:zoomScale:](candrawmaprect_zoomscale_.md) — Returns a Boolean value indicating whether the overlay view is ready to draw its content. _(deprecated)_
- [drawMapRect:zoomScale:inContext:](drawmaprect_zoomscale_incontext_.md) — Draws the contents of the overlay view. _(deprecated)_
- [setNeedsDisplayInMapRect:](setneedsdisplayinmaprect_.md) — Invalidates the view in the given map rectangle at all zoom scales. _(deprecated)_
