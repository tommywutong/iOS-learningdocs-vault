---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingButtonstotheMainSafariToolbar/AddingButtonstotheMainSafariToolbar.html
archived_at: '2026-07-27T06:57:07.637708Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20Extension%20Menus.md)[Previous](Adding%20a%20Global%20HTML%20Page.md)

# Adding Buttons to the Main Safari Toolbar

Safari has a user-customizable toolbar that can contain a selection of buttons, such as a Home button, Zoom button, and New Tab button. Your extension can define new toolbar items that can be installed in the toolbar. These items also appear in the Customize Toolbar panel.

You control the actions of a toolbar item from either the global HTML page or from an extension bar by installing a listener function for the `"command"` event.

Your extension can add more than one button to the toolbar, but if you are adding more than a few, you should not have them installed by default; you might also consider creating an extension bar for them instead.

Adding a button requires three steps: creating an image, filling out the appropriate fields in Extension Builder, and adding logic to make the button do something.

You can add either a pop-up menu or a popover window to a toolbar item. See [Adding Extension Menus](Adding%20Extension%20Menus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrqfvjvomi) and [Adding Popovers](Adding%20Popovers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrrfvjvomi) for details.

__Note:__ You can assign either a menu _or_ a popover to a toolbar item, but not both.

## Creating an Image

Buttons on the Safari toolbar are largely transparent, allowing them to be filled with the appropriate gradient for the current OS X or Windows user interface. You do not need to draw the button itself, only the opaque part of its contents.

If you are used to working with alpha channels, create a 16x16 image consisting solely of an 8-bit alpha channel, with alpha set to 255 for the transparent part of the button (including the outline); alpha set to 0 for the opaque parts of the button, which will appear in black; and intermediate alpha values for anti-aliasing.

If you are not used to working with alpha channels, create a 16x16 pixel image with a transparent background. Fill in the button contents in black, or simply set the opacity for those pixels to 100%. If you draw or put text on the button in black, notice that some pixels are gray. This is anti-aliasing. These pixels are not completely black, so they are shaded. This is illustrated in Figure 6-1.

__Figure 6-1__  Anti-aliased text in black on transparent background

（原归档配图获取待重试：`textbutton.jpg`）

If you save your image as-is, these shaded pixels appear as black because they are completely opaque. To preserve the anti-aliasing, make these gray pixels partly transparent. Depending on your image editor, this may be accomplished by partly erasing the pixels or by setting the pixel opacity directly.

Save your image as a `.png` file.

## Setting Up Extension Builder

If you have not already done so, click the + button in Extension Builder, choose New Extension, and give your extension a name. Create an image for each button you are adding and drag it into your extension folder.

Click New Toolbar Item in Extension Builder. This expands the Toolbar Items pane, as shown in Figure 6-2.

__Figure 6-2__  Adding toolbar items

（原归档配图获取待重试：`ToolbarItems.png`）

- Enter a label for your toolbar item. This is a text label that is displayed if the bar has more buttons than can be shown and the user clicks the chevron to see the overflow.
- Enter a palette label for your toolbar item. This is the text label that is displayed when the user is customizing the toolbar. It can be the same as the label, or it can be a bit longer if that makes the function of your toolbar item clearer. If this field is left blank, the label is used.
- Enter a tooltip for your toolbar item. This is the text displayed when the mouse pointer hovers over the item. If this field is left blank, the label is used.
- Drag a `.png` image file into your extension folder. The image should ideally be 14x14 or 16x16 pixels. Larger images are cropped at 18x18 pixels. The image is an alpha mask. It must contain an 8-bit alpha channel defining the part of the button face that is drawn, and nothing else. Using an alpha mask allows your button to blend in with Safari’s native toolbar buttons on different platforms, even if the Safari UI should change. Once you have an image file in your extension folder, you can choose it from the Image pop-up menu. An image is required.

  You can include an alternate image at double the resolution for use on high-resolution displays. Use the same name for the alternate image file, but append the characters `@2x`. For example, if your image is named `myToolBarImg.png`, the high-resolution image should be named `myToolBarImg@2x.png`.
- If you have created a menu to be triggered by this toolbar item, select it from the pop-up menu.
- If you have created a popover to be triggered by this toolbar item, select it from the pop-up menu.
- Enter an identifier. This field is required. The identifier is your name for the toolbar item. The name must be unique in your extension. You can identify the toolbar item later by iterating through the array of items and checking the value of the `identifier` property:

  ```
  var itemArray = safari.extension.toolbarItems;
  for (var i = 0; i < itemArray.length; ++i) {
      var item = itemArray[i];
      if (item.identifier == "my lovely button")
         {
         /* Do something. */
         }
  ```
