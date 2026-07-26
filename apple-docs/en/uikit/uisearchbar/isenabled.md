---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/isenabled.json'
content_hash: 'sha256:d2bdc3c926703392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the search bar is in the enabled state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Set the value of this property to `true` to enable the search bar or `false` to disable it. An enabled search bar responds to user interactions; a disabled search bar ignores touch events and takes on a disabled appearance.

If the search bar is associated with a [UINavigationItem](../uinavigationitem.md) with [UINavigationItemSearchBarPlacementInline](../uinavigationitem/searchbarplacement-swift.enum/inline.md), then the minimized (icon-only) [UISearchBar](../uisearchbar.md) won’t grow to the text field while [enabled](isenabled.md) is `false`.

The default value of this property is `true` for a newly created search bar. You can set the search bar’s initial enabled state in your storyboard file.

## See Also

### Configuring the search bar

- [barTintColor](bartintcolor.md) — The tint color to apply to the search bar background.
- [searchBarStyle](searchbarstyle.md) — A search bar style that specifies the search bar’s appearance.
- [Style](style.md) — Specifies whether the search bar has a background.
- [tintColor](tintcolor.md) — The tint color to apply to key elements in the search bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [barStyle](barstyle.md) — A bar style that specifies the search bar’s appearance.
- [UIBarStyle](../uibarstyle.md) — Defines the stylistic appearance of different types of views.
