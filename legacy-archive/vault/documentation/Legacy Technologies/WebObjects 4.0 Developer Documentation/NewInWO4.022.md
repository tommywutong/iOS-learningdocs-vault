---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.022.html
archived_at: '2026-07-15T07:58:32.853566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.021.md)

## Comparison of Request Processing

The following table shows the sequence of events in processing a traditional, component action request and compares it to the sequence of events for processing a new direct action. Note that in both component actions and direct actions, the bulk of the time is spent in the generate response phase, in which the component performs __appendToResponse:inContext:__ and sends each of its dynamic elements __appendToResponse:inContext:__. This step is the same in component actions and direct actions.

|  Component Action |  Direct Action |
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

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.023.md)
