---
title: Legacy customizations
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar-legacy-customizations.json'
content_hash: 'sha256:84f353219f4447dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md) · [UIToolbar](uitoolbar.md)

# Legacy customizations

<sub>API Collection</sub>

Customize appearance information directly on the toolbar object.

## Overview

In iOS 13 and later, customize your toolbar using the [standardAppearance](uitoolbar/standardappearance.md) and [compactAppearance](uitoolbar/compactappearance.md) properties. You may continue to use these legacy accessors to customize your toolbar’s appearance directly, but you must update the appearance for different bar configurations yourself.

## Topics

### Setting the bar’s style

- [barStyle](uitoolbar/barstyle.md) — The toolbar style that specifies its appearance.
- [UIBarStyle](uibarstyle.md) — Defines the stylistic appearance of different types of views.

### Configuring bar button items

- [tintColor](uitoolbar/tintcolor.md) — The tint color to apply to the bar button items.

### Changing the background

- [barTintColor](uitoolbar/bartintcolor.md) — The tint color to apply to the toolbar background.
- [- backgroundImageForToolbarPosition:barMetrics:](<uitoolbar/backgroundimage(fortoolbarposition_barmetrics_).md>) — Returns the image to use for the background in a given position and with given metrics.
- [- setBackgroundImage:forToolbarPosition:barMetrics:](<uitoolbar/setbackgroundimage(__fortoolbarposition_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.

### Adding a shadow

- [- shadowImageForToolbarPosition:](<uitoolbar/shadowimage(fortoolbarposition_).md>) — Returns the image to use for the toolbar shadow in a given position.
- [- setShadowImage:forToolbarPosition:](<uitoolbar/setshadowimage(__fortoolbarposition_).md>) — Sets the image to use for the toolbar shadow in a given position.

## See Also

### Customizing appearance

- [standardAppearance](uitoolbar/standardappearance.md) — The appearance settings to use for a standard-height toolbar.
- [compactAppearance](uitoolbar/compactappearance.md) — The appearance settings to use for a compact-height toolbar.
- [scrollEdgeAppearance](uitoolbar/scrolledgeappearance.md) — The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [compactScrollEdgeAppearance](uitoolbar/compactscrolledgeappearance.md) — The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [translucent](uitoolbar/istranslucent.md) — A Boolean value that indicates whether the toolbar is translucent.
