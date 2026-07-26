---
title: searchSuggestions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/searchsuggestions
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/searchsuggestions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/searchsuggestions.json'
content_hash: 'sha256:d6d4a62fc3b82986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# searchSuggestions

<sub>Instance Property</sub>

A list of suggestions to offer as shortcuts below the search field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var searchSuggestions: [any UISearchSuggestion]? { get set }
```

## Discussion

Provide search suggestions to help people complete their query quickly. Update the suggestions as a person types by implementing [- updateSearchResultsForSearchController:](<../uisearchresultsupdating/updatesearchresults(for_).md>).

The presentation of the search suggestions varies according to the platform and [searchBarPlacement](../uinavigationitem/searchbarplacement-swift.property.md):

- In tvOS, the suggestions appear in a list below the keyboard.
- In iOS, the suggestions appear in a menu below the search field when the search bar placement is [UINavigationItemSearchBarPlacementInline](../uinavigationitem/searchbarplacement-swift.enum/inline.md), and in a list that overlays the [searchResultsController](searchresultscontroller.md) when the search bar placement is [UINavigationItemSearchBarPlacementStacked](../uinavigationitem/searchbarplacement-swift.enum/stacked.md). To prevent the search controller from creating and presenting a search suggestions view controller when the [searchBarPlacement](searchbarplacement.md) is [UINavigationItemSearchBarPlacementStacked](../uinavigationitem/searchbarplacement-swift.enum/stacked.md), set [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) to [true](../../swift/true.md) when you create the search controller.

When you assign new suggestions to this property, the suggestions onscreen refresh automatically. When a person selects a suggestion, the system sets this property to `nil` and dismisses the search suggestions menu. Implement [- updateSearchResultsForSearchController:selectingSearchSuggestion:](<../uisearchresultsupdating/updatesearchresults(for_selecting_).md>) to execute any necessary updates when a person selects a suggestion.

> [!note] Note
> In tvOS, when a person selects a search suggestion, the search controller automatically updates the search bar’s [text](../uisearchbar/text.md) according to the value of [localizedSuggestion](../uisearchsuggestion/localizedsuggestion.md).

If the search suggestions menu dismisses for other reasons, such as a person tapping outside the search bar, [searchSuggestions](searchsuggestions.md) doesn’t reset to `nil` immediately. The system sets [searchSuggestions](searchsuggestions.md) to `nil` only when a person interacts with search directly — for example, by typing in the search field, canceling search, or changing the search scope using the search bar’s scope bar. To dismiss the menu manually, set this property to `nil` or `[]`.

## See Also

### Providing search suggestions

- [ignoresSearchSuggestionsForSearchBarPlacementStacked](ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [UISearchSuggestionItem](../uisearchsuggestionitem.md) — A selectable search parameter.
- [UISearchSuggestion](../uisearchsuggestion.md) — A set of attributes that a selectable search suggestion must provide.
