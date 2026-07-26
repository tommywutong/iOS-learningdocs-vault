---
title: 'searchBarTextDidBeginEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbartextdidbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbartextdidbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbartextdidbeginediting%28_%3A%29.json'
content_hash: 'sha256:13f6de8a41178e18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBarTextDidBeginEditing(_:)

<sub>Instance Method</sub>

Tells the delegate when the user begins editing the search text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBarTextDidBeginEditing(_ searchBar: UISearchBar)
```

## Parameters

- `searchBar` — The search bar that is being edited.

## See Also

### Managing the search text

- [- searchBar:textDidChange:](<searchbar(__textdidchange_).md>) — Tells the delegate that the user changed the search text.
- [- searchBar:shouldChangeTextInRange:replacementText:](<searchbar(__shouldchangetextin_replacementtext_).md>) — Ask the delegate if text in a specified range should be replaced with given text. _(deprecated)_
- [- searchBarShouldBeginEditing:](<searchbarshouldbeginediting(__).md>) — Asks the delegate if editing should begin in the specified search bar.
- [- searchBarShouldEndEditing:](<searchbarshouldendediting(__).md>) — Asks the delegate if editing should stop in the specified search bar.
- [- searchBarTextDidEndEditing:](<searchbartextdidendediting(__).md>) — Tells the delegate that the user finished editing the search text.
