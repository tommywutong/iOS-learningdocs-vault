---
title: 'searchBarSearchButtonClicked(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbarsearchbuttonclicked(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarsearchbuttonclicked(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbarsearchbuttonclicked%28_%3A%29.json'
content_hash: 'sha256:00f41285af862562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBarSearchButtonClicked(_:)

<sub>Instance Method</sub>

Tells the delegate that the search button was tapped.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBarSearchButtonClicked(_ searchBar: UISearchBar)
```

## Parameters

- `searchBar` — The search bar that was tapped.

## Discussion

You should implement this method to begin the search. Use the [text](../uisearchbar/text.md) property of the search bar to get the text. You can also send [- becomeFirstResponder](<../uiresponder/becomefirstresponder().md>) to the search bar to begin editing programmatically.

## See Also

### Responding to clicks in search controls

- [- searchBarBookmarkButtonClicked:](<searchbarbookmarkbuttonclicked(__).md>) — Tells the delegate that the bookmark button was tapped.
- [- searchBarCancelButtonClicked:](<searchbarcancelbuttonclicked(__).md>) — Tells the delegate that the cancel button was tapped.
- [- searchBarResultsListButtonClicked:](<searchbarresultslistbuttonclicked(__).md>) — Tells the delegate that the search results list button was tapped.
