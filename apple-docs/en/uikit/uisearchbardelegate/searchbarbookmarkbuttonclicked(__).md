---
title: 'searchBarBookmarkButtonClicked(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbarbookmarkbuttonclicked(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarbookmarkbuttonclicked(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbarbookmarkbuttonclicked%28_%3A%29.json'
content_hash: 'sha256:9ebb069db87e2ecb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBarBookmarkButtonClicked(_:)

<sub>Instance Method</sub>

Tells the delegate that the bookmark button was tapped.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchBarBookmarkButtonClicked(_ searchBar: UISearchBar)
```

## Parameters

- `searchBar` — The search bar that was tapped.

## Discussion

There is no automatic bookmark support provided by the search bar. It’s the application’s responsibility to implement this method to perform some action if the bookmark button is tapped by the user.

## See Also

### Related Documentation

- [showsBookmarkButton](../uisearchbar/showsbookmarkbutton.md) — A Boolean value indicating whether the bookmark button is displayed.

### Responding to clicks in search controls

- [- searchBarCancelButtonClicked:](<searchbarcancelbuttonclicked(__).md>) — Tells the delegate that the cancel button was tapped.
- [- searchBarSearchButtonClicked:](<searchbarsearchbuttonclicked(__).md>) — Tells the delegate that the search button was tapped.
- [- searchBarResultsListButtonClicked:](<searchbarresultslistbuttonclicked(__).md>) — Tells the delegate that the search results list button was tapped.
