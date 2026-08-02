---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingExtensionMenus/AddingExtensionMenus.html
archived_at: '2026-07-27T06:57:07.648761Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20Popovers.md)[Previous](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md)

# Adding Extension Menus

You can create menus that pop up when the user clicks a toolbar item that you have created. If the toolbar item’s `command` property is set to `null`, clicking the toolbar item displays the menu immediately. If the `command` property is _not_ `null`, the user must press and hold in order to see the menu—clicking alone sends the command instead. You can set a toolbar item’s `command` property to `null` either programmatically or simply by leaving the toolbar item’s Command field blank in Extension Builder.

You normally associate a menu with a toolbar item using Extension Builder, but you can also attach a menu to a toolbar item programmatically by setting the toolbar item’s `menu` property.

When the user clicks your toolbar item, a `"menu"` event is generated prior to displaying the menu, followed by `"validate"` events for each menu item. When the user chooses one of your menu items, a `"command"` event is generated for that menu item.

__Note:__ You can assign either a menu or a popover to a toolbar item, but not both.

## Setting Up Menus in Extension Builder

To add a menu to a toolbar item, start by clicking the New Menu button in Extension Builder; the Menus pane expands, as shown in Figure 7-1.

__Figure 7-1__  Extension Menus pane

（原归档配图未能恢复：`ExtensionMenus.png`）

Give the menu a unique identifier, then add any menu items that normally appear in your menu—you can add and delete menu items at runtime as well.

For each menu item, set the following values:

- Type—choose Normal for a menu item, or Separator for a line separating groups of menu items.
- Title—the text shown on your menu item.
- Image—the filename of an image you created for this menu item. The image must be in your extension folder for you to see it in the pop-up menu. This value is optional. You can also assign the URL of an image file to the menu item dynamically at runtime.
- State—the default menu item state: checked, unchecked, or mixed. You can modify the state at runtime.
- Submenu—the menu to activate if this menu item is selected. Create submenus by clicking New Menu.
- Disabled—select this option if the menu item should be grayed-out by default. You can change this property at runtime.
- Identifier—a unique identifier for this menu item.
- Command—the `command` property of the `"command"` event generated when this menu item is clicked. If this field is left blank, the identifier is used as the command.

After you have created your menu, go to the toolbar item you want to associate with this menu and click the Menu button. Then choose this menu’s identifier from the pop-up menu, as illustrated in Figure 7-2.

__Figure 7-2__  Attaching a menu to a toolbar item

（原归档配图未能恢复：`ToolbarItemWithMenu.png`）

## Creating an Image (Optional)

You can create an image to display alongside any item in your menu. For best results, create your image as a 16x16 pixel image on a transparent background. Images larger than 16x16 are scaled down. Unlike the image in a toolbar item, colored images are displayed normally.

Save your image as a `.png` file. Put the image file inside your extension folder. Use a filename that is URL-friendly (no blank spaces, ampersands, or periods, for example).

Choose the filename from the pop-up menu in the Image field for your menu item.

You can include an alternate image at double the resolution for use on high-resolution displays. Use the same name for the alternate image file, but append the characters `@2x`. For example, if your image is named `myToolBarImg.png`, the high-resolution image should be named `myToolBarImg@2x.png`.

You can assign an image to a menu item at runtime, in which case you supply the URL of the image. The URL is absolute and can refer to either an image file in your extension package or an image on the web.

## Responding to Events

In your global HTML file, register on the Safari app for `"command"` events to receive commands when one of your menu items is clicked. You may also want to add listener functions for `"validate"` and `"menu"` events if your menu changes dynamically. For example:

`safari.application.addEventListener("validate", validateHandler, true);`

`safari.application.addEventListener("menu", menuHandler, true);`

`safari.application.addEventListener("command", commandHandler, true);`

Safari generates `"validate"` events on the toolbar item periodically, including just before your menu is displayed. Use this event if you need to dynamically enable and disable the toolbar item itself, or to update a badge on the toolbar item to reflect changes in your menu. If your toolbar item is always enabled and has no badge, you don’t need to respond to this event. Check to see whether the `event.target.identifier` property for the `"validate"` event is the identifier for your toolbar item. For example:

`if (event.target.identifier !== "myToolbarItemID") return;`

Safari generates a `"menu"` event when your menu is about to be displayed. This event is your opportunity to add, remove, or modify menu items dynamically. If your menu does not change dynamically, you don’t need to respond to this event. The event target is a menu, so the `event.target.identifier` property for the `"menu"` event is the identifier of the target menu.

Safari generates a `"validate"` event for each menu item prior to displaying your menu, but after the `"menu"` event. You can use this event to dynamically enable, disable, or modify individual menu items. If your menu items do not change dynamically, you do not need to respond to these events. The `event.target.identifier` property for the `"validate"` event is the identifier of your menu item.

When the user clicks one of your menu items, Safari generates a `"command"` event. The `event.command` property is the command value assigned to your menu item. You need to listen for and respond to this event in order for your menu to do anything. You typically write a single command handler for your menu, with a case statement to sort the commands by menu item.

Your global HTML page is the best place to put event handlers.

If your menu changes depending on things such as currently open windows or tabs, you may want to listen for other events as well. See [The Windows and Tabs API](The%20Windows%20and%20Tabs%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjxfvjvomi) for details.

## Modifying the Menu Dynamically

You can dynamically add, delete, and modify menu items at runtime. You can also create a menu at runtime and attach it to a toolbar item you have created. There is a `menus` array that is a property of the `extension` object.

__Important:__ You cannot add, delete, or modify menus or menu items while the menu is visible. Attempting to do so fails and causes an exception to be thrown. Check the `visible` property of your menu instance before making any changes, and hide the menu by calling `myMenu.hide()` if you must modify or delete it immediately.

- Create a menu by calling `myMenu = safari.extension.createMenu(ID)`.
- Assign a menu to a toolbar item by setting the toolbar item’s `menu` property to the menu.

  You can obtain an instance of your toolbar item by iterating through the `extension` object’s `toolbarItems` array and testing the `identifier` property for your toolbar item.
- Delete a menu by calling `safari.extension.removeMenu(ID)`. Set the toolbar item’s `menu` property to `null` before deleting its menu.
- Delete a menu item by calling `removeMenuItem(index)` on the `menu` object.
- Add a menu item by calling `appendMenuItem(identifier, title)` or `insertMenuItem(index, identifier, title)` on the `menu` object.
- Add an image to a menu item by setting the menu item’s `image` property to the URL of an image file (this can be the filename of an image in your extension folder or the HTTP or HTTPS URL of an image on the Internet).
- Modify a menu item by changing its `title`, `disabled`, `checkedState`, and `image` properties. See [SafariExtensionMenuItem](https://developer.apple.com/documentation/safariextensions/safariextensionmenuitem) Reference for details.

  __Note:__ Disabled menu items in extension menus are displayed as grayed-out, unlike contextual menu items, which are not displayed when they are disabled.
- Add a separator to your menu by calling `appendSeparator()` or `insertSeparator(index)` on the menu object.

[Next](Adding%20Popovers.md)[Previous](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md)
