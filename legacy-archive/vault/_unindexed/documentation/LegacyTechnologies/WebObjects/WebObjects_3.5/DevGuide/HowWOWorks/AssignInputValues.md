---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/AssignInputValues.html
archived_at: '2026-07-15T07:51:45.768983Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](RequestPage.md)

### Assigning Input Values

At this point, the application, session, and component objects have been created (if necessary) and awakened so that they are ready for the request. The next step is to extract user-entered values and assign them to variables. Here is the basic sequence of events in preparing for a request:

- The application object sends __takeValuesFromRequest:inContext:__ (in Java, __takeValuesFromRequest__) to itself; its implementation simply invokes the session object's __takeValuesFromRequest:inContext:__ method.
- The session sends the __takeValuesFromRequest:inContext:__ message to the request component.
- The component, in its implementation of __takeValuesFromRequest:inContext:__, gets its template and forwards the message to the template's root object. A _template_ is an object graph that represents the static HTML elements, dynamic HTML elements, and subcomponents that together compose the page associated with a component instance.
- All dynamic elements in the page template and in the templates of subcomponents receive the __takeValuesFromRequest:inContext:__ message. If one of these elements "owns" a user-entered value, it responds to the message by storing the value in the appropriate variable defined in the request component's declarations file.

For more on how components are associated with templates, and on how HTML elements participate in request-handling, see ["How HTML Pages Are Generated"](ComponentElement.md#apple-gy2dsmq).

[!Table of Contents](HowWOWorks.md) [!Next Section](InvokeAction.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
