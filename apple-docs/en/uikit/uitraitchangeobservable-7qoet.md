---
title: UITraitChangeObservable
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitchangeobservable-7qoet
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-7qoet.json'
content_hash: 'sha256:a3df57f378501810'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitChangeObservable

<sub>Protocol</sub>

A type that calls your code in reaction to changes in the trait environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UITraitChangeObservable
```

## Overview

Types that conform to `UITraitChangeObservable` can execute your code in response to changes in their trait collection. When you register for trait changes, the system observes the specified traits, and calls your code when any of the observed traits change value.

Keep your trait registrations focused, and avoid doing work not directly relevant to updated traits. Traits may change more than once before the system updates a view, so avoid expensive work in response to trait changes. For example, use the trait change notification to call [- setNeedsDisplay](<uiview/setneedsdisplay().md>), and update your view in [- drawRect:](<uiview/draw(__).md>).

UIKit cleans up registrations at the end of the object lifecycle. Unregister only in the rare situations when you need to dynamically change which traits you observe.

## Relationships

- **Conforming Types**: [UIPresentationController](uipresentationcontroller.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md), [UIWindowScene](uiwindowscene.md)

## Topics

### Observing trait changes

- [registerForTraitChanges:withAction:](uitraitchangeobservable-7qoet/registerfortraitchanges_withaction_.md) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges:withHandler:](uitraitchangeobservable-7qoet/registerfortraitchanges_withhandler_.md) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges:withTarget:action:](uitraitchangeobservable-7qoet/registerfortraitchanges_withtarget_action_.md) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges:](uitraitchangeobservable-7qoet/unregisterfortraitchanges_.md) — Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](uitraitchangehandler.md)
- [UITraitChangeRegistration](uitraitchangeregistration.md)

### Registering traits for observation

- [UITraitAccessibilityContrast](uitraitaccessibilitycontrast-c.class.md) — A class that represents the accessibility contrast setting trait.
- [UITraitActiveAppearance](uitraitactiveappearance-c.class.md) — A class that represents the active appearance trait.
- [UITraitDisplayGamut](uitraitdisplaygamut-c.class.md) — A class that represents the display gamut trait.
- [UITraitDisplayScale](uitraitdisplayscale-c.class.md) — A class that represents the display scale trait.
- [UITraitForceTouchCapability](uitraitforcetouchcapability-c.class.md) — A class that represents the Force Touch capability trait.
- [UITraitHDRHeadroomUsageLimit](uitraithdrheadroomusagelimit-c.class.md) — A class that represents the HDR headroom usage limit trait.
- [UITraitHorizontalSizeClass](uitraithorizontalsizeclass-c.class.md) — A class that represents the horizontal size class trait.
- [UITraitImageDynamicRange](uitraitimagedynamicrange-c.class.md) — A class that represents the image dynamic range trait.
- [UITraitLayoutDirection](uitraitlayoutdirection-c.class.md) — A class that represents the layout direction trait.
- [UITraitLegibilityWeight](uitraitlegibilityweight-c.class.md) — A class that represents the legibility weight trait.
- [UITraitListEnvironment](uitraitlistenvironment-c.class.md) — A class that represents the list environment trait.
- [UITraitPreferredContentSizeCategory](uitraitpreferredcontentsizecategory-c.class.md) — A class that represents the preferred content size category trait.
- [UITraitResolvesNaturalAlignmentWithBaseWritingDirection](uitraitresolvesnaturalalignmentwithbasewritingdirection-c.class.md) — A class that represents the trait that indicates whether the system resolves natural alignment with base writing direction.
- [UITraitSceneCaptureState](uitraitscenecapturestate-c.class.md) — A class that represents the scene capture state trait.
- [UITraitSplitViewControllerLayoutEnvironment](uitraitsplitviewcontrollerlayoutenvironment-c.class.md) — A class that represents the split view controller layout environment trait.
- [UITraitTabAccessoryEnvironment](uitraittabaccessoryenvironment-c.class.md) — A class that represents the tab accessory environment trait.
- [UITraitToolbarItemPresentationSize](uitraittoolbaritempresentationsize-c.class.md) — A class that represents the toolbar item presentation size trait.
- [UITraitTypesettingLanguage](uitraittypesettinglanguage-c.class.md) — A class that represents the typesetting language trait.
- [UITraitUserInterfaceIdiom](uitraituserinterfaceidiom-c.class.md) — A class that represents the user interface idiom trait.
- [UITraitUserInterfaceLevel](uitraituserinterfacelevel-c.class.md) — A class that represents the user interface level trait.
- [UITraitUserInterfaceStyle](uitraituserinterfacestyle-c.class.md) — A class that represents the user interface style trait.
- [UITraitVerticalSizeClass](uitraitverticalsizeclass-c.class.md) — A class that represents the vertical size class trait.

## See Also

### Observing and managing traits

- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [UIMutableTraits](uimutabletraits-8l00o.md) — A mutable container of traits.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
