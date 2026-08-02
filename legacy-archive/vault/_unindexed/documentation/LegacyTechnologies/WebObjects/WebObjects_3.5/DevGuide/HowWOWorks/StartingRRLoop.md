---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/StartingRRLoop.html
archived_at: '2026-07-15T07:51:54.825815Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](PhasesRRLoop.md)

## Starting the Request-Response Loop

A WebObjects application can start up in one of two ways: automatically, when it receives a request (autostarting), or manually, when it's run from the command line. Either way, its entry point is the same as that of any C program: the __main__ function. In a WebObjects application, __main__ is usually very short. Its job is to create and run the application.
The __main__ function begins by creating an autorelease pool that's used for the automatic deallocation of objects that receive an __autorelease__ message. It then calls a function that loads the Java Virtual Machine (VM) if necessary.
The next step is to create a WOApplication (or WebApplication) object. This seems fairly straightforward, but in the __init__ method or constructor the application creates and stores, in an instance variable, one or more adaptors. These adaptors, all instances of a WOAdaptor subclass, handle communication between an HTTP server and the WOApplication object. The application first parses the command line for the specified adaptors (with necessary arguments); if none are specified, as happens when the application is autostarted, it creates a suitable default adaptor.
The __run__ method initiates the request-response loop. When __run__ is invoked, the application sends __registerForEvents__ to each of its adaptors to tell them to begin receiving events. Then the application begins running in its run loop.
The autorelease pool is released and recreated immediately before the __run__ message is sent. Releasing the autorelease pool at this point releases any temporary variables created during initialization of the application class. Creating a new autorelease pool before sending __run__ ensures that all variables created while running the application will be released. The last message releases the autorelease pool, which in turn releases any object that has been added to the pool since the application started running.
In the rest of this section, we look at what happens during one complete cycle of the request-response loop.

[!Table of Contents](HowWOWorks.md) [!Next Section](TakeValues.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
