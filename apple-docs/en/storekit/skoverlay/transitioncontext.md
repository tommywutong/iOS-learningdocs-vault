---
title: SKOverlay.TransitionContext
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/transitioncontext
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/transitioncontext.json'
content_hash: 'sha256:027d2ed0f4d8b7b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# SKOverlay.TransitionContext

<sub>Class</sub>

A context object you can use to animate UI changes while the platform presents or dismisses an overlay.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class TransitionContext
```

## Overview

For more information on animating UI changes while the system presents or dismisses an overlay, see [- storeOverlay:willStartPresentation:](<../skoverlaydelegate/storeoverlaywillstartpresentation(__transitioncontext_).md>) and [- storeOverlay:willStartDismissal:](<../skoverlaydelegate/storeoverlaywillstartdismissal(__transitioncontext_).md>).

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Adding an Animation

- [- addAnimationBlock:](<transitioncontext/addanimation(__).md>) — Adds a closure you can use to animate view properties.
- [startFrame](transitioncontext/startframe.md) — The size and location of the overlay before the transition.
- [endFrame](transitioncontext/endframe.md) — The size and location of the overlay at the end of the transition.

## See Also

### Responding to the Overlay’s Appearance and Disappearance

- [- storeOverlay:willStartPresentation:](<../skoverlaydelegate/storeoverlaywillstartpresentation(__transitioncontext_).md>) — Indicates that the platform presents an overlay.
- [- storeOverlay:didFinishPresentation:](<../skoverlaydelegate/storeoverlaydidfinishpresentation(__transitioncontext_).md>) — Indicates that the platform finished presenting an overlay.
- [- storeOverlay:willStartDismissal:](<../skoverlaydelegate/storeoverlaywillstartdismissal(__transitioncontext_).md>) — Indicates that the platform dismisses an overlay.
- [- storeOverlay:didFinishDismissal:](<../skoverlaydelegate/storeoverlaydidfinishdismissal(__transitioncontext_).md>) — Indicates that platform finished dismissing an overlay.
