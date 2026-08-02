---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/InitializationMethods.html
archived_at: '2026-07-15T07:47:28.357896Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](Introduction.md)

# Initialization Methods

The application, session, and component objects in a WebObjects application receive two messages that allow the objects to initialize themselves. The two methods, __init__ and __awake__, are invoked in both scripted and compiled instances of WOApplication, WOSession, and WOComponent subclasses. The main difference between the methods is _when_ they are invoked.

## When init and awake are Sent

When objects are created, they receive an __init__ message. The __init__ method gives the receiver an opportunity to initialize its state and behavior just after it is created. The initialization is effective over the lifetime of an object; this lifetime varies according to the object's type:

- The WOApplication object exists from the time the application is started until it is terminated (either explicitly or through application time-out).
- The WOSession object persists through a session. As session is a period during which a particular user is accessing the application, and during which resources are allocated accordingly. An application can have multiple concurrent sessions. The application object creates a WOSession object if a request is the first from a user (that is, there is no session ID associated with it). Sessions can be explicitly terminated or can end when a _session time-out_---a period of no user activity---occurs.
- The WOComponent objects of an application are created each time a page is directly requested via URL and each time a __pageWithName:__ message is sent to the application object. There are a couple exceptions to this. If page caching is turned on, as it is by default, the session object stores each component instance (page) at the end of each request-response loop. If the user backtracks through a session, the application restores page instances from this cache. Also, if the request component returns __self__ or (preferably) __nil__ in an action method, the application returns the cached instance of the request component rather than re-creating a new instance.

An object's __awake__ method, on the other hand, is invoked at that point in each cycle of the request-response loop that the object begins to participate in request handling. This usually occurs right after __init__, except in those two cases noted above where an page is restored from a cache rather than created. In these cases, the __awake__ method is invoked without a prior invocation of the __init__ method.

See "[How WebObjects Works](../HowWOWorks/HowWOWorks.mif.book.md)" for a discussion of __init__ and __awake__ in the context of the request-response loop.

[!Table of Contents](RunLoop.book.md)
[!Next Section](StructureOfInitAwake.md)
