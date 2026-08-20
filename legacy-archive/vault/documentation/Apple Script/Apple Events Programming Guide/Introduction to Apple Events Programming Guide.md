---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/intro_aepg/intro_aepg.html
archived_at: '2026-07-15T05:19:29.834367Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Apple%20Events.md)

# Introduction to Apple Events Programming Guide

_Apple Events Programming Guide_ provides conceptual information and programming examples for working with Apple events.

An _Apple event_ is a type of interprocess message that can specify complex operations and data. Apple events allow you to gather all the data necessary to accomplish a high level task into a single package that can be passed across process boundaries, evaluated, and returned with results. The Mac OS uses Apple events to communicate with applications. Apple events are also an essential part of the AppleScript scripting system, which allows users to automate actions using _scriptable applications_—applications that can respond to a variety of Apple events by performing operations or supplying data.

_Apple Events Programming Guide_ assumes that you are familiar with the information in _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_.

The information in this document applies primarily to Carbon applications. While Cocoa applications can take advantage of most of the described features, in many cases they won’t need to. For more information, see [Framework and Language Support](About%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgiwugrkhjfeugqsi).

You should read this document if you want to:

- Make your Carbon application respond to the Apple events sent by the Mac OS (for launching and quitting applications, opening documents, and so on).
- Work with Apple events as part of writing a scriptable Carbon application.
- Use Apple events to communicate with other applications.
- Gain background information about Apple events for your work with scriptable Cocoa applications, AppleScript Studio applications, Automator workflows, or AppleScript scripts.

This document is organized into the following chapters:

- [About Apple Events](About%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgiwueqkcirauur2c) defines Apple events, explains when they’re useful, and provides a quick overview of common tasks for working with them. It also provides a brief description of the framework and language support available in Mac OS X and provides links to additional information in _Apple Events Programming Guide_ and in other documents.
- [Building an Apple Event](Building%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgmwueqkcirauur2c) provides an overview of Apple event data structures and describes how to build an Apple event.
- [Apple Event Dispatching](Apple%20Event%20Dispatching.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgqwueqkcirauur2c) shows how your application works with the Apple Event Manager to register the Apple events it can handle and dispatch those events to the code that should handle them.
- [Working With the Data in an Apple Event](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqseiffeoqq) describes how to extract data from Apple events and the data structures that comprise them.
- [Responding to Apple Events](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywueqkcirauur2c) describes how to respond to an Apple event by examining the event, performing the requested action, interacting with the user (if necessary), and returning a reply event. It also provides an overview of how to respond to Apple events sent by the Mac OS.
- [Creating and Sending Apple Events](Creating%20and%20Sending%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhewueqkcirauur2c) provides information and sample code that will help you create and send Apple events and respond to reply Apple events.
- [Writing and Installing Coercion Handlers](Writing%20and%20Installing%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawueqkcirauur2c) describes how to write coercion handlers that convert between various types of data and how to install them so that they are available to your application.
- [Testing and Debugging Apple Event Code](Testing%20and%20Debugging%20Apple%20Event%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgawueqkcirauur2c) provides tips for displaying and debugging Apple events in your application.
- [Selected Apple Event Manager Functions](Selected%20Apple%20Event%20Manager%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgewueqkcirauur2c) provides information about some commonly used functions.
- [Selected Apple Event Constants](Selected%20Apple%20Event%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgiwueqkcirauur2c) provides information about some commonly used constants.
- [Default Coercion Handlers](Default%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgmwueqkcirauur2c) lists the type conversions performed by the default coercion handlers provided by the Mac OS.

The following documents provide related information.

- _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_ provides information that is useful for working with AppleScript and Apple events, including a description of the Open Scripting Architecture, on which both rely.
- _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_ describes the API for sending and receiving Apple events and working with the information they contain.
- Technical Note TN2106, [Scripting Interface Guidelines](https://developer.apple.com/technotes/tn2002/tn2106.html), describes how to design the scripting interface for a scriptable application.
- [AppleScript Language Guide](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html) describes the features and terminology of the AppleScript scripting language.
- For information on sending Apple events to web services, see _[XML-RPC and SOAP Programming Guide](../XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw)_.
[Next](About%20Apple%20Events.md)

