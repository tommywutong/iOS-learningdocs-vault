---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingExtensionToolbars/AddingExtensionToolbars.html
archived_at: '2026-07-27T06:57:07.612014Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20a%20Global%20HTML%20Page.md)[Previous](Accessing%20Resources%20Within%20Your%20Extension%20Folder.md)

# Adding Extension Bars

Extension bars are toolbar-sized areas that serve as dedicated display space for extensions. Each extension bar is 30 pixels tall, so it’s an appropriate place to put controls, a set of links, or a single line of information such as a scrolling headline or a stock ticker.

## About Extension Bars

Extension bars are stacked between the bookmarks bar and the tab bar. Each extension bar’s visibility can be toggled on and off using the View menu (OS X) or Action button (Windows). An extension can have multiple extension bars.

You designate an HTML file as the source of an extension bar using Extension Builder. For an example, see [Building a Simple Extension](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknlto).

Your extension bar can contain JavaScript functions defined in any of the usual ways, such as within the `head` element or in an included `.js` file.

Extension bar source files are loaded and interpreted each time a new browser window is opened. When the user opens a new window, Safari creates an instance of the `SafariExtensionBar` object for each bar. If no windows are open, there are zero extension bar instances. Hiding a bar using the View menu does not remove the instance. The extension’s global HTML page and other extension bar files can access the extension bar and its properties using the `safari.extension.bars` array.

Multiple instances of an extension bar are independent, like the same webpage loaded in multiple windows. If an extension bar contains an audio player, for example, the play and pause button in a given extension bar act on the `audio` element in that bar, so if you start playing music, open a new window, and want to stop the music, you need to go back to the original window. To have the play and pause buttons in any copy of an extension bar act on the same `audio` element, put the `audio` element in a global HTML page.

## The extension.bars Array

To address a particular instance of an extension bar, iterate through the `safari.extension.bars` array, using the `identifier` property of the extension bar to identify the particular bar, and the `browserWindow` property to identify the window instance. For example, to address the bar named Audio Controls in the active window, you might do this:

```
const bars = safari.extension.bars;
const activeBrowserWindow = safari.application.activeBrowserWindow;
for (var i = 0; i < bars.length; ++i) {
    var bar = bars[i];
    if (bar.browserWindow === activeBrowserWindow && bar.identifier === "Audio Controls")
       {
       /* Do something. */
       }
}
```

## Domain, URLs, and Access

An HTML file that acts as the source for an extension bar behaves pretty much the way any webpage would in a 30-pixel tall window, with the following exceptions:

- The domain of an extension bar is unique to the extension.
- Relative URLs are relative to the copy of the extension bar source file in the extension package. URLs outside of the extension package on the user’s drive cannot be accessed.
- If you need to refer to a file in the package using an absolute URL, the URL is `safari.extension.baseURI + "relative-path/filename"`.
- An extension bar file has access to the Safari app’s windows, tabs, contextual menu items, and toolbar items.
- An extension bar file can receive command events from contextual menu items or Safari toolbar items, as well as message events sent from injected scripts; this requires installing a listener function for the `command` event or `message` event.
- An extension bar file can send messages to the webpage proxy. These messages can be received by listener functions in injected scripts.
- An extension bar file has access to the global HTML page, if your extension has one.
- Extension bars can issue `XMLHttpRequest` to other domains. This allows your extension bar to read an RSS feed or a news site, for example, into a string that can be parsed for information to display in the bar. You set the domains your extension has permission to access using Extension Builder. For details, see [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).

## Displaying Content in an Extension Bar

The HTML in an extension bar file is automatically rendered in the extension bar. The shape of the extension bar, particularly its height, makes it suitable for particular tasks, such as the following:

- A toolbar for your extension.
- A specialized bookmarks bar.
- A ticker or news-crawl with headlines, stock price, weather, flight status, or other information suitable for single-line presentation that can be obtained using `XMLHttpRequest`.

The user can hide the extension bar using the View menu, but the extension bar page still loads every time a window is opened and any JavaScript still executes—only the display is suppressed by the View menu.

### Creating an Extension Control Bar

To create an extension control bar, design a page that presents as a series of buttons, links, or controls, using the `title` attribute of your control elements to show tooltips. The shape, placement, and function of the controls are up to you, as long as they fit in the allotted space.

