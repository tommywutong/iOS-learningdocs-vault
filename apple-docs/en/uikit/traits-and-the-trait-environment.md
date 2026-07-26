---
title: Traits and the trait environment
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/traits-and-the-trait-environment
source_url: 'https://developer.apple.com/documentation/uikit/traits-and-the-trait-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/traits-and-the-trait-environment.json'
content_hash: 'sha256:41a62b46fbc11295'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# Traits and the trait environment

<sub>API Collection</sub>

Get information about traits and the environment in which your app runs, and share data with your view hierarchy.

## Overview

Traits represent independent pieces of data that UIKit automatically distributes through your app’s view and view controller hierarchies. The trait system provides a unified way to share configuration information, making it easier to build adaptive interfaces that respond to changes in device orientation, appearance modes, accessibility settings, and custom app states.

The trait system propagates values from the top of the hierarchy downward. When you modify a trait at any level using trait overrides, that change affects the modified object and all of its descendants. Setting a trait override on a window scene affects all view controllers and views within that scene. Setting a trait override on a specific view affects only that view and its subviews.

Use custom traits to propagate data that needs to flow through these parts of your view hierarchy:

- Window scene ([UIWindowScene](uiwindowscene.md))
- Window ([UIWindow](uiwindow.md))
- Presentation controller ([UIPresentationController](uipresentationcontroller.md))
- View controller ([UIViewController](uiviewcontroller.md))
- View ([UIView](uiview.md))
- Subview ([UIView](uiview.md))

Custom traits are particularly useful for:

- Configuration settings that affect entire sections of your interface
- Appearance states that need to cascade through view hierarchies
- Custom app themes or styling modes
- Feature flags that enable or disable UI elements

Avoid using custom traits in cases where you can directly set properties on a view controller, view, or subview.

## Topics

### Essentials

- [Adapting your app when traits change](adapting-your-app-when-traits-change.md) — Find out when system changes happen that affect your app, then update your app efficiently.

### Observing and managing traits

- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — A type that calls your code in reaction to changes in the trait environment.
- [UIMutableTraits](uimutabletraits-13ja5.md) — A mutable container of traits.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.

### Custom traits

- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md) — Share data that needs to flow hierarchically across multiple levels of your view hierarchy.
- [UIMutableTraits](uimutabletraits-13ja5.md) — A mutable container of traits.
- [UITrait](uitrait-9423.md) — A type representing a trait in a trait collection.
- [UITraitDefinition](uitraitdefinition-64c15.md) — A type representing a trait in a trait collection.

## See Also

### Adaptivity and traits

- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md) — Change images and resources dynamically when the screen gamut on your device changes.
