---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/DebuggingExtensions/DebuggingExtensions.html
archived_at: '2026-07-27T06:57:07.784148Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Converting%20Other%20Extensions%20and%20Greasemonkey%20Scripts.md)[Previous](Settings%20and%20Local%20Storage.md)

# Debugging Extensions

To test and debug extensions, use Safari’s built-in Web Inspector. Learn how to use these tools by reading _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

This chapter shows you how to apply the developer tools specifically to Safari extensions, but does not go into detail about using the tools.

## Debugging Extension Bars

To debug an extension bar, Control-click or right-click on the extension bar. From the context menu presented, select Inspect Element.

This opens Web Inspector with the element in the extension bar selected, as illustrated in Figure 19-1.

__Figure 19-1__  Inspecting extension bars

（原归档配图获取待重试：`inspectingbars.png`）

The Resource navigator shows the DOM tree for the extension bar, including any inline JavaScript. If your extension bar includes any `.js` files or other resources, they will appear under the Resource navigator. JavaScript errors are listed under the Issue navigator.

Clicking an element highlights it in the extension bar of the browser window, displays its attributes and styles, and allows you to edit them interactively (double-click an attribute or style value to edit it). If you use the Node navigator, you can display event listeners for all nodes, or any given node.

In addition, the `console` API is supported for extension bars and is compatible with Firebug. You can log data to the console and see it using the Log navigator in Web Inspector. For example, you can call the following line of JavaScript in your extension to log the URL of the current tab:

`console.log(safari.application.activeBrowserWindow.tabs[0].url);`

You can enable JavaScript debugging, set breakpoints, profile your JavaScript, look at how resources load, or examine HTML5 local storage databases, just as you would on a website you were developing. For details, see _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

## Debugging Injected Scripts

Debugging an injected script or style sheet with the Safari developer tools is very much like debugging a script or style sheet for your own website. The main difference is that you must load a webpage to which your extension has access in order to inject the script for debugging.

Choose Show Web Inspector from the Develop menu, or right-click on the webpage and choose Inspect Element. Then under the Resource navigator, choose your script from the folder labeled Extension Scripts.

__Figure 19-2__  Inspecting injected scripts

（原归档配图获取待重试：`debuggingscripts.png`）

Any detected errors in the script are shown in the Issue navigator. Click in the gutter between the line number and script to set a breakpoint. The Firebug-compatible console API is available for logging data.

__Note:__ Currently, you cannot use the console to interactively enter the names of injected script objects, such as variables or functions defined in the script. You can log data to the console using the console API, set breakpoints, profile scripts, and so on, but the private namespace of your injected script keeps the console from recognizing object names defined in the script.

For more information on debugging scripts, see _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

## Debugging a Global HTML Page

To bring up Web Inspector for the global page, choose Show Extension Builder from the Develop menu. When your extension has a global HTML page, a button is added to the Extension Builder interface, in the Global Page section, as illustrated in Figure 19-3.

__Figure 19-3__  Inspect Global Page button

（原归档配图获取待重试：`inspectglobalpage.png`）

Click Inspect Global Page to open Web Inspector with your global page selected for debugging.

For details on debugging HTML and JavaScript using Safari’s integrated tools, see _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

[Next](Converting%20Other%20Extensions%20and%20Greasemonkey%20Scripts.md)[Previous](Settings%20and%20Local%20Storage.md)
