---
title: bottomBar
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/pagedpickersubscriptionstorecontrolstyle/placement/bottombar
source_url: 'https://developer.apple.com/documentation/storekit/pagedpickersubscriptionstorecontrolstyle/placement/bottombar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/pagedpickersubscriptionstorecontrolstyle/placement/bottombar.json'
content_hash: 'sha256:2157f36ca85ed9ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [PagedPickerSubscriptionStoreControlStyle](../../pagedpickersubscriptionstorecontrolstyle.md) · [Placement](../placement.md)

# bottomBar

<sub>Type Property</sub>

A placement that locates the paged picker in a bar near the bottom of the main scroll view in a subscription store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var bottomBar: PagedPickerSubscriptionStoreControlStyle.Placement { get }
```

## Discussion

The bottom bar conditonally applies a special visual treatment when it overlaps the main content of the subscription store view. The content within the bottom bar doesn’t scroll with the rest of the content in the main scroll view.

## See Also

### Getting a placement

- [automatic](automatic.md)
- [buttonsInBottomBar](buttonsinbottombar.md) — A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.
- [scrollView](scrollview.md)
