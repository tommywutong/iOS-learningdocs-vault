---
title: UINavigationItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem.json'
content_hash: 'sha256:a87e07420d8743c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationItem

<sub>Class</sub>

The items that a navigation bar displays when the associated view controller is visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UINavigationItem
```

## Overview

When building a navigation interface, each view controller that you push onto the navigation stack must have a [UINavigationItem](uinavigationitem.md) object that contains the buttons and views you want to display in the navigation bar. The managing [UINavigationController](uinavigationcontroller.md) object uses the navigation items of the topmost two view controllers to populate the navigation bar with content.

A navigation item always reflects information about its associated view controller. The navigation item must provide a title to display when the view controller is topmost on the navigation stack. The item can also contain additional buttons to display on the right (or trailing) side of the navigation bar. You can specify buttons and views to display on the left (or leading) side of the toolbar using the [leftBarButtonItems](uinavigationitem/leftbarbuttonitems.md) property, but the navigation controller displays those buttons only when space is available.

To convey additional information about the view that a navigation item represents, use the [subtitle](uinavigationitem/subtitle.md) property. For example, in a view controller that displays a list of messages, you could use the `subtitle` to indicate the number of unread messages or the last time the app fetched messages. To apply text styles to a navigation item’s title or subtitle, use the [attributedTitle](uinavigationitem/attributedtitle-25fxb.md), [attributedSubtitle](uinavigationitem/attributedsubtitle-wrjk.md), and [largeAttributedSubtitle](uinavigationitem/largeattributedsubtitle-4z2gx.md) properties.

The [backBarButtonItem](uinavigationitem/backbarbuttonitem.md) property of a navigation item reflects the Back button you want to display when the current view controller is just below the topmost view controller. The Back button doesn’t appear when the current view controller is topmost.

When specifying buttons for a navigation item, you must use [UIBarButtonItem](uibarbuttonitem.md) objects. If you want to display custom views in the navigation bar, you must wrap those views inside a [UIBarButtonItem](uibarbuttonitem.md) object before adding them to the navigation item.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing an item

- [- initWithTitle:](<uinavigationitem/init(title_).md>) — Creates a navigation item with the specified title.
- [- initWithCoder:](<uinavigationitem/init(coder_).md>) — Creates a navigation item from data in an unarchiver.

### Configuring the title

- [title](uinavigationitem/title.md) — The navigation item’s title that displays in the navigation bar.
- [attributedTitle](uinavigationitem/attributedtitle-25fxb.md)
- [largeTitle](uinavigationitem/largetitle.md) — String to be used as the large title.
- [largeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md) — The mode for displaying the title of the navigation bar.
- [LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md) — Constants that indicate how to size the title of this item.

### Configuring the subtitle

- [subtitle](uinavigationitem/subtitle.md) — A string to display as the subtitle in the navigation bar.
- [attributedSubtitle](uinavigationitem/attributedsubtitle-wrjk.md)
- [largeSubtitle](uinavigationitem/largesubtitle.md) — String to be rendered below the large title.
- [largeAttributedSubtitle](uinavigationitem/largeattributedsubtitle-4z2gx.md)

### Configuring the Back button

- [backBarButtonItem](uinavigationitem/backbarbuttonitem.md) — The bar button item for adding a Back button to the navigation bar.
- [backButtonTitle](uinavigationitem/backbuttontitle.md) — The custom title of the Back button.
- [backButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md) — The display mode of the Back button.
- [BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.enum.md) — Constants that describe the display modes of the Back button.
- [hidesBackButton](uinavigationitem/hidesbackbutton.md) — A Boolean value that determines whether the navigation item hides the Back button.
- [- setHidesBackButton:animated:](<uinavigationitem/sethidesbackbutton(__animated_).md>) — Hides or shows the Back button, optionally animating the transition.
- [backAction](uinavigationitem/backaction.md) — The back action for the navigation bar.

### Specifying the navigation style

- [style](uinavigationitem/style.md) — A style that determines how the content of the navigation item lays out in the navigation bar.
- [ItemStyle](uinavigationitem/itemstyle.md) — Constants that determine how the content of the navigation item lays out in the navigation bar.

### Specifying custom views

- [centerItemGroups](uinavigationitem/centeritemgroups.md) — Customizable item groups to display in the center section of the navigation bar.
- [leadingItemGroups](uinavigationitem/leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](uinavigationitem/trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [pinnedTrailingGroup](uinavigationitem/pinnedtrailinggroup.md) — The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [titleView](uinavigationitem/titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [subtitleView](uinavigationitem/subtitleview.md) — A custom view to display below the title in the navigation bar.
- [largeSubtitleView](uinavigationitem/largesubtitleview.md) — A custom view to display below the large title.
- [leftBarButtonItems](uinavigationitem/leftbarbuttonitems.md) — An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [leftBarButtonItem](uinavigationitem/leftbarbuttonitem.md) — A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [rightBarButtonItems](uinavigationitem/rightbarbuttonitems.md) — An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItem](uinavigationitem/rightbarbuttonitem.md) — A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [- setLeftBarButtonItems:animated:](<uinavigationitem/setleftbarbuttonitems(__animated_).md>) — Sets the left bar button items, optionally animating the transition to the new items.
- [- setLeftBarButtonItem:animated:](<uinavigationitem/setleftbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the new item.
- [- setRightBarButtonItems:animated:](<uinavigationitem/setrightbarbuttonitems(__animated_).md>) — Sets the right bar button items, optionally animating the transition to the new items.
- [- setRightBarButtonItem:animated:](<uinavigationitem/setrightbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the view.

### Getting and setting properties

- [prompt](uinavigationitem/prompt.md) — A single line of text that displays at the top of the navigation bar.
- [leftItemsSupplementBackButton](uinavigationitem/leftitemssupplementbackbutton.md) — A Boolean value that indicates whether the left items display in addition to the Back button.

### Overriding the navigation bar’s appearance settings

- [standardAppearance](uinavigationitem/standardappearance.md) — The appearance settings for a standard-height navigation bar.
- [compactAppearance](uinavigationitem/compactappearance.md) — The appearance settings for a compact-height navigation bar.
- [scrollEdgeAppearance](uinavigationitem/scrolledgeappearance.md) — The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [compactScrollEdgeAppearance](uinavigationitem/compactscrolledgeappearance.md) — The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

### Integrating search into your interface

- [searchController](uinavigationitem/searchcontroller.md) — The search controller to integrate into your navigation interface.
- [hidesSearchBarWhenScrolling](uinavigationitem/hidessearchbarwhenscrolling.md) — A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [searchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md) — The placement of the search bar in the navigation bar.
- [preferredSearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md) — The preferred placement of the search bar in the navigation bar.
- [SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum.md) — Constants that determine where the search bar appears in the navigation bar.
- [searchBarPlacementAllowsExternalIntegration](uinavigationitem/searchbarplacementallowsexternalintegration.md) — A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [searchBarPlacementAllowsToolbarIntegration](uinavigationitem/searchbarplacementallowstoolbarintegration.md) — A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [searchBarPlacementBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md) — An item you use to control the placement of the search bar in a toolbar on iPhone.

### Supporting navigation bar customization

- [customizationIdentifier](uinavigationitem/customizationidentifier.md) — A globally unique string that enables user customization of the navigation bar layout.

### Working with the overflow menu

- [additionalOverflowItems](uinavigationitem/additionaloverflowitems.md) — Additional items to present in the overflow menu.
- [overflowPresentationSource](uinavigationitem/overflowpresentationsource.md) — The item you can use as an anchor to present a custom UI from the overflow menu button.

### Customizing the title menu

- [titleMenuProvider](uinavigationitem/titlemenuprovider.md) — A closure that generates the navigation item’s title menu.
- [documentProperties](uinavigationitem/documentproperties.md) — An object that provides the document header for the title menu.
- [UIDocumentProperties](uidocumentproperties.md) — Information that UIKit uses to generate a document header for a navigation item’s title menu.

### Renaming documents

- [renameDelegate](uinavigationitem/renamedelegate-8jiuf.md) — The delegate for renaming the navigation item.
- [UINavigationItemRenameDelegate](uinavigationitemrenamedelegate-5j4ws.md) — Methods an object implements to rename a navigation item.

### Instance Properties

- [navigationBarMinimization](uinavigationitem/navigationbarminimization-1kj9z.md)

## See Also

### Container view controllers

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md) — Create a composite interface by combining content from one or more view controllers with other custom views.
- [UISplitViewController](uisplitviewcontroller.md) — A container view controller that implements a hierarchical interface.
- [UINavigationController](uinavigationcontroller.md) — A container view controller that defines a stack-based scheme for navigating hierarchical content.
- [UINavigationBar](uinavigationbar.md) — Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [UITabBarController](uitabbarcontroller.md) — A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [UITabBar](uitabbar.md) — A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [UITabBarItem](uitabbaritem.md) — An object that describes an item in a tab bar.
- [UITab](uitab.md) — An object that manages a tab in a tab bar.
- [UITabAccessory](uitabaccessory.md)
- [UISearchTab](uisearchtab.md) — A tab subclass that represents the system’s search tab.
- [UITabGroup](uitabgroup.md) — An object that manages a collection of tab objects.
- [UIPageViewController](uipageviewcontroller.md) — A container view controller that manages navigation between pages of content, where a subview controller manages each page.
