---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingContextualMenuItems/AddingContextualMenuItems.html
archived_at: '2026-07-27T06:57:07.702944Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Injecting%20Scripts.md)[Previous](Adding%20Popovers.md)

# Adding Contextual Menu Items

Contextual menus pop up when the user Control-clicks or right-clicks over an object. Safari presents different contextual menus when the mouse pointer is over the toolbar, Bookmarks bar, an extension bar, the tab bar, or the contents of a webpage.

Your extension can add menu items to the contextual menu that pops up over web content. You control the actions of the menu item by installing a listener function for the `"command"` event in either your global HTML page or in an extension bar.

Your extension can add multiple items to the contextual menu. The simplest way to add menu items is through Extension Builder, but you can also add them programmatically.

__Note:__ Adding menu items to existing Safari contextual menus is similar to, but distinct from, creating your own extension menus. See [Adding Extension Menus](Adding%20Extension%20Menus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrqfvjvomi) for a description of extension menus.

## Context Menu Events

When the user Control-clicks or right-clicks in the web content window, a series of events are fired before the contextual menu is displayed:

1. A `"contextmenu"` DOM event that you can listen for in an injected script.

   This event gives you the opportunity to add context information to the event or to prevent the menu from displaying.
2. A `"contextmenu"` extension event that you can listen for in your global page or an extension bar.

   This event gives you the opportunity to add menu items programmatically. You can read the context information set by your injected script to help you determine what menu items to add.
3. A `"validate"` event for each menu item.

   This event gives you the opportunity to disable menu items that should not be displayed, or modify a menu item’s title.

__Note:__ There are two versions of the `"contextmenu"` event—a DOM event that you can listen for in an injected script, and an extension event that you can listen for in your global page or an extension bar. The DOM event is always sent first.

You are not required to respond to any of these events. You can add contextual menu items using Extension Builder, and if the menu items should be included in the contextual menu, you need to respond only to the `"command"` event generated when the user actually chooses one of your items from the menu. The `"contextmenu"` and `"validate"` events provide opportunities for you to modify this default behavior.

## Adding a Contextual Menu Item Using Extension Builder

You add an item to the contextual menu by clicking New Context Menu Item in Extension Builder. This expands the contextual menu items pane, as shown in Figure 9-1.

__Figure 9-1__  Contextual Menu Items pane

（原归档配图获取待重试：`AddingMenuItems.jpg`）

Enter a title for the menu item. This is the text that will appear in the contextual menu. This field is required.

Enter an identifier. This is required. The identifier must be unique within your extension.

Enter a command name. This is the name of the `"command"` event that is generated when the user chooses your item from the menu. It does not need to be unique. For example, you might have both a toolbar item and a contextual menu item that issue the same command. If this field is left blank, the identifier is used.

## Responding to Commands

When the user chooses your contextual menu item, Safari emits a `"command"` event. The `command` property of the event is the string you entered in the Command field in Extension Builder. If you left the Command field blank, the identifier is used instead.

Respond to the `"command"` event by installing a listener function in either the global HTML page or an extension bar.

You can’t receive the `"command"` event in an injected script. If you need the command to initiate an action in an injected script, respond to the command in the global HTML page or an extension bar and send a message to the script. For details, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

Before the contextual menu displays, Safari will ask you to validate the command by sending a `"validate"` event.

Your `"validate"` event handler should verify that it is appropriate to display the command. For example, if your menu item reloads the active tab, you should verify that the active tab has a URL to reload. If the tab is empty, your validate function should disable the menu item by setting `event.target.disabled = true`.

If you disable the contextual menu item, it is not displayed. This is different from the behavior of an extension menu item, which is displayed as grayed-out.

If there is no possibility that the command is invalid, such as a "new tab" menu item, you are not required to implement a validate handler function.

You can have multiple UI items that issue the same command, such as a toolbar button and a contextual menu item. You can use the same event handlers for command and validation, regardless of the source.

If your functions are part of the global HTML page, you should register your listener functions with the app:

`safari.application.addEventListener("command", myCommandHandler, false);`

`safari.application.addEventListener("validate", myValidateHandler, false);`

If your functions are part of an extension bar, you should register your listener functions with the extension bar’s parent window:

`safari.self.browserWindow.addEventListener("command", myCommandHandler, false);`

`safari.self.browserWindow.addEventListener("validate", myValidateHandler, false);`

While you can implement the event handlers in either a global HTML page or in an extension bar, it is more efficient to use a global HTML page, because the code is loaded only once per session instead of once per page.

## Modifying the Default Behavior

If you add contextual menu items using Extension Builder, the default behavior is for the items to be displayed when the user opens a contextual menu over web content, and for a `"command"` event to be generated when the user chooses a menu item. You can modify this behavior in the following ways.

### Adding Context Information

