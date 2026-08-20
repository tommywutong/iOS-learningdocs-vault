---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses14.html
archived_at: '2026-07-15T08:06:11.627149Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses13.md)

### Invoking an Action

In the second phase of the request-response loop (see [Figure 25](#apple-gm2tkmq)), the application first determines which dynamic element the user has clicked (or otherwise activated) and then has that element trigger the appropriate action method in the request component. This method returns the _response page_-the component responsible for generating an HTTP response. If the user has not triggered an action, the request component is used as the response component.

!

Figure 25. Invoking an Action

Here is the basic sequence of events for invoking an action:

- The application object sends __invokeActionForRequest:inContext:__ (in Java, __invokeAction__) to itself; its implementation simply invokes the session object's __invokeActionForRequest:inContext:__ method.
- The session sends __invokeActionForRequest:inContext:__ to the request component.
- The component, in its implementation of __invokeActionForRequest:inContext:__, gets the template of the component and forwards the message to the template's root object.
- Suitable dynamic elements in the request-page template and in subcomponent templates handle the __invokeActionForRequest:inContext:__ message and invoke the appropriate action method in the request component. This action method returns the response page.

To be suitable, an element must be able to respond to user actions (a WOSubmitButton or a WOActiveImage, for example). Each of these elements evaluates the invoked action to determine if it "owns" it (that is, its __elementID__ matches the request's __senderID__).

For more on how components are associated with templates and on how HTML elements participate in request-handling, see ["How HTML Pages Are Generated"](How%20HTML%20Pages%20Are%20Generated.md#apple-haytioa).

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses15.md)
