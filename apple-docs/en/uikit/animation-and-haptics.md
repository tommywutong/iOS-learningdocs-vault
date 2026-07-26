---
title: Animation and haptics
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/animation-and-haptics
source_url: 'https://developer.apple.com/documentation/uikit/animation-and-haptics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/animation-and-haptics.json'
content_hash: 'sha256:01565e93673f6b23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Animation and haptics

<sub>API Collection</sub>

Provide feedback to users using view-based animations and haptics.

## Topics

### Content animations

- [Property-based animations](property-based-animations.md) — Create animations by changing the properties of a view.
- [View controller transitions](view-controller-transitions.md) — Define custom transitions from one view controller to another.
- [Unifying your app’s animations](../swiftui/unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [Optimizing iPhone and iPad apps to support ProMotion displays](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — Improve your app’s visual appearance and save power by requesting preferred refresh rates and synchronizing your animations with the system.

### Physics-based animations

- [UIKit Dynamics](uikit-dynamics.md) — Apply physics-based animations to your views.

### Parallax effects

- [Motion effects](motion-effects.md) — Add subtle motion to views to provide a 3D appearance.

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIFeedbackGenerator](uifeedbackgenerator.md) — The abstract superclass for all feedback generators.
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.

## See Also

### User interface

- [Views and controls](views-and-controls.md) — Present your content onscreen and define the interactions allowed with that content.
- [View controllers](view-controllers.md) — Manage your interface using view controllers and facilitate navigation around your app’s content.
- [View layout](view-layout.md) — Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.
- [Appearance customization](appearance-customization.md) — Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.
- [Windows and screens](windows-and-screens.md) — Provide a container for your view hierarchies and other content.