If the controls operate solely on the Safari app (manipulating windows and tabs, for example), or on elements declared in the extension bar, the code can be entirely within the extension bar file or the global HTML page.

If the extension bar triggers actions that need access to content loaded in a browser tab, however, the code that acts on the content must be injected into the webpage. The extension bar cannot call functions in injected scripts directly. The extension must send a message to the webpage proxy, and the injected script must have a listener function registered for the `"message"` event. See [Interacting with Injected Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknlto).

The following example, Listing 4-1, is HTML that displays two buttons. Setting the `title` attribute on the buttons creates tooltips. The `<audio>` element loads an audio file from a remote server. The buttons play and pause the music.

__Listing 4-1__  Music player bar

```
<!DOCTYPE html>
<html>
<head>
    <title>Music Player Extension Bar</title>
    <script type="text/javascript">
    function playIt() {
       document.getElementById("music").play();
        }
    function pauseIt() {
       document.getElementById("music").pause();
        }
    </script>
</head>
<body>
My Music:
&nbsp;&nbsp;
<input type=button value=">" onclick="playIt()"  title="Play">
&nbsp;&nbsp;
<input type=button value="||" onclick="pauseIt()" title="Pause">
<audio id="music" src="http://homepage.mac.com/qt4web/testmusic.m4a">
</audio>
</body>
</html>
```

To make this example into an extension bar, follow these steps:

1. Save the example as an HTML file.
2. Open Extension Builder, click +, choose New Extension, and give the extension a name (see [Using Extension Builder](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltc)).
3. Drag the HTML file into the extension folder you just created.
4. Click New Bar in Extension Builder and choose the HTML file from the pop-up menu.

Click Install. You should see the music player toolbar in Safari, as shown in Figure 4-1.

__Figure 4-1__  Music player toolbar

（原归档配图获取待重试：`musicPlayerToolbar.jpg`）

Note that you can create several instances of the music bar by opening new windows, and that each bar plays and pauses independently.

## Working with Windows and Tabs

An extension bar can use either HTML or JavaScript to display content in a tab.

__Note:__ Be sure to set your extension’s website access to Some or All in Extension Builder before working with tabs—most tab properties return `undefined` unless your extension has access to the domain of the URL loaded in the tab.

A link in an extension bar, such as `<a src=URL> link text </a>`, opens the linked URL in the active browser tab, just as it would from a webpage. Unlike a normal webpage, the extension bar is not replaced with the linked file, however. Consequently, an extension bar can contain a set of persistent links, similar to the bookmarks bar.

The standard `window.open()` method cannot be used to open a new tab and window from an extension bar. Instead, extension bars have access to the `SafariApplication`, `SafariBrowserWindow`, and `SafariBrowserTab` classes, which allow you to open, close, activate, and manipulate windows and tabs.

For example, this opens a window and returns the active tab:

`var newTab = safari.application.openBrowserWindow().activeTab;`

And this opens a new tab in the window containing the extension bar:

`var newTab = safari.self.browserWindow.openTab();`

For more details, see [The Windows and Tabs API](The%20Windows%20and%20Tabs%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjxfvjvomi).

[Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknltm) shows how to implement an extension bar that opens content in a new tab of the extension bar’s window.

__Listing 4-2__  Safari developer reference bar

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Safari Developer Reference</title>

    <script type="text/javascript">
    var server="http://developer.apple.com/";
    var reflib="safari/library/documentation/AppleApplications/Reference/"
    function openInTab(source){
        var newTab=safari.self.browserWindow.openTab();
        newTab.url=source;
        }
    </script>

