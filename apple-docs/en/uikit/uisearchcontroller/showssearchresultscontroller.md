---
title: showsSearchResultsController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/showssearchresultscontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/showssearchresultscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/showssearchresultscontroller.json'
content_hash: 'sha256:3aa34d3a0deceb37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# showsSearchResultsController

<sub>Instance Property</sub>

A Boolean indicating whether the search results controller is visible when the search controller is active.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsSearchResultsController: Bool { get set }
```

## Discussion

Set this property to directly control the visibility of the search results controller. If you set this property, [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) becomes [false](../../swift/false.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
