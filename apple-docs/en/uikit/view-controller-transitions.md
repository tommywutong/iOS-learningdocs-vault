---
title: View controller transitions
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/view-controller-transitions
source_url: 'https://developer.apple.com/documentation/uikit/view-controller-transitions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/view-controller-transitions.json'
content_hash: 'sha256:a10d95f762ef4923'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Animation and haptics](animation-and-haptics.md)

# View controller transitions

<sub>API Collection</sub>

Define custom transitions from one view controller to another.

## Topics

### Essentials

- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md) — Use the fluid zoom transition to provide a continuously interactive and responsive experience in your app.

### Animation delegate

- [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md) — A set of methods that vend objects used to manage a fixed-length or interactive transition between view controllers.

### Non-interactive transitions

- [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) — A set of methods for implementing the animations for a custom view controller transition.
- [UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md) — A set of methods that provide contextual information for transition animations between view controllers.

### Interactive transitions

- [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md) — An object that drives an interactive animation between one view controller and another.
- [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) — A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.
- [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) — An interface for modifying an animation while it’s running.

### Transition coordinators

- [UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md) — A set of methods that provides support for animations associated with a view controller transition.
- [UIViewControllerTransitionCoordinatorContext](uiviewcontrollertransitioncoordinatorcontext.md) — A set of methods that provides information about an in-progress view controller transition.

## See Also

### Content animations

- [Property-based animations](property-based-animations.md) — Create animations by changing the properties of a view.
- [Unifying your app’s animations](../swiftui/unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [Optimizing iPhone and iPad apps to support ProMotion displays](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md) — Improve your app’s visual appearance and save power by requesting preferred refresh rates and synchronizing your animations with the system.
