---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/HowMenusWork.html
archived_at: '2026-07-15T07:16:42.683644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Using%20Menu%20Item%20States.md)[Previous](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)

# How Menus Work

The classes [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) and [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem) are the basis for all types of menus. An instance of `NSMenu` manages a collection of menu items and draws them one beneath another. An instance of `NSMenuItem` represents a menu item; it encapsulates all the information its `NSMenu` object needs to draw and manage it, but does no drawing or event-handling itself. Generally, you use Interface Builder to create and modify any type of menu. However, `NSMenu` and `NSMenuItem` provide you with methods to change your application's menus dynamically.

Cocoa gives you a core set of classes that handle menus no matter where they appear. Menus commonly appear in various parts of the user interface:

- The application’s menu bar. This is at the top of the screen.
- A pop-up menu. This can appear anywhere in a window.
- The status bar. This begins at the right side of the menu bar (to the left of Menu Extras and the menu bar clock) and grows to the left as items are added to it.
- Contextual menus. These appear when the user right-clicks or left-Control-clicks an item.
- The Dock menu. A menu for each dock icon appears when the user right-clicks or left-Control-clicks the icon, or when the user left-presses the mouse pointer on the icon.

The classes [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) and [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem) are the basis for all types of menus. An instance of `NSMenu` manages a collection of menu items and draws them one beneath another. An instance of `NSMenuItem` represents a menu item; it encapsulates all the information its `NSMenu` object needs to draw and manage it, but does no drawing or event-handling itself.

Menu views are capable of having one attached menu view at any given time. An attached menu view displays the contents of a submenu and is typically positioned next to the menu item with which it is associated.

`NSMenuItem` lets you set the titles, actions, targets, tags, images, enabled states, and similar attributes of individual menu items, as well as to obtain the current values of these attributes. Whenever an attribute for a menu item changes, it notifies its associated `NSMenu` with the [itemChanged:](https://developer.apple.com/documentation/appkit/nsmenu/1518154-itemchanged) method.

_You typically use Interface Builder to create and modify any type of menu, so often there is no need to write any code._ However, `NSMenu` and `NSMenuItem` provide you with methods to change your application's menus dynamically, in particular to allow you to enable and disable existing menu items (see [Enabling Menu Items](Enabling%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi3dclkciffeershivca)).

All of an application’s menus in the menu bar are owned by one `NSMenu` instance that’s created by the application when it starts up. You can retrieve this main menu with the `NSApplication` method [mainMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428634-mainmenu).

Application menus drop down from the menu bar when the user clicks in a menu’s title, and submenus appear to the right or left of their menus, depending on the available screen space.

Pop-up buttons are implemented by the `NSPopUpButton` class. You can choose from a pop-up list or a pull-down list, with the [setPullsDown:](https://developer.apple.com/documentation/appkit/nspopupbutton/1532070-pullsdown) method:

- A pop-up list lets the user choose one option among several and generally displays the option that was last selected.

  You should use a pop-up list to select items from a medium-sized set of options, approximately 5 to 12 items. Generally, smaller lists are better handled with a group of radio buttons; and larger lists, with a scrolling list. However, if space is at a premium a pop-up list may be appropriate for other list sizes. For example, a pop-up list displaying various zoom factors can easily fit next to a scroll bar at the bottom of a window.
- A pull-down list is generally used for selecting commands in a specific context.

An `NSPopUpButton` object contains an `NSPopUpButtonCell` object. The button contains the button’s data, and the cell controls the button’s appearance. Generally, you’ll invoke methods on the `NSPopUpButton` object, although most of the work is handled by the `NSPopUpButtonCell` instance. Most of `NSPopUpButton`‘s methods are convenience methods which simply invoke the same method on the cell.

To implement its menu, the button cell contains an `NSMenu` object, which in turn contains several `NSMenuItem` objects, one for each item in the menu. Avoid invoking methods on the `NSMenu` object directly, but instead invoke methods on the `NSPopUpButton` instance, which may need to do some housekeeping before invoking the appropriate methods on the menu. However, you can retrieve the menu with the `NSPopUpButton` method `menu`. The `NSPopUpButton` methods you use most often are the methods that tell you which item is selected.

Generally, you create an `NSPopUpButton` object with Interface Builder. You can define the `NSPopUpButton` object’s target and action, as well as the targets and actions of each item in the button’s list, programmatically or through Interface Builder.

You can attach a contextual menu to any `NSView` object. When the user Control-clicks on that view, the menu appears. To assign a menu to a view, use `setMenu:`, which `NSView` inherits from `NSResponder`.

Your subclass can define a menu that’s used for all instances by implementing the `defaultMenu` class method. To change the menu displayed based on the mouse event, override the `menuForEvent:` instance method. This allows the view clicked to display different menus based on the location of the mouse and of the view’s state, or to change or enable individual menu items based on the commands available for the view or for that region of the view.

[Next](Using%20Menu%20Item%20States.md)[Previous](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)

