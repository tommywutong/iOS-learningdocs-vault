---
title: Creating Carbon Menus
apple_id: TP30001065
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-02-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/carbonmenus/carbonmenus_conc/carbonmenus_conc.html
archived_at: '2026-07-15T05:24:56.863158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Carbon%20Menu%20Tasks.md)

# Carbon Menus Concepts

This chapter gives conceptual information about menus that is useful for developers of Carbon applications.

Note that this chapter does not describe general menu appearance, usage, or behavior. For that information, see _Apple Human Interface Guidelines_.

All menus are displayed in the menu bar, which runs across the top of the main display screen. The menu bar is also called the root menu.

A menu reference (type `MenuRef`) identifies an instance of a menu. This opaque structure contains information about the menu such as its size, position, menu items, and so on.

Each menu can have an associated menu ID, which must be a positive integer that uniquely identifies the menu within the application. Many Menu Manager functions require a menu ID to specify the menu to be acted upon.

Each menu has one or more menu items associated with it.

Menu items have a menu item index associated with them that specifies its position within a given menu. That is, a menu item with index 2 is the second item down in the menu. You can then specify any given menu item in an application by its parent menu and its menu item index.

A menu item may also be a submenu. Sometimes called hierarchical menus, a submenu opens an additional menu and displays another set of menu items. In most cases, you cannot select the submenu itself, but only one of its menu items.

Each menu item can have a command key associated with it. Better known as the keyboard equivalent or command key equivalent, the user can enter this key combination as an alternate way to select the menu item.

Note that the command key equivalent can be either a character code or a virtual keycode. A character code specifies a typeable character (for example, “k”, “K”, or “3”), while a virtual keycode identifies the physical key on the keyboard, some of which may not have a corresponding character (such as F10 or the Delete key). To display such “characterless” keys, the Menu Manager uses special keyboard glyphs.

Each menu item (even those with submenus) can have a command ID associated with it. This ID uniquely identifies the menu item within the application. When the user selects a menu item, the Carbon Event Manager can send an event containing the command ID to your application, where you can take appropriate action. You can also use the command ID internally to find a menu item even if you don’t know the item’s parent menu.

In Mac OS X v10.3 and later, all standard menu content is drawn using the HIView drawing model. This object-oriented view system for drawing user interface elements improves performance and reduces the amount of code needed for custom objects. If you are using standard menus and menu items, you do not need to worry about adopting HIView as that is done for you. However, if you want to use custom menus, you should learn how to do so using the HIView model. For more details, see _[HIView Programming Guide](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt)_.

[Next](Carbon%20Menu%20Tasks.md)

