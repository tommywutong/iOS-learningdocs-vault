---
title: 'storeOverlayDidFinishDismissal(_:transitionContext:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishdismissal%28_%3Atransitioncontext%3A%29.json'
content_hash: 'sha256:67b7df7f8e7105cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlayDelegate](../skoverlaydelegate.md)

# storeOverlayDidFinishDismissal(_:transitionContext:)

<sub>Instance Method</sub>

Indicates that platform finished dismissing an overlay.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func storeOverlayDidFinishDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

## Parameters

- `overlay` — An app banner object that disappeared.

- `transitionContext` — The context you can use to animate changes to UI components when the overlay disappears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:willStartPresentation:](<storeoverlaywillstartpresentation(__transitioncontext_).md>) — Indicates that the platform presents an overlay.
- [- storeOverlay:didFinishPresentation:](<storeoverlaydidfinishpresentation(__transitioncontext_).md>) — Indicates that the platform finished presenting an overlay.
- [- storeOverlay:willStartDismissal:](<storeoverlaywillstartdismissal(__transitioncontext_).md>) — Indicates that the platform dismisses an overlay.
- [TransitionContext](../skoverlay/transitioncontext.md) — A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
