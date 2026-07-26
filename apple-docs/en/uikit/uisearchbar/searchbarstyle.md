---
title: searchBarStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/searchbarstyle
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/searchbarstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/searchbarstyle.json'
content_hash: 'sha256:a61e47e40cc62aef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# searchBarStyle

<sub>Instance Property</sub>

A search bar style that specifies the search bar’s appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var searchBarStyle: UISearchBar.Style { get set }
```

## Discussion

This property can be used together with [barStyle](barstyle.md). The style [UISearchBarStyleMinimal](style/minimal.md) provides no default background color or image but will display one if customized as such.

Custom background and search field images take precedence over this property.

See [Style](style.md) for possible values. The default value is [UISearchBarStyleDefault](style/default.md).

## See Also

### Configuring the search bar

- [enabled](isenabled.md) — A Boolean value indicating whether the search bar is in the enabled state.
- [barTintColor](bartintcolor.md) — The tint color to apply to the search bar background.
- [Style](style.md) — Specifies whether the search bar has a background.
- [tintColor](tintcolor.md) — The tint color to apply to key elements in the search bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [barStyle](barstyle.md) — A bar style that specifies the search bar’s appearance.
- [UIBarStyle](../uibarstyle.md) — Defines the stylistic appearance of different types of views.
