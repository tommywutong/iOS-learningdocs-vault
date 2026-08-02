---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html
archived_at: '2026-07-15T07:14:46.783868Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Why%20Use%20WebKit.md)

# Introduction to WebKit Objective-C Programming Guide

The WebKit framework provides a set of core classes to display web content in windows, and by default, implements features such as following links clicked by the user. WebKit greatly simplifies the complicated process of loading webpages—that is, asynchronously requesting web content from an HTTP server over the network where the response may arrive incrementally, in random order, or partially due to network errors. WebKit also simplifies the process of displaying content that can contain various MIME types, and multiple frames each with their own set of scrollbars.

You use WebKit to display web content in a window of your application. It’s as simple as creating a view, placing it in a window, and sending a URL load request message. By default, your WebKit application behaves as you would expect without error. WebKit conveniently creates and manages all the views needed to handle different MIME types. When the user clicks on a link in a page, WebKit automatically creates the views needed to display the next page.

However, WebKit doesn’t implement a complete set of web browser features. You can, however, extend WebKit by implementing custom delegate, view, and model objects. For example, you can implement a delegate to display load status, and the current URL.

WebKit also offers web content editing. If you enable editing in your WebView, users can edit the web content it displays. You can programmatically control the current selection and control editing behavior using a WebView delegate. You can also modify the Document Object Model directly using an Objective-C API.

You can also access JavaScript from Objective-C and vice versa.

The WebKit Objective-C API is specifically designed for embedding web content in your Cocoa or Carbon applications—developing web client applications _not_ web server applications or web content. It is also not suitable for implementing non-GUI applications such as web crawlers. If you are a web content creator or JavaScript programmer, refer to _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_.

The following articles cover key concepts in understanding how WebKit works:

- [Why Use WebKit?](Why%20Use%20WebKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdglkdjjbeksscjbea) describes the purpose of WebKit and why you might want to use it in your applications.
- [Core WebKit Classes](Core%20WebKit%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdilkdjjbeksscjbea) describes the core WebKit classes and the object-oriented design that is fundamental to understanding how WebKit works.

The following articles explain how to display web content in views:

- [Simple Browsing](Simple%20Browsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdklkdjjbekscbifdq) shows how to embed web content in your application by following a few simple steps.
- [Multiple Windows](Multiple%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdmlkdjjbekscbifdq) shows how to add support for multiple windows, and open windows automatically.
- [Loading Pages](Loading%20Pages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdolkdjjbekscbifdq) shows how to track the progress of loading frame content.
- [Loading Resources](Loading%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdqlkdjjbekscbifdq) shows how to track the progress of loading individual resources on a page.
- [Paging Back and Forward](Paging%20Back%20and%20Forward.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaztalkdjjbekscbifdq) shows how to implement a back-forward list and add Back and Forward buttons to your application.
- [Managing History](Managing%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaztclkdjjbekscbifdq) shows how to maintain a history of all the visited pages, and allow the user to go to a previously visited page.
- [Spoofing](Spoofing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdslkdjjbekscbifdq) shows how to use user-agent strings.
- [Accessing WebKit From Carbon Applications](Accessing%20WebKit%20From%20Carbon%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaztklkdjjbekscbifdq) explains how to embed web content in Carbon applications.
- [Determining WebKit Availability](Determining%20WebKit%20Availability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha2dmlkciffekqkjivcq) explains how to determine if WebKit is available on your system.

The following articles explain how to implement web content editing:

- [Enabling Editing](Enabling%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimrtfvbuuqsfjbaucry) shows how to enable user editing in a WebView.
- [Saving and Loading Web Content](Saving%20and%20Loading%20Web%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinzsfvbuuqsfjbaucry) shows how to save and load web content edited by the user.
- [Modifying the Current Selection](Modifying%20the%20Current%20Selection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimrufvbuuqsfjbaucry) shows how to programmatically modify the current selection.
- [Changing Editing Behavior](Changing%20Editing%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimrvfvbecssfifeukri) explains how to use the WebView editing delegate to customize editing behavior.
- [Using Undo When Editing](Using%20Undo%20When%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinztfvbuuqsfjbaucry) shows how to implement undo when editing web content.

The following articles explain how to use the Document Object Model Objective-C API:

- [Using the Document Object Model from Objective-C](Using%20the%20Document%20Object%20Model%20from%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembwfvbegskhinausri) describes the DOM Objective-C API in terms of the specification.
- [Using the Document Object Model Extensions](Using%20the%20Document%20Object%20Model%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembxfvbeeq2kjjeegsa) describes WebKit extensions to the DOM API.

Read this article if you want to access JavaScript from your application:

- [Using JavaScript From Objective-C](Using%20JavaScript%20From%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiytilkcineusrkbizea) shows how to access the scripting environment from an Objective-C application.

You begin using WebKit by first embedding web content in your application. Read [Simple Browsing](Simple%20Browsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdklkdjjbekscbifdq), and, optionally, [Loading Pages](Loading%20Pages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdolkdjjbekscbifdq) and [Loading Resources](Loading%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdqlkdjjbekscbifdq) to embed web content. If you want to add more browser-like features or implement a custom user interface, read [Core WebKit Classes](Core%20WebKit%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgazdilkdjjbeksscjbea) first and any other articles based on your application needs. If you want to edit web content, read [Enabling Editing](Enabling%20Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimrtfvbuuqsfjbaucry).

For more details on the Objective-C WebKit API, read:

- _[WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit)_
- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_

There are other technologies, not covered in this topic, that can be used in conjunction with WebKit or separately to solve related problems.

Refer to this document for more details on the URL loading system:

- _URL Loading System Programming Guide_

If you are accessing WebKit from a Carbon application, refer to these documents:

- _WebKit C Reference_

If you are creating web content for Safari or Dashboard, refer to these documents:

- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_
- _[Dashboard Reference](../../Apple%20Applications/Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_

The `/Developer/Examples/WebKit` folder also contains more in-depth code examples.

Other related text book resources are:

- _HTML and XHTML: The Definitive Guide_ (O’Reilly)
- _Cascading Style Sheets: The Definitive Guide_ (O’Reilly)
- _JavaScript: The Definitive Guide_ (O’Reilly)

Also refer to the World Wide Web Consortium at [www.w3.org](http://www.w3.org/) for the latest information on web standards.

[Next](Why%20Use%20WebKit.md)

