---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/Spoofing.html
archived_at: '2026-07-15T07:14:55.236213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Accessing%20WebKit%20From%20Carbon%20Applications.md)[Previous](Using%20JavaScript%20From%20Objective-C.md)

# Spoofing

Some websites will deliver different content to different programs that ask for the same page. In extreme cases, a website may deny access completely to some programs. When this happens, you can try to gain access to the site by “spoofing” as another browser.

A client browser sends a special string, called a _user agent_, to websites to identify itself. The web server or JavaScript in the downloaded webpage, detects the client’s identity and modifies its behavior accordingly. In the simplest case, the string includes an application name (for example, “Navigator”) and version information (for example, 4.7 or 6.0). You can use these user-agent methods in WebView to make the identity of your application known and in some cases, to hide the identity of your application, a technique called _spoofing_:

- [setCustomUserAgent:](https://developer.apple.com/documentation/webkit/webview/1408377-customuseragent) —sets the user-agent string.
- [setApplicationNameForUserAgent:](https://developer.apple.com/documentation/webkit/webview/1408381-applicationnameforuseragent) —sets the application name used in the user-agent string.

Note that some websites use the user-agent string to determine whether they support a client browser or not. If they don’t, they may send dumbed-down versions of pages or deny access to the website too. In that case, you can modify the user-agent string to pretend to be a popular browser and then access the website. Although, this may not work if the website expects your application to implement browser-specific extensions. For this reason, you should only consider spoofing as a last resort.

[Next](Accessing%20WebKit%20From%20Carbon%20Applications.md)[Previous](Using%20JavaScript%20From%20Objective-C.md)

