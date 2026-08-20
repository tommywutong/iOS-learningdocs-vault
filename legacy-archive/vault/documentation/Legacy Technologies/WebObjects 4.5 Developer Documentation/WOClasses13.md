---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses13.html
archived_at: '2026-07-15T08:06:11.130841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses12.md)

### Taking Input Values From a Request

At this point, the application, session, and component objects have been created (if necessary) and awakened so that they are ready for the request. The next step is to extract user-entered values and assign them to variables. The application checks the WORequest object to see if it contains any user-entered values. If so, the following basic sequence of events takes place:

- The application object sends __takeValuesFromRequest:inContext:__ (in Java, __takeValuesFromRequest__) to itself; its implementation simply invokes the session object's __takeValuesFromRequest:inContext:__ method.
- The session sends the __takeValuesFromRequest:inContext:__ message to the request component.
- The component, in its implementation of __takeValuesFromRequest:inContext:__, gets its template and forwards the message to the template's root object. A _template_ is an object graph that represents the static HTML elements, dynamic HTML elements, and subcomponents that together compose the page associated with a component instance.
- All dynamic elements in the page template and in the templates of subcomponents receive the __takeValuesFromRequest:inContext:__ message. If one of these elements "owns" a user-entered value, it responds to the message by storing the value in the appropriate variable defined in the request component's declarations file.

For more on how components are associated with templates, and on how HTML elements participate in request-handling, see ["How HTML Pages Are Generated"](How%20HTML%20Pages%20Are%20Generated.md#apple-haytioa).

This step takes place _only if the request has input values_. If the request does not have input values, __takeValuesFromRequest:inContext:__ is not performed.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses14.md)
