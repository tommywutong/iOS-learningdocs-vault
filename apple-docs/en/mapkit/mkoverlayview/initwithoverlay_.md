---
title: 'initWithOverlay:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkoverlayview/initwithoverlay:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayview/initwithoverlay:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayview/initwithoverlay%3A.json'
content_hash: 'sha256:960a3cdc631f3d89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayView](../mkoverlayview.md)

# initWithOverlay:

<sub>Instance Method</sub>

Initializes and returns the overlay view and associates it with the specified overlay object.

> [!warning] Deprecated
> Use an [MKOverlayRenderer](../mkoverlayrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithOverlay:(id<MKOverlay>) overlay;
```

## Parameters

- `overlay` — The overlay object to use when drawing the overlay on the map. This object provides the data needed to draw the overlay’s shape. This object is retained by the overlay view.

## Return Value

An initialized overlay object.

## Discussion

Upon initialization, the frame of the overlay view is set to [CGRectZero](../../coregraphics/cgrectzero.md). The map view sets the size and position of the view at display time, and you should not change those values yourself.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
