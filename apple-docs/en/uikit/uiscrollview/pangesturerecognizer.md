---
title: panGestureRecognizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/pangesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/pangesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/pangesturerecognizer.json'
content_hash: 'sha256:fead1b96ee641be4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# panGestureRecognizer

<sub>Instance Property</sub>

The underlying gesture recognizer for pan gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var panGestureRecognizer: UIPanGestureRecognizer { get }
```

## Discussion

Your application accesses this property when it wants to more precisely control which pan gestures are recognized by the scroll view.

## See Also

### Zooming and panning

- [pinchGestureRecognizer](pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [- zoomToRect:animated:](<zoom(to_animated_).md>) — Zooms to a specific area of the content so that it’s visible in the scroll view.
- [zoomScale](zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [- setZoomScale:animated:](<setzoomscale(__animated_).md>) — A floating-point value that specifies the current zoom scale.
- [maximumZoomScale](maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zoomBouncing](iszoombouncing.md) — A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [zooming](iszooming.md) — A Boolean value that indicates whether the content view is currently zooming in or out.
- [zoomAnimating](iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
