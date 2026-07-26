---
title: searchBarPlacementBarButtonItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/searchbarplacementbarbuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementbarbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/searchbarplacementbarbuttonitem.json'
content_hash: 'sha256:2d0eaa8911c7df35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# searchBarPlacementBarButtonItem

<sub>Instance Property</sub>

An item you use to control the placement of the search bar in a toolbar on iPhone.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchBarPlacementBarButtonItem: UIBarButtonItem { get }
```

## Overview

When [searchBarPlacement](searchbarplacement-swift.property.md) is `.integrated` or `.integratedButton` and a search controller is present, use this bar button item in the view controller’s [toolbarItems](../uiviewcontroller/toolbaritems.md) to control the placement of the search bar among them when the search bar is appearing in the [UIToolbar](../uitoolbar.md) on iPhone. Without this bar button item, the positioning for the search bar defaults to trailingmost for the [UIToolbar](../uitoolbar.md) case.

The system ignores this bar button item during toolbar layout if [searchController](searchcontroller.md) is `nil`. [UIBarButtonItemGroup](../uibarbuttonitemgroup.md) throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) when you include this bar button item in its initialization. [UINavigationItem](../uinavigationitem.md) throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) when you include this bar button item in [leftBarButtonItems](leftbarbuttonitems.md) or [rightBarButtonItems](rightbarbuttonitems.md).

## See Also

### Integrating search into your interface

- [searchController](searchcontroller.md) — The search controller to integrate into your navigation interface.
- [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [searchBarPlacement](searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementAllowsToolbarIntegration](searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
