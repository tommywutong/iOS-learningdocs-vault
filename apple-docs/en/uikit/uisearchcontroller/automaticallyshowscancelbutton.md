---
title: automaticallyShowsCancelButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/automaticallyshowscancelbutton
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowscancelbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/automaticallyshowscancelbutton.json'
content_hash: 'sha256:5180cb278a82a4f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# automaticallyShowsCancelButton

<sub>Instance Property</sub>

A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyShowsCancelButton: Bool { get set }
```

## Discussion

By default, [UISearchController](../uisearchcontroller.md) shows the search bar’s cancel button when search becomes active and hides it when the user dismisses search. You can take over responsibility for showing and hiding the cancel button by setting this property to [false](../../swift/false.md). If you set the search bar’s [showsCancelButton](../uisearchbar/showscancelbutton.md) property, this property becomes [false](../../swift/false.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
