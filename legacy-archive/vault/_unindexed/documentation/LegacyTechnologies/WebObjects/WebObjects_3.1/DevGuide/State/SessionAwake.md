---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/SessionAwake.html
archived_at: '2026-07-15T07:47:49.887137Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](SessionTimeout.md)

# Using awake and sleep

Another strategy for managing session state is to create it at the beginning of the request-response loop and then release at the end. WOSession's __awake__ and __sleep__ methods provide the hooks you need to implement this strategy. A session object receives an __awake__ message at the beginning of the request-response loop (where you could reinitialize the session state) and a __sleep__ message at the end (where you could release it).

[!Table of Contents](ManagingState.book.md)
[!Next Section](ControllingComponentState.md)
