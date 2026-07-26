---
title: 'searchBar(_:selectedScopeButtonIndexDidChange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbar(_:selectedscopebuttonindexdidchange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:selectedscopebuttonindexdidchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbar%28_%3Aselectedscopebuttonindexdidchange%3A%29.json'
content_hash: 'sha256:75b3ff5f77183b06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBar(_:selectedScopeButtonIndexDidChange:)

<sub>Instance Method</sub>

Tells the delegate that the scope button selection changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBar(_ searchBar: UISearchBar, selectedScopeButtonIndexDidChange selectedScope: Int)
```

## Parameters

- `searchBar` — The search bar that was tapped.

- `selectedScope` — The index of the selected scope button (see [selectedScopeButtonIndex](../uisearchbar/selectedscopebuttonindex.md)).
