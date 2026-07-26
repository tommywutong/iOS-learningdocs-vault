---
title: 'searchBar(_:shouldChangeTextIn:replacementText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（27.0 起废弃）, iPadOS 3.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbar%28_%3Ashouldchangetextin%3Areplacementtext%3A%29.json'
content_hash: 'sha256:dc66cdefde2b45be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBar(_:shouldChangeTextIn:replacementText:)

<sub>Instance Method</sub>

Ask the delegate if text in a specified range should be replaced with given text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

## Parameters

- `searchBar` — The search bar that is being edited.

- `range` — The range of the text to be changed.

- `text` — The text to replace existing text in `range`.

## Return Value

[true](../../swift/true.md) if text in `range` should be replaced by `text`, otherwise, [false](../../swift/false.md).

## See Also

### Managing the search text

- [- searchBar:textDidChange:](<searchbar(__textdidchange_).md>) — Tells the delegate that the user changed the search text.
- [- searchBarShouldBeginEditing:](<searchbarshouldbeginediting(__).md>) — Asks the delegate if editing should begin in the specified search bar.
- [- searchBarTextDidBeginEditing:](<searchbartextdidbeginediting(__).md>) — Tells the delegate when the user begins editing the search text.
- [- searchBarShouldEndEditing:](<searchbarshouldendediting(__).md>) — Asks the delegate if editing should stop in the specified search bar.
- [- searchBarTextDidEndEditing:](<searchbartextdidendediting(__).md>) — Tells the delegate that the user finished editing the search text.
