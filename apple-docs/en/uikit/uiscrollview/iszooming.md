---
title: isZooming
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/iszooming
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/iszooming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/iszooming.json'
content_hash: 'sha256:8d0aab360fc1d68b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isZooming

<sub>Instance Property</sub>

A Boolean value that indicates whether the content view is currently zooming in or out.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isZooming: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if user is making a zoom gesture; otherwise, it’s [false](../../swift/false.md).

## See Also

### Zooming and panning

- [panGestureRecognizer](pangesturerecognizer.md) — The underlying gesture recognizer for pan gestures.
- [pinchGestureRecognizer](pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [- zoomToRect:animated:](<zoom(to_animated_).md>) — Zooms to a specific area of the content so that it’s visible in the scroll view.
- [zoomScale](zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [- setZoomScale:animated:](<setzoomscale(__animated_).md>) — A floating-point value that specifies the current zoom scale.
- [maximumZoomScale](maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zoomBouncing](iszoombouncing.md) — A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [zoomAnimating](iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
