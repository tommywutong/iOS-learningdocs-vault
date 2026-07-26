---
title: isActive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/isactive
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/isactive.json'
content_hash: 'sha256:ff0828efa45bea0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# isActive

<sub>Instance Property</sub>

The presented state of the search interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isActive: Bool { get set }
```

## Discussion

When the user taps in the search field of a managed search bar, the search controller automatically displays the search results controller. Usually, you get the value of this property to determine whether the search results are displayed. However, you can set this property to [true](../../swift/true.md) to force the search interface to appear, even if the user hasn’t tapped in the search field.

The default value of this property is [false](../../swift/false.md).

## See Also

### Managing the search results

- [searchBar](searchbar.md) — The search bar to install in your interface.
- [searchResultsUpdater](searchresultsupdater.md) — The object responsible for updating the contents of the search results controller.
- [searchResultsController](searchresultscontroller.md) — The view controller that displays the results of the search.
