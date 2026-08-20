---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/SimpleBrowsing.html
archived_at: '2026-07-15T07:14:54.722779Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Multiple%20Windows.md)[Previous](Core%20WebKit%20Classes.md)

# Simple Browsing

By writing just a few lines of code using WebKit, you can embed web content in your application and enable your users to navigate the web.

The code example below assumes you already have a WebView object inside a window that represents the webpage. You can create a WebView object and attach it to a window either programmatically or by using Interface Builder. Using Interface Builder, drag a WebView from the Library into a window. You should also connect the WebView object to an outlet so that you can send messages to it programmatically.

Next, you load a webpage by sending a [loadRequest:](https://developer.apple.com/documentation/webkit/webframe/1494250-load) message to the main frame of your WebView object, as in this example:

```
[[webView mainFrame] loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:urlText]]];
```

Here, `webView` is an instance of WebView and `urlText` is a valid URL address such as `http://www.apple.com`. You can do this after the nib file is loaded, so that your WebView object displays a default page.

When you run your application you’ll notice that the URL (if it is valid) is successfully displayed in the window and most links are followed automatically when clicked. Content that contains multiple frames is automatically handled. WebKit does this by creating a hierarchy of WebFrameView and WebFrame objects to handle frame content—even content that contains QuickTime movies, JavaScript, or Flash movies works.

Even though navigating works, this simple example doesn’t contain many of the features you would expect in a web browser—namely, a text field for typing in URLs, back and forward buttons, a history menu, multiple windows, and status or error messages. You can add some of these features by assigning delegates to your WebView object and implementing delegate methods. Because the delegate methods are informal protocols, you can choose which methods you want to implement.

[Next](Multiple%20Windows.md)[Previous](Core%20WebKit%20Classes.md)

