---
title: MKOverlayRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlayrenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer.json'
content_hash: 'sha256:887668e07b8cc278'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKOverlayRenderer

<sub>Class</sub>

The shared infrastructure for drawing overlays on the map surface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKOverlayRenderer
```

## Overview

An overlay renderer draws the visual representation of an overlay object — that is, an object that conforms to the [MKOverlay](mkoverlay.md) protocol. This class defines the drawing infrastructure the map view uses. Subclasses need to override the [- drawMapRect:zoomScale:inContext:](<mkoverlayrenderer/draw(__zoomscale_in_).md>) method to draw the contents of the overlay.

The MapKit framework provides several concrete instances of overlay renderers. Specifically, it provides renderers for each of the concrete overlay objects. You can use one of these existing renderers or define your own subclasses if you want to draw the overlay contents differently.

You can subclass `MKOverlayRenderer` to create overlays based on custom shapes, content, or drawing techniques. The only method subclasses need to override is the [- drawMapRect:zoomScale:inContext:](<mkoverlayrenderer/draw(__zoomscale_in_).md>) method. However, if your class contains content that may not be ready for drawing right away, you need to also override the [- canDrawMapRect:zoomScale:](<mkoverlayrenderer/candraw(__zoomscale_).md>) method and use it to report when your class is ready and able to draw.

The map view may tile large overlays and distribute the rendering of each tile to separate threads. Therefore, the implementation of your [- drawMapRect:zoomScale:inContext:](<mkoverlayrenderer/draw(__zoomscale_in_).md>) method needs to be safe to run from background threads and from multiple threads simultaneously.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MKOverlayPathRenderer](mkoverlaypathrenderer.md), [MKTileOverlayRenderer](mktileoverlayrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an overlay view

- [- initWithOverlay:](<mkoverlayrenderer/init(overlay_).md>) — Creates and returns the overlay renderer and associates it with the specified overlay object.

### Attributes of the overlay

- [overlay](mkoverlayrenderer/overlay.md) — The overlay object containing the data for drawing.
- [alpha](mkoverlayrenderer/alpha.md) — The amount of transparency to apply to the overlay.
- [contentScaleFactor](mkoverlayrenderer/contentscalefactor.md) — The scale factor for drawing the overlay’s content.
- [blendMode](mkoverlayrenderer/blendmode.md) — The blend mode to apply to the overlay.

### Converting points on the map

- [- pointForMapPoint:](<mkoverlayrenderer/point(for_).md>) — Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.
- [- mapPointForPoint:](<mkoverlayrenderer/mappoint(for_).md>) — Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.
- [- rectForMapRect:](<mkoverlayrenderer/rect(for_).md>) — Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
- [- mapRectForRect:](<mkoverlayrenderer/maprect(for_).md>) — Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.

### Drawing the overlay

- [- canDrawMapRect:zoomScale:](<mkoverlayrenderer/candraw(__zoomscale_).md>) — Returns a Boolean value that indicates whether the overlay view is ready to draw its content.
- [- drawMapRect:zoomScale:inContext:](<mkoverlayrenderer/draw(__zoomscale_in_).md>) — Draws the overlay’s contents at the specified location on the map.
- [- setNeedsDisplay](<mkoverlayrenderer/setneedsdisplay().md>) — Invalidates the entire contents of the overlay for all zoom scales.
- [- setNeedsDisplayInMapRect:](<mkoverlayrenderer/setneedsdisplay(__).md>) — Invalidates the specified portion of the overlay at all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](<mkoverlayrenderer/setneedsdisplay(__zoomscale_).md>) — Invalidates the specified portion of the overlay, but only at the specified zoom scale.

### Types

- [MKZoomScale](mkzoomscale.md) — A scale factor to use in conjunction with a map.
- [MKRoadWidthAtZoomScale](<mkroadwidthatzoomscale(__).md>) — Returns the width (in screen points) of roads on a map at the specified zoom level.

## See Also

### Shared behavior

- [MKOverlay](mkoverlay.md) — An interface for associating content with a specific map region.
- [MKShape](mkshape.md) — An abstract class that defines the basic properties for all shape-based overlay objects.
- [MKMultiPoint](mkmultipoint.md) — An abstract class that defines the common behavior that open and closed polygon overlays share.
- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
