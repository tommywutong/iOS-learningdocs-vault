---
title: 'lookAroundViewControllerWillDismissFullScreen(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen%28_%3A%29.json'
content_hash: 'sha256:4e7f4859f387e709'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLookAroundViewControllerDelegate](../mklookaroundviewcontrollerdelegate.md)

# lookAroundViewControllerWillDismissFullScreen(_:)

<sub>Instance Method</sub>

Tells the delegate when the view controller is about to exit full-screen mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func lookAroundViewControllerWillDismissFullScreen(_ viewController: MKLookAroundViewController)
```

## Parameters

- `viewController` — The [MKLookAroundViewController](../mklookaroundviewcontroller.md).

## See Also

### Entering and exiting full-screen modes

- [- lookAroundViewControllerWillPresentFullScreen:](<lookaroundviewcontrollerwillpresentfullscreen(__).md>) — Tells the delegate when the view controller is about to enter full-screen mode.
- [- lookAroundViewControllerDidPresentFullScreen:](<lookaroundviewcontrollerdidpresentfullscreen(__).md>) — Tells the delegate when the view controller enters full-screen mode.
- [- lookAroundViewControllerDidDismissFullScreen:](<lookaroundviewcontrollerdiddismissfullscreen(__).md>) — Tells the delegate when the view controller exits full-screen mode.
