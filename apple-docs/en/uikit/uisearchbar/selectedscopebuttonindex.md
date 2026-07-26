---
title: selectedScopeButtonIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/selectedscopebuttonindex
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/selectedscopebuttonindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/selectedscopebuttonindex.json'
content_hash: 'sha256:e8301a6c528ca088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# selectedScopeButtonIndex

<sub>Instance Property</sub>

The index of the selected scope button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedScopeButtonIndex: Int { get set }
```

## Discussion

The indexes of the scope buttons are determined by the indexes of the strings in [scopeButtonTitles](scopebuttontitles.md).

## See Also

### Configuring scope bar buttons

- [scopeButtonTitles](scopebuttontitles.md) — An array of strings indicating the titles of the scope buttons.
- [showsScopeBar](showsscopebar.md) — Specifies whether the scope bar is displayed.
- [- setShowsScopeBar:animated:](<setshowsscope(__animated_).md>) — Specifies whether the scope bar is displayed, optionally using an animation.
