---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects6.html
archived_at: '2026-07-15T08:06:56.510196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects5.md)

## The Request-Response Loop

WebObjects applications are event driven, but instead of responding to mouse and keyboard events, they respond to HTTP requests. The main loop of a WebObjects application is called the _request-response loop_. During each cycle of the request-response loop, the application receives an HTTP request for an action, responds to it, and then waits for the next request. The application continues to respond to requests until it terminates.
The basic request-response loop is illustrated in [Figure 8](#apple-he2dimi), below.

!

Figure 8. The Request-Response Loop

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects7.md)
