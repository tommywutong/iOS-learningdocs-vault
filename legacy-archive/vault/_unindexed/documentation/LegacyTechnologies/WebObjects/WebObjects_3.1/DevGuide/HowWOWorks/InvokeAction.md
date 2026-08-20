---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/InvokeAction.html
archived_at: '2026-07-15T07:46:53.206945Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](TakeValues.md)

# __Invoking an Action__

In the second phase of the request-response loop, the application sends the __invokeActionForRequest:inContext:__ message to itself, and eventually to all other objects involved in handling this request. The purpose of this message is to locate the dynamic element which the user has clicked (or otherwise activated) and have that element trigger the appropriate action method in the request component. This method returns the _response page_---the component responsible for generating an HTTP response. If the user has not triggered an action, the request component is used as the response component.

This is the basic sequence of events in invoking an action:

1. The WOApplication object sends __invokeActionForRequest:inContext:__ to itself; its implementation simply invokes the WOSession object's __invokeActionForRequest:inContext:__.
2. The session, in its implementation of __invokeActionForRequest:inContext:__, gets the template of the component and forwards the message to it.
3. Suitable dynamic elements in the request-page template, and in subcomponent templates, handlethe __invokeActionForRequest:inContext:__ message. To be suitable, an element must be able to respond to user actions (a WOSubmitButton or a WOActiveImage, for example). Each of these elements evaluates the invoked action to determine if it "owns" it. If so, it invokes the appropriate action method in the request page, which returns the response page.

For more on how components are associated with templates, and on how HTML elements participate in request-handling, see the section "[Component and Element](ComponentElement.md#apple-kjcumnbwgy4ds)."

!

Figure 4: Invoking an Action

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](AppendToResponse.md)
