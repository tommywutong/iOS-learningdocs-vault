---
title: ignoresSearchSuggestionsForSearchBarPlacementStacked
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.json'
content_hash: 'sha256:39bbd0d00bf25316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# ignoresSearchSuggestionsForSearchBarPlacementStacked

<sub>Instance Property</sub>

A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool { get set }
```

## Discussion

Defaults to [false](../../swift/false.md). To prevent the search controller from creating and presenting a search suggestions view controller when the [searchBarPlacement](searchbarplacement.md) is [UINavigationItemSearchBarPlacementStacked](../uinavigationitem/searchbarplacement-swift.enum/stacked.md), set to [true](../../swift/true.md) when you create the search controller.

If you set this value to [true](../../swift/true.md) after the search controller has already displayed search suggestions, it hides the search suggestions view controller and won’t display it again until you set the value to [false](../../swift/false.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
