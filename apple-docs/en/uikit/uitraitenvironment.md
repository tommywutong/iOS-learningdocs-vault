---
title: UITraitEnvironment
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitenvironment
source_url: 'https://developer.apple.com/documentation/uikit/uitraitenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitenvironment.json'
content_hash: 'sha256:c584ddceb78f8e90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitEnvironment

<sub>Protocol</sub>

A set of methods that makes the iOS interface environment available to your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITraitEnvironment : NSObjectProtocol
```

## Overview

The system represents the iOS interface environment with _traits_, such as horizontal and vertical size class, display scale, and user interface idiom. You access the trait environment of an object that adopts this protocol with the [traitCollection](uitraitenvironment/traitcollection.md) property.

The trait system propagates values from the top of the view hierarchy downward, to every view controller and view in your app. When you modify a trait at any level using trait overrides, that change affects the modified object and all of its descendants. This hierarchical propagation makes it easy to apply configuration changes to entire subtrees of your interface.

For example, setting a trait override on a window scene affects all view controllers and views within that scene. Similarly, setting a trait override on a specific view affects only that view and its subviews.

For more information about how traits propagate through the system, see [Unleash the UIKit trait system](https://developer.apple.com/videos/play/wwdc2023/10057).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewController](uicollectionviewcontroller.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIEventAttributionView](uieventattributionview.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIInputViewController](uiinputviewcontroller.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UINavigationController](uinavigationcontroller.md), [UIPageControl](uipagecontrol.md), [UIPageViewController](uipageviewcontroller.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIPopoverPresentationController](uipopoverpresentationcontroller.md), [UIPresentationController](uipresentationcontroller.md), [UIProgressView](uiprogressview.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UIRefreshControl](uirefreshcontrol.md), [UIScreen](uiscreen.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISheetPresentationController](uisheetpresentationcontroller.md), [UISlider](uislider.md), [UISplitViewController](uisplitviewcontroller.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITabBarController](uitabbarcontroller.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewController](uitableviewcontroller.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md), [UIWindowScene](uiwindowscene.md)

## Topics

### Accessing a trait collection

- [traitCollection](uitraitenvironment/traitcollection.md) — The traits, such as the size class and scale factor, that describe the current environment of the object.

### Responding to a change in the interface environment

- [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) — Reports changes in the iOS interface environment. _(deprecated)_

## See Also

### Adaptivity

- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [Automatic trait tracking](automatic-trait-tracking.md) — Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
