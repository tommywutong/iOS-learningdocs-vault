---
title: searchBarPlacementAllowsExternalIntegration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/searchbarplacementallowsexternalintegration
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementallowsexternalintegration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/searchbarplacementallowsexternalintegration.json'
content_hash: 'sha256:21c509b1687b1fd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# searchBarPlacementAllowsExternalIntegration

<sub>Instance Property</sub>

A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchBarPlacementAllowsExternalIntegration: Bool { get set }
```

## Overview

Set this value to indicate whether an object at a higher scope may take the search bar and integrate it somewhere other than the navigation bar (or toolbar) directly associated with this navigation item. [UISplitViewController](../uisplitviewcontroller.md) uses this to allow Mac-like placement of the search bar on iPad. Defaults to [false](../../swift/false.md).

Set to [true](../../swift/true.md) to allow the containing [UISplitViewController](../uisplitviewcontroller.md) to place the search bar in the navigation bar for the trailingmost column independent of the column used for this view controller. Ignored when [searchController](searchcontroller.md) is `nil`, when [searchBarPlacement](searchbarplacement-swift.property.md) is [UINavigationItemSearchBarPlacementStacked](searchbarplacement-swift.enum/stacked.md), or when not contained in a [UISplitViewController](../uisplitviewcontroller.md).

When the top view controller’s navigation item has this property set to [true](../../swift/true.md) in more than one column at the same time, only one will be respected; the columns are checked in order of [UISplitViewControllerColumnInspector](../uisplitviewcontroller/column/inspector.md), [UISplitViewControllerColumnSecondary](../uisplitviewcontroller/column/secondary.md), [UISplitViewControllerColumnSupplementary](../uisplitviewcontroller/column/supplementary.md), [UISplitViewControllerColumnPrimary](../uisplitviewcontroller/column/primary.md). If the search bar has a scope bar, the scope bar will not be moved into a different column.

## See Also

### Integrating search into your interface

- [searchController](searchcontroller.md) — The search controller to integrate into your navigation interface.
- [hidesSearchBarWhenScrolling](hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [searchBarPlacement](searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsToolbarIntegration](searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [searchBarPlacementBarButtonItem](searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.
