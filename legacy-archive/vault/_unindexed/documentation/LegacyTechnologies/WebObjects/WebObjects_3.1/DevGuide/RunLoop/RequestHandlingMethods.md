---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/RequestHandlingMethods.html
archived_at: '2026-07-15T07:47:29.363992Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](ActionMethods.md)

# Request-Handling Methods

WebObjects defines three request-handling methods that are invoked at particular points in the request-response loop if you implement them:

- takeValuesFromRequest:inContext:
- invokeActionForRequest:inContext:
- appendToResponse:inContext:

As with __init__ and __awake__ methods, the request-handling methods can be implemented for an application, a session, and the application's components. All versions of a request-handling method work identically, and can be used for similar purposes. You choose to implement a method for the application, the session, or a component based on which is more appropriate for the behavior you need to provide. Generally, you implement request-handling methods in the application or the session object when the specified behavior should affect every request. You implement request-handling methods in a component when the behavior should affect a particular page.

The WOApplication, WOSession, and WOComponent classes each declare and implement the three methods that handle requests and responses. The implementations of these methods that you provide in scripts---__Application.wos__, __Session.wos__, and component scripts---are dynamically added to the appropriate subclass object that WebObjects generates at run time. Consequently, when WOApplication sends __takeValuesFromRequest:inContext:__ to __self__, the __takeValuesFromRequest:inContext:__ method defined in the corresponding __Application.wos__ (ifit exists) is invoked. In compiled subclasses of WOApplication, WOSession, and WOComponent, you can override the request-handling methods, but it is more common to implement them in a script.

In your implementations of request-handling methods you must invoke __super__'s implementation of the same methods. _Where_ you invoke it is an important consideration because it can affect the request, response, and context information available at any given point. You will want to perform certain tasks before __super__ is invoked and, for other tasks, after __super__ is invoked.

[!Table of Contents](RunLoop.book.md)
[!Next Section](takeValuesFromRequest.md)
