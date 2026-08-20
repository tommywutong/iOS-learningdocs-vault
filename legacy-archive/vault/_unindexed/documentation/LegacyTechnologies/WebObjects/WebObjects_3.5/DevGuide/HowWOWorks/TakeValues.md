---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/TakeValues.html
archived_at: '2026-07-15T07:51:56.284660Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](StartingRRLoop.md)

## Taking Values From the Request

The first phase of the request-response loop (see [Figure 19](#apple-gm2dcmi)) synchronizes the state of the request component with the HTML page as submitted by the user. In this phase, the appropriate dynamic elements extract the values that users enter and the choices they make in the request page and assign them to declared variables.

For example, if the user clicked a checkbox, the dynamic element that represents that checkbox must be set to the "checked" state. In other words, the __checked__ attribute of the appropriate WOCheckbox dynamic element must be set to YES.!Figure 19. Taking Values From the Request
A cycle of the request-response loop begins when the WOAdaptor receives an incoming HTTP request. The adaptor object packages this request in a WORequest and forwards this object to the application object in a __handleRequest:__ message. Upon receiving this message, the application object does the following:

- It creates the WOResponse and WOContext objects that will be needed.
- It invokes its own __awake__ method.
- It determines which session and which request page are associated with the request, as described next.

[!Table of Contents](HowWOWorks.md) [!Next Section](AccessSession.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
