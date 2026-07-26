---
title: 'zoom(to:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/zoom(to:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/zoom(to:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/zoom%28to%3Aanimated%3A%29.json'
content_hash: 'sha256:2e78d79bfc150721'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# zoom(to:animated:)

<sub>Instance Method</sub>

Zooms to a specific area of the content so that it’s visible in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func zoom(to rect: CGRect, animated: Bool)
```

## Parameters

- `rect` — A rectangle defining an area of the content view. The rectangle should be in the coordinate space of the view returned by [- viewForZoomingInScrollView:](<../uiscrollviewdelegate/viewforzooming(in_).md>).

- `animated` — [true](../../swift/true.md) if the scrolling should be animated, [false](../../swift/false.md) if it should be immediate.

## Discussion

This method zooms so that the content view becomes the area defined by `rect`, adjusting the [zoomScale](zoomscale.md) as necessary.

## See Also

### Zooming and panning

- [panGestureRecognizer](pangesturerecognizer.md) — The underlying gesture recognizer for pan gestures.
- [pinchGestureRecognizer](pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [zoomScale](zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [- setZoomScale:animated:](<setzoomscale(__animated_).md>) — A floating-point value that specifies the current zoom scale.
- [maximumZoomScale](maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zoomBouncing](iszoombouncing.md) — A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [zooming](iszooming.md) — A Boolean value that indicates whether the content view is currently zooming in or out.
- [zoomAnimating](iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.
