---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/delegate.json'
content_hash: 'sha256:6b025013cfe7e934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlay](../skoverlay.md)

# delegate

<sub>Instance Property</sub>

The overlay’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any SKOverlayDelegate)? { get set }
```

## See Also

### Setting a delegate

- [SKOverlayDelegate](../skoverlaydelegate.md) — Methods for responding to the overlay’s appearance, dismissal, or failure to load.
