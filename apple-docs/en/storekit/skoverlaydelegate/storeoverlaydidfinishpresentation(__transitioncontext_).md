---
title: 'storeOverlayDidFinishPresentation(_:transitionContext:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishpresentation%28_%3Atransitioncontext%3A%29.json'
content_hash: 'sha256:042cbb9a08670337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlayDelegate](../skoverlaydelegate.md)

# storeOverlayDidFinishPresentation(_:transitionContext:)

<sub>Instance Method</sub>

Indicates that the platform finished presenting an overlay.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func storeOverlayDidFinishPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

## Parameters

- `overlay` — The overlay object that appears.

- `transitionContext` — A context you can use to animate changes to UI components after the overlay appears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:willStartPresentation:](<storeoverlaywillstartpresentation(__transitioncontext_).md>) — Indicates that the platform presents an overlay.
- [- storeOverlay:willStartDismissal:](<storeoverlaywillstartdismissal(__transitioncontext_).md>) — Indicates that the platform dismisses an overlay.
- [- storeOverlay:didFinishDismissal:](<storeoverlaydidfinishdismissal(__transitioncontext_).md>) — Indicates that platform finished dismissing an overlay.
- [TransitionContext](../skoverlay/transitioncontext.md) — A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
