---
title: 'updateSearchResults(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchresultsupdating/updatesearchresults%28for%3A%29.json'
content_hash: 'sha256:b49d32f7e9696b8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchResultsUpdating](../uisearchresultsupdating.md)

# updateSearchResults(for:)

<sub>Instance Method</sub>

Asks the object to update the search results for a specified controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateSearchResults(for searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object used as the search bar.

## Discussion

The system calls this method when the search bar becomes the first responder or the search bar’s text changes. Perform any required filtering and updating of search results or suggestions inside of this method.

## See Also

### Updating the search bar

- [- updateSearchResultsForSearchController:selectingSearchSuggestion:](<updatesearchresults(for_selecting_).md>) — Asks the object to update the search results for a specified controller after the user selects a search suggestion.
