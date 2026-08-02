---
title: Toolbar Programming Topics for Cocoa
apple_id: 10000109i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Tasks/SettingTBItemRep.html
archived_at: '2026-07-15T07:20:53.290719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Toolbar Programming Topics for Cocoa](Introduction%20to%20Toolbars.md)


[Next](Validating%20Toolbar%20Items.md)[Previous](Creating%20a%20Toolbar%20in%20Interface%20Builder.md)

# Setting a Toolbar Item’s Representation

The `label` attribute of a toolbar item is displayed as the text for the toolbar item when the toolbar is in Icon & Text Mode or Text Only Mode. By default, the label is also used in the overflow menu as the title of the menu item representing the toolbar item. The `paletteLabel` attribute of an item is used instead of label in the customization palette. (If `paletteLabel` is not set, the customization palette does not use `label` by default.)

Clicking on the label of an image item in Text Only Mode or selecting an image item’s overflow menu item simply invokes the image item’s action.

View items, on the other hand are more complex and can’t usually be handled so simply. Primarily to give view items more flexibility, NSToolbarItem provides a `menuFormRepresentation` attribute.

Every toolbar item has a menu form representation, which is a menu item. The toolbar provides an initial default menu form representation that uses the toolbar item’s label as the menu item’s title. The application can provide a custom menu form representation which can have a submenu and which can have a title different from the toolbar item’s label. If a toolbar item’s custom menu form representation has a submenu, then the toolbar drops down that submenu under the toolbar item in Text Only Mode and displays the submenu in the overflow menu.

If a view item’s menu form representation attribute has not been set, NSToolbar disables the overflow menu item as well as the toolbar item’s text in Text Only Mode. If the attribute has been set and the menu form representation has a submenu, NSToolbar enables the overflow menu item as well as the toolbar item’s text in Text Only Mode. If the attribute has been set and the menu form representation does not have a submenu, the toolbar validates the menu item to determine whether to enable the toolbar item’s text in Text Only Mode and the toolbar item’s overflow menu item. For more detail on how the validation works, see [Validating Toolbar Items](Validating%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tglkciffeorsiirca).

Image items as well as view items can use a simple `menuFormRepresentation` without a submenu merely for the purpose of replacing `label` as the title of the toolbar item’s overflow menu item. The only situation in which you should use this feature is when the label is empty.

[Next](Validating%20Toolbar%20Items.md)[Previous](Creating%20a%20Toolbar%20in%20Interface%20Builder.md)

