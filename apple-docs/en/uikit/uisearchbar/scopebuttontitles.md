---
title: scopeButtonTitles
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/scopebuttontitles
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/scopebuttontitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/scopebuttontitles.json'
content_hash: 'sha256:dfcd533f5a188cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# scopeButtonTitles

<sub>Instance Property</sub>

An array of strings indicating the titles of the scope buttons.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scopeButtonTitles: [String]? { get set }
```

## Discussion

The order of the strings in the array indicates the order that the corresponding buttons will be displayed, from left to right. The index in the array corresponds to the index used in [selectedScopeButtonIndex](selectedscopebuttonindex.md).

## See Also

### Configuring scope bar buttons

- [selectedScopeButtonIndex](selectedscopebuttonindex.md) — The index of the selected scope button.
- [showsScopeBar](showsscopebar.md) — Specifies whether the scope bar is displayed.
- [- setShowsScopeBar:animated:](<setshowsscope(__animated_).md>) — Specifies whether the scope bar is displayed, optionally using an animation.
