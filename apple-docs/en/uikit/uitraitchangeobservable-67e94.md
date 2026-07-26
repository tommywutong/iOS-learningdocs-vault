---
title: UITraitChangeObservable
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitchangeobservable-67e94
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-67e94.json'
content_hash: 'sha256:3861948dd589d333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitChangeObservable

<sub>Protocol</sub>

A type that calls your code in reaction to changes in the trait environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITraitChangeObservable
```

## Overview

Types that conform to [UITraitChangeObservable](uitraitchangeobservable-67e94.md) can execute your code in response to changes in their trait collection. When you register for trait changes, the system observes the specified traits, and calls your code when any of the observed traits change value.

Keep your trait registrations focused, and avoid doing work not directly relevant to updated traits. Traits may change more than once before the system updates a view, so avoid expensive work in response to trait changes. For example, use the trait change notification to call [- setNeedsDisplay](<uiview/setneedsdisplay().md>), and update your view in [- drawRect:](<uiview/draw(__).md>).

UIKit cleans up registrations at the end of the object lifecycle. Unregister only in the rare situations when you need to dynamically change which traits you observe.

## Relationships

- **Conforming Types**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewController](uicollectionviewcontroller.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIEventAttributionView](uieventattributionview.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIInputViewController](uiinputviewcontroller.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UINavigationController](uinavigationcontroller.md), [UIPageControl](uipagecontrol.md), [UIPageViewController](uipageviewcontroller.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIPopoverPresentationController](uipopoverpresentationcontroller.md), [UIPresentationController](uipresentationcontroller.md), [UIProgressView](uiprogressview.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISheetPresentationController](uisheetpresentationcontroller.md), [UISlider](uislider.md), [UISplitViewController](uisplitviewcontroller.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITabBarController](uitabbarcontroller.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewController](uitableviewcontroller.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md), [UIWindowScene](uiwindowscene.md)

## Topics

### Observing trait changes

- [registerForTraitChanges(_:action:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__action_).md>) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges(_:handler:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges(_:)](<uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>) — Tells the system to stop observing previously registered traits.
- [TraitChangeHandler](uitraitchangeobservable-67e94/traitchangehandler.md) — A closure the system executes when observed traits change.
- [UITraitChangeRegistration](uitraitchangeregistration.md)

### Registering traits for observation

- [UITraitAccessibilityContrast](uitraitaccessibilitycontrast-swift.struct.md) — A struct that represents the accessibility contrast setting trait.
- [UITraitActiveAppearance](uitraitactiveappearance-swift.struct.md) — A struct that represents the active appearance trait.
- [UITraitDisplayGamut](uitraitdisplaygamut-swift.struct.md) — A struct that represents the display gamut trait.
- [UITraitDisplayScale](uitraitdisplayscale-swift.struct.md) — A struct that represents the display scale trait.
- [UITraitForceTouchCapability](uitraitforcetouchcapability-swift.struct.md) — A struct that represents the Force Touch capability trait.
- [UITraitHDRHeadroomUsageLimit](uitraithdrheadroomusagelimit-swift.struct.md) — A struct that represents the HDR headroom usage limit trait.
- [UITraitHorizontalSizeClass](uitraithorizontalsizeclass-swift.struct.md) — A struct that represents the horizontal size class trait.
- [UITraitImageDynamicRange](uitraitimagedynamicrange-swift.struct.md) — A struct that represents the image dynamic range trait.
- [UITraitLayoutDirection](uitraitlayoutdirection-swift.struct.md) — A struct that represents the layout direction trait.
- [UITraitLegibilityWeight](uitraitlegibilityweight-swift.struct.md) — A struct that represents the legibility weight trait.
- [UITraitListEnvironment](uitraitlistenvironment-swift.struct.md) — A struct that represents the list environment trait.
- [UITraitPreferredContentSizeCategory](uitraitpreferredcontentsizecategory-swift.struct.md) — A struct that represents the preferred content size category trait.
- [UITraitResolvesNaturalAlignmentWithBaseWritingDirection](uitraitresolvesnaturalalignmentwithbasewritingdirection-swift.struct.md) — A struct that represents the trait that indicates whether the system resolves natural alignment with base writing direction.
- [UITraitSceneCaptureState](uitraitscenecapturestate-swift.struct.md) — A struct that represents the scene capture state trait.
- [UITraitSplitViewControllerLayoutEnvironment](uitraitsplitviewcontrollerlayoutenvironment-swift.struct.md) — A struct that represents the split view controller layout environment trait.
- [UITraitTabAccessoryEnvironment](uitraittabaccessoryenvironment-swift.struct.md) — A struct that represents tab accessory environment trait.
- [UITraitToolbarItemPresentationSize](uitraittoolbaritempresentationsize-swift.struct.md) — A struct that represents the toolbar item presentation size trait.
- [UITraitTypesettingLanguage](uitraittypesettinglanguage-swift.struct.md) — A struct that represents the typesetting language trait.
- [UITraitUserInterfaceIdiom](uitraituserinterfaceidiom-swift.struct.md) — A struct that represents the user interface idiom trait.
- [UITraitUserInterfaceLevel](uitraituserinterfacelevel-swift.struct.md) — A struct that represents the user interface level trait.
- [UITraitUserInterfaceStyle](uitraituserinterfacestyle-swift.struct.md) — A struct that represents the user interface style trait.
- [UITraitVerticalSizeClass](uitraitverticalsizeclass-swift.struct.md) — A struct that represents the vertical size class trait.

## See Also

### Observing and managing traits

- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [UIMutableTraits](uimutabletraits-13ja5.md) — A mutable container of traits.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
