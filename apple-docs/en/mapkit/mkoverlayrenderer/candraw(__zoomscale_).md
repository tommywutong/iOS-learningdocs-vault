---
title: 'canDraw(_:zoomScale:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/candraw(_:zoomscale:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/candraw(_:zoomscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/candraw%28_%3Azoomscale%3A%29.json'
content_hash: 'sha256:094259906ff2d908'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# canDraw(_:zoomScale:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the overlay view is ready to draw its content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canDraw(_ mapRect: MKMapRect, zoomScale: MKZoomScale) -> Bool
```

## Parameters

- `mapRect` — The map rectangle that the renderer needs to update.

- `zoomScale` — The current scale factor applied to the map.

## Return Value

[true](../../swift/true.md) if this overlay renderer is ready to draw its contents on the map or [false](../../swift/false.md) if it is not.

## Discussion

Overlay renderers can override this method in situations where they may depend on the availability of other information to draw their contents. For example, a renderer showing traffic information might want to delay drawing until it has all of the traffic data it needs. In such a case, it can return [false](../../swift/false.md) from this method to indicate that it’s not ready. An overlay renderer might also return [false](../../swift/false.md) if it doesn’t draw content in the specified rectangle.

If you return [false](../../swift/false.md) from this method, your application is responsible for calling the [- setNeedsDisplayInMapRect:zoomScale:](<setneedsdisplay(__zoomscale_).md>) method when the overlay renderer subsequently becomes ready to draw its contents.

The default implementation of this method returns [true](../../swift/true.md).

## See Also

### Drawing the overlay

- [- drawMapRect:zoomScale:inContext:](<draw(__zoomscale_in_).md>) — Draws the overlay’s contents at the specified location on the map.
- [- setNeedsDisplay](<setneedsdisplay().md>) — Invalidates the entire contents of the overlay for all zoom scales.
- [- setNeedsDisplayInMapRect:](<setneedsdisplay(__).md>) — Invalidates the specified portion of the overlay at all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](<setneedsdisplay(__zoomscale_).md>) — Invalidates the specified portion of the overlay, but only at the specified zoom scale.
