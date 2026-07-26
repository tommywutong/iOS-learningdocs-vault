---
title: isZoomBouncing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/iszoombouncing
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/iszoombouncing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/iszoombouncing.json'
content_hash: 'sha256:dbd9df636ab79ab0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isZoomBouncing

<sub>Instance Property</sub>

A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isZoomBouncing: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the scroll view is zooming back to a minimum or maximum zoom scaling value; otherwise, the value is [false](../../swift/false.md).

## See Also

### Zooming and panning

- [panGestureRecognizer](pangesturerecognizer.md) — The underlying gesture recognizer for pan gestures.
- [pinchGestureRecognizer](pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [- zoomToRect:animated:](<zoom(to_animated_).md>) — Zooms to a specific area of the content so that it’s visible in the scroll view.
- [zoomScale](zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [- setZoomScale:animated:](<setzoomscale(__animated_).md>) — A floating-point value that specifies the current zoom scale.
- [maximumZoomScale](maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zooming](iszooming.md) — A Boolean value that indicates whether the content view is currently zooming in or out.
- [zoomAnimating](iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
