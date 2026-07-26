---
title: 'storeOverlayWillStartPresentation(_:transitionContext:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate/storeoverlaywillstartpresentation%28_%3Atransitioncontext%3A%29.json'
content_hash: 'sha256:773e1a62977a12eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlayDelegate](../skoverlaydelegate.md)

# storeOverlayWillStartPresentation(_:transitionContext:)

<sub>Instance Method</sub>

Indicates that the platform presents an overlay.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func storeOverlayWillStartPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

## Parameters

- `overlay` — An overlay object that’s about to appear.

- `transitionContext` — A context you can use to animate changes to UI components as the overlay appears.

## Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main thread. For example, make a [UIImageView](../../uikit/uiimageview.md) disappear by animating the change of its opacity to 0% as shown in the following code:

```swift
func storeOverlayWillStartPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext) {
    transitionContext.addAnimation { [self] in
        self.imageView.layer.opacity = 0
    }
}
```

## See Also

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:didFinishPresentation:](<storeoverlaydidfinishpresentation(__transitioncontext_).md>) — Indicates that the platform finished presenting an overlay.
- [- storeOverlay:willStartDismissal:](<storeoverlaywillstartdismissal(__transitioncontext_).md>) — Indicates that the platform dismisses an overlay.
- [- storeOverlay:didFinishDismissal:](<storeoverlaydidfinishdismissal(__transitioncontext_).md>) — Indicates that platform finished dismissing an overlay.
- [TransitionContext](../skoverlay/transitioncontext.md) — A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
