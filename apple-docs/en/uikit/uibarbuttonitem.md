---
title: UIBarButtonItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem.json'
content_hash: 'sha256:4ed5d0eaac4a62a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarButtonItem

<sub>Class</sub>

A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBarButtonItem
```

## Overview

You typically use Interface Builder to create and configure bar button items. However, you can customize the appearance of buttons by sending the setter messages to [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) to customize all buttons, or to a specific [UIBarButtonItem](uibarbuttonitem.md) instance. You can use customized buttons in standard places in a [UINavigationItem](uinavigationitem.md) object or a [UIToolbar](uitoolbar.md) instance.

In general, specify a value for the normal state so that other states without a custom value set can use it. Similarly, when a property depends on the bar metrics (for instance, on the iPhone in landscape orientation, bars have a different height from the standard), specify a value of [UIBarMetricsDefault](uibarmetrics/default.md).

## Relationships

- **Inherits From**: [UIBarItem](uibaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIAppearance](uiappearance.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)

## Topics

### Creating items

- [init(title:image:primaryAction:menu:)](<uibarbuttonitem/init(title_image_primaryaction_menu_).md>) — Creates a plain-style item using the specified title, image, primary action, and context menu.
- [init(title:image:target:action:menu:)](<uibarbuttonitem/init(title_image_target_action_menu_).md>) — Creates a plain-style item using the specified title, image, target, action, and context menu.
- [- init](<uibarbuttonitem/init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<uibarbuttonitem/init(coder_).md>) — Creates an item from data in an unarchiver.

### Creating items of a specific style

- [- initWithTitle:style:target:action:](<uibarbuttonitem/init(title_style_target_action_).md>) — Creates an item using the specified title, style, target, and action.
- [- initWithImage:style:target:action:](<uibarbuttonitem/init(image_style_target_action_).md>) — Creates an item using the specified image, style, target, and action.
- [- initWithImage:landscapeImagePhone:style:target:action:](<uibarbuttonitem/init(image_landscapeimagephone_style_target_action_).md>) — Creates an item using the specified images, style, target, and action.

### Creating system items

- [init(systemItem:primaryAction:menu:)](<uibarbuttonitem/init(systemitem_primaryaction_menu_).md>) — Creates an item using the specified system item, primary action, and context menu.
- [- initWithBarButtonSystemItem:target:action:](<uibarbuttonitem/init(barbuttonsystemitem_target_action_).md>) — Creates an item using the specified system item, target, and action.
- [SystemItem](uibarbuttonitem/systemitem.md) — Constants that define system-supplied images for bar button items.

### Creating custom items

- [- initWithCustomView:](<uibarbuttonitem/init(customview_).md>) — Creates an item using the specified custom view.

### Creating space items

- [+ fixedSpaceItemOfWidth:](<uibarbuttonitem/fixedspace(__).md>) — Creates a new fixed-width space item.
- [+ fixedSpaceItem](<uibarbuttonitem/fixedspace().md>) — Creates a new fixed space item of zero width.
- [+ flexibleSpaceItem](<uibarbuttonitem/flexiblespace().md>) — Creates a new flexible-width space item.

### Creating groups

- [creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)](<uibarbuttonitem/creatingoptionalgroup(customizationidentifier_isindefaultcustomization_).md>) — Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- creatingFixedGroup](<uibarbuttonitem/creatingfixedgroup().md>) — Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [- creatingMovableGroupWithCustomizationIdentifier:](<uibarbuttonitem/creatingmovablegroup(customizationidentifier_).md>) — Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.

### Managing the custom view

- [customView](uibarbuttonitem/customview.md) — A custom view representing the item.

### Managing the action

- [primaryAction](uibarbuttonitem/primaryaction.md) — The action associated with the item.
- [changesSelectionAsPrimaryAction](uibarbuttonitem/changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button represents an action or selection.
- [action](uibarbuttonitem/action.md) — The selector defining the action message to send to the target object when the user taps this bar button item.
- [target](uibarbuttonitem/target.md) — The object that receives an action when the user selects the item.

### Managing the context menu

- [menu](uibarbuttonitem/menu.md) — The context menu for this button.
- [preferredMenuElementOrder](uibarbuttonitem/preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.

### Customizing item appearance

- [style](uibarbuttonitem/style-swift.property.md) — The style of the item.
- [Style](uibarbuttonitem/style-swift.enum.md) — Constants that specify the style of an item.
- [tintColor](uibarbuttonitem/tintcolor.md) — The tint color to apply to the button item.
- [hidden](uibarbuttonitem/ishidden.md) — A Boolean that determines the visibility of the item.
- [selected](uibarbuttonitem/isselected.md) — A Boolean value that indicates whether the button is in a selected state.
- [width](uibarbuttonitem/width.md) — The width of the item.
- [possibleTitles](uibarbuttonitem/possibletitles.md) — The set of possible titles to display on the bar button.

### Customizing the Back button

- [- backButtonBackgroundImageForState:barMetrics:](<uibarbuttonitem/backbuttonbackgroundimage(for_barmetrics_).md>) — Returns the back button background image for a specified control state and bar metrics.
- [- setBackButtonBackgroundImage:forState:barMetrics:](<uibarbuttonitem/setbackbuttonbackgroundimage(__for_barmetrics_).md>) — Sets the back button background image for a specified control state and bar metrics.
- [- backButtonTitlePositionAdjustmentForBarMetrics:](<uibarbuttonitem/backbuttontitlepositionadjustment(for_).md>) — Returns the back button title offset for specified bar metrics.
- [- setBackButtonTitlePositionAdjustment:forBarMetrics:](<uibarbuttonitem/setbackbuttontitlepositionadjustment(__for_).md>) — Sets the back button title offset for specified bar metrics.
- [- backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:](<uibarbuttonitem/backbuttonbackgroundverticalpositionadjustment(for_).md>) — Returns the back button vertical position offset for specified bar metrics.
- [- setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:](<uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(__for_).md>) — Sets the back button vertical position offset for specified bar metrics.

### Customizing the background

- [- backgroundVerticalPositionAdjustmentForBarMetrics:](<uibarbuttonitem/backgroundverticalpositionadjustment(for_).md>) — Returns the background vertical position offset for specified bar metrics.
- [- setBackgroundVerticalPositionAdjustment:forBarMetrics:](<uibarbuttonitem/setbackgroundverticalpositionadjustment(__for_).md>) — Sets the background vertical position offset for specified bar metrics.
- [- backgroundImageForState:barMetrics:](<uibarbuttonitem/backgroundimage(for_barmetrics_).md>) — Returns the background image for a specified state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<uibarbuttonitem/setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for a specified state and bar metrics.
- [- backgroundImageForState:style:barMetrics:](<uibarbuttonitem/backgroundimage(for_style_barmetrics_).md>) — Returns the background image for the specified state, style, and metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<uibarbuttonitem/setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

### Customizing the title placement

- [- titlePositionAdjustmentForBarMetrics:](<uibarbuttonitem/titlepositionadjustment(for_).md>) — Returns the title offset for specified bar metrics.
- [- setTitlePositionAdjustment:forBarMetrics:](<uibarbuttonitem/settitlepositionadjustment(__for_).md>) — Sets the title offset for specified bar metrics.

### Configuring symbol effects

- [symbolAnimationEnabled](uibarbuttonitem/issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect(_:options:animated:)](<uibarbuttonitem/addsymboleffect(__options_animated_)-3iew0.md>) — Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<uibarbuttonitem/addsymboleffect(__options_animated_)-6jx3e.md>) — Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<uibarbuttonitem/addsymboleffect(__options_animated_)-9dytr.md>) — Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:)](<uibarbuttonitem/setsymbolimage(__contenttransition_options_).md>) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffect(ofType:options:animated:)](<uibarbuttonitem/removesymboleffect(oftype_options_animated_)-214pl.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<uibarbuttonitem/removesymboleffect(oftype_options_animated_)-7m567.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<uibarbuttonitem/removesymboleffect(oftype_options_animated_)-8zc4d.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<uibarbuttonitem/removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the bar button item, using the specified options and animation setting.

### Getting the group

- [buttonGroup](uibarbuttonitem/buttongroup.md) — The group that the button belongs to.

### Representing the item in a menu

- [menuRepresentation](uibarbuttonitem/menurepresentation.md) — A menu element that represents the item when it appears in a menu.

### Adding a badge

- [badge](uibarbuttonitem/badge-4sz3f.md)
- [Badge](uibarbuttonitem/badge-swift.struct.md)

### Customizing placement in a toolbar

- [hidesSharedBackground](uibarbuttonitem/hidessharedbackground.md) — A boolean value indicating whether the background this item may share with other items in the bar should be hidden.
- [sharesBackground](uibarbuttonitem/sharesbackground.md) — A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.

### Instance Properties

- [identifier](uibarbuttonitem/identifier.md) — An identifier used to match bar button items across transitions in a navigation bar or toolbar.
- [paddingRemoved](uibarbuttonitem/ispaddingremoved.md) — Whether the standard padding around the item should be removed. Default: NO _(beta)_
- [visibilityPriority](uibarbuttonitem/visibilitypriority.md) — Visibility priority for this item when placed in a button bar. _(beta)_

## See Also

### Bars

- [UIBarItem](uibaritem.md) — An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.
- [UIBarButtonItemGroup](uibarbuttonitemgroup.md) — A group of one or more bar button items for placement on a navigation bar or shortcuts bar.
- [UIBarButtonItemVisibilityPriority](uibarbuttonitemvisibilitypriority.md) _(beta)_
- [UINavigationBar](uinavigationbar.md) — Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [UISearchBar](uisearchbar.md) — A specialized view for receiving search-related information from the user.
- [UIToolbar](uitoolbar.md) — A control that displays one or more buttons along an edge of your interface.
- [UITabBar](uitabbar.md) — A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [UITabBarItem](uitabbaritem.md) — An object that describes an item in a tab bar.
- [UIBarPositioning](uibarpositioning.md) — A set of methods for defining the positioning of bars in iOS apps.
- [UIBarPositioningDelegate](uibarpositioningdelegate.md) — A set of methods that support the positioning of a bar that conforms to the [UIBarPositioning](uibarpositioning.md) protocol.
- [UIBarMinimization](uibarminimization-swift.struct.md)
