---
title: 'lookAroundViewControllerWillPresentFullScreen(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen%28_%3A%29.json'
content_hash: 'sha256:85c1b00745f8272c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLookAroundViewControllerDelegate](../mklookaroundviewcontrollerdelegate.md)

# lookAroundViewControllerWillPresentFullScreen(_:)

<sub>Instance Method</sub>

Tells the delegate when the view controller is about to enter full-screen mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func lookAroundViewControllerWillPresentFullScreen(_ viewController: MKLookAroundViewController)
```

## Parameters

- `viewController` — The [MKLookAroundViewController](../mklookaroundviewcontroller.md).

## See Also

### Entering and exiting full-screen modes

- [- lookAroundViewControllerDidPresentFullScreen:](<lookaroundviewcontrollerdidpresentfullscreen(__).md>) — Tells the delegate when the view controller enters full-screen mode.
- [- lookAroundViewControllerWillDismissFullScreen:](<lookaroundviewcontrollerwilldismissfullscreen(__).md>) — Tells the delegate when the view controller is about to exit full-screen mode.
- [- lookAroundViewControllerDidDismissFullScreen:](<lookaroundviewcontrollerdiddismissfullscreen(__).md>) — Tells the delegate when the view controller exits full-screen mode.
