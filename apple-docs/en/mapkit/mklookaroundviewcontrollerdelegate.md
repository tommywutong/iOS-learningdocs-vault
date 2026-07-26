---
title: MKLookAroundViewControllerDelegate
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklookaroundviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundviewcontrollerdelegate.json'
content_hash: 'sha256:21131b1a415d1143'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLookAroundViewControllerDelegate

<sub>Protocol</sub>

Methods you implement to respond to changes in the LookAround view controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol MKLookAroundViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to scene changes

- [- lookAroundViewControllerWillUpdateScene:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillupdatescene(__).md>) — Tells the delegate that the scene is about to update.
- [- lookAroundViewControllerDidUpdateScene:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidupdatescene(__).md>) — Tells the delegate that the scene updated.

### Entering and exiting full-screen modes

- [- lookAroundViewControllerWillPresentFullScreen:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(__).md>) — Tells the delegate when the view controller is about to enter full-screen mode.
- [- lookAroundViewControllerDidPresentFullScreen:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidpresentfullscreen(__).md>) — Tells the delegate when the view controller enters full-screen mode.
- [- lookAroundViewControllerWillDismissFullScreen:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen(__).md>) — Tells the delegate when the view controller is about to exit full-screen mode.
- [- lookAroundViewControllerDidDismissFullScreen:](<mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdiddismissfullscreen(__).md>) — Tells the delegate when the view controller exits full-screen mode.

## See Also

### Interacting with the controller

- [delegate](mklookaroundviewcontroller/delegate.md) — An object you provide to receive events related to the user’s interaction with the LookAround view controller.
