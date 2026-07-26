---
title: isTranslucent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/istranslucent
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/istranslucent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/istranslucent.json'
content_hash: 'sha256:20da7822f5e6ac61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# isTranslucent

<sub>Instance Property</sub>

A Boolean value that indicates whether the search bar is translucent (true) or not (false).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isTranslucent: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). If the search bar has a custom background image, the default is [true](../../swift/true.md) if any pixel of the image has an alpha value of less than `1.0`, and [false](../../swift/false.md) otherwise.

If you set this property to [true](../../swift/true.md) on a search bar with an opaque custom background image, the search bar will apply a system opacity less than `1.0` to the image.

If you set this property to [false](../../swift/false.md) on a search bar with a translucent custom background image, the search bar provides an opaque background for the image using black if the search bar has [UIBarStyleBlack](../uibarstyle/black.md) style, white if the search bar has [UIBarStyleDefault](../uibarstyle/default.md), or the search bar’s [barTintColor](bartintcolor.md) if a custom value is defined.

## See Also

### Configuring the search bar

- [enabled](isenabled.md) — A Boolean value indicating whether the search bar is in the enabled state.
- [barTintColor](bartintcolor.md) — The tint color to apply to the search bar background.
- [searchBarStyle](searchbarstyle.md) — A search bar style that specifies the search bar’s appearance.
- [Style](style.md) — Specifies whether the search bar has a background.
- [tintColor](tintcolor.md) — The tint color to apply to key elements in the search bar.
- [barStyle](barstyle.md) — A bar style that specifies the search bar’s appearance.
- [UIBarStyle](../uibarstyle.md) — Defines the stylistic appearance of different types of views.
