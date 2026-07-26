---
title: 'drawMapRect:zoomScale:inContext:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/drawmaprect:zoomscale:incontext:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/drawmaprect:zoomscale:incontext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/drawmaprect%3Azoomscale%3Aincontext%3A.json'
content_hash: 'sha256:21fddc9ae897c0b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# drawMapRect:zoomScale:inContext:

<sub>Instance Method</sub>

Draws the contents of the overlay view.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) drawMapRect:(MKMapRect) mapRect zoomScale:(MKZoomScale) zoomScale inContext:(CGContextRef) context;
```

## Parameters

- `mapRect` — The map rectangle that needs to be updated. You can use this rectangle to limit drawing to only the portion of the view that changed.

- `zoomScale` — The current scale factor applied to the map content. You can use this value for configuring the stroke width of lines or other attributes that might be affected by the scale of the view’s content.

- `context` — The graphics context to use for drawing the view’s content.

## Discussion

The default implementation of this method does nothing. Subclasses are expected to override this method (instead of the [draw(_:)](<../../uikit/uiview/draw(__).md>) method) and use it to draw the contents of the view.

In your drawing code, you should specify the position of any rendered content relative to the map itself and not relative to the view’s bounds or frame. In other words, compute the position and size of any overlay content using map points and map rectangles, convert those values to [CGPoint](../../corefoundation/cgpoint.md) and [CGRect](../../corefoundation/cgrect.md) types (using the methods of this class), and then use the converted points to build paths or specify the rendering location for items.

You should also not make assumptions that the view’s frame matches the bounding rectangle of the overlay. The view’s frame is actually bigger than the bounding rectangle to allow you to draw lines for things like roads that might be located directly on the border of that rectangle. For some types of content, such as gradients, this also means that you might need to apply a clipping rectangle to `context` to ensure drawing is contained to the correct area.

It is recommended that you use Core Graphics to draw any content for your overlays. If you choose to use UIKit classes and methods for drawing instead, you must push the specified graphics context onto the context stack (using the [UIGraphicsPushContext(_:)](<../../uikit/uigraphicspushcontext(__).md>) function) before making any drawing calls. When you are done drawing, you must similarly pop the graphics context off the stack using the [UIGraphicsPopContext()](<../../uikit/uigraphicspopcontext().md>). During drawing, you may draw content normally but should avoid manipulating views and other classes that are safe to use only from the application’s main thread.

To improve drawing performance, the map view may tile overlays that become large enough and render the tiles from separate threads. Your implementation of this method must therefore be capable of safely running from multiple threads simultaneously. In addition, you should avoid drawing the entire contents of the overlay each time this method is called. Instead, your implementation should always take the `mapRect` parameter into consideration and avoid drawing content outside that rectangle. Failure to do so could lead to performance problems.

## See Also

### Related Documentation

- [pointForMapPoint:](pointformappoint_.md) — Returns the point in the overlay view that corresponds to specified point on the map. _(deprecated)_
- [rectForMapRect:](rectformaprect_.md) — Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map. _(deprecated)_

### Drawing the overlay

- [canDrawMapRect:zoomScale:](candrawmaprect_zoomscale_.md) — Returns a Boolean value indicating whether the overlay view is ready to draw its content. _(deprecated)_
- [setNeedsDisplayInMapRect:](setneedsdisplayinmaprect_.md) — Invalidates the view in the given map rectangle at all zoom scales. _(deprecated)_
- [setNeedsDisplayInMapRect:zoomScale:](setneedsdisplayinmaprect_zoomscale_.md) — Invalidates the view in the given map rectangle but only at the specified zoom scale. _(deprecated)_
