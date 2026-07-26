---
title: showsScopeBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/showsscopebar
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/showsscopebar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/showsscopebar.json'
content_hash: 'sha256:a1ef77045bb026e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# showsScopeBar

<sub>Instance Property</sub>

Specifies whether the scope bar is displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsScopeBar: Bool { get set }
```

## Discussion

If the search bar is owned by a [UISearchController](../uisearchcontroller.md), then setting this property implicitly sets the search controller’s [automaticallyShowsScopeBar](../uisearchcontroller/automaticallyshowsscopebar.md) property to [false](../../swift/false.md).

## See Also

### Configuring scope bar buttons

- [scopeButtonTitles](scopebuttontitles.md) — An array of strings indicating the titles of the scope buttons.
- [selectedScopeButtonIndex](selectedscopebuttonindex.md) — The index of the selected scope button.
- [- setShowsScopeBar:animated:](<setshowsscope(__animated_).md>) — Specifies whether the scope bar is displayed, optionally using an animation.
