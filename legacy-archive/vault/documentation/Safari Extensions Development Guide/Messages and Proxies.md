---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/MessagesandProxies/MessagesandProxies.html
archived_at: '2026-07-27T06:57:07.753880Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Communicating%20with%20your%20OS%20X%20App.md)[Previous](Working%20with%20Safari%20Reader.md)

# Messages and Proxies

Code in your global HTML page and extension bars interacts with the Safari app; it can’t directly access the contents of a webpage loaded in a browser tab. Similarly, an injected script interacts with web content; it can’t access the same Safari Extensions API as extension bars or a global page.

But it’s sometimes desirable to cross this boundary. You may have controls in an extension bar or the main Safari toolbar that you want to affect web content, for example, or you may have a large block of code or data in an extension bar or your global HTML page that you want to use from an injected script.

The solution is to pass messages between parts of your extension. Because your global HTML page and extension bars can’t address webpages directly, they send messages to the `SafariWebPageProxy`. Similarly, injected scripts can’t address the global HTML page or an extension bar directly, so they send messages to the `SafariContentBrowserTabProxy`.

## Message Structure

A message is an event whose type is `"message"`. You send a message by calling `dispatchMessage(name, data)` and receive messages by registering a listener function for `"message"` events.

A message event has a `name` property and a `message` property, which are the name and data you pass in `dispatchMessage`.

This can be a little confusing, so it bears repeating: `event.name` is the message name, and `event.message` is the message data.

Message data is not limited to a single data type; it can be Boolean, numeric, a string, an array, a RegExp object, or anything that conforms to the W3C standard for safe passing of structured cloned data. It can also be null, undefined, or left blank, in cases where the command needs no data.

For example, the following snippet sends an array in a message:

```
var myArray = ["a", "b", "c"];
safari.self.tab.dispatchMessage("passArray", myArray);
```

## Sending Messages to an Injected Script

To send messages to an injected script, you call the `SafariWebPageProxy` object’s `dispatchMessage()` method. The proxy stands in for the web content, which can be accessed as the `page` property of a `SafariBrowserTab` object, which is in the `tabs` array or `activeTab` property of a `SafariBrowserWindow` object. So, sending a message to a script takes the general form:

`safari.application.activeBrowserWindow.activeTab.page.dispatchMessage("name", "data");`

Another example would be:

`safari.self.tabs[0].page.dispatchMessage(myMessageName,myData);`

__Important:__ When dispatching a message to a page, the message could be sent to pages not currently visible. The Safari application instance could also receive messages from multiple pages that target the same tab. For more information, read [Messages Sent to Tabs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomjs) .

The second example sends a message to the page in the leftmost tab of the window containing the extension bar.

In order to receive the message, your injected script must have a listener function defined and registered for `"message"` events. The listener function is called for all messages, so it needs to check the message name to be sure it’s responding to the desired message. For example, the following function looks for an `activateMyScript` message, then parses the message content:

```
function handleMessage(msgEvent) {
    var messageName = msgEvent.name;
    var messageData = msgEvent.message;
    if (messageName === "activateMyScript") {
        if (messageData === "stop") {
            stopIt();
        }
        if (messageData === "start") {
            startIt();
        }
    }
}
```

The listener function in an injected script is added as a listener for `"message"` events in the `SafariContentWebPage` object (`safari.self`):

`safari.self.addEventListener("message", handleMessage, false);`

__Note:__ The `addEventListener()` method takes three parameters: a string for the event type, the name of the listener function (not in quotes, and without the usual trailing `()`), and a Boolean that tells the system whether the listener function should be given the event in the capture phase or the bubble phase. The Boolean value is usually set to `false`.

### Messages Sent to Tabs

Safari may preload webpages in the background to improve the user experience. Therefore, it is possible for each tab to be associated with more than one webpage, some of which are hidden from the user.

When dispatching messages to the `page` property of `SafariBrowserTab` objects, Safari dispatches your message to all pages associated with that tab, including pages not visible to the user. Updating the UI of a non-visible page impacts battery life and does not benefit the user. If your extension updates the UI of the page, first ensure that the page is visible to avoid executing code on hidden webpages.

You ensure the current page is visible by using the [Page Visibility API](https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/PageVisibility/Overview.html). Query that `document.hidden` is false before running code on the webpage. Also listen for the `visibilitychange` JavaScript event to determine whether the visibility of the page has changed.

## Receiving Messages from an Injected Script

A receiver function in an extension bar or global HTML page behaves identically to a receiver function in a script (it checks the message name before evaluating the message). But instead of registering with the `SafariContentWebPage`, a receiver function in an extension bar or global HTML page can register for the event at the tab, window, or app level:

```
safari.application.activeBrowserWindow.activeTab.addEventListener("message", waitForMessage, false);
safari.application.activeBrowserWindow.addEventListener("message", waitForMessage, false);
safari.application.addEventListener("message", waitForMessage, false);
```

The message is sent first to the app, then filters down to the window and tab. At each level, the event is sent to listener functions registered with Boolean `true`. If no one has claimed it, the message then bubbles up from the tab through the window and back to the app, this time for listeners registered with Boolean `false`. In most cases, it makes no practical difference at which level you intercept the message.

To send a message to an extension bar or global HTML page from an injected script, the script dispatches the message to the tab proxy:

`safari.self.tab.dispatchMessage("heyExtensionBar","Klaatu barada nikto");`

## Example: Calling a Function from an Injected Script

If an injected script makes use of a large block of code or an extensive table of data, it is more efficient to put the bulky code or data in an extension bar or a global HTML page than in the injected script.

The following example is an injected script, [Listing 15-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvony), that makes a function call to a global HTML page, [Listing 15-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvooa), using messages. To see the example in action, follow these steps:

1. Create an extension folder using Extension Builder.
2. Copy the listings into a text editor and save as `Injected.js` and `Global.html`.
3. Drag `Injected.js` and `Global.html` into your extension folder.
4. Click Extension Global Page in Extension Builder and choose `Global.html`.
5. Click New Script in End Scripts and choose `Injected.js`.
6. Set the Extension Website Access level to All.
7. Click Install.

__Listing 15-1__  Injected.js

```
var initialVal=1;
var calculatedVal=0 ;

function doBigCalc(theData) {
    safari.self.tab.dispatchMessage("calcThis",theData);
}

function getAnswer(theMessageEvent) {
    if (theMessageEvent.name === "theAnswer") {
        calculatedVal=theMessageEvent.message;
        console.log(calculatedVal);
    }
}
safari.self.addEventListener("message", getAnswer, false);

doBigCalc(initialVal);
```

__Listing 15-2__  Global.html

```
<!DOCTYPE HTML>
<html>
<head>
<title>global HTML page</title>
<script type="text/javascript">

function bigCalc(startVal, event) {
    // imagine hundreds of lines of code here...
    var endVal = startVal + 2;
    // return to sender
    event.target.page.dispatchMessage("theAnswer", endVal);
}

function respondToMessage(theMessageEvent) {
    if(theMessageEvent.name === "calcThis") {
        var startVal=theMessageEvent.message;
        bigCalc(startVal, theMessageEvent);
    }
}

    safari.application.addEventListener("message",respondToMessage,false);
</script>
</head>
<body>
</body>
</html>
```

In [Listing 15-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvony), the final value of the calculation is logged to the webpage console. To see the log entry, choose Show Web Inspector in the Develop menu.

For an example that shows how to pass messages to a script from an extension bar, see [Message-Passing Example](Adding%20Extension%20Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknlts).

[Next](Communicating%20with%20your%20OS%20X%20App.md)[Previous](Working%20with%20Safari%20Reader.md)
