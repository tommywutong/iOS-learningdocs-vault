---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingaGlobalHTMLPage/AddingaGlobalHTMLPage.html
archived_at: '2026-07-27T06:57:07.625689Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md)[Previous](Adding%20Extension%20Bars.md)

# Adding a Global HTML Page

A global HTML page is a place for you to put JavaScript code, data tables, and other resources requiring no user interface that your extension needs to load only once per Safari session. The global page is not mandatory. You can have at most one global page per extension.

The main uses for a global page are:

- To hold the logic for handling Safari toolbar items.
- To hold the logic for handling extension menus and contextual menu items.
- To hold the logic for handling settings changes.
- To hold large blocks of logic or data used by extension bars.
- To hold large blocks of logic or data used by injected scripts.

You can also use the global page to hold logic or data used by a popover, but if the popover is specified in Extension Builder, the popover file loads only once, just like the global page file, so there is no gain in efficiency. If you have multiple popovers that use the same data or logic, however, it makes sense to have one copy in the global page, instead of a copy in each popover.

## Adding a Global Page in Extension Builder

First create the global HTML page. The global HTML page is an HTML file that is loaded but never displayed. It can contain JavaScript functions declared in `script` elements or in external `.js` files included using the `script` element’s `src` attribute. The `.js` files can be located inside the extension folder and referenced by relative URL.

If you have not already done so, click + in Extension Builder and choose New Extension. You are prompted to give the extension a name and choose a location for it. Extension Builder creates a folder with the name you choose and the file extension `.safariextension`.

Drag the HTML file that you want to use as your global page into the extension folder using the Finder or Windows file system. Drag in any external `.js` files or other resources the global page needs as well.

Click Global Page File in Extension Builder and choose the file from the pop-up menu.

__Note:__ When you add a global page, an Inspect Global Page button is added to Extension Builder. Click this button to invoke Web Inspector to help debug your global page. For details, see [Debugging Extensions](Debugging%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqojnknltc).

## Handling Toolbar Items

The global page is the ideal place for the logic that handles toolbar items. You can also put the logic in an extension bar, but since the logic doesn’t need to be loaded on a per-window basis and doesn’t need any display space, it usually belongs in a global page.

To handle toolbar items, add a listener function for `"command"` events in your global page. Have the listener function test the event name to see if it is the name of the command you specified for the toolbar item in Extension Builder. If the event name is your command name, the user has clicked your toolbar item and you should execute the command.

If there is any possibility that the toolbar item should be disabled, add a listener function for the `"validate"` event as well. If the event name is the same as your command name, determine whether the toolbar item should be disabled. If so, set `event.target.disabled = true`.

For details and examples, see [Adding Buttons to the Main Safari Toolbar](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmznknltc).

A toolbar item can also generate `"menu"` or `"popover"` events. See [Adding Extension Menus](Adding%20Extension%20Menus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrqfvjvomi) and [Adding Popovers](Adding%20Popovers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrrfvjvomi) for details.

## Handling Contextual Menu Items

The global page is also the ideal place for the logic that handles contextual menu items. Again, you can put the logic in an extension bar, but since the logic doesn’t need to be loaded on a per-window basis and it doesn’t need any display space, it usually belongs in a global page.

To handle contextual menu items, add a listener function for `"command"` events in your global page. Have the listener function test the event name to see if it is the name of the command you specified for the contextual menu item in Extension Builder. If the event name is your command name, the user has chosen your contextual menu item and you should execute the command.

If there is any possibility that the contextual menu item should not be displayed, add a listener function for the `"validate"` event as well. If the event name is the same as your command name, determine whether the contextual menu item should be displayed. If not, set `event.target.disabled = true`.

If you need to obtain information from the webpage, such as the element that was clicked to initiate the contextual menu, you can add event listeners for the `"contextmenu"` event in the global page and an injected script. The script’s listener is called first, and can set pass information to the global page.

For details and examples, see [Adding Contextual Menu Items](Adding%20Contextual%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnbnknltc).

## Support Logic for Extension Bars and Popovers

Functions and global variables declared in the global page can be accessed directly from extension bars or popovers, as properties of `safari.extension.globalPage.contentWindow`. So, for example, if you define a `myCalc()` function in your global page, you can call it from an extension bar or popover using `safari.extension.globalPage.contentWindow.myCalc()`.

To simplify things, declare a constant in your extension bar or popover, such as:

`const myGlobal = safari.extension.globalPage.contentWindow;`

