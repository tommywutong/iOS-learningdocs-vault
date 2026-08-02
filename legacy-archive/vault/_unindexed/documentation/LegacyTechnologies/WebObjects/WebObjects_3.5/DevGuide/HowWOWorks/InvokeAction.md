---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/InvokeAction.html
archived_at: '2026-07-15T07:51:48.893888Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](AssignInputValues.md)

## Invoking an Action

In the second phase of the request-response loop (see [Figure 23](#apple-gm2tkmq)), the application first determines which dynamic element the user has clicked (or otherwise activated) and then has that element trigger the appropriate action method in the request component. This method returns the _response page_-the component responsible for generating an HTTP response. If the user has not triggered an action, the request component is used as the response component.

!Figure 23. Invoking an Action
Here is the basic sequence of events for invoking an action:

- The application object sends __invokeActionForRequest:inContext:__ (in Java, __invokeAction__) to itself; its implementation simply invokes the session object's __invokeActionForRequest:inContext:__ method.
- The session sends __invokeActionForRequest:inContext:__ to the request component.
- The component, in its implementation of __invokeActionForRequest:inContext:__, gets the template of the component and forwards the message to the template's root object.
- Suitable dynamic elements in the request-page template and in subcomponent templates handle the __invokeActionForRequest:inContext:__ message and invoke the appropriate action method in the request component. This action method returns the response page.

To be suitable, an element must be able to respond to user actions (a WOSubmitButton or a WOActiveImage, for example). Each of these elements evaluates the invoked action to determine if it "owns" it.

For more on how components are associated with templates and on how HTML elements participate in request-handling, see ["How HTML Pages Are Generated"](ComponentElement.md#apple-gy2dsmq).

[!Table of Contents](HowWOWorks.md) [!Next Section](AppendToResponse.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
