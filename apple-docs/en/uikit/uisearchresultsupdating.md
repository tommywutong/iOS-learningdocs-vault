---
title: UISearchResultsUpdating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchresultsupdating
source_url: 'https://developer.apple.com/documentation/uikit/uisearchresultsupdating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchresultsupdating.json'
content_hash: 'sha256:52a6945526dc9abc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchResultsUpdating

<sub>Protocol</sub>

A set of methods that let you update search results based on information the user enters into the search bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISearchResultsUpdating : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Updating the search bar

- [- updateSearchResultsForSearchController:](<uisearchresultsupdating/updatesearchresults(for_).md>) — Asks the object to update the search results for a specified controller.
- [- updateSearchResultsForSearchController:selectingSearchSuggestion:](<uisearchresultsupdating/updatesearchresults(for_selecting_).md>) — Asks the object to update the search results for a specified controller after the user selects a search suggestion.

## See Also

### Search interface

- [UISearchContainerViewController](uisearchcontainerviewcontroller.md) — A view controller that manages the presentation of search results in your interface.
- [UISearchController](uisearchcontroller.md) — A view controller that manages the display of search results based on interactions with a search bar.
- [UISearchBar](uisearchbar.md) — A specialized view for receiving search-related information from the user.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md) — Create a search interface with a table view of suggested searches.
