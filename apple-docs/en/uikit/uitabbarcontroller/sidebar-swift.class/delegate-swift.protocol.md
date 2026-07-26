---
title: UITabBarController.Sidebar.Delegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol.json'
content_hash: 'sha256:8a143016551ced95'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# UITabBarController.Sidebar.Delegate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol Delegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- tabBarController:sidebar:contextMenuConfigurationForTab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_contextmenuconfigurationfor_).md>) — Called when the sidebar is about to display a context menu for the specified `tab`. Return either a concrete `UIContextMenuConfiguration` or nil if the tab does not show context menus.
- [- tabBarController:sidebar:didEndDisplayingTab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_didenddisplaying_).md>) — Notifies the delegate when the sidebar has finished displaying the row representing the specified `tab`
- [- tabBarController:sidebar:itemForRequest:](<delegate-swift.protocol/tabbarcontroller(__sidebar_itemfor_).md>) — Return a `UITabSidebarItem` for the specified item request. When created, the item will be preconfigured to the appropriate defaults for its given content. If this method is not implemented, a default sidebar item will be provided for the request.
- [- tabBarController:sidebar:itemsForAddingToDragSession:tab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_itemsforaddingto_tab_).md>) — Called when a new drag session is requesting items to add to the existing drag session in the sidebar from the specified `tab`. Return items if the specified tab can add to the drag session, or an empty array if nothing should be added.
- [- tabBarController:sidebar:itemsForBeginningDragSession:tab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_itemsforbeginning_tab_).md>) — Called when a new drag session has begun in the sidebar from the specified `tab`. Return drag items if the specified tab can be dragged, or an empty array if no drags should begin. Note that if drag items are returned on tabs in groups that allow reordering, then tab reordering is disabled when the sidebar is not in editing.
- [- tabBarController:sidebar:leadingSwipeActionsConfigurationForTab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_leadingswipeactionsconfigurationfor_).md>) — Called when the sidebar is about to show leading swipe actions for the specified `tab`. Return either a concrete `UISwipeActionsConfiguration` or nil if the tab does not show swipe actions.
- [- tabBarController:sidebar:sidebarAction:group:acceptItemsFromDropSession:](<delegate-swift.protocol/tabbarcontroller(__sidebar_sidebaraction_group_acceptitemsfrom_).md>) — Receive the drop from into the `sidebarAction` using the specified session. This is only called if the drop operation returned from `tabBarController:sidebar:sidebarAction:operationForAcceptingItemsFromDropSession` is valid for a drop.
- [- tabBarController:sidebar:sidebarAction:group:operationForAcceptingItemsFromDropSession:](<delegate-swift.protocol/tabbarcontroller(__sidebar_sidebaraction_group_operationforacceptingitemsfrom_).md>) — Determines if items from the specified drop session can be dropped into the specified `sidebarAction`. If the operation is either a `.move` or `.copy`, then the drop will proceed and `tabBarController:sidebar:sidebarAction:acceptItemsFromDropSession:` is called. By default, the drop will be treated as a cancel operation if this is not implemented.
- [- tabBarController:sidebar:trailingSwipeActionsConfigurationForTab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_trailingswipeactionsconfigurationfor_).md>) — Called when the sidebar is about to show trailing swipe actions for a particular tab. Return either a UISwipeActionsConfiguration object or nil if this tab does not show swipe actions.
- [- tabBarController:sidebar:updateItem:](<delegate-swift.protocol/tabbarcontroller(__sidebar_update_).md>) — Called whenever the sidebar item’s `configurationState` changes or the item is reconfigured. The passed in item will accrue all modifications until the delegate requests for a new sidebar item from the delegate method `tabBarController:sidebar:itemForRequest:`
- [- tabBarController:sidebar:willBeginDisplayingTab:](<delegate-swift.protocol/tabbarcontroller(__sidebar_willbegindisplaying_).md>) — Notifies the delegate when the sidebar is about to display the row representing the specified `tab`
- [- tabBarController:sidebarAvailabilityDidChange:](<delegate-swift.protocol/tabbarcontroller(__sidebaravailabilitydidchange_).md>) — Notifies the delegate when `UITabBarController.Sidebar.isAvailable` changes. _(beta)_
- [- tabBarController:sidebarVisibilityWillChange:animator:](<delegate-swift.protocol/tabbarcontroller(__sidebarvisibilitywillchange_animator_).md>) — Notifies the delegate when the visibility of the sidebar is about to change when `sidebar.isHidden` changes. Add animations to the animator to run alongside the visibility update. Alongside animations and completions will run immediately if the sidebar visibility is changed without animation.

## See Also

### Setting the sidebar delegate

- [delegate](delegate-swift.property.md) — The object managing the delegate of the sidebar.
