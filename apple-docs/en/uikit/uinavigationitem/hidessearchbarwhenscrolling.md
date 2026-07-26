---
title: hidesSearchBarWhenScrolling
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/hidessearchbarwhenscrolling
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/hidessearchbarwhenscrolling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/hidessearchbarwhenscrolling.json'
content_hash: 'sha256:0a95e1be874fa9cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# hidesSearchBarWhenScrolling

<sub>Instance Property</sub>

A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hidesSearchBarWhenScrolling: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the search bar is visible only when the scroll position equals the top of your content view. When the user scrolls down, the search bar collapses into the navigation bar. Scrolling back to the top reveals the search bar again. When the value of this property is [false](../../swift/false.md), the search bar remains regardless of the current scroll position.

You must configure the [searchController](searchcontroller.md) property for this property to have any effect. The navigation controller hides and shows only the search bar provided by the search controller in that property.

## See Also

### Integrating search into your interface

- [searchController](searchcontroller.md) — The search controller to integrate into your navigation interface.
- [searchBarPlacement](searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementAllowsToolbarIntegration](searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [searchBarPlacementBarButtonItem](searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.
