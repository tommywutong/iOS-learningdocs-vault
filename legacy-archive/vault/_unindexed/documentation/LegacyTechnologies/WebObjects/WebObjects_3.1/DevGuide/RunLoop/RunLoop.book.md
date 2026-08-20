---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/RunLoop.book.html
archived_at: '2026-07-15T07:47:29.385697Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../DevGuide.md)

# Integrating Your Code Into the Request-Response Loop

On each cycle of the request-response loop, an application initiates a series of messages to objects that are participating in request handling. These messages are "hooks" that allow you to integrate your code into the request-response loop and affect the outcome of request handling. This chapter describes the methods invoked by these messages.

## Table of Contents

: __[Introduction](Introduction.md#apple-kjcummrugq2dg)

: [Initialization Methods](InitializationMethods.md#apple-kjcummjthaydg)

:__[When __init__ and __awake__ are Sent](InitializationMethods.md#apple-kjcumojxgm3da)

: [The Structures of __init__ and __awake__](StructureOfInitAwake.md#apple-kjcumobtguzdk)

: [The __sleep__ and __dealloc__ Methods](sleepAnddealloc.md#apple-kjcumnzyga4tg)

: [When Use __init__, When Use __awake__?](initOrAwake.md#apple-kjcumnzqg4zte)

: [Application Initialization](ApplicationInit.md#apple-kjcumnztgq2dq)

: [Session Initialization](SessionInit.md#apple-kjcumnzug42dk)

: [Component Initialization](ComponentInit.md#apple-kjcummjzg4ytg)

: __[Action Methods](ActionMethods.md#apple-kjcumojzgi4ta)

: [Request-Handling Methods](RequestHandlingMethods.md#apple-kjcumnbrha2tg)

:__[takeValuesFromRequest:inContext:](takeValuesFromRequest.md#apple-kjcumnbzgq2ds)

: [invokeActionForRequest:inContext:](invokeActionForRequest.md#apple-kjcumnzqhaydg)

: [appendToResponse:inContext:](appendToResponse.md#apple-kjcummzygi2dk)

: __[Summary](Summary.md#apple-kjcumnrtgi2tq)

### Related Topics

: [How WebObjects Works](../HowWOWorks/HowWOWorks.mif.book.md)

: [Using WebScript](../WebScript/WebScript.mif.book.md)

: [Managing State](http://devworld.apple.com/dev/SWTechPubs/Documents/WebObjects/DevGuide/State/ManagingState.book.html)__

[!First Section](Introduction.md)
