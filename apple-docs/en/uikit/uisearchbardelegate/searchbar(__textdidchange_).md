---
title: 'searchBar(_:textDidChange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbar(_:textdidchange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:textdidchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbar%28_%3Atextdidchange%3A%29.json'
content_hash: 'sha256:cdc72c10430e69d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBar(_:textDidChange:)

<sub>Instance Method</sub>

Tells the delegate that the user changed the search text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String)
```

## Parameters

- `searchBar` — The search bar that is being edited.

- `searchText` — The current text in the search text field.

## Discussion

This method is also invoked when text is cleared from the search text field.

## See Also

### Managing the search text

- [- searchBar:shouldChangeTextInRange:replacementText:](<searchbar(__shouldchangetextin_replacementtext_).md>) — Ask the delegate if text in a specified range should be replaced with given text. _(deprecated)_
- [- searchBarShouldBeginEditing:](<searchbarshouldbeginediting(__).md>) — Asks the delegate if editing should begin in the specified search bar.
- [- searchBarTextDidBeginEditing:](<searchbartextdidbeginediting(__).md>) — Tells the delegate when the user begins editing the search text.
- [- searchBarShouldEndEditing:](<searchbarshouldendediting(__).md>) — Asks the delegate if editing should stop in the specified search bar.
- [- searchBarTextDidEndEditing:](<searchbartextdidendediting(__).md>) — Tells the delegate that the user finished editing the search text.
