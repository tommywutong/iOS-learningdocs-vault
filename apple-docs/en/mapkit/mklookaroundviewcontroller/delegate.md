---
title: delegate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklookaroundviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundviewcontroller/delegate.json'
content_hash: 'sha256:cf8074783e92e271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLookAroundViewController](../mklookaroundviewcontroller.md)

# delegate

<sub>Instance Property</sub>

An object you provide to receive events related to the user’s interaction with the LookAround view controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@IBOutlet weak var delegate: (any MKLookAroundViewControllerDelegate)? { get set }
```

## See Also

### Interacting with the controller

- [MKLookAroundViewControllerDelegate](../mklookaroundviewcontrollerdelegate.md) — Methods you implement to respond to changes in the LookAround view controller.
