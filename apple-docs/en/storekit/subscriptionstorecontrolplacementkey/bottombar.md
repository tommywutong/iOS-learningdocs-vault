---
title: bottomBar
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolplacementkey/bottombar
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolplacementkey/bottombar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolplacementkey/bottombar.json'
content_hash: 'sha256:a9498f5f79aa4ce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlPlacementKey](../subscriptionstorecontrolplacementkey.md)

# bottomBar

<sub>Type Property</sub>

A placement that locates the subscription controls in a bar near the bottom of the main scroll view in a subscription store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var bottomBar: SubscriptionStoreControlPlacementKey { get }
```

## Discussion

The bottom bar conditonally applies a special visual treatment when it overlaps the main content of the subscription store view. The content within the bottom bar doesn’t scroll with the rest of the content in the main scroll view.

## See Also

### Placing subscription store controls

- [bottom](bottom.md) — A placement that anchors the subscription controls to the bottom edge of the view.
- [leading](leading.md) — A placement that anchors the subscription controls to the leading edge of the view.
- [scrollView](scrollview.md) — A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [trailing](trailing.md) — A placement that anchors the subscription controls to the trailing edge of the view.
- [buttonsInBottomBar](buttonsinbottombar.md) — A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.
