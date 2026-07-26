---
title: automaticallyShowsSearchResultsController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/automaticallyshowssearchresultscontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowssearchresultscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/automaticallyshowssearchresultscontroller.json'
content_hash: 'sha256:861d58fd8340b147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# automaticallyShowsSearchResultsController

<sub>Instance Property</sub>

A Boolean indicating whether the search controller manages the visibility of its results controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var automaticallyShowsSearchResultsController: Bool { get set }
```

## Discussion

The default value for this property is [true](../../swift/true.md). When it’s [true](../../swift/true.md), [UISearchController](../uisearchcontroller.md) automatically shows its results controller based on the contents of its text property. If you set [showsSearchResultsController](showssearchresultscontroller.md), this property becomes [false](../../swift/false.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
