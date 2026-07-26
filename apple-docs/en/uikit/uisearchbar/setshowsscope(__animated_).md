---
title: 'setShowsScope(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setshowsscope(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setshowsscope(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setshowsscope%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:aec60be4e099650f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setShowsScope(_:animated:)

<sub>Instance Method</sub>

Specifies whether the scope bar is displayed, optionally using an animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setShowsScope(_ show: Bool, animated animate: Bool)
```

## Parameters

- `show` — A Boolean value that indicates whether the scope bar is shown.

- `animate` — A Boolean value that indicates whether the scope bar animates when it appears and disappears.

## Discussion

If the search bar is owned by a [UISearchController](../uisearchcontroller.md), then calling this method implicitly sets the search controller’s [automaticallyShowsScopeBar](../uisearchcontroller/automaticallyshowsscopebar.md) property to [false](../../swift/false.md).

## See Also

### Configuring scope bar buttons

- [scopeButtonTitles](scopebuttontitles.md) — An array of strings indicating the titles of the scope buttons.
- [selectedScopeButtonIndex](selectedscopebuttonindex.md) — The index of the selected scope button.
- [showsScopeBar](showsscopebar.md) — Specifies whether the scope bar is displayed.
