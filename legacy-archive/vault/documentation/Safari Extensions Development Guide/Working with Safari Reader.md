---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/WorkingWiththeReader/WorkingWiththeReader.html
archived_at: '2026-07-27T06:57:07.740760Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Messages%20and%20Proxies.md)[Previous](The%20Windows%20and%20Tabs%20API.md)

# Working with Safari Reader

Reader is a Safari feature that allows users to read online articles in a continuous, clutter-free view, with no ads or visual distractions. Reader concatenates multipage articles into a single scrolling pane. There are events that fire when Reader is available, activated, or deactivated. In your extension, you can enter and exit Reader programmatically, inspect properties on the Reader object, and inject scripts and style sheets.

## Reader Events

Safari generates the following Reader events on the relevant tab:

- Available—an `"available"` event on a tab when Reader is available to be invoked.
- Activate—an `"activate"` event on a tab when Reader is invoked.
- Deactivate—a `"deactivate"` event on a tab when Reader is dismissed.

You can listen for these events on the tab itself, or on the window or app. Only the `"available"` event bubbles, however, so either listen on the tab or set the `capture` parameter to `true` when installing your listener functions. For example:

`safari.application.addEventListener("activate", activeHandler, true);`

`tab.addEventListener("available", availHandler, true);`

`tab.addEventListener("deactivate", deactivateHandler, false);`

In your `"available"` event handler, you should test the event target to make sure that it is a Reader instance that has become available, and not something else. See [Listing 14-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrsfvjvomi):

__Listing 14-1__  Reader "available" handler

```
function availHandle(event) {
    if (event.target instanceof SafariReader) {
        myReader = event.target;
        myReader.enter();
    }
}
```

__Note:__ There is no `"unavailable"` event for Reader. Once Reader is available, it remains available until the next `"navigate"` event.

## Reader Methods and Properties

The Reader object is an instance of the [SafariReader](https://developer.apple.com/documentation/safariextensions/safarireader) class. You can invoke the `enter()` and `exit()` methods to create or dismiss a Reader view.

If a `SafariReader` instance is available, you can obtain it by getting the `reader` property of the tab that received the `"available"` event. For example:

`theReader = myTab.reader;`

Because the event target of a Reader `"available"` event is a tab, you can also obtain a Reader instance from the event target, as shown in [Listing 14-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrsfvjvomi).

Once you have an instance of Reader, you can open a Reader view by calling `theReader.enter();`.

To close the Reader view, call `theReader.exit();`.

You can also inspect properties of a Reader instance, specifically `available`, `visible`, and `tab`. The `available` property generates an event when it becomes true, and the `visible` property generates `"activate"` and `"deactivate"` events when it changes, so there is normally no need to poll these properties.

The `tab` property contains the tab the Reader instance is available or active within.

For more information, see _[SafariReader Class Reference](https://developer.apple.com/documentation/safariextensions/safarireader)_.

## Injecting Style Sheets and Scripts into Reader

You can automatically inject style sheets and scripts into Reader by specifying the safari-reader scheme in the whitelist and blacklist in Extension Builder. See [Whitelists and Blacklists](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknlto) for more information.

If you need to dynamically add a new style sheet or script, you can use the `addContentStyleSheet` and `addContentScript` APIs.

### Injecting into Reader Dynamically

To inject into Reader dynamically, you can call `addContentStyleSheetFromURL` and `addContentScriptFromURL` on the `SafariExtension` object using the whitelist and blacklist to limit the scope of the style sheet or script to only Reader pages.

`safari.extension.addContentStyleSheetFromURL("pathToYourStylesheet", ["safari-reader://*/*"]);`

See [Whitelists and Blacklists](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknlto) to see how to work with whitelists and blacklists.

Similarly, to remove a style sheet or script from a Reader page, you can call `removeContentStyleSheet` or `removeContentScript` on the `SafariExtension` object:

`safari.extension.removeContentStyleSheet("pathToYourStylesheet");`

Adding or removing style sheets applies to all pages immediately. Adding or removing a script, however, only applies to pages opened or reloaded after that point.

### Sending Messages to Scripts Injected into Reader

Like your style sheets, your scripts are injected into every webpage to which your extension has access. When dealing with injected scripts in Reader pages, the only difference is that when you want to message an injected script from, for example, the global HTML page, you must use the `dispatchMessage` method on the `Reader` object.

```
// Example of dispatching a message to a Content Script injected into Reader.
    var browserWindows = safari.application.browserWindows;
    for (var i = 0; i < browserWindows.length; ++i) {
        var tabs = browserWindows[i].tabs;
        for (var j = 0; j < tabs.length; ++j) {
            var tab = tabs[j];
            if (!tab.reader.visible)
                continue;
            tab.reader.dispatchMessage("Message to the Content Scripts injected into Reader");
```

[Next](Messages%20and%20Proxies.md)[Previous](The%20Windows%20and%20Tabs%20API.md)
