---
title: UIMutableTraits
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutabletraits-13ja5
source_url: 'https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutabletraits-13ja5.json'
content_hash: 'sha256:013716f93998163a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMutableTraits

<sub>Protocol</sub>

A mutable container of traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIMutableTraits
```

## Overview

The [UIMutableTraits](uimutabletraits-13ja5.md) protocol provides read-write access to get and set trait values on an underlying container. UIKit uses this protocol to facilitate working with instances of [UITraitCollection](uitraitcollection.md), which are immutable and read-only. The [UITraitCollection](uitraitcollection.md) initializer [init(mutations:)](<uitraitcollection/init(mutations_).md>) uses an instance of [UIMutableTraits](uimutabletraits-13ja5.md), which enables you to set a batch of trait values in one method call. [UITraitOverrides](uitraitoverrides-swift.struct.md) conforms to [UIMutableTraits](uimutabletraits-13ja5.md), making it easy to set trait overrides on trait environments such as views and view controllers.

When you define a custom trait, declare a property for the trait in an extension to [UIMutableTraits](uimutabletraits-13ja5.md) so that you can access your custom trait using standard property syntax.

The following example defines an extension and sets the theme on the [traitOverrides](uiview/traitoverrides-fd9z.md) property:

```swift
// ThemeTrait conforms to UITraitDefinition, and has a defaultValue type of Theme
extension UIMutableTraits {
    var theme: Theme {
        get { self[ThemeTrait.self] }
        set { self[ThemeTrait.self] = newValue }
    }
}

// Apply an override for the custom theme trait.
view.traitOverrides.theme = .monochrome
```

## Relationships

- **Conforming Types**: [UITraitOverrides](uitraitoverrides-swift.struct.md)

## Topics

### Getting and setting trait values

- [accessibilityContrast](uimutabletraits-13ja5/accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [activeAppearance](uimutabletraits-13ja5/activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [displayGamut](uimutabletraits-13ja5/displaygamut.md) — The gamut of the current display.
- [displayScale](uimutabletraits-13ja5/displayscale.md) — The display scale of the trait collection.
- [forceTouchCapability](uimutabletraits-13ja5/forcetouchcapability.md) — The Force Touch capability value of the trait collection.
- [headroomUsageLimit](uimutabletraits-13ja5/headroomusagelimit.md) — The HDR headroom usage limit associated with the current environment.
- [horizontalSizeClass](uimutabletraits-13ja5/horizontalsizeclass.md) — The horizontal size class of the trait collection.
- [imageDynamicRange](uimutabletraits-13ja5/imagedynamicrange.md) — The image dynamic range associated with the current environment.
- [layoutDirection](uimutabletraits-13ja5/layoutdirection.md) — The layout direction associated with the current environment.
- [legibilityWeight](uimutabletraits-13ja5/legibilityweight.md) — The font weight to apply to text.
- [listEnvironment](uimutabletraits-13ja5/listenvironment.md) — The style of the containing list in a collection view or table view.
- [preferredContentSizeCategory](uimutabletraits-13ja5/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [resolvesNaturalAlignmentWithBaseWritingDirection](uimutabletraits-13ja5/resolvesnaturalalignmentwithbasewritingdirection.md) — The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [sceneCaptureState](uimutabletraits-13ja5/scenecapturestate.md) — The scene capture state for the current environment.
- [splitViewControllerLayoutEnvironment](uimutabletraits-13ja5/splitviewcontrollerlayoutenvironment.md) — The split view controller layout for the current environment.
- [tabAccessoryEnvironment](uimutabletraits-13ja5/tabaccessoryenvironment.md) — The tab accessory environment for the current trait collection.
- [toolbarItemPresentationSize](uimutabletraits-13ja5/toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
- [typesettingLanguage](uimutabletraits-13ja5/typesettinglanguage.md) — The typesetting language associated with the current environment.
- [userInterfaceIdiom](uimutabletraits-13ja5/userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [userInterfaceLevel](uimutabletraits-13ja5/userinterfacelevel.md) — The elevation level of the interface.
- [userInterfaceStyle](uimutabletraits-13ja5/userinterfacestyle.md) — The style associated with the user interface.
- [verticalSizeClass](uimutabletraits-13ja5/verticalsizeclass.md) — The vertical size class of the trait collection.

### Instance Properties

- [systemPrefersReducedResourceUsage](uimutabletraits-13ja5/systemprefersreducedresourceusage.md)

### Subscripts

- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-19j2e.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-1b2k9.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-1k64j.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-2n1bn.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-2tbov.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-4tqsr.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-5h7go.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-6s6f5.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-7jap6.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-7kxs.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-7m9p0.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-8vqxe.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-9ld0y.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-9za2c.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-dwij.md>)
- [subscript(_:)](<uimutabletraits-13ja5/subscript(__)-ve6h.md>)

## See Also

### Related Documentation

- [init(mutations:)](<uitraitcollection/init(mutations_).md>)
- [modifyingTraits(_:)](<uitraitcollection/modifyingtraits(__).md>)

### Observing and managing traits

- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — A type that calls your code in reaction to changes in the trait environment.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
