---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/WorkingwithWindowsandTabs/WorkingwithWindowsandTabs.html
archived_at: '2026-07-27T06:57:07.731411Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Working%20with%20Safari%20Reader.md)[Previous](Using%20Your%20Extension%20to%20Block%20Content.md)

# The Windows and Tabs API

The standard `window.open()` JavaScript method cannot be used to open a new tab and window from a global HTML file or an extension bar. Instead, the global file and extension bars have access to the `SafariApplication`, `SafariBrowserWindow`, and `SafariBrowserTab` classes, whose methods and properties allow you to work with windows and tabs.

Safari generates events:

- When a window or tab is opened
- Before a window or tab is closed
- When a window or tab is activated
- Before a window or tab is deactivated
- Before a search is performed from the Smart Search Field
- Before navigating to a new URL
- After navigating to a new URL (when the main frame is loaded)

Navigation occurs whenever the user loads a new page in any manner—clicking a link in a tab or window, opening a bookmark, entering a URL in the address field, or typing a query in the web search field.

## SafariApplication

There is one instance of the `SafariApplication` class: `safari.application`. The `SafariApplication` instance has a method for opening browser windows:

`var myWin = safari.application.openBrowserWindow()`;

All open browser windows can be accessed as properties of the `SafariApplication` instance: `safari.application.browserWindows` is an array of all open windows, and `safari.application.activeBrowserWindow` is the currently active browser window.

## SafariBrowserWindow

Each open browser window is an instance of the `SafariBrowserWindow` class, which has methods to activate windows, close them, and determine if a window is visible onscreen. The `SafariBrowserWindow` class also gives direct access to tabs.

- `browserWindow.tabs`—returns an array of all the tabs in the window, in left-to-right order.
- `browserWindow.openTab()`—creates a new tab at any point in the array. The tab can be hidden.
- `browserWindow.insertTab()`—inserts an existing tab at any point in the array.
- `browserWindow.activeTab`—returns the currently selected tab in the window.

A browser window is commonly accessed as a property of the Safari app instance:

`safari.application.browserWindows[n]`

or:

`safari.application.activeBrowserWindow`

## SafariBrowserTab

The `SafariBrowserTab` class allows you to identify a tab’s parent browser window, get and set the URL associated with a tab, make a tab active, close a tab, and extract a `data://` URL containing a snapshot image of what is rendered in the tab as a base-64 encoded PNG.

For example, this opens a window and returns the active tab:

`var newTab = safari.application.openBrowserWindow().activeTab;`

And this opens a new tab in the window containing the extension bar:

`var newTab = safari.self.browserWindow.openTab();`

## Events

You can listen for and respond to the following window and tab events:

- Open—Safari sends an `"open"` event to a window or tab when it is first opened.
- Close—Safari sends a `"close"` event to a window or tab when it is about to close.
- Activate—Safari sends an `"activate"` event to a window or tab whenever it is activated.
- Deactivate—Safari sends a `"deactivate"` event to a window or tab when it is about to be deactivated.
- Before Navigate—Safari sends a `"beforeNavigate"` event to a tab whenever a new URL is about to load there. You can prevent Safari from loading the URL by calling `preventDefault()` on the event. The event has a `url` property that you can inspect to see where the navigation event leads.
- Navigate—Safari sends a `"navigate"` event to a tab when the main frame of the new URL has loaded.
- Before Search—Safari sends a `"beforeSearch"` event to a tab whenever Safari is about to start a search and show the results in that tab. You can intercept the query and execute an alternate task.

You can listen for these events on the `application` object from an extension bar or your global HTML page. You can also listen on a specific window or tab in the app.

__Important:__ These events do not bubble, so either listen for them on the target tab or window, or else set the capture parameter to `true` when installing your event listener. For example:

`safari.application.addEventListener("open", openHandler, true);`

`myTab.addEventListener("close", closeHandler, false);`

[Next](Working%20with%20Safari%20Reader.md)[Previous](Using%20Your%20Extension%20to%20Block%20Content.md)
