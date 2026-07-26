---
title: 'setShowsCancelButton(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setshowscancelbutton(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setshowscancelbutton(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setshowscancelbutton%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:90a1e0f2e1be2518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setShowsCancelButton(_:animated:)

<sub>Instance Method</sub>

Sets the display state of the cancel button optionally with animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setShowsCancelButton(_ showsCancelButton: Bool, animated: Bool)
```

## Parameters

- `showsCancelButton` — [true](../../swift/true.md) to display the cancel button, otherwise [false](../../swift/false.md).

- `animated` — [true](../../swift/true.md) to use animation to change the display state of the cancel button, otherwise [false](../../swift/false.md).

## Discussion

Cancel buttons are not displayed for apps running on iPad, even when you specify [true](../../swift/true.md) for the `showsCancelButton` parameter

## See Also

### Configuring the search interface

- [showsBookmarkButton](showsbookmarkbutton.md) — A Boolean value indicating whether the bookmark button is displayed.
- [showsCancelButton](showscancelbutton.md) — A Boolean value indicating whether the cancel button is displayed.
- [showsSearchResultsButton](showssearchresultsbutton.md) — A Boolean value indicating whether the search results button is displayed.
- [searchResultsButtonSelected](issearchresultsbuttonselected.md) — A Boolean value indicating whether the search results button is selected.
