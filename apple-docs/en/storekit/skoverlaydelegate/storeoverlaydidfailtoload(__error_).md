---
title: 'storeOverlayDidFailToLoad(_:error:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlaydelegate/storeoverlaydidfailtoload(_:error:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfailtoload(_:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlaydelegate/storeoverlaydidfailtoload%28_%3Aerror%3A%29.json'
content_hash: 'sha256:30052d1cab33babe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKOverlayDelegate](../skoverlaydelegate.md)

# storeOverlayDidFailToLoad(_:error:)

<sub>Instance Method</sub>

Indicates that an overlay failed to load.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func storeOverlayDidFailToLoad(_ overlay: SKOverlay, error: any Error)
```

## Parameters

- `overlay` — An overlay object that failed to load.

- `error` — An indication of why the overlay failed to load.

## Discussion

Common cases for a failure when loading an overlay are:

- Using invalid iTunes identifiers.
- Trying to present an overlay for media that’s not an app.
- Trying to present an overlay from an app extension or the simulator.