You can then access the `myCalc()` function from your extension bar or popover using `myGlobal.myCalc()`.

The global page has access to the same API as an extension bar or popover, so it can do all the same things, except that it has no visible display area of its own. Consequently, it’s easy to move large chunks of code from an extension bar or popover to your global page. Listing 5-1 shows how to move logic from an extension bar, but it would work the same way from a popover.

This is an example of an extension bar that has a button. Clicking the button performs a simple calculation.

__Listing 5-1__  Moving logic to your global page

```
<!DOCTYPE HTML>
<html>
<head>
   <title>old extension bar page</title>
   <script type="text/javascript">

   var theAnswer = 0;
    function calcThis(x) {
       x++;
       theAnswer = x;
    }

    function doButton() {
       calcThis(theAnswer);
       var mButton = document.getElementById("myButton");
       mButton.value = ("Increment " + theAnswer);
    }
   </script>
</head>
<body>
   <input type="button" value="Increment 0"
    onclick="doButton();" id="myButton" >
</body>
</html>
```

Here’s a version of the same extension bar, with the calculation moved to the global page. The code exported to the global file is unchanged. A constant is defined in the extension bar and prepended to anything called in the global file.

```
<!DOCTYPE HTML>
<html>
<head>
   <title>global page</title>
   <script type="text/javascript">

    var theAnswer = 0;
    function calcThis(x) {
      x++;
      theAnswer = x;
    }

   </script>
</head>
<body> </body>
</html>

<!DOCTYPE HTML>
<html>
<head>
   <title>extension bar page</title>
   <script type="text/javascript">

   const myGlobal = safari.extension.globalPage.contentWindow;

   function doButton() {
      myGlobal.calcThis(myGlobal.theAnswer);
      var mButton = document.getElementById("myButton");
      mButton.value = ("Increment " + myGlobal.theAnswer);
   }

   </script>
</head>
<body>
   <input type="button" value="Increment 0"
    onclick="doButton();" id="myButton" >
</body>
</html>
```

You can also make function calls from the global page into an extension bar or popover. Calling functions in this direction is slightly more complex. You still call into the content window, but there is an array of extension bars and an array of popovers, so you need to specify which element of the array you are addressing, even if your extension has only one bar or popover. There is also an instance of each extension bar and all its functions per open window. Your global page needs to identify which instance it wants to access, or iterate through them to access them all.

For example, suppose your extension has a single extension bar; the following snippet iterates through the extension bar instances and calls the `doSomething()` function defined in each one, but calls the `doSomethingSpecial()` function only on the extension bar in the active window:

```
const myBars = safari.extension.bars;
function updateAllBars {
    for (var i = 0; i < myBars.length; ++i) {
        var barWindow = myBars[i].contentWindow;
        barWindow.doSomething();
        var myWindow = safari.application.activeBrowserWindow;
        if (myBars[i].browserWindow == myWindow) {
            barWindow.doSomethingSpecial();
        }
    }
}
```

To call a function in a popover, you need to identify the particular element in the `popovers` array that you want to call into, but there is a single popover instance shared by all windows. If your extension has a single popover, you can call a function in the popover by calling `safari.extension.popovers[0].contentWindow.functionName()`.

## Support Logic for Injected Scripts

JavaScript functions and variables in your global page cannot be called directly from injected scripts, but injected scripts can send messages that trigger functions in the global page, and the global page can send messages to injected scripts that trigger functions or contain the result of calculations.

For details and examples, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

## Working with Windows and Tabs

__Note:__ Be sure to set your extension’s website access to Some or All in Extension Builder before working with tabs—most tab properties return `undefined` unless your extension has access to the domain of the URL loaded in the tab.

The global HTML page itself is not displayed, but it can open windows and tabs and use them to display content. The standard `window.open()` method cannot be used to open a new tab and window from the global HTML page, however. Instead, the global page has access to the `SafariApplication`, `SafariBrowserWindow`, and `SafariBrowserTab` classes, which allow you to open, close, activate, and manipulate windows and tabs.

For example, this opens a window and returns the active tab:

`var newTab = safari.application.openBrowserWindow().activeTab;`

Safari generates events when a window or tab opens, closes, gains or loses focus, or when the user navigates to another page.

For details, see [The Windows and Tabs API](The%20Windows%20and%20Tabs%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjxfvjvomi).

[Next](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md)[Previous](Adding%20Extension%20Bars.md)
