---
title: UIFocusItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem.json'
content_hash: 'sha256:1c898707fb22fa19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusItem

<sub>Protocol</sub>

An object that can become focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIFocusItem : UIFocusEnvironment
```

## Overview

An object that conforms to the [UIFocusItem](uifocusitem.md) protocol is capable of participating in the focus system; further, only [UIFocusItem](uifocusitem.md) objects can be focused.

Even when an object that conforms to [UIFocusItem](uifocusitem.md) isn’t currently focusable, it may still have an effect on the focus system. For example, items that aren’t focusable, but that completely obscure other items, may prevent those other items from being focusable, because they aren’t visible to the user. Also, because [UIFocusItem](uifocusitem.md) conforms to [UIFocusEnvironment](uifocusenvironment.md), items that aren’t focusable may still affect the focus behavior of items they contain, or react to focus updates.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIFocusEnvironment](uifocusenvironment.md)

- **Conforming Types**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIEventAttributionView](uieventattributionview.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIView](uiview.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md)

## Topics

### Determining focusability

- [canBecomeFocused](uifocusitem/canbecomefocused.md) — A Boolean value that indicates whether the item can become focused.

### Retrieving the item frame

- [frame](uifocusitem/frame.md) — The geometric frame of the item.

### Determining the focus priority

- [focusGroupPriority](uifocusitem/focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
- [UIFocusGroupPriority](uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.

### Providing movement hints

- [- didHintFocusMovement:](<uifocusitem/didhintfocusmovement(__).md>) — Indicates to the currently focused item that focus movement might occur.
- [UIFocusMovementHint](uifocusmovementhint.md) — Provides movement hint information for the focused item.

### Indicating focus visually

- [focusEffect](uifocusitem/focuseffect.md) — The visual effect to apply when the item becomes focused.

### Working with transparent items

- [isTransparentFocusItem](uifocusitem/istransparentfocusitem.md) — Indicates if the focus item is transparent, which allows items behind it to become focused.

### Instance Properties

- [focusItemDeferralMode](uifocusitem/focusitemdeferralmode.md) — If this property is present and returns `UIFocusItemDeferralModeNever`, the focus deferral will not be enabled again after the user engagement timeout has expired if this item is currently focused and programmatic focus updates pointing to this item will be executed immediatly. If it returns `UIFocusItemDeferralModeAlways` focus will always be deferred when this item is supposed to be focused. Does nothing when focus deferral is not supported on the platform.
- [isFocused](uifocusitem/isfocused-7tl52.md)
- [isFocused](uifocusitem/isfocused-hli8.md)

## See Also

### Focus interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md) — Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [UIFocusEnvironment](uifocusenvironment.md) — A set of methods that define the focus behavior for a branch of the view hierarchy.
- [UIFocusSystem](uifocussystem.md) — Queries and reevaluates the currently focused item.
- [UIFocusUpdateContext](uifocusupdatecontext.md) — An object that provides information relevant to a specific focus update from one view to another.
- [UIFocusMovementHint](uifocusmovementhint.md) — Provides movement hint information for the focused item.
- [UIFocusItemContainer](uifocusitemcontainer.md) — The container responsible for providing geometric context to focus items within a given focus environment.
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — A type of focus item container that supports automatic scrolling of focusable content.
- [UIFocusGroupPriority](uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