</head>
<body style="color:#C02020;background:#C0C0C0;">
Safari Developer Reference Bar
&nbsp;&nbsp;
<a href="javascript:openInTab(server+'safari/');"> Dev Center </a>
&nbsp;&nbsp;
<a href="javascript:openInTab(server+reflib+'SafariHTMLRef/');"> HTML Ref </a>
&nbsp;&nbsp;
<a href="javascript:openInTab(server+reflib+'SafariCSSRef/');"> CSS Ref </a>
</body>
</html>
```

Figure 4-2 shows what the example looks like when all three tabs have been opened.

__Figure 4-2__  Reference extension bar

（原归档配图获取待重试：`DevRefBar.jpg`）

## Interacting with Injected Scripts

Extension bars cannot address the content of webpages, but they can interact with injected scripts indirectly, by sending and receiving messages. There are two primary reasons to do this:

1. You might activate or control an injected script using controls in an extension bar.
2. Your extension bar might contain code that your injected script needs to call.

Injected scripts are interpreted each time the user loads a URL the script applies to, including subframes, so it’s important to keep your injected scripts lightweight. Otherwise, the load time for every page is slowed. An extension bar is loaded only once per window, regardless of how many tabs are opened and URLs are loaded. Consequently, if a script needs user controls, it’s better to put them in an extension bar than to inject them into each page.

Similarly, if your script needs to perform significant calculations, or refer to a large table of data, it’s better to load the data or large block of code once per window than once per page. In general, it’s better still to load the code or data in your global HTML page and do it only once per session, but in cases where you need one copy per window, the extension bar can be used.

In order to control an injected script, your extension bar needs to send a message by calling the `SafariWebPageProxy` object’s `dispatchMessage()` method. The proxy stands in for the web content, which can be accessed as the `page` property of a `SafariBrowserTab` object, which is in the `tabs` array or `activeTab` property of a `SafariBrowserWindow` object, so sending a message to a script takes the general form:

`safari.application.activeBrowserWindow.activeTab.page.dispatchMessage(msgName, data)`

or:

`safari.application.browserWindows[n].tabs[n].page.dispatchMessage(name, data)`

The injected script in the specified page must have a listener function registered for `message` events in the `SafariContentWebPage` object (`safari.self`):

`safari.self.addEventListener("message", respondToMessage, false);`

In order to execute functions in your extension bar in response to a request from an injected script, you must define and register a listener function for `message` events in your extension bar. You should generally register your listener function at the window level. For example:

`safari.self.browserWindow.addEventListener("message", respondToMessage, false);`

For more details and examples, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

### Message-Passing Example

The following example shows an extension bar file, [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknltema), and an injected End Script, [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknltemi). The extension bar has a button to send a message and a text field that changes when it receives a message. The script adds a text field to webpages that changes when it receives a message.

To see the example in action, follow these steps:

1. Copy the text in the following listings into a text editor and save as `extensionbar.html` and `injected.js`.
2. Create an extension folder using Extension Builder and drag `injected.js` and `extensionbar.html` into the folder.
3. In Extension Builder, set Extension Website Access to All.
4. Click New Bar in Extension Builder and choose `extensionbar.html`.
5. Click New Script under Injected Extension Content—End Scripts: and choose `injected.js`.
6. Click Install, then load a webpage in Safari to load the script.

__Note:__ You must designate `injected.js` as an End Script. If you attempt to run it as a Start Script, `document.body` is undefined, as the webpage that the script is being injected into is not yet parsed.

__Listing 4-3__  Extensionbar.html

```
<!DOCTYPE HTML>
<html>
<head>
<script type="text/javascript">

    function sendMessage() {
        document.getElementById("textField").innerHTML="Sending message...";
        safari.application.activeBrowserWindow.activeTab.page.dispatchMessage("hey", "there");
    }

    function respondToMessage(messageEvent) {
        if(messageEvent.name === "gotIt")
        document.getElementById("textField").innerHTML=messageEvent.message;
    }

    safari.self.browserWindow.addEventListener("message",respondToMessage,false);

</script>
</head>
<body> Message Sender Bar &nbsp;&nbsp;
    <input type="button" value="Send" onclick="sendMessage()" >
    <span id="textField">...waiting... </span>
</body>
</html>
```

__Listing 4-4__  Injected.js

```
var theBody = document.body;
// create a para and insert it at the top of the body
var element = document.createElement("p");
element.id = "status";
element.style.cssText = "float:right; color:red";
element.textContent = "Waiting...";
theBody.insertBefore(element, theBody.firstChild);

function replyToMessage(aMessageEvent) {
   if (aMessageEvent.name === "hey") {
    document.getElementById("status").textContent="Message received.";
    safari.self.tab.dispatchMessage("gotIt","Message acknowledged.");
    }
}
// register for message events
safari.self.addEventListener("message", replyToMessage, false);
```

Figure 4-3 shows the extension bar and the webpage modified by the injected script, before and after sending messages.

__Figure 4-3__  Before and after

（原归档配图获取待重试：`BeforeAndAfter.jpg`）

[Next](Adding%20a%20Global%20HTML%20Page.md)[Previous](Accessing%20Resources%20Within%20Your%20Extension%20Folder.md)
