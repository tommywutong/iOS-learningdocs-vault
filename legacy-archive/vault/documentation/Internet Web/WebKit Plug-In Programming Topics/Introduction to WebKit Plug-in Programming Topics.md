---
title: WebKit Plug-In Programming Topics
apple_id: TP40001521
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2011-05-17'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/WebKit_PluginProgTopic/WebKitPluginTopics.html
archived_at: '2026-07-15T07:44:15.790907Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Web%20Browser%20Plug-ins.md)

# Introduction to WebKit Plug-in Programming Topics

Web browser plug-ins are compiled bundles that help extend the content types supported by common web browsers. Installed locally on a computer, they can run code native to the user’s operating system and provide a powerful way to expand on standard web content.

This document is designed for a number of different audiences:

- If you are a Cocoa and WebKit developer, you should read about the plug-in architecture used by WebKit and learn how compiled plug-ins operate within WebKit-based applications, including Safari.
- If you are a developer who is concerned with cross-platform compatibility for your software, but who also wants to deploy special content via a web browser, you should read about the Netscape-based plug-in architecture and learn how it is supported in a variety of browsers.
- If you are a web content developer, you should read about both plug-in architectures and learn how to integrate their features into custom plug-ins to support your content.

The topic contains the following articles:

- [About Web Browser Plug-ins](About%20Web%20Browser%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2dqlkciffeosskifea) describes the benefits of web browser plug-ins and how they are integrated into common browsers. It also discusses the advantages and disadvantages of both plug-in models, and how to deploy plug-ins on computers and web sites.
- [Creating Plug-ins with the Netscape API](Creating%20Plug-ins%20with%20the%20Netscape%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talkciffeosskifea) describes how to use the Netscape plug-in architecture to develop and deploy web browser plug-ins across multiple browsers and platforms.
- [Creating Legacy Plug-ins with Cocoa and WebKit](Creating%20Legacy%20Plug-ins%20with%20Cocoa%20and%20WebKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2dslkciffeosskifea) describes the legacy WebKit-based plug-in architecture.

There are lots of helpful resources available to guide you through plug-in development.

- Mozilla’s [Plug-ins Project](http://www.mozilla.org/projects/plugins/) discusses the cross-browser Netscape API and also includes lots of sample code.
- [Plug-in Detections](https://developer.apple.com/internet/webcontent/detectplugins.html) discusses how to tune your web content to detect plug-ins (if registration did not solve the problem).
- Read the _[WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit)_ for the full WebKit plug-in reference and the reference detailing the WebKit-scripting environment bridge.
- Read the _[WebKit Objective-C Programming Guide](../../Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i)_ for tips on good WebKit application design and how the web scripting environment can access WebKit methods and properties (and vice versa).
[Next](About%20Web%20Browser%20Plug-ins.md)

