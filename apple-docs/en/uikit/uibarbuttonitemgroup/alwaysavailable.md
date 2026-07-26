---
title: alwaysAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemgroup/alwaysavailable
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/alwaysavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/alwaysavailable.json'
content_hash: 'sha256:c03a36fc30b3f166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# alwaysAvailable

<sub>Instance Property</sub>

A Boolean value that determines whether the group is always available through the UI.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var alwaysAvailable: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) to ensure that the functionality in this group is available to people regardless of the customization of the groups.

When the value is [true](../../swift/true.md), UIKit places the items in this group in the overflow menu for the [UIUserInterfaceIdiomPhone](../uiuserinterfaceidiom/phone.md) and [UIUserInterfaceIdiomPad](../uiuserinterfaceidiom/pad.md) idioms. This property doesn’t have an effect for the [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) idiom.

## See Also

### Configuring the group

- [barButtonItems](barbuttonitems.md) — The bar button items to display on the bar.
- [representativeItem](representativeitem.md) — The item to display for a group when space is constrained.
