---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingPopovers/AddingPopovers.html
archived_at: '2026-07-27T06:57:07.661409Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20Contextual%20Menu%20Items.md)[Previous](Adding%20Extension%20Menus.md)

# Adding Popovers

A popover is an HTML window that pops up over the existing windows—no navigation required. The popover window closes automatically when the user changes focus (by clicking in another window, for example). Use popovers to display intermediate amounts of data—more than fits conveniently in an extension bar, but less than you would need a full page to display. The _OS X Human Interface Guidelines_ describes popovers in Content Views.

You can assign a popover to a Safari toolbar item that you have created. If the toolbar item’s `command` property is set to `null`, clicking the toolbar item immediately displays the popover. If the `command` property is _not_ `null`, the user must press and hold in order to see the popover—clicking alone sends the command instead. You can set a toolbar item’s `command` property to `null` either programmatically or simply by leaving the toolbar item’s Command field blank in Extension Builder.

You normally assign a popover to a toolbar item using Extension Builder, but you can also attach a popover to a toolbar item dynamically by setting the toolbar item’s `popover` property.

__Note:__ You can associate a toolbar item with either a menu or a popover, but not both.

Your extension can have multiple popovers. Each popover is an element in the `safari.extension.popovers` array. There is a single instance of each popover, regardless of the number of open windows. Only the active window can display the popover.

## Creating the Popover Content File

A popover displays the contents of an HTML file in your extension folder. You can modify the contents of the DOM created from this file at runtime using JavaScript. If the file is specified in Extension Builder, the file loads once when the app launches. If the popover is created at runtime, the specified content file loads then.

JavaScript in the HTML file containing your popover content can make direct calls to functions in your global HTML page, using the following syntax:

`safari.extension.globalPage.contentWindow.functionName()`

You can also make function calls from a popover into an extension bar, but the situation is slightly more complex. There can be multiple extension bars belonging to an extension, and there is one instance of each extension bar and all its functions per open window. Your popover needs to identify which instance of which bar it wants to access, or iterate through them to access them all.

For example, if an extension has a single bar, the following snippet iterates through the extension bar instances in each open window and calls the `doSomething()` function defined in each one, but also calls the `doSomethingSpecial()` function only in the instance in the active window:

```
const myBars = safari.extension.bars;
function updateAllBars {
    for (var i = 0; i < myBars.length; ++i) {
        var barWindow = myBars[i].contentWindow;
        barWindow.doSomething();
        var myWindow = safari.application.activeBrowserWindow;
        if (myBars[i].browserWindow === myWindow) {
            barWindow.doSomethingSpecial();
        }
    }
}
```

If you need to communicate with injected scripts from your popover, you must send a message to [SafariWebPageProxy](https://developer.apple.com/documentation/safariextensions/safariwebpageproxy). See [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi) for details.

Your popover file can reference media and data from within the extension using relative URLs or from the Internet using absolute URLs.

## Setting Up Popovers in Extension Builder

To add a popover to a toolbar item, start by clicking the New Popover button in Extension Builder. The Popovers pane expands, as shown in Figure 8-1.

__Figure 8-1__  Popovers pane

（原归档配图获取待重试：`popoverPane.png`）

Give the popover a unique identifier and choose the HTML file for your popover content from the pop-up menu. The file must already be in your extension folder to appear in the menu.

If your popover has a fixed height and width, enter them here. If the height or width is unspecified, Safari uses a default width of 400 pixels and a default height of 300 pixels. You can change the `height` and `width` properties of your popover at runtime.

After you have added your popover in Extension Builder, go to the section for the toolbar item you want to associate with this popover and click the Popover button, then choose this popover’s identifier from the pop-up menu, as illustrated in Figure 8-2.

__Figure 8-2__  Associating a popover with a toolbar item

（原归档配图获取待重试：`ToolbarWithPopover.png`）

## Responding to Events

If your popover generates its content dynamically, you should listen for `"popover"` events, and possibly `"validate"` events. In your popover HTML file or your global HTML file, register on the Safari app for the events. For example:

```
safari.application.addEventListener("validate", validateHandler, true);
safari.application.addEventListener("popover", popoverHandler, true);
```

Safari generates `"validate"` events on the toolbar item periodically, including just before your popover is displayed. Use this event if you need to dynamically enable and disable the toolbar item or update a badge on the toolbar item. In some instances, a `"validate"` event is also a good time to update your popover content. If your popover responds to `"validate"` events, check to see whether the `event.target` property for the `"validate"` event is the identifier for your toolbar item. For example:

`if (event.target.identifier !== "myToolbarItemID") return;`

Safari generates a `"popover"` event when your popover is about to be displayed. This is your opportunity to modify the popover content before it is seen. If your popover content does not change dynamically, you don’t need to respond to this event. The `event.target.identifier` property for `"popover"` events that pertain to you is the identifier of your popover.

Handle user interaction with your popover using HTML and JavaScript, as you would in any webpage.

## Creating a Popover at Runtime

Create a popover at runtime by calling `createPopover()` on the `extension` object, passing in an identifier, the URL of the content page, and optionally a width and height. For example:

`myPop = safari.extension.createPopover(`

`"myPopoverID", safari.extension.baseURI + "myFile.html", width, height);`

The `width` and `height` parameters are optional; if omitted, the default values are used.

To assign the popover to a toolbar item, set the toolbar item’s `popover` property. For example:

`myToolbarItem.popover=myPop;`

You can obtain an instance of your toolbar item by iterating through the `extension` object’s `toolbarItems` array and testing the `identifier` property for your toolbar item.

To deallocate a popover, call `safari.extension.removePopover(ID)`. Be sure to set the toolbar item’s `popover` property to `null` before removing its popover.

__Important:__ Do not attempt to deallocate a popover while it is being displayed (check the popover’s [visible](https://developer.apple.com/documentation/safariextensions/safariextensionpopover/1635360-visible) property). Such an attempt fails and an exception is thrown. If necessary, you can hide the popover by calling the [hide](https://developer.apple.com/documentation/safariextensions/safariextensionpopover/1635507-hide) method.

[Next](Adding%20Contextual%20Menu%20Items.md)[Previous](Adding%20Extension%20Menus.md)
