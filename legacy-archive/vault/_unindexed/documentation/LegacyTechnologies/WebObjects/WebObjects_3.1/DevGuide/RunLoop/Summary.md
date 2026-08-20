---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/Summary.html
archived_at: '2026-07-15T07:47:30.936810Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](appendToResponse.md)

# Summary

##  What request-response loop "hooks" can you implement?

There are three types of methods that allow your application to influence what happens in the request-response loop:

- _Initialization methods_---__init__ and __awake__--- are invoked, respectively, when an object is created and just before the receiver begins to participate in each cycle of the request-response loop. The methods __dealloc__ and __sleep__ allow the deallocation of variables initialized in __init__ and __awake__.
- _Action methods_ are associated with a particular user action such as clicking a button or hyperlink.
- _Request--handling methods_, if implemented, are invoked in application, session, and component objects at particular points in the request-response loop.

You can participate in the request-response loop by implementing any of these methods.

## What you can use the hooks for?

The following list summarizes common uses of the request-response loop "hooks":

- Action methods perform page navigation.
- Application __init__ and __awake__ methods are places to initialize application variables and configure application behavior.
- Session __init__ and __awake__ methods are places to initialize session variables and configure session behavior.
- Component __init__ and __awake__ methods are places to initialize component variables and configure component behavior.
- The __sleep__ and __dealloc__ methods are places to deallocate variables initialized in __awake__ and __init__, respectively.
- In most situations, you can use __init__ to initialize variables. To optimize applications, you might do more of your initializations in __awake__, especially if they involve inexpensive operations.
- Use __takeValuesForRequest:inContext:__ methods to access request and context information and to perform postprocessing of user input.
- Use __invokeActionForRequest:inContext:__ methods to substitute a different page for the response (except for initial requests).
- Use __appendToResponse:inContext:__ methods to add to the response content or otherwise manipulate the HTTP response.
