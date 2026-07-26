---
title: 'storeOverlayWillStartDismissal(_:transitionContext:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate/storeoverlaywillstartdismissal%28_%3Atransitioncontext%3A%29.json'
content_hash: 'sha256:ac38484a0f2170c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlayDelegate](../skoverlaydelegate.md)

# storeOverlayWillStartDismissal(_:transitionContext:)

<sub>Instance Method</sub>

Indicates that the platform dismisses an overlay.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func storeOverlayWillStartDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

## Parameters

- `overlay` — An overlay object that’s about to disappear.

- `transitionContext` — The context you can use to animate changes to UI components when the overlay disappears.

## Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main thread. For example, make a [UIImageView](../../uikit/uiimageview.md) appear by animating the change of its opacity to 100%`,` as shown in the following code:

```swift
func storeOverlayWillStartDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext) {
    transitionContext.addAnimation { [self] in
        self.imageView.layer.opacity = 1
    }
}
```

## See Also

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:willStartPresentation:](<storeoverlaywillstartpresentation(__transitioncontext_).md>) — Indicates that the platform presents an overlay.
- [- storeOverlay:didFinishPresentation:](<storeoverlaydidfinishpresentation(__transitioncontext_).md>) — Indicates that the platform finished presenting an overlay.
- [- storeOverlay:didFinishDismissal:](<storeoverlaydidfinishdismissal(__transitioncontext_).md>) — Indicates that platform finished dismissing an overlay.
- [TransitionContext](../skoverlay/transitioncontext.md) — A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
