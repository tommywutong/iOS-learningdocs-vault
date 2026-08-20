---
title: Toolbar Programming Topics for Cocoa
apple_id: 10000109i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Tasks/ValidatingTBItems.html
archived_at: '2026-07-15T07:20:55.798607Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Toolbar Programming Topics for Cocoa](Introduction%20to%20Toolbars.md)


[Next](Setting%20a%20Toolbar%20Item%E2%80%99s%20Size.md)[Previous](Setting%20a%20Toolbar%20Item%E2%80%99s%20Representation.md)

# Validating Toolbar Items

The toolbar validates every visible image item and every invisible item’s overflow menu item.

By default toolbar items have click-through behavior, which is to say that toolbar items remain enabled and clickable when the user switches to another window or even another application. To change this behavior for a toolbar item, your validation code needs to take the larger environment into account. See _Aqua Human Interface Guidelines_ for more information on click-through behavior.

The toolbar automatically takes care of darkening an image item when it is clicked and fading it when it is disabled. All your code has to do is validate the item. If an image item has a valid target/action pair, then the toolbar will call NSToolbarItemValidation’s `validateToolbarItem:` on target if the target implements it; otherwise the item is enabled by default.

In the absence of a custom menu form representation, NSToolbar validates an image item’s overflow menu in the same way that it validates the toolbar item in the toolbar.

Validation for view items is not automatic because a view item can be of unknown complexity. To implement validation for a view item, you must subclass NSToolbarItem and override `validate` (because NSToolbarItem’s implementation of `validate` does nothing for view items). In your override method, do the validation specific to the behavior of the view item and then enable or disable whatever you want in the contents of the view accordingly. If the view is an NSControl you can call `setEnabled:`, which will in turn call `setEnabled:` on the control.

In the absence of a custom menu form representation, NSToolbar by default disables a view item’s overflow menu item.

If a toolbar item has a custom menu form representation with no submenu, then the toolbar will validate the overflow menu item and the toolbar item’s text in Text Only Mode differently than it would with the default menu form representation: If the menu form representation menu item’s target implements `validateMenuItem:` (part of NSMenuValidation), the toolbar calls that method to validate both the overflow menu item and the toolbar item’s text in Text Only Mode.

[Next](Setting%20a%20Toolbar%20Item%E2%80%99s%20Size.md)[Previous](Setting%20a%20Toolbar%20Item%E2%80%99s%20Representation.md)

