---
title: Legacy customizations
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar-legacy-customizations.json'
content_hash: 'sha256:0ad76e5cc11d1f93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UITabBar](uitabbar.md)

# Legacy customizations

<sub>API Collection</sub>

Customize appearance information directly on the tab bar object.

## Overview

In iOS 13 and later, customize your tab bar using the [standardAppearance](uitabbar/standardappearance.md) property. You may also continue to use these legacy accessors to customize your tab bar’s appearance directly.

## Topics

### Setting the bar’s style

- [barStyle](uitabbar/barstyle.md) — The tab bar style that specifies its appearance.
- [UIBarStyle](uibarstyle.md) — Defines the stylistic appearance of different types of views.

### Configuring tab bar items

- [tintColor](uitabbar/tintcolor.md) — The tint color to apply to the tab bar items.

### Customizing item spacing

- [itemPositioning](uitabbar/itempositioning-swift.property.md) — The positioning scheme for the tab bar items in the tab bar.
- [ItemPositioning](uitabbar/itempositioning-swift.enum.md) — Constants that specify tab bar item positioning.
- [itemSpacing](uitabbar/itemspacing.md) — The amount of space (in points) to use between tab bar items.
- [itemWidth](uitabbar/itemwidth.md) — The width (in points) of tab bar items.

### Configuring selection appearance

- [unselectedItemTintColor](uitabbar/unselecteditemtintcolor.md) — The tint color to apply to unselected tabs.
- [selectionIndicatorImage](uitabbar/selectionindicatorimage.md) — The image to use for the selection indicator.
- [selectedImageTintColor](uitabbar/selectedimagetintcolor.md) — The tint color applied to the selected tab bar item. _(deprecated)_

### Changing the background

- [barTintColor](uitabbar/bartintcolor.md) — The tint color to apply to the tab bar background.
- [backgroundImage](uitabbar/backgroundimage.md) — The custom background image for the tab bar.

### Adding a shadow

- [shadowImage](uitabbar/shadowimage.md) — The shadow image to use for the tab bar.

## See Also

### Customizing tab bar appearance

- [standardAppearance](uitabbar/standardappearance.md) — The appearance settings for a standard-height tab bar.
- [scrollEdgeAppearance](uitabbar/scrolledgeappearance.md) — The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [leadingAccessoryView](uitabbar/leadingaccessoryview.md) — The view at the leading edge of a tab bar on tvOS.
- [trailingAccessoryView](uitabbar/trailingaccessoryview.md) — The view at the trailing edge of a tab bar on tvOS.
- [translucent](uitabbar/istranslucent.md) — A Boolean value that indicates whether the tab bar is translucent.
