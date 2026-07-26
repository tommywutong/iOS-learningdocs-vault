---
title: UIActivityItemsConfigurationProviding
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfigurationproviding
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationproviding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfigurationproviding.json'
content_hash: 'sha256:66478b32dbc08eb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemsConfigurationProviding

<sub>Protocol</sub>

An interface that provides a source for shareable content to fulfill user requests to share current content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIActivityItemsConfigurationProviding : NSObjectProtocol
```

## Overview

The user can share content from your app in a number of ways:

- Ask Siri to “share this” on an iOS device.
- Click an [NSSharingServicePickerToolbarItem](../appkit/nssharingservicepickertoolbaritem.md) in the toolbar of an app built with Mac Catalyst.
- Start a [UIContextMenuInteraction](uicontextmenuinteraction.md) by using Force Touch or a long press gesture.

When one of these interactions happens, the system asks your view controller for content to share. Supply multiple representations of the current content, such as a file, image, and URL.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIAccessibilityElement](uiaccessibilityelement.md), [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UIAlertView](uialertview.md), [UIApplication](uiapplication.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewController](uicollectionviewcontroller.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIEventAttributionView](uieventattributionview.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIInputViewController](uiinputviewcontroller.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UINavigationController](uinavigationcontroller.md), [UIPageControl](uipagecontrol.md), [UIPageViewController](uipageviewcontroller.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UIRefreshControl](uirefreshcontrol.md), [UIResponder](uiresponder.md), [UIScene](uiscene.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UISplitViewController](uisplitviewcontroller.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITabBarController](uitabbarcontroller.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewController](uitableviewcontroller.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md), [UIWindowScene](uiwindowscene.md)

## Topics

### Providing shareable content

- [activityItemsConfiguration](uiactivityitemsconfigurationproviding/activityitemsconfiguration.md) — An object or value that specifies items to share.

## See Also

### Activities interface

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md) — Share data and collaborate with people from your app.
- [UIActivityViewController](uiactivityviewcontroller.md) — A view controller that you use to offer standard services from your app.
- [UIActivityItemProvider](uiactivityitemprovider.md) — A proxy for data that passes to an activity view controller.
- [UIActivityItemSource](uiactivityitemsource.md) — A set of methods that an activity view controller uses to retrieve the data items to act on.
- [UIActivity](uiactivity.md) — An abstract class that you subclass to implement app-specific services.
