---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/AppendToResponse.html
archived_at: '2026-07-15T07:51:44.308853Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](InvokeAction.md)

## Generating the Response

In the final phase of request-response loop (see [Figure 24](#apple-gm2tqmq)), the response page generates an HTTP response. Generally, the response contains a dynamically generated HTML page. Each element (static and dynamic) that makes up the response page appends its HTML code to the total stream of HTML code that will be interpreted by the client browser.

!Figure 24. Generating the Response
Here is the basic sequence of events for generating a response:

- The application object stores the response component indicated by the action method's return value. (This action method was invoked during the second phase of the request-response loop.)
- If the response component is different from the request component, application sends the __awake__ message to the response component.
- The application object sends __appendToResponse:inContext:__ to itself; its implementation simply invokes the session object's __appendToResponse:inContext:__ method.
- The session pushes the response component onto the WOContext stack and sends the response component the __appendToResponse:inContext:__ message.
- The response component, in its implementation of __appendToResponse:inContext:__, gets the template for the component and sends __appendToResponse:inContext:__ to the template's root object.
- All static and dynamic HTML elements in the response-page template, and in subcomponent templates, receive the __appendToResponse:inContext:__ message. In it, they append to the content of the response the HTML code that represents them. For dynamic elements, this code includes the values assigned to variables.
- When control returns to the session object, the session object asks the WOStatisticsStore to record statistics about the response. WOStatisticsStore sends the session a __descriptionForResponse:inContext:__ message. The session, in turn, sends the response component __descriptionForResponse:inContext:__ message. By default, this method returns the response component's name.

After the response has been generated, but before returning the response to the adaptor, the application object concludes request handling by doing the following:

- It causes the __sleep__ method-the counterpart of __awake__-to be invoked in all components involved in the cycle (request, response, and subcomponents). As described in the chapter ["Managing State"](../State/StateTOC.md#apple-gu4tmmq), in the __sleep__ method, objects can release resources that don't have to be saved between cycles.
- It requests the session object to save the response page in the page cache.
- It invokes the session object's __sleep__ method.
- It saves the session object in the session store.
- It invokes its own __sleep__ method.

When an Objective-C object is about to be destroyed, its __dealloc__ method is invoked at an undefined point in time after a cycle (indicated by the vertical ellipses in [Figure 24](#apple-gm2tqmq)). In the __dealloc__ method, the object releases any retained instance variables. In WebScript, this usually happens implicitly; you therefore usually don't need to implement the __dealloc__ method in any objects you write. In Java, objects have automatic garbage collection, so this deallocation step is unnecessary.

[!Table of Contents](HowWOWorks.md) [!Next Section](ComponentElement.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
