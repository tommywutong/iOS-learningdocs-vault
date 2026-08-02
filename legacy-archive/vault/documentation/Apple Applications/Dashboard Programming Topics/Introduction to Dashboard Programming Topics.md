---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Introduction/Introduction.html
archived_at: '2026-07-15T05:17:34.799483Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Widget%20Basics.md)

# Introduction to Dashboard Programming Topics

This document provides an overview of Dashboard and the widgets that exist in it. It discusses optional features that may be implemented in a widget, various WebKit technologies you may find useful, and touches on native code integration through a widget plug-in.

_Dashboard Programming Topics_ is for anyone who wants to create and enhance a Dashboard widget. It will provide you with an understanding of different techniques useful for improving your widget's functionality.

If you haven't developed a Dashboard widget before, be sure to start with [Widget Basics](Widget%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmjxfvjvomq).

This document contains the following articles:

- [Widget Basics](Widget%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmjxfvjvomq) introduces the Dashboard environment and describes how to develop a simple widget.
- [Designing Widgets](Designing%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjtfvjvomy) provides guidelines and tips for designing successful widgets.
- [Introduction to the Apple Classes](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomi) discusses the Apple Classes, what they offer, and how to include them in your widget.
- [Using Scroll Areas](Using%20Scroll%20Areas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbrfvjvomq) talks about integrating a scroll area into your widget.
- [Using an Apple Slider](Using%20an%20Apple%20Slider.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenbsfvjvomq) tells you how to use a slider control in your widget.
- [Using Animation](Using%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobxfvjvomi) discusses using the animation-focused Apple Classes.
- [Using an Apple Button](Using%20an%20Apple%20Button.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobvfvjvoni) talks about using the `AppleButton` class to build your own buttons, and how to use the `AppleGlassButton` subclass for standard-style buttons.
- [Widget Backs and Preferences](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvomy) tells you how to display, save, and retrieve preferences.
- [Syncing Widgets](Syncing%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbyfvjvomi) looks at the Dashboard Sync feature in OS X v.10.5 and how you can handle syncing in your widget.
- [Using Widget Events](Using%20Widget%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbufvjvomi) discusses Dashboard and widget events that your widget may want to be aware of.
- [Declaring Control Regions](Declaring%20Control%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbvfvjvomy) defines and explains how to work with control regions, areas where controls are present in a widget.
- [Resizing Widgets](Resizing%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbwfvjvomi) provides code useful for implementing resizing in your widget.
- [Using the Canvas](Drawing%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztmlkciffeosskifea) talks about using the Canvas feature of WebKit within your widget.
- [Using the Pasteboard From JavaScript](Cutting%2C%20Copying%2C%20and%20Pasting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztilkciffeosskifea) talks about supporting copy, cut, and paste in a widget.
- [Using Drag and Drop From JavaScript](Dragging%20and%20Dropping.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztglkciffeosskifea) tells you about the handlers needed to support drag and drop in your widget.
- [Localizing Widgets](Localizing%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbxfvjvomq) discusses offering your widget with international users in mind, using localizable strings and other resources.
- [Specifying Access Keys](Specifying%20Access%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbyfvjvomq) describes the widget access keys, used to turn on resource access for your widget.
- [Accessing External Resources](Accessing%20External%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbzfvjvomi) talks about opening applications or web pages in a browser with your widget.
- [Accessing Command Line Utilities](Accessing%20Command%20Line%20Utilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjqfvjvomi) tells you how to access command-line utilities and scripts from within your widget.
- [Creating a Widget Plug-in](Creating%20a%20Widget%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjrfvjvomi) discusses native code plug-ins that your widget uses to interact with other applications.
- [Calling Objective-C Methods From JavaScript](Calling%20Objective-C%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiytklkcijbuerskinca) provides more detail on bridging Objective-C and JavaScript.
- [Delivering Widgets](Delivering%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjsfvjvomi) tells you about packaging and distributing your widget.

This document also contains a revision history.

All of the Dashboard-specific information discussed in this document is covered more in depth in _[Dashboard Reference](../Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_. You might also be interested in [iAd Producer](https://developer.apple.com/iad/iad-producer/), which enables some widget creation tasks and helps you create iBooks content.

In addition to these documents, _WebKit DOM Reference_ provides reference information on most of these topics.

The `XMLHttpRequest` object allows you to parse XML in JavaScript and use the results. Read [Dynamic HTML and XML: The XMLHttpRequest Object](https://developer.apple.com/internet/webcontent/xmlhttpreq.html) for more information.

[Next](Widget%20Basics.md)

