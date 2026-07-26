---
title: 'searchBar(_:shouldChangeTextInRanges:replacementText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextinranges:replacementtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextinranges:replacementtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbardelegate/searchbar%28_%3Ashouldchangetextinranges%3Areplacementtext%3A%29.json'
content_hash: 'sha256:9763b4268ea6f225'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBarDelegate](../uisearchbardelegate.md)

# searchBar(_:shouldChangeTextInRanges:replacementText:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextInRanges ranges: [NSValue], replacementText: String) -> Bool
```

## Parameters

- `searchBar` — The search bar asking the delegate

- `ranges` — The ranges of the text that should be deleted before replacing

- `replacementText` — The replacement text

## Return Value

Returns true if the text at the `ranges` should be replaced.

## Discussion

Asks the delegate if the text at the specified `ranges` should be replaced with `text`.

If this method returns YES then the search bar will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementText` before deleting the text at the other ranges. If the delegate does not implement this method then the `searchBar:shouldChangeTextInRange:replacementText:` method will be called and passed the union range instead. If the delegate also does not implement that method then YES is assumed.
