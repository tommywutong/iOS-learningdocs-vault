---
title: showsCancelButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/showscancelbutton
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/showscancelbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/showscancelbutton.json'
content_hash: 'sha256:354c079106f96091'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# showsCancelButton

<sub>Instance Property</sub>

A Boolean value indicating whether the cancel button is displayed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsCancelButton: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the cancel button is displayed if the app is running on iPhone. The value of this property is ignored, and no cancel button is displayed, for apps running on iPad. The default value is [false](../../swift/false.md).

## See Also

### Configuring the search interface

- [showsBookmarkButton](showsbookmarkbutton.md) — A Boolean value indicating whether the bookmark button is displayed.
- [- setShowsCancelButton:animated:](<setshowscancelbutton(__animated_).md>) — Sets the display state of the cancel button optionally with animation.
- [showsSearchResultsButton](showssearchresultsbutton.md) — A Boolean value indicating whether the search results button is displayed.
- [searchResultsButtonSelected](issearchresultsbuttonselected.md) — A Boolean value indicating whether the search results button is selected.
