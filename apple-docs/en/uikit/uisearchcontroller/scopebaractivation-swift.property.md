---
title: scopeBarActivation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/scopebaractivation-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/scopebaractivation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/scopebaractivation-swift.property.json'
content_hash: 'sha256:1e25137aacd16f08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# scopeBarActivation

<sub>Instance Property</sub>

A mode that determines when the search controller shows and hides the scope bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var scopeBarActivation: UISearchController.ScopeBarActivation { get set }
```

## Discussion

> [!note] Note
> [UISearchBar](../uisearchbar.md) doesn’t show the scope bar if [scopeButtonTitles](../uisearchbar/scopebuttontitles.md) contains fewer than two titles.

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
