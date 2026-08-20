---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/StandardMethods.html
archived_at: '2026-07-15T07:51:05.992463Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](CreateMethods.md)

 Standard Methods You May Want to Implement

|  |  |
| --- | --- |
|  | ---  Standard Methods You May Want to Implement Applications, sessions, and components define some common methods that you may want to implement. These methods are invoked during initialization, deallocation, and the request-response loop. (The request-response loop is a WebObjects application's main loop. It begins when the user generates a request by typing an URL or clicking a button on the page. It ends when the application has processed the request and generated a response page. One request-response loop cycle is called a _transaction_.) The list below provides a brief description of when you want to implement these methods.  __Important:__ The chapter "[Integrating Your Code Into the Request-Response Loop](../../DevGuide/RunLoop/RunLoop.book.md)" in the _WebObjects Developer's Guide_ provides full details on how to implement these methods. Read it before you write any code.  **__init__** : Initializes application variables, session variables, and any component variables that should persist as long as the component persists.  **__dealloc__** : Deallocates all variables initialized in the __init__ method.  **__awake__** : Initializes variables that need to be reinitialized at the top of the request- response loop.  **__sleep__** : Sets to nil all variables that were initialized in the __awake__ method.  **__takeValuesFromRequest:inContext:__** : Invoked at the beginning of the request-response loop, right after the __awake__ method. Use this method to perform any tasks that need to be performed before the action of the page but after the bindings have been synchronized. (Bindings are synchronized by calling the superclass, WOComponent, implementation of t__takeValuesFromRequest:inContext:__ .)  **__invokeActionForRequest:inContext:__** : Invoked when the component is about to perform an action based on user input. Use this method if you want to generate a different object for the response page than would normally be created.  **__appendToResponse:inContext:__** : Invoked right after the request page has generated the response page. Use this method if you want to append text to the response page.     --- |

[!Table of Contents](Script.book.md)
[!Next Section](ScriptWindow.md)
