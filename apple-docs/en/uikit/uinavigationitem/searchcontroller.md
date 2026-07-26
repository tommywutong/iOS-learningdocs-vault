---
title: searchController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/searchcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/searchcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/searchcontroller.json'
content_hash: 'sha256:2accdec0dab80c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# searchController

<sub>Instance Property</sub>

The search controller to integrate into your navigation interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var searchController: UISearchController? { get set }
```

## Discussion

When a view controller in your navigation interface supports search, assign the corresponding search controller to this property. The navigation controller integrates the search bar from your search controller into the navigation bar interface, presenting a single bar for both search and navigation. Use the [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) property to control the visibility of the search bar when scrolling.

## See Also

### Integrating search into your interface

- [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [searchBarPlacement](searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementAllowsToolbarIntegration](searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [searchBarPlacementBarButtonItem](searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.