- Enter a command name. This is the `event.command` property of the event that is generated when the user clicks your item in the toolbar. It does not need to be unique. For example, you might have both a toolbar button and a contextual menu item that issue the same command. If this field is left blank, the identifier is used.

  If you add a menu or a popover to the toolbar item, you may want to leave the Command field blank. Leaving the field blank sets the `command` property to `null` and causes the menu or popover to be displayed immediately when the user clicks your toolbar item. Otherwise, the command executes when the button is clicked, and the menu or popover is displayed only when the user clicks and holds.

If you select the Include By Default checkbox, the item is installed in the toolbar when the extension is installed. Otherwise, the user must choose to add the item in the Customize Toolbar window.

## Responding to Commands

When the user clicks the button, Safari emits a `"command"` event, if one is specified. The `command` property of the event is the string you entered in the Command field in Extension Builder. If you left the Command field blank, the identifier is used instead.

__Note:__ You can assign a popover or an extension menu to a toolbar item. If you leave the Command field blank, the menu or popover is displayed and no `"command"` event is generated.

You can respond to the `"command"` event by installing a listener function in your global HTML page or an extension bar or popover.

You can’t receive the `"command"` event in an injected script. If you need the command to initiate an action in an injected script, respond to the command in the global HTML page or an extension bar and send a message to the script. For details, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

At various times, such as when a tab is added, Safari will ask you to validate the command. If there is any possibility that the command could be invalid, you should add a listener function for the `"validate"` event.

Your validate function should verify that the command is ready and should be enabled. For example, if your command reloads the active tab, you should verify that the active tab has a URL to reload. If the tab is empty, your validate function should disable the button. You can also modify the item’s image to reflect a modified behavior.

The `"validate"` event is fired when an item is added to the toolbar, so this is also a good moment to update badges.

You can have multiple UI items that issue the same command, such as a toolbar item and a contextual menu item. You can use the same event handlers, regardless of the source.

If your functions are part of the global HTML page, you should register your listener functions with the app:

`safari.application.addEventListener("command", myCommandHandler, false);`

`safari.application.addEventListener("validate", myValidateHandler, false);`

If your functions are part of an extension bar, you should register your listener functions with the extension bar’s parent window:

`safari.self.browserWindow.addEventListener("command", myCommandHandler, false);`

`safari.self.browserWindow.addEventListener("validate", myValidateHandler, false);`

While you can implement the event handlers in either a global HTML page or in an extension bar, it is more efficient to use a global HTML page, because the code is loaded only once, when Safari loads the extension, instead of once per window.

## Deciding Where to Respond

When your button is clicked, a `"command"` event is generated. You can listen for the event in either a global HTML page, a popover, or in an extension bar. If you put the event handler in the global file or in a popover, you should register for the event at the app level. If your event handler is in an extension bar, you should register with the extension bar’s parent window.

The difference is that there is only one instance of the popover or global HTML page’s functions, but there is an instance of an extension bar in every open window.

If every instance of the extension bar registers for events at the app level, every instance responds to the command. If each instance registers with its parent window, only the instance in the window where the button is clicked responds to the command.

Using the global page is more efficient, as it loads only once. Furthermore, you shouldn’t create an empty extension bar just to hold an event handler. If your extension has a bar, however, it might make sense to put the event handler there, particularly if the action it takes is window-specific, like rearranging the tabs.

The only time you might want to put an event handler in the extension bar and register it with the app is if your command acts on all open windows. Then your choice would be to iterate through the windows in a global function or have a function local to each window that acts independently.

### If You Respond from a Global HTML Page

- Register with the app: `safari.application.addEventListener()`.
- The window the event comes from is: `event.target.browserWindow`.

### If You Respond from an Extension Bar

- Register with the parent page: `safari.self.browserWindow.addEventListener()`.
- The window the event comes from is: `self.browserWindow` or `event.target.browserWindow`. The two are equivalent.

## Example: Implementing a Reload Button

[Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmznknlts) responds to the `"reload-page"` command event and the `"reload-page"` validate event. The validate handler disables the control if there’s nothing for it to do, but the command handler checks anyway, in case things have changed since validation.

__Listing 6-1__  Reload command and validate handlers

```
function performCommand(event)
{
    if (event.command === "reload-page") {
        var currentURL = event.target.browserWindow.activeTab.url;
        if (currentURL)
            event.target.browserWindow.activeTab.url = currentURL;
    }
}

function validateCommand(event)
{
    if (event.command === "reload-page") {
        // Disable the button if there is no URL loaded in the tab.
        event.target.disabled = !event.target.browserWindow.activeTab.url;
    }
}

// if event handlers are in the global HTML page,
// register with application:
safari.application.addEventListener("command", performCommand, false);
safari.application.addEventListener("validate", validateCommand, false);
// if event handlers are in an extension bar,
// register with parent window:
// safari.self.browserWindow.addEventListener("command", performCommand, false);
// safari.self.browserWindow.addEventListener("validate", validateCommand, false);
```

[Next](Adding%20Extension%20Menus.md)[Previous](Adding%20a%20Global%20HTML%20Page.md)
