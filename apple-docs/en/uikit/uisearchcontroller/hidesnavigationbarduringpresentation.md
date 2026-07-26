---
title: hidesNavigationBarDuringPresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/hidesnavigationbarduringpresentation
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/hidesnavigationbarduringpresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/hidesnavigationbarduringpresentation.json'
content_hash: 'sha256:ed5fe37fb2e231d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# hidesNavigationBarDuringPresentation

<sub>Instance Property</sub>

A Boolean indicating whether to hide the navigation bar when searching.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hidesNavigationBarDuringPresentation: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md).

## See Also

### Configuring the search interface

- [obscuresBackgroundDuringPresentation](obscuresbackgroundduringpresentation.md) — A Boolean indicating whether to obscure the underlying content during a search.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
