---
title: 'updateSearchResults(for:selecting:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:selecting:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:selecting:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchresultsupdating/updatesearchresults%28for%3Aselecting%3A%29.json'
content_hash: 'sha256:6188cddb58721c73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchResultsUpdating](../uisearchresultsupdating.md)

# updateSearchResults(for:selecting:)

<sub>Instance Method</sub>

Asks the object to update the search results for a specified controller after the user selects a search suggestion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func updateSearchResults(for searchController: UISearchController, selecting searchSuggestion: any UISearchSuggestion)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object used as the search bar.

- `searchSuggestion` — The suggestion the user selected.

## Discussion

The system calls this method when the user selects a search suggestion. Perform any required filtering and updating of search results or suggestions inside of this method.

## See Also

### Updating the search bar

- [- updateSearchResultsForSearchController:](<updatesearchresults(for_).md>) — Asks the object to update the search results for a specified controller.
