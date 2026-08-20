---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState15.html
archived_at: '2026-07-15T08:05:41.552714Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState14.md)

## Using awake and sleep

Another strategy for managing session state is to create it at the beginning of the request-response loop and then release it at the end. The session object's __awake__ and __sleep__ methods provide the hooks you need to implement this strategy. A session object receives an __awake__ message at the beginning of the request-response loop (where you can re-initialize the session state) and a __sleep__ message at the end (where you can release it). Remember that __awake__ and __sleep__ are not sent during the direct action request-response loop, but the direct action request-response loop does not use session objects by default.

[!Table of Contents](Managing%20State.md) [!Next Section](Controlling%20Component%20State.md)
