---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Concepts/WhyWebKit.html
archived_at: '2026-07-15T07:14:46.777986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Core%20WebKit%20Classes.md)[Previous](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)

# Why Use WebKit?

Many applications need to display web content in windows, whether it’s live content on the web, or static files on disk. Some applications are full-featured browsers, but more often applications embed web content as a convenience, as in a custom document system. HTML is the de facto standard representation of documents on the internet, so it’s only natural that you will want to display that content without having to launch a web browser for each file or link clicked by the user.

Some applications might want to display web content on demand but don’t necessarily want to parse it or understand its structure to display it. Applications like this may not want to open multiple windows or provide back and forward buttons. WebKit provides a set of classes to support a variety of web content—from the most trivial embedded web content application (with web content displayed in a single window) to a full-featured web browser such as Safari.

WebKit does this by hiding the details of the complex task of loading and displaying web content. The web is based on a client-server architecture, in which clients make asynchronous requests to web servers for page content. During this process any number of problems can occur not only when transmitting these requests and responses over the network but also when displaying the content once it’s received by your application. Content may be complex. It can contain multiple frame elements, multiple MIME types, such as images and movies. Some MIME types require browser plug-ins to display them.

By default, WebKit core classes transparently handle programmatic and client requests. WebKit creates all the necessary model and view classes used to represent and display the incoming content. When a user clicks a link, WebKit automatically relinquishes control of the old objects and creates new ones to handle the new page. WebKit views are designed to handle multiple frames, each with their own scroll bar, and many MIME types. You do not need to implement custom views for your application to display web content in your application.

On the other hand, if you are implementing a custom, full-featured browser or other internet application, you can extend WebKit to handle the details of client requests, frame and resource loading, window operations, and downloading. You do this by implementing delegate objects. WebKit provides a number of “hooks” allowing applications to customize the user interface. For example, you can specify the menu items that are displayed when the user clicks a particular type of resource. You can also implement your own document models and views to handle specific MIME types. Because of this extensibility, WebKit can be used to develop some innovative internet applications.

[Next](Core%20WebKit%20Classes.md)[Previous](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)

