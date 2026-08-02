---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.017.html
archived_at: '2026-07-15T07:58:29.820181Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.016.md)

# Direct Actions

Previously, all WebObjects applications used the same request-handling scheme: the request to perform an action is passed from the application to the session to the request component. The request component is the component that generated the response for the previous request. Thus, the component that generates the response for one request must be preserved so that it can perform the next requested action. Because components had to be preserved across cycles of the request-response loop, all applications were required to keep some session state.
In WebObjects 4.0, you can set up all or part of your application to handle direct actions. With direct actions, the action is sent directly to an object that can handle it. Direct actions have several advantages over component actions:

- Direct actions have simpler, static URLs. Your users can bookmark a direct action URL and return to it at any time.
- Direct actions have simpler request handling.
- By default, direct actions don't use session objects and thus don't store state. If you are writing a stateless application, you may find it easier to frame your application logic using direct actions instead of component actions.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.018.md)
