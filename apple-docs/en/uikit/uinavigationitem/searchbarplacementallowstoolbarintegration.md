---
title: searchBarPlacementAllowsToolbarIntegration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/searchbarplacementallowstoolbarintegration
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementallowstoolbarintegration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/searchbarplacementallowstoolbarintegration.json'
content_hash: 'sha256:ab6b627425abf0dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# searchBarPlacementAllowsToolbarIntegration

<sub>Instance Property</sub>

A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchBarPlacementAllowsToolbarIntegration: Bool { get set }
```

## Overview

Defaults to [true](../../swift/true.md). Set to [false](../../swift/false.md) to prevent the system from placing the search bar among other [UIToolbar](../uitoolbar.md) items on iPhone.

## See Also

### Integrating search into your interface

- [searchController](searchcontroller.md) — The search controller to integrate into your navigation interface.
- [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [searchBarPlacement](searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementBarButtonItem](searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.
