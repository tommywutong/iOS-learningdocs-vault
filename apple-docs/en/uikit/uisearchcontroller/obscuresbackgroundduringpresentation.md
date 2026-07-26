---
title: obscuresBackgroundDuringPresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/obscuresbackgroundduringpresentation
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/obscuresbackgroundduringpresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/obscuresbackgroundduringpresentation.json'
content_hash: 'sha256:8a8cb8e9bdd9f739'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# obscuresBackgroundDuringPresentation

<sub>Instance Property</sub>

A Boolean indicating whether to obscure the underlying content during a search.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var obscuresBackgroundDuringPresentation: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the search controller obscures the view controller containing your searchable content as soon as the user interacts with the search bar. When this property is [false](../../swift/false.md), the search controller doesn’t obscure the original view controller. This property controls only whether the original view controller is initially obscured. When the user enters text in the search bar, the search controller immediately displays the search results controller with the results.

If you use the same view controller to display the searchable content and search results, it’s recommended that you set this property to [false](../../swift/false.md). The default value of this property is [true](../../swift/true.md).

## See Also

### Configuring the search interface

- [hidesNavigationBarDuringPresentation](hidesnavigationbarduringpresentation.md) — A Boolean indicating whether to hide the navigation bar when searching.
- [automaticallyShowsCancelButton](automaticallyshowscancelbutton.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [automaticallyShowsSearchResultsController](automaticallyshowssearchresultscontroller.md) — A Boolean indicating whether the search controller manages the visibility of its results controller.
- [showsSearchResultsController](showssearchresultscontroller.md) — A Boolean indicating whether the search results controller is visible when the search controller is active.
- [searchBarPlacement](searchbarplacement.md) — The placement of the search bar in the navigation bar.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [automaticallyShowsScopeBar](automaticallyshowsscopebar.md) — A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar. _(deprecated)_
- [scopeBarActivation](scopebaractivation-swift.property.md) — A mode that determines when the search controller shows and hides the scope bar.
- [ScopeBarActivation](scopebaractivation-swift.enum.md) — Constants that specify the modes for showing and hiding the scope bar.
