---
title: prefersLargeTitles
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/preferslargetitles
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/preferslargetitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/preferslargetitles.json'
content_hash: 'sha256:5342cf08c3de94ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# prefersLargeTitles

<sub>Instance Property</sub>

A Boolean value that indicates whether the title displays in a large format.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersLargeTitles: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the navigation bar allows the title to be displayed out-of-line and using a larger font. The navigation item used to build the bar must specify whether it wants its title displayed in the large or small format. Use the [largeTitleDisplayMode](../uinavigationitem/largetitledisplaymode-swift.property.md) property to configure the title’s appearance.

When the property is set to [false](../../swift/false.md), the navigation bar displays the title inline with the other bar button items.

## See Also

### Customizing the bar’s appearance

- [standardAppearance](standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](scrolledgeappearance.md) — The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [translucent](istranslucent.md) — A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md) — Customize appearance information directly on the navigation bar object.
