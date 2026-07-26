---
title: searchResultsUpdater
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/searchresultsupdater
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/searchresultsupdater'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/searchresultsupdater.json'
content_hash: 'sha256:59f9b80a25b6201f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# searchResultsUpdater

<sub>Instance Property</sub>

The object responsible for updating the contents of the search results controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var searchResultsUpdater: (any UISearchResultsUpdating)? { get set }
```

## Discussion

Assign an object that adopts the [UISearchResultsUpdating](../uisearchresultsupdating.md) protocol. Use the methods of that protocol to search your content and deliver the results to your search results view controller. The object contained by the [searchResultsUpdater](searchresultsupdater.md) property is often the view controller that’s set during initialization.

## See Also

### Managing the search results

- [searchBar](searchbar.md) — The search bar to install in your interface.
- [searchResultsController](searchresultscontroller.md) — The view controller that displays the results of the search.
- [active](isactive.md) — The presented state of the search interface.
