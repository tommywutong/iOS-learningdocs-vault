---
title: UITabBarControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate.json'
content_hash: 'sha256:1723b5ddc82b1653'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabBarControllerDelegate

<sub>Protocol</sub>

A set of methods you implement to customize the behavior of a tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITabBarControllerDelegate : NSObjectProtocol
```

## Overview

You use the [UITabBarControllerDelegate](uitabbarcontrollerdelegate.md) protocol when you want to augment the behavior of a tab bar. In particular, you can use it to determine whether specific tabs should be selected, to perform actions after a tab is selected, or to perform actions before or after the user customizes the order of the tabs. After implementing these methods in your custom object, you should then assign that object to the [delegate](uitabbarcontroller/delegate.md) property of the corresponding [UITabBarController](uitabbarcontroller.md) object.

All of the methods in this protocol are optional. For more information on how to use and configure tab bar controllers and their delegates, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing tab bar selections

- [- tabBarController:shouldSelectViewController:](<uitabbarcontrollerdelegate/tabbarcontroller(__shouldselect_).md>) — Asks the delegate whether the specified view controller should be made active.
- [- tabBarController:didSelectViewController:](<uitabbarcontrollerdelegate/tabbarcontroller(__didselect_).md>) — Tells the delegate that the user selected an item in the tab bar.

### Managing tab bar customizations

- [- tabBarController:willBeginCustomizingViewControllers:](<uitabbarcontrollerdelegate/tabbarcontroller(__willbegincustomizing_).md>) — Tells the delegate that the tab bar customization sheet is about to be displayed.
- [- tabBarController:willEndCustomizingViewControllers:changed:](<uitabbarcontrollerdelegate/tabbarcontroller(__willendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet is about to be dismissed.
- [- tabBarController:didEndCustomizingViewControllers:changed:](<uitabbarcontrollerdelegate/tabbarcontroller(__didendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet was dismissed.

### Overriding view rotation settings

- [- tabBarControllerSupportedInterfaceOrientations:](<uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations(__).md>) — Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.
- [- tabBarControllerPreferredInterfaceOrientationForPresentation:](<uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.

### Supporting custom tab bar transition animations

- [- tabBarController:animationControllerForTransitionFromViewController:toViewController:](<uitabbarcontrollerdelegate/tabbarcontroller(__animationcontrollerfortransitionfrom_to_).md>) — Called to allow the delegate to return a [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.
- [- tabBarController:interactionControllerForAnimationController:](<uitabbarcontrollerdelegate/tabbarcontroller(__interactioncontrollerfor_).md>) — Called to allow the delegate to return a [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.

### Instance Methods

- [- tabBarController:didSelectTab:previousTab:](<uitabbarcontrollerdelegate/tabbarcontroller(__didselecttab_previoustab_).md>) — Tells the delegate that the user selected the specified @c selectedTab in the tab bar controller.
- [- tabBarController:displayOrderDidChangeForGroup:](<uitabbarcontrollerdelegate/tabbarcontroller(__displayorderdidchangefor_).md>) — Notifies the delegate that the display order for the specified tab has been changed by the user.
- [- tabBarController:displayedViewControllersForTab:proposedViewControllers:](<uitabbarcontrollerdelegate/tabbarcontroller(__displayedviewcontrollersfor_proposedviewcontrollers_).md>) — Used with `UITabGroup.managingNavigationController`, this method allows the delegate to customize the displayed view controllers within the navigation stack for each level of selected tab. This method is called by the system if the selected tab in the `UITabBarController` belongs to or is in the hierarchy of a managing tab group (i.e. a `UITabGroup` with a non-nil `managingNavigationController`). By default, if this method is not implemented, the system will build the navigation stack by adding each tab’s `viewController` into the hierarchy, if one exists. This is especially useful to hide certain view controllers when transitioning between compact and regular size classes.
- [- tabBarController:shouldSelectTab:](<uitabbarcontrollerdelegate/tabbarcontroller(__shouldselecttab_).md>) — Asks the delegate whether the specified tab should be made active.
- [- tabBarController:tab:acceptItemsFromDropSession:](<uitabbarcontrollerdelegate/tabbarcontroller(__tab_acceptitemsfrom_).md>) — Notifies the delegate to perform a drop into the specified @c tab from the specified session.
- [- tabBarController:tab:operationForAcceptingItemsFromDropSession:](<uitabbarcontrollerdelegate/tabbarcontroller(__tab_operationforacceptingitemsfrom_).md>) — Asks the delegate for a drop operation to determine if drag items can be dropped into the specified @c tab
- [- tabBarController:visibilityDidChangeForTabs:](<uitabbarcontrollerdelegate/tabbarcontroller(__visibilitydidchangefor_).md>) — Notifies the delegate when editing has ended and the specified tabs have had their `isHidden` values changed by the user.
- [- tabBarControllerDidEndEditing:](<uitabbarcontrollerdelegate/tabbarcontrollerdidendediting(__).md>) — Notifies the delegate when the tab bar controller’s current editing state has ended.
- [- tabBarControllerWillBeginEditing:](<uitabbarcontrollerdelegate/tabbarcontrollerwillbeginediting(__).md>) — Notifies the delegate when the tab bar controller is about to begin editing.

## See Also

### Customizing the tab bar behavior

- [delegate](uitabbarcontroller/delegate.md) — The tab bar controller’s delegate object.
- [tabBarMinimizeBehavior](uitabbarcontroller/tabbarminimizebehavior.md) — Defines the minimize behavior for the tab bar, if it is supported.
- [MinimizeBehavior](uitabbarcontroller/minimizebehavior.md)
