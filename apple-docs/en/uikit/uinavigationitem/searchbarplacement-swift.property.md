---
title: searchBarPlacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/searchbarplacement-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/searchbarplacement-swift.property.json'
content_hash: 'sha256:8e9ecdce96299680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# searchBarPlacement

<sub>Instance Property</sub>

The placement of the search bar in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var searchBarPlacement: UINavigationItem.SearchBarPlacement { get }
```

## Discussion

Use this property to determine the actual search bar placement when the [preferredSearchBarPlacement](preferredsearchbarplacement.md) is [UINavigationItemSearchBarPlacementAutomatic](searchbarplacement-swift.enum/automatic.md).

This property only applies when the navigation item has a [searchController](searchcontroller.md).

## See Also

### Integrating search into your interface

- [searchController](searchcontroller.md) — The search controller to integrate into your navigation interface.
- [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementAllowsToolbarIntegration](searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [searchBarPlacementBarButtonItem](searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.
