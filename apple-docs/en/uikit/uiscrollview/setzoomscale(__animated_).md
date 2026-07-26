---
title: 'setZoomScale(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/setzoomscale(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/setzoomscale(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/setzoomscale%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:1c24f4b287a2e731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# setZoomScale(_:animated:)

<sub>Instance Method</sub>

A floating-point value that specifies the current zoom scale.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setZoomScale(_ scale: CGFloat, animated: Bool)
```

## Parameters

- `scale` — The new value to scale the content to.

- `animated` — [true](../../swift/true.md) to animate the transition to the new scale, [false](../../swift/false.md) to make the transition immediate.

## Discussion

The new scale value should be between the [minimumZoomScale](minimumzoomscale.md) and the [maximumZoomScale](maximumzoomscale.md).

## See Also

### Zooming and panning

- [panGestureRecognizer](pangesturerecognizer.md) — The underlying gesture recognizer for pan gestures.
- [pinchGestureRecognizer](pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [- zoomToRect:animated:](<zoom(to_animated_).md>) — Zooms to a specific area of the content so that it’s visible in the scroll view.
- [zoomScale](zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [maximumZoomScale](maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zoomBouncing](iszoombouncing.md) — A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [zooming](iszooming.md) — A Boolean value that indicates whether the content view is currently zooming in or out.
- [zoomAnimating](iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
