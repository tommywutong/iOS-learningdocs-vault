---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClasses18.html
archived_at: '2026-07-18T01:20:28.681859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses17.md)

## Component Actions vs. Direct Actions

[Figure 28](#apple-ha4temy) shows the sequence of events in processing a component action request and compares it to the sequence of events for processing the direct action. Note that in both component actions and direct actions, the bulk of the time is spent in the generate response phase, in which the component performs __appendToResponse:inContext:__ and sends each of its dynamic elements __appendToResponse:inContext:__. This step is the same in component actions and direct actions.

|  __Component Action__ |  Direct Action |
|  The adaptor creates a WORequest object and passes it to the application. |  The adaptor creates a WORequest object and passes it to the application. |
|  The application determines that the WOComponentRequestHandler should handle the request. |  The application determines that the WODirectActionRequestHandler should handle the request. |
|  The application, session, and the request component are created, if necessary, and sent the __awake__ message. |  Application __awake__ is called. |
|  The __takeValuesFromRequest:inContext:__ message is propagated from the application to the session to the request component to each dynamic element in the request component (if the request has input values). |  WODirectActionRequestHandler parses the URL and instantiates the WODirectAction class. |
|  The __invokeActionForRequest:inContext:__ message is propagated from the application to the session to the request component to each dynamic element in the request component, resulting in the appropriate action method in the component being invoked. |  WODirectActionRequestHandler sends the message __performActionNamed:__ to the WODirectAction, resulting in the appropriate action being invoked.  If there are any input values, WODirectAction uses __takeFormValues...__ methods to extract them from the WORequest. |
|  The __action__ method creates and returns a response component or response. |  The __action__ method creates and returns a response component or response. |
|  The application awakens the response component.  The __appendToResponse:inContext:__ message is propagated from the application to the session to the response component to each dynamic element in the response component. |  The object returned by the action method is sent a __generateResponse__ method to guarantee that the object returned is a WOResponse.  If the action returns a WOComponent, WOComponent's __generateResponse__ invokes __appendToResponse:inContext:__, which sends each dynamic element in the component an __appendToResponse:inContext:__ message as well. |
|  The application forwards the WOResponse to the adaptor. |  The application forwards the WOResponse to the adaptor. |
|  The application, session, and all of the components are sent the __sleep__ message. |  The WODirectAction is release or marked for garbage collection. Application __sleep__ is called. |
|  The component is saved in the session so it can handle any subsequent requests. |  If the returned component contained any component actions, the component is saved in the session so it can handle any subsequent requests. |

```
```


Figure 28. Comparison of Component Action and Direct Action request processing.

The major differences between component actions and direct actions are:

- Component actions require state, primarily so that they can determine which component should perform the action.

Direct actions are stateless actions. They do not require any state to be preserved between requests. For this reason, direct actions do not create session objects by default. WODirectAction defines a method that does create a session, so direct actions can create a session and store state if necessary.

- Component actions extract input values from the request without requiring you to write any code to do so.

Direct actions do not automatically extract input values from the request. If there are input values, the HTML element places them in the HTTP request, and the action method must explicitly request them from the WORequest object.

- Component actions have dynamic, unpredictable URLs because the URL contains the session ID and context ID, which are unique to each session.

Direct actions have static, predictable URLs. Regardless of which session is performing the action, the URL for the action always refers to a specific action-one that was determined when the current page was generated (not when the request is handled).

Because their URLs are static and because they do not require state, direct action requests can be bookmarked by your application's users and can be revisited at any time.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](How%20HTML%20Pages%20Are%20Generated.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
