---
title: automaticallyShowsScopeBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 13.0+, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchcontroller/automaticallyshowsscopebar
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowsscopebar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/automaticallyshowsscopebar.json'
content_hash: 'sha256:8e1ad8cde57c5ffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# automaticallyShowsScopeBar

<sub>Instance Property</sub>

A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.

> [!warning] Deprecated
> In iOS, use [scopeBarActivation](scopebaractivation-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyShowsScopeBar: Bool { get set }
```

## Discussion

By default, [UISearchController](../uisearchcontroller.md) shows the search bar’s scope bar when search becomes active and hides it when the user dismisses the search. Set this to [false](../../swift/false.md) if you want to show and hide the scope bar in your own code. If you set the [showsScopeBar](../uisearchbar/showsscopebar.md) property, that also changes this property to [false](../../swift/false.md).

> [!note] Note
> The search bar doesn’t show its scope bar at all if there are fewer than two titles in the search bar’s [scopeButtonTitles](../uisearchbar/scopebuttontitles.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
