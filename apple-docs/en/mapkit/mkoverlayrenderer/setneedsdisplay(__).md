---
title: 'setNeedsDisplay(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/setneedsdisplay(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/setneedsdisplay%28_%3A%29.json'
content_hash: 'sha256:b7d2a99b2f1fb933'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# setNeedsDisplay(_:)

<sub>Instance Method</sub>

Invalidates the specified portion of the overlay at all zoom scales.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setNeedsDisplay(_ mapRect: MKMapRect)
```

## Parameters

- `mapRect` — The portion of the overlay to update. Specify this value using a map coordinates.

## Discussion

Marking a rectangle as invalid causes that portion of the overlay to be redrawn during the next update cycle. This method invalidates the overlay regardless of the current zoom scale associated with the map.

## See Also

### Drawing the overlay

- [- canDrawMapRect:zoomScale:](<candraw(__zoomscale_).md>) — Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [- drawMapRect:zoomScale:inContext:](<draw(__zoomscale_in_).md>) — Draws the overlay’s contents at the specified location on the map.
- [- setNeedsDisplay](<setneedsdisplay().md>) — Invalidates the entire contents of the overlay for all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](<setneedsdisplay(__zoomscale_).md>) — Invalidates the specified portion of the overlay, but only at the specified zoom scale.
