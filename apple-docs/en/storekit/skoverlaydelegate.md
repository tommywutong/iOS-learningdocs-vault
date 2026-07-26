---
title: SKOverlayDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlaydelegate
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate.json'
content_hash: 'sha256:2d85a343d7e3fb8a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKOverlayDelegate

<sub>Protocol</sub>

Methods for responding to the overlay’s appearance, dismissal, or failure to load.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol SKOverlayDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:willStartPresentation:](<skoverlaydelegate/storeoverlaywillstartpresentation(__transitioncontext_).md>) — Indicates that the platform presents an overlay.
- [- storeOverlay:didFinishPresentation:](<skoverlaydelegate/storeoverlaydidfinishpresentation(__transitioncontext_).md>) — Indicates that the platform finished presenting an overlay.
- [- storeOverlay:willStartDismissal:](<skoverlaydelegate/storeoverlaywillstartdismissal(__transitioncontext_).md>) — Indicates that the platform dismisses an overlay.
- [- storeOverlay:didFinishDismissal:](<skoverlaydelegate/storeoverlaydidfinishdismissal(__transitioncontext_).md>) — Indicates that platform finished dismissing an overlay.
- [TransitionContext](skoverlay/transitioncontext.md) — A context object you can use to animate UI changes while the platform presents or dismisses an overlay.

### Responding to Failures

- [- storeOverlay:didFailToLoadWithError:](<skoverlaydelegate/storeoverlaydidfailtoload(__error_).md>) — Indicates that an overlay failed to load.

## See Also

### Setting a delegate

- [delegate](skoverlay/delegate.md) — The overlay’s delegate.
