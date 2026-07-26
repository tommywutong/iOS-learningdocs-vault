---
title: 'draw(_:zoomScale:in:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/draw(_:zoomscale:in:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/draw(_:zoomscale:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/draw%28_%3Azoomscale%3Ain%3A%29.json'
content_hash: 'sha256:a5e21347c0ac0fbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# draw(_:zoomScale:in:)

<sub>Instance Method</sub>

Draws the overlay’s contents at the specified location on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func draw(_ mapRect: MKMapRect, zoomScale: MKZoomScale, in context: CGContext)
```

## Parameters

- `mapRect` — The map rectangle that the renderer needs to update. Your drawing code needs to avoid drawing outside of this rectangle.

- `zoomScale` — The zoom factor to apply to the map content. You can use this value for configuring the stroke width of lines or other attributes that the scale of the map’s contents might affect.

- `context` — The graphics context to use for drawing the overlay’s contents.

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to draw the overlay’s contents.

When determining where to draw content, make your initial calculations relative to the map itself. Compute the position and size of any overlay content using map points and map rectangles, convert those values to regular [CGPoint](../../corefoundation/cgpoint.md) and [CGRect](../../corefoundation/cgrect.md) types using the methods of this class, and then pass the converted points to any drawing primitives.

Use Core Graphics to draw any content for your overlays. If you choose to draw using UIKit classes and methods instead, push the specified graphics context onto the context stack (using the [UIGraphicsPushContext(_:)](<../../uikit/uigraphicspushcontext(__).md>) function) before making any drawing calls. When you finish drawing, you need to similarly pop the graphics context off the stack using the [UIGraphicsPopContext()](<../../uikit/uigraphicspopcontext().md>). Overlay drawing typically occurs on background threads to improve performance, so don’t manipulate UIKit views or other objects that you can only manipulate on the app’s main thread.

To improve drawing performance, the map view may divide your overlay into multiple tiles and render each one on a separate thread. Therefore, your implementation of this method needs to be capable of safely running multiple threads simultaneously. In addition, avoid drawing the entire contents of the overlay each time the overlay renderer calls this method. Instead, be sure to take the `mapRect` parameter into consideration and avoid drawing content outside that rectangle.

## See Also

### Drawing the overlay

- [- canDrawMapRect:zoomScale:](<candraw(__zoomscale_).md>) — Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [- setNeedsDisplay](<setneedsdisplay().md>) — Invalidates the entire contents of the overlay for all zoom scales.
- [- setNeedsDisplayInMapRect:](<setneedsdisplay(__).md>) — Invalidates the specified portion of the overlay at all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](<setneedsdisplay(__zoomscale_).md>) — Invalidates the specified portion of the overlay, but only at the specified zoom scale.
