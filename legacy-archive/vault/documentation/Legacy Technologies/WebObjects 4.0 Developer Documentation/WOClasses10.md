---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClasses10.html
archived_at: '2026-07-18T01:20:22.460103Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses9.md)

## Handling Component Action Requests

The first phase of the component action request-response loop (see [Figure 22](#apple-gm2dcmi)) synchronizes the state of the request component with the HTML page as submitted by the user. In this phase, the appropriate dynamic elements extract the values that users enter and the choices they make in the request page and assign them to declared variables.

For example, if the user clicked a checkbox, the dynamic element that represents that checkbox must be set to the "checked" state. In other words, the __checked__ attribute of the appropriate WOCheckbox dynamic element must be set to YES.

!

Figure 22. Taking Values from the Request

When the component action request handler receives the __handleRequest:__ message from the application, it does the following:

- It creates the WOResponse and WOContext objects that will be needed.
- It invokes the application's __awake__ method.
- It determines which session and which request page are associated with the request, as described next.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses11.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