If you add a listener for the DOM `"contextmenu"` event in an injected script, you can set context information by calling `setContextMenuEventUserInfo` in your event handler.

You can add the listener event to the document or any of its children, such as the body or a particular node. For example:

`document.addEventListener("contextmenu", handleContextMenu, false);`

The following listener function stores the element name that the user clicks, so your extension can respond differently to a click on an image or a paragraph, for example:

```
function handleContextMenu(event) {
    safari.self.tab.setContextMenuEventUserInfo(event, event.target.nodeName);
}
```

The data you store can be retrieved from the `userInfo` property of later events. You can store any data as user info that you can pass in a message.

### Disabling the Contextual Menu

You can prevent the contextual menu from displaying at all by calling `event.preventDefault()` from an injected script in response to the DOM `"contextmenu"` event.

The following snippet prevents the contextual menu from displaying if the user clicks a video element:

```
document.addEventListener("contextmenu", handleContextMenu, false);

function handleContextMenu(event) {
    if (event.target.nodeName == "VIDEO") {
        event.preventDefault();
    }
}
```

### Adding Contextual Menu Items Programmatically

You can add menu items to the contextual menu by responding to the extension version of the `"contextmenu"` event in your global page or an extension bar. If you stored information on the event by calling `setContextEventUserInfo()` in your injected script, you can use that information to help you decide what menu items to add.

For example, the following snippet adds an Enlarge Image menu item to the contextual menu if the user clicks an image. (This snippet relies on an injected script to store the event target’s node name as user info.)

```
safari.application.addEventListener("contextmenu", handleContextMenu, false);

function handleContextMenu(event) {
    if (event.userInfo === "IMG") {
        event.contextMenu.appendContextMenuItem("enlarge", "Enlarge Item");
    }
}
```

__Note:__ You can only add menu items in response to the `"contextmenu"` event, not delete them. To temporarily delete a menu item, set `event.target.disabled = true` in response to the menu item’s `"validate"` event.

### Changing the Contextual Menu Item Title

You can modify a menu item’s title before it is displayed by setting the `event.target.title` property in a `"validate"` event handler.

If you set user info in an injected script using a `"contextmenu"` event handler, you can read the `event.userInfo` property in your `"validate"` event handler to help decide how to change the label.

For example, if an injected script stores the selected text being clicked, you could change a Search Google Scholar menu item to include the selected text using the following snippet:

`event.target.title = "Search for \u201C" + event.userInfo + "\u201D on Google Scholar";`

In this example, you would also want to use the `event.userInfo` in your `"command"` event handler.

## Deciding Where to Respond

When your contextual menu item is chosen, a `"command"` event is generated. You can listen for the event in either a global HTML page or in an extension bar. If you put the event handler in the global file, you should register for the event at the app level. If your event handler is in an extension bar, you should register with the extension bar’s parent window.

The difference is that there is only one instance of the global HTML page’s functions, but there is an instance of an extension bar in every open window.

If every instance of the extension bar registers for events at the app level, every instance responds to the command. If each instance registers with its parent window, only the instance in the window where the item was chosen responds to the command.

Using the global file is more efficient, as it loads only once. Furthermore, you shouldn’t create an empty extension bar just to hold an event handler. If your extension has a bar, however, it might make sense to put the event handler there, particularly if the action it takes is window-specific, like rearranging the tabs.

The only time you might want to put an event handler in the extension bar and register it with the app is if your command acts on all open windows. Then your choice would be to iterate through the windows in a global function or have a function local to each window that responds to the event independently.

### If You Respond from a Global HTML Page

- Register with the app: `safari.application.addEventListener()`.
- The window the event came from is `safari.application.activeBrowserWindow`.

### If You Respond from an Extension Bar

- Register with the parent page: `safari.self.browserWindow.addEventListener()`.
- The window the event came from is `safari.application.activeBrowserWindow`.

## Example: Implementing a New Window Contextual Menu Item

The following example adds a New Window item to the contextual menu, which opens a new browser window.

You add the menu item in Extension Builder, as illustrated in Figure 9-2.

__Figure 9-2__  Adding a menu item

（原归档配图获取待重试：`NewWindowItem.jpg`）

The code in the following listing responds to the `new-window` command event and the `new-window` validate event. Since opening a new window is possible any time, there is no validate handler. The `"command"` listener function is registered with the app.

[Listing 9-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnbnknltcma) is intended to be included in your global HTML page. If it is included in an extension bar, the event listeners need to be added to the bar’s parent window instead of the app. Otherwise each instance of the extension bar executes the command—instead of adding just one window, every open window adds a window, and the number of windows is doubled.

__Listing 9-1__  New window command handlers

```
function performCommand(event) {
    if (event.command === "new-window") {
        safari.application.openBrowserWindow();
    }
}
safari.application.addEventListener("command", performCommand, false);
```

[Next](Injecting%20Scripts.md)[Previous](Adding%20Popovers.md)
