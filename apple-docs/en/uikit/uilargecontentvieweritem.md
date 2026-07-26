---
title: UILargeContentViewerItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentvieweritem
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentvieweritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentvieweritem.json'
content_hash: 'sha256:f96accbeaa06d4c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILargeContentViewerItem

<sub>Protocol</sub>

Methods that provide details about how to display your custom content in the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UILargeContentViewerItem : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIEventAttributionView](uieventattributionview.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIView](uiview.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md)

## Topics

### Integrating with the large content viewer

- [showsLargeContentViewer](uilargecontentvieweritem/showslargecontentviewer.md) — A Boolean value that indicates whether or not to show the item in the large content viewer.

### Configuring display properties

- [largeContentTitle](uilargecontentvieweritem/largecontenttitle.md) — A string that describes an item to display in the large content viewer.
- [largeContentImage](uilargecontentvieweritem/largecontentimage.md) — An image that represents an item to display in the large content viewer.
- [largeContentImageInsets](uilargecontentvieweritem/largecontentimageinsets.md) — Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
- [scalesLargeContentImage](uilargecontentvieweritem/scaleslargecontentimage.md) — A Boolean value that indicates whether the view scales the item’s image to a larger size or not.

## See Also

### Content viewer

- [UILargeContentViewerInteraction](uilargecontentviewerinteraction.md) — An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.
- [UILargeContentViewerInteractionDelegate](uilargecontentviewerinteractiondelegate.md) — An object that customizes the behavior of the large content viewer interactions.
