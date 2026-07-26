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
doc_path: /documentation/uikit/uinavigationbar-legacy-customizations
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar-legacy-customizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar-legacy-customizations.json'
content_hash: 'sha256:d23a7bc380d726f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UINavigationBar](uinavigationbar.md)

# Legacy customizations

<sub>API Collection</sub>

Customize appearance information directly on the navigation bar object.

## Overview

In iOS 13 and later, customize your navigation bar using the [standardAppearance](uinavigationbar/standardappearance.md), [compactAppearance](uinavigationbar/compactappearance.md), and [scrollEdgeAppearance](uinavigationbar/scrolledgeappearance.md) properties. You may continue to use these legacy accessors to customize your navigation bar’s appearance directly, but you must update the appearance for different bar configurations yourself.

## Topics

### Configuring the navigation bar

- [Customizing your app’s navigation bar](customizing-your-app-s-navigation-bar.md) — Create custom titles, prompts, and buttons in your app’s navigation bar.

### Setting the bar’s style

- [barStyle](uinavigationbar/barstyle.md) — The navigation bar style that specifies its appearance.
- [UIBarStyle](uibarstyle.md) — Defines the stylistic appearance of different types of views.

### Configuring the title

- [titleTextAttributes](uinavigationbar/titletextattributes.md) — Display attributes for the bar’s title text.
- [largeTitleTextAttributes](uinavigationbar/largetitletextattributes.md) — Display attributes for the bar’s large title text.
- [- titleVerticalPositionAdjustmentForBarMetrics:](<uinavigationbar/titleverticalpositionadjustment(for_).md>) — Returns the title’s vertical position adjustment for given bar metrics.
- [- setTitleVerticalPositionAdjustment:forBarMetrics:](<uinavigationbar/settitleverticalpositionadjustment(__for_).md>) — Sets the title’s vertical position adjustment for given bar metrics.

### Configuring bar button items

- [tintColor](uinavigationbar/tintcolor.md) — The tint color to apply to the navigation items and bar button items.

### Configuring the Back button

- [backIndicatorImage](uinavigationbar/backindicatorimage.md) — The image shown beside the Back button.
- [backIndicatorTransitionMaskImage](uinavigationbar/backindicatortransitionmaskimage.md) — The image used as a mask for content during push and pop transitions.

### Changing the background

- [barTintColor](uinavigationbar/bartintcolor.md) — The tint color to apply to the navigation bar background.
- [- backgroundImageForBarMetrics:](<uinavigationbar/backgroundimage(for_).md>) — Returns the background image for given bar metrics.
- [- setBackgroundImage:forBarMetrics:](<uinavigationbar/setbackgroundimage(__for_).md>) — Sets the background image for given bar metrics.
- [- backgroundImageForBarPosition:barMetrics:](<uinavigationbar/backgroundimage(for_barmetrics_).md>) — Returns the background image to use for a given bar position and set of metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<uinavigationbar/setbackgroundimage(__for_barmetrics_).md>) — Sets the background image to use for a given bar position and set of metrics.

### Adding a shadow

- [shadowImage](uinavigationbar/shadowimage.md) — The shadow image to be used for the navigation bar.

## See Also

### Customizing the bar’s appearance

- [prefersLargeTitles](uinavigationbar/preferslargetitles.md) — A Boolean value that indicates whether the title displays in a large format.
- [standardAppearance](uinavigationbar/standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](uinavigationbar/compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](uinavigationbar/scrolledgeappearance.md) — The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](uinavigationbar/compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [translucent](uinavigationbar/istranslucent.md) — A Boolean value that indicates whether the navigation bar is translucent.
