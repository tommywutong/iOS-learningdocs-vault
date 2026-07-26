---
title: Appearance customization
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/appearance-customization
source_url: 'https://developer.apple.com/documentation/uikit/appearance-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/appearance-customization.json'
content_hash: 'sha256:b0575097b429da6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Appearance customization

<sub>API Collection</sub>

Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.

## Topics

### Liquid Glass effects

- [UIGlassEffect](uiglasseffect.md) — A visual effect that renders a glass material.
- [UIGlassContainerEffect](uiglasscontainereffect.md) — A `UIGlassContainerEffect` renders multiple glass elements into a combined effect.

### Interacting with adjacent views

- [UIBackgroundExtensionView](uibackgroundextensionview.md) — A view that extends content to fill its own bounds.
- [UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md) — Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.

### Dark Mode

- [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md) — Update colors, images, and behaviors so that your app adapts automatically when Dark Mode is active.
- [Adopting iOS Dark Mode](adopting-ios-dark-mode.md) — Adopt Dark Mode in your iOS app by using dynamic colors and visual effects.

### Appearance and content

- [Configurations](configurations.md) — Specify the appearance and content of your views and cells using configurations.

### Navigation bar appearance

- [UINavigationBarAppearance](uinavigationbarappearance.md) — An object for customizing the appearance of a navigation bar.

### Toolbar appearance

- [UIToolbarAppearance](uitoolbarappearance.md) — An object for customizing the appearance of a toolbar.

### Tab bar appearance

- [UITabBarAppearance](uitabbarappearance.md) — An object for customizing the appearance of a tab bar.
- [UITabBarItemAppearance](uitabbaritemappearance.md) — An object for customizing the appearance of tab bar items.
- [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) — A data object containing the specific customizations for tab bar items in a particular state.

### Shared appearance

- [UIBarAppearance](uibarappearance.md) — An object for customizing the basic appearance of system bars.
- [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) — An object for customizing the appearance of bar button items.
- [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) — A data object containing the specific customizations for a bar button item in a particular state.

### Appearance proxies

- [UIAppearance](uiappearance.md) — A collection of methods that gives you access to the appearance proxy for a class.
- [UIAppearanceContainer](uiappearancecontainer.md) — A protocol that a class must adopt to allow appearance customization using the [UIAppearance](uiappearance.md) API.

## See Also

### User interface

- [Views and controls](views-and-controls.md) — Present your content onscreen and define the interactions allowed with that content.
- [View controllers](view-controllers.md) — Manage your interface using view controllers and facilitate navigation around your app’s content.
- [View layout](view-layout.md) — Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.
- [Animation and haptics](animation-and-haptics.md) — Provide feedback to users using view-based animations and haptics.
- [Windows and screens](windows-and-screens.md) — Provide a container for your view hierarchies and other content.
