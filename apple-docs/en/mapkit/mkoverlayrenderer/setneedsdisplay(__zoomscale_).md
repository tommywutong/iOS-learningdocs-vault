---
title: 'setNeedsDisplay(_:zoomScale:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:zoomscale:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:zoomscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/setneedsdisplay%28_%3Azoomscale%3A%29.json'
content_hash: 'sha256:857315822693f194'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# setNeedsDisplay(_:zoomScale:)

<sub>Instance Method</sub>

Invalidates the specified portion of the overlay, but only at the specified zoom scale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setNeedsDisplay(_ mapRect: MKMapRect, zoomScale: MKZoomScale)
```

## Parameters

- `mapRect` — The portion of the overlay to update. Specify this value using a map coordinates.

- `zoomScale` — The zoom scale for which you want to invalidate the overlay.

## Discussion

Marking a rectangle as invalid causes that portion of the overlay to be redrawn during the next update cycle. This method invalidates the overlay only at the specified zoom scale.

## See Also

### Drawing the overlay

- [- canDrawMapRect:zoomScale:](<candraw(__zoomscale_).md>) — Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [- drawMapRect:zoomScale:inContext:](<draw(__zoomscale_in_).md>) — Draws the overlay’s contents at the specified location on the map.
- [- setNeedsDisplay](<setneedsdisplay().md>) — Invalidates the entire contents of the overlay for all zoom scales.
- [- setNeedsDisplayInMapRect:](<setneedsdisplay(__).md>) — Invalidates the specified portion of the overlay at all zoom scales.
