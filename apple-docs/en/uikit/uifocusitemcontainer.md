---
title: UIFocusItemContainer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemcontainer
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemcontainer.json'
content_hash: 'sha256:3426e8dc3851b8f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusItemContainer

<sub>Protocol</sub>

The container responsible for providing geometric context to focus items within a given focus environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIFocusItemContainer : NSObjectProtocol
```

## Overview

Focus item containers are used by the focus engine to find focus items for a focus environment in specific geometric regions.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)

- **Conforming Types**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIEventAttributionView](uieventattributionview.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIView](uiview.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md)

## Topics

### Retrieving focus items

- [- focusItemsInRect:](<uifocusitemcontainer/focusitems(in_).md>) — Retrieves all of the focus items within this container that intersect with the provided rectangle.
- [coordinateSpace](uifocusitemcontainer/coordinatespace.md) — The coordinate space of the focus items contained in the focus item container.

## See Also

### Focus interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md) — Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [UIFocusEnvironment](uifocusenvironment.md) — A set of methods that define the focus behavior for a branch of the view hierarchy.
- [UIFocusSystem](uifocussystem.md) — Queries and reevaluates the currently focused item.
- [UIFocusUpdateContext](uifocusupdatecontext.md) — An object that provides information relevant to a specific focus update from one view to another.
- [UIFocusItem](uifocusitem.md) — An object that can become focused.
- [UIFocusMovementHint](uifocusmovementhint.md) — Provides movement hint information for the focused item.
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — A type of focus item container that supports automatic scrolling of focusable content.
- [UIFocusGroupPriority](uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
