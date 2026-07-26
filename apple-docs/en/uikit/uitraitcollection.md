---
title: UITraitCollection
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection.json'
content_hash: 'sha256:73e130867d6e6d3f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitCollection

<sub>Class</sub>

A collection of data that represents the environment for an individual element in your app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UITraitCollection
```

## Overview

The [traitCollection](uitraitenvironment/traitcollection.md) property of the [UITraitEnvironment](uitraitenvironment.md) protocol contains traits that describe the state of various elements of the iOS user interface, such as size class, display scale, and layout direction. Together, these traits compose the UIKit trait environment.

The following classes adopt [UITraitEnvironment](uitraitenvironment.md): [UIScreen](uiscreen.md), [UIWindow](uiwindow.md), [UIWindowScene](uiwindowscene.md), [UIViewController](uiviewcontroller.md), [UIPresentationController](uipresentationcontroller.md), and [UIView](uiview.md). To create an adaptive interface, write code to adjust your app’s layout according to changes in these traits. You access specific trait values using the [UITraitCollection](uitraitcollection.md) [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md), [verticalSizeClass](uitraitcollection/verticalsizeclass.md), [displayScale](uitraitcollection/displayscale.md), [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md), and other properties.

To make your view controllers and views responsive to changes in the iOS interface environment, use automatic trait tracking in supported [UIViewController](uiviewcontroller.md) and [UIView](uiview.md) methods, or register to track specific trait changes with [UITraitChangeObservable](uitraitchangeobservable-67e94.md) methods. For more information, see [Adapting your app when traits change](adapting-your-app-when-traits-change.md).

To customize view controller animations in response to interface environment changes, override the [- willTransitionToTraitCollection:withTransitionCoordinator:](<uicontentcontainer/willtransition(to_with_).md>) method of the [UIContentContainer](uicontentcontainer.md) protocol.

For more information about the horizontal (width) and vertical (height) size classes your app can encounter when running full-screen on various devices, see Human Interface Guidelines \> [Layout](../design/human-interface-guidelines/layout.md#iOS-iPadOS-device-size-classes).

You can create standalone trait collections to assist in matching against specific environments. The [UITraitCollection](uitraitcollection.md) class includes four specialized constructors, as well as a constructor that enables you to combine an array of trait collections, [+ traitCollectionWithTraitsFromCollections:](<uitraitcollection/init(traitsfrom_).md>).

One important use of standalone trait collections is to enable conditional use of images based on the current iOS interface environment. You can associate a trait collection with a [UIImage](uiimage.md) instance by way of a [UIImageAsset](uiimageasset.md) instance, as described in the overview section of [UIImageAsset](uiimageasset.md). For information on configuring asset catalogs graphically from within the Xcode IDE, see [Managing assets with asset catalogs](../xcode/managing-assets-with-asset-catalogs.md).

You can employ a standalone trait collection to enable a two-column split view in landscape orientation on iPhone. See the [- setOverrideTraitCollection:forChildViewController:](<uiviewcontroller/setoverridetraitcollection(__forchild_).md>) method of the [UIViewController](uiviewcontroller.md) class.

You can also use a standalone trait collection to customize view appearance with the [+ appearanceForTraitCollection:](<uiappearance/appearance(for_).md>) protocol method, as described in [UIAppearance](uiappearance.md).

For information on creating custom traits, see [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the current traits

- [currentTraitCollection](uitraitcollection/current.md) — The trait collection for the current execution context.

### Getting related traits

- [systemTraitsAffectingColorAppearance](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)
- [systemTraitsAffectingImageLookup](uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)

### Modifying traits

- [init(mutations:)](<uitraitcollection/init(mutations_).md>)
- [modifyingTraits(_:)](<uitraitcollection/modifyingtraits(__).md>)
- [TraitMutations](uitraitcollection/traitmutations.md)

### Getting trait changes

- [changedTraits(from:)](<uitraitcollection/changedtraits(from_).md>)

### Comparing trait collections

- [- hasDifferentColorAppearanceComparedToTraitCollection:](<uitraitcollection/hasdifferentcolorappearance(comparedto_).md>) — Queries whether changing between the specified and current trait collections would affect color values.
- [- containsTraitsInCollection:](<uitraitcollection/containstraits(in_).md>) — Queries whether a trait collection contains all of another trait collection’s values. _(deprecated)_

### Performing actions with the current traits

- [- performAsCurrentTraitCollection:](<uitraitcollection/performascurrent(__).md>) — Executes custom code using the traits of the receiving trait collection.

### Retrieving size class traits

- [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md) — The horizontal size class of the trait collection.
- [verticalSizeClass](uitraitcollection/verticalsizeclass.md) — The vertical size class of the trait collection.
- [UIUserInterfaceSizeClass](uiuserinterfacesizeclass.md) — Constants that indicate the size class of a view.

### Retrieving display-related traits

- [displayScale](uitraitcollection/displayscale.md) — The display scale of the trait collection.
- [displayGamut](uitraitcollection/displaygamut.md) — The gamut of the current display.
- [UIDisplayGamut](uidisplaygamut.md) — Constants that indicate the gamut of the current display.

### Retrieving interface-related traits

- [userInterfaceStyle](uitraitcollection/userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](uitraitcollection/userinterfacelevel.md) — The elevation level of the interface.
- [UIUserInterfaceLevel](uiuserinterfacelevel.md) — Constants that indicate the visual level for content in the window.
- [layoutDirection](uitraitcollection/layoutdirection.md) — The layout direction associated with the current environment.
- [UITraitEnvironmentLayoutDirection](uitraitenvironmentlayoutdirection.md) — Constants that indicate the layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](uitraitcollection/accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](uitraitcollection/legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](uitraitcollection/activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
- [UINSToolbarItemPresentationSize](uinstoolbaritempresentationsize.md) — Constants that specify the presentation size of a toolbar item in an AppKit toolbar.
- [hdrHeadroomUsageLimit](uitraitcollection/hdrheadroomusagelimit.md) — If HDR headroom should be used for the current UI configuration. Headroom usage is disabled in certain UI configurations, such as when all an application’s windows are in the background.
- [UIHDRHeadroomUsageLimit](uihdrheadroomusagelimit.md)

### Retrieving the force touch capability traits

- [forceTouchCapability](uitraitcollection/forcetouchcapability.md) — The force touch capability value of the trait collection.
- [UIForceTouchCapability](uiforcetouchcapability.md) — Keys that indicate the availability of 3D Touch on a device.

### Retrieving content size category information

- [preferredContentSizeCategory](uitraitcollection/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategory](uicontentsizecategory.md) — Constants that indicate the preferred size of your content.

### Retrieving layout environment traits

- [listEnvironment](uitraitcollection/listenvironment.md) — The list environment represents whether a given trait collection is from a view in a UITableView or a UICollectionView list section.
- [UIListEnvironment](uilistenvironment.md) — Constants that indicate the style of the containing list in a collection view or table view.
- [splitViewControllerLayoutEnvironment](uitraitcollection/splitviewcontrollerlayoutenvironment.md) — The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.
- [LayoutEnvironment](uisplitviewcontroller/layoutenvironment.md) — Constants that indicate the current layout of the containing split view controller.
- [tabAccessoryEnvironment](uitraitcollection/tabaccessoryenvironment.md) — The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [Environment](uitabaccessory/environment.md)

### Retrieving scene capture state

- [sceneCaptureState](uitraitcollection/scenecapturestate.md) — Scene capture state represents whether a scene is currently being mirrored or recorded.
- [UISceneCaptureState](uiscenecapturestate.md)

### Retrieving dynamic range traits

- [imageDynamicRange](uitraitcollection/imagedynamicrange.md) — The imageDynamicRange determines how HDR images will render in the given trait environment. SDR images are unaffected.

### Retrieving typesetting language traits

- [typesettingLanguage](uitraitcollection/typesettinglanguage-6i635.md)

### Getting an image configuration object

- [imageConfiguration](uitraitcollection/imageconfiguration.md) — An image configuration object compatible with this trait collection.

### Creating a trait collection

- [- init](<uitraitcollection/init().md>) — Creates a trait collection whose traits are set to their default (unspecified) values.
- [+ traitCollectionWithUserInterfaceIdiom:](<uitraitcollection/init(userinterfaceidiom_).md>) — Creates a trait collection that contains only a specified interface idiom.
- [+ traitCollectionWithHorizontalSizeClass:](<uitraitcollection/init(horizontalsizeclass_).md>) — Creates a trait collection that contains only a specified horizontal size class.
- [+ traitCollectionWithVerticalSizeClass:](<uitraitcollection/init(verticalsizeclass_).md>) — Creates a trait collection that contains only a specified vertical size class.
- [+ traitCollectionWithUserInterfaceStyle:](<uitraitcollection/init(userinterfacestyle_).md>) — Creates a trait collection that contains only the specified user interface style trait.
- [+ traitCollectionWithAccessibilityContrast:](<uitraitcollection/init(accessibilitycontrast_).md>) — Creates a trait collection that contains only the specified accessibility contrast trait.
- [+ traitCollectionWithUserInterfaceLevel:](<uitraitcollection/init(userinterfacelevel_).md>) — Creates a trait collection that contains only the specified user interface level trait.
- [+ traitCollectionWithLegibilityWeight:](<uitraitcollection/init(legibilityweight_).md>) — Creates a trait collection that contains only the specified legibility weight trait.
- [+ traitCollectionWithForceTouchCapability:](<uitraitcollection/init(forcetouchcapability_).md>) — Creates a trait collection that contains only a specified force touch capability trait.
- [+ traitCollectionWithDisplayScale:](<uitraitcollection/init(displayscale_).md>) — Creates a trait collection that contains only a specified display scale.
- [+ traitCollectionWithDisplayGamut:](<uitraitcollection/init(displaygamut_).md>) — Creates a trait collection that contains only the specified display gamut trait.
- [+ traitCollectionWithLayoutDirection:](<uitraitcollection/init(layoutdirection_).md>) — Creates a trait collection that contains only the specified layout direction trait.
- [+ traitCollectionWithPreferredContentSizeCategory:](<uitraitcollection/init(preferredcontentsizecategory_).md>) — Creates a trait collection that contains only the specified content size category trait.
- [+ traitCollectionWithActiveAppearance:](<uitraitcollection/init(activeappearance_).md>) — Creates a trait collection that contains only the specified active appearance trait.
- [+ traitCollectionWithToolbarItemPresentationSize:](<uitraitcollection/init(toolbaritempresentationsize_).md>) — Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [+ traitCollectionWithHDRHeadroomUsageLimit:](<uitraitcollection/init(hdrheadroomusagelimit_)-5zqph.md>)
- [+ traitCollectionWithImageDynamicRange:](<uitraitcollection/init(imagedynamicrange_).md>) — Construct a new trait collection with the given image content dynamic range.
- [+ traitCollectionWithListEnvironment:](<uitraitcollection/init(listenvironment_).md>) — Construct a new trait collection with the given `listEnvironment`.
- [init(resolvesNaturalAlignmentWithBaseWritingDirection:)](<uitraitcollection/init(resolvesnaturalalignmentwithbasewritingdirection_).md>)
- [+ traitCollectionWithSceneCaptureState:](<uitraitcollection/init(scenecapturestate_).md>) — Construct a new trait collection with the given scene capture state.
- [+ traitCollectionWithTabAccessoryEnvironment:](<uitraitcollection/init(tabaccessoryenvironment_).md>) — Constructs a new trait collection with the given `tabAccessoryEnvironment`.
- [init(typesettingLanguage:)](<uitraitcollection/init(typesettinglanguage_).md>)
- [- initWithCoder:](<uitraitcollection/init(coder_).md>) — Creates a trait collection from data in an unarchiver.
- [+ traitCollectionWithTraitsFromCollections:](<uitraitcollection/init(traitsfrom_).md>) — Creates a trait collection that consists of traits merged from a specified array of trait collections. _(deprecated)_

### Initializers

- [init(HDRHeadroomUsageLimit:)](<uitraitcollection/init(hdrheadroomusagelimit_)-3nnko.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-3as8f.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-3fg2.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-4100d.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-48zja.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-4shto.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-4slti.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-55rvq.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-58ia2.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-59di1.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-59u4e.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-6h22m.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-7sd52.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-7toc9.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-836bk.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-8k1t1.md>)
- [init(_:value:)](<uitraitcollection/init(__value_)-vvgw.md>)
- [init(systemPrefersReducedResourceUsage:)](<uitraitcollection/init(systemprefersreducedresourceusage_).md>)
- [init(traitsFromCollections:)](<uitraitcollection/init(traitsfromcollections_).md>) _(deprecated)_

### Instance Properties

- [systemPrefersReducedResourceUsage](uitraitcollection/systemprefersreducedresourceusage-1yl57.md)

### Instance Methods

- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-162et.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-1n0uk.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-1wvrv.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-227ps.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-3p47.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-418p6.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-4c3s8.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-5swjm.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-7jssv.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-8gf97.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-8yat4.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-8z10u.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-8z152.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-8zl00.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-9op5s.md>)
- [replacing(_:value:)](<uitraitcollection/replacing(__value_)-o6qa.md>)

### Subscripts

- [subscript(_:)](<uitraitcollection/subscript(__)-10ujz.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-1kkve.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-1n030.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-2bvk.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-32r6h.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-3ztj.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-43in7.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-4gjs6.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-4zpi4.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-5wwet.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-6cdgq.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-6jr9c.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-8rqo4.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-90z0t.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-96v58.md>)
- [subscript(_:)](<uitraitcollection/subscript(__)-9nfd8.md>)

## See Also

### Adaptivity

- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
