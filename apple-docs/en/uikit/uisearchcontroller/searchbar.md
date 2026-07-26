---
title: searchBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/searchbar
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/searchbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/searchbar.json'
content_hash: 'sha256:60cb13b9d7b6d3a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# searchBar

<sub>Instance Property</sub>

The search bar to install in your interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var searchBar: UISearchBar { get }
```

## Discussion

Before presenting your searchable content, install the search bar somewhere in your view hierarchy. The search bar becomes the starting point for searching your contents. Interactions with the search bar are handled automatically by the `UISearchController` object, which notifies the object in the [searchResultsUpdater](searchresultsupdater.md) property whenever the search information changes.

You can provide a custom search bar by subclassing [UISearchController](../uisearchcontroller.md) and overriding this property to return your custom implementation. To ensure the correct configuration of your search bar, lazily initialize it when it’s first requested, as shown in the code below.

**Swift**

```swift
class CustomSearchController: UISearchController {

    // Mark this property as lazy to defer initialization until
    // the searchBar property is called.
    private lazy var customSearchBar = CustomSearchBar()

    // Override this property to return your custom implementation.
    override var searchBar: UISearchBar { customSearchBar }
}
```

**Objective-C**

```objc
@implementation CustomSearchController {
    CustomSearchBar *customSearchBar;
}

// Override this property to return your custom implementation.
- (UISearchBar *)searchBar {
    // Lazily initialize your custom search bar.
    if (!customSearchBar) {
        customSearchBar = [[CustomSearchBar alloc] init];
    }
    return customSearchBar;
}

@end
```

## See Also

### Managing the search results

- [searchResultsUpdater](searchresultsupdater.md) — The object responsible for updating the contents of the search results controller.
- [searchResultsController](searchresultscontroller.md) — The view controller that displays the results of the search.
- [active](isactive.md) — The presented state of the search interface.
