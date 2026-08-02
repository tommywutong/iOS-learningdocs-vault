---
title: Networking Overview
apple_id: TP40010220
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/DisplayingWebContent/DisplayingWebContent.html
archived_at: '2026-07-18T01:33:56.479218Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Overview](About%20Networking.md)


[Next](Making%20HTTP%20and%20HTTPS%20Requests.md)[Previous](Discovering%20and%20Advertising%20Network%20Services.md)

# Displaying Web and Multimedia Content

OS X and iOS provide an assortment of APIs to allow you to display web content and streaming multimedia content. In general, if these higher-level multimedia- and web-specific APIs meet your needs, you should use them rather than using networking APIs directly. The sections below briefly summarize these APIs.

To open a webpage or streaming URL in the user’s default browser or media viewer:

- In iOS, use the [openURL:](https://developer.apple.com/documentation/uikit/uiapplication/1622961-openurl) method of the [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication) class.

  For a real-world example, see QA1629: _[Launching the App Store from an iOS application](https://developer.apple.com/library/archive/qa/qa1629/_index.html#//apple_ref/doc/uid/DTS40008173)_.
- In OS X, use the [LSOpenCFURLRef](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref) or [LSOpenFromURLSpec](https://developer.apple.com/documentation/coreservices/1441986-lsopenfromurlspec) functions in the Launch Services API.

  For details, see [Launch Services Tasks](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/LaunchServicesConcepts/LSCTasks/LSCTasks.html#//apple_ref/doc/uid/TP30000999-CH203) in _[Launch Services Programming Guide](../../Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_.

OS X and iOS provide an easy way to load and display a webpage with the WebKit engine, the same rendering engine used by Safari.

- In OS X, you load web content with the [WebView](https://developer.apple.com/documentation/webkit/webview) class. You can add a web view by including it in your application’s nib file or by programmatically constructing a `WebView` object and calling the [initWithFrame:frameName:groupName:](https://developer.apple.com/documentation/webkit/webview/1408359-initwithframe) method. Load content by calling the [loadRequest:](https://developer.apple.com/documentation/webkit/webframe/1494250-load) method on the web view’s main frame (which you can obtain with the [mainFrame](https://developer.apple.com/documentation/webkit/webview/1408470-mainframe) method).
- In iOS, you load web content with the [loadRequest:](https://developer.apple.com/documentation/uikit/uiwebview/1617957-loadrequest) method of the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class. You can add a web view by including it in your application’s nib file or by programmatically creating a `UIWebView` object and initializing it with the [initWithFrame:](https://developer.apple.com/documentation/uikit/uiview/1622488-init) method.

For more information, see [Simple Browsing](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/SimpleBrowsing.html#//apple_ref/doc/uid/20002025) in _[WebKit Objective-C Programming Guide](../../Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i)_ (OS X) and _[UIWebView Class Reference](https://developer.apple.com/documentation/uikit/uiwebview)_ (iOS).

There are several frameworks available for displaying streaming multimedia content in OS X and iOS:

- In OS X, use the QTKit Framework for basic playback or the AV Foundation framework for more complex functionality.
- In iOS, use the Media Player Framework for basic playback or the AV Foundation framework for more complex functionality.

For more information, read _[Getting Started with Audio & Video](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_MusicAudio/_index.html#//apple_ref/doc/uid/TP30001095)_, _[Multimedia Programming Guide](../../Audio%20Video/Multimedia%20Programming%20Guide/About%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrx)_ (iOS), _[QTKit Application Programming Guide](../../Cocoa/QTKit%20Application%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjw)_ (OS X), and _[AVFoundation Programming Guide](../../Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_.

[Next](Making%20HTTP%20and%20HTTPS%20Requests.md)[Previous](Discovering%20and%20Advertising%20Network%20Services.md)

