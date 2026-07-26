---
title: searchResultsController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/searchresultscontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/searchresultscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/searchresultscontroller.json'
content_hash: 'sha256:21932edb428cfa12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# searchResultsController

<sub>Instance Property</sub>

The view controller that displays the results of the search.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var searchResultsController: UIViewController? { get }
```

## Discussion

When the user enters text in the search bar, the search controller displays this view controller immediately and without any animations. You’re responsible for passing the search results to this view controller so that they can be displayed. You do this using the object in the [searchResultsUpdater](searchresultsupdater.md) property.

When the value of this property is `nil`, the search controller doesn’t present a separate view controller for the search results. Instead, you should display the results using the original view controller containing the search bar and searchable contents.

## See Also

### Managing the search results

- [searchBar](searchbar.md) — The search bar to install in your interface.
- [searchResultsUpdater](searchresultsupdater.md) — The object responsible for updating the contents of the search results controller.
- [active](isactive.md) — The presented state of the search interface.
