---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClasses15.html
archived_at: '2026-07-18T01:20:26.483410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses14.md)

### Generating the Response

In the final phase of request-response loop (see [Figure 26](#apple-gm2tqmq)), the response page generates an HTTP response. Generally, the response contains a dynamically generated HTML page. Each element (static and dynamic) that makes up the response page appends its HTML code to the total stream of HTML code that will be interpreted by the client browser.

!

Figure 26. Generating the Response

Here is the basic sequence of events for generating a response:

- The application object stores the response component indicated by the action method's return value. (This action method was invoked during phase 2.)
- If the response component is different from the request component, application sends the __awake__ message to the response component.
- The application object sends __appendToResponse:inContext:__ to itself; its implementation simply invokes the session object's __appendToResponse:inContext:__ method.
- The session pushes the response component onto the WOContext stack and sends the response component the __appendToResponse:inContext:__ message.
- The response component, in its implementation of __appendToResponse:inContext:__, gets the template for the component and sends __appendToResponse:inContext:__ to the template's root object.
- All static and dynamic HTML elements in the response-page template, and in subcomponent templates, receive the __appendToResponse:inContext:__ message. In it, they append to the content of the response the HTML code that represents them. For dynamic elements, this code includes the values assigned to variables.
- When control returns to the session object, the session object asks the WOStatisticsStore to record statistics about the response. WOStatisticsStore sends the session a __descriptionForResponse:inContext:__ message. The session, in turn, sends the response component __descriptionForResponse:inContext:__ message. By default, this method returns the response component's name.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses16.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
