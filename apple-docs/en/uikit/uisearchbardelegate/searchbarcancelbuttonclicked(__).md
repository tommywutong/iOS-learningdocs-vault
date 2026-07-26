---
title: 'searchBarCancelButtonClicked(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbarcancelbuttonclicked(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarcancelbuttonclicked(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbarcancelbuttonclicked%28_%3A%29.json'
content_hash: 'sha256:d42130a639b158ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBarCancelButtonClicked(_:)

<sub>Instance Method</sub>

Tells the delegate that the cancel button was tapped.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchBarCancelButtonClicked(_ searchBar: UISearchBar)
```

## Parameters

- `searchBar` — The search bar that was tapped.

## Discussion

Typically, you implement this method to dismiss the search bar.

## See Also

### Related Documentation

- [showsCancelButton](../uisearchbar/showscancelbutton.md) — A Boolean value indicating whether the cancel button is displayed.

### Responding to clicks in search controls

- [- searchBarBookmarkButtonClicked:](<searchbarbookmarkbuttonclicked(__).md>) — Tells the delegate that the bookmark button was tapped.
- [- searchBarSearchButtonClicked:](<searchbarsearchbuttonclicked(__).md>) — Tells the delegate that the search button was tapped.
- [- searchBarResultsListButtonClicked:](<searchbarresultslistbuttonclicked(__).md>) — Tells the delegate that the search results list button was tapped.
