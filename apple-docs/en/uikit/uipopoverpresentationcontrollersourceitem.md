---
title: UIPopoverPresentationControllerSourceItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontrollersourceitem
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollersourceitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontrollersourceitem.json'
content_hash: 'sha256:00d3c1a546e0a4b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPopoverPresentationControllerSourceItem

<sub>Protocol</sub>

A type that can be an anchor for a popover presentation controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIPopoverPresentationControllerSourceItem : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSUIViewToolbarItem](nsuiviewtoolbaritem.md), [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIBarButtonItem](uibarbuttonitem.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIEventAttributionView](uieventattributionview.md), [UIFocusGuide](uifocusguide.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md), [UILabel](uilabel.md), [UILayoutGuide](uilayoutguide.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchTab](uisearchtab.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITab](uitab.md), [UITabBar](uitabbar.md), [UITabBarItem](uitabbaritem.md), [UITabGroup](uitabgroup.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UITrackingLayoutGuide](uitrackinglayoutguide.md), [UIView](uiview.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md)

## Topics

### Instance Methods

- [frame(in:)](<uipopoverpresentationcontrollersourceitem/frame(in_).md>)

## See Also

### Specifying the popover’s anchor point

- [sourceItem](uipopoverpresentationcontroller/sourceitem.md) — The item on which to anchor the popover.
- [sourceView](uipopoverpresentationcontroller/sourceview.md) — The view containing the anchor rectangle for the popover.
- [sourceRect](uipopoverpresentationcontroller/sourcerect.md) — The area in the source view in which you anchor the popover.
- [barButtonItem](uipopoverpresentationcontroller/barbuttonitem.md) — The bar button item on which to anchor the popover. _(deprecated)_
