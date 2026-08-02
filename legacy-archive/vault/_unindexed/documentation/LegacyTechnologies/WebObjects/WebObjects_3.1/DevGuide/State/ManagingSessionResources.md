---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/ManagingSessionResources.html
archived_at: '2026-07-15T07:47:46.378205Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](CreatingSessionState.md)

# Managing Session Resources

If you choose to store state in memory on the application server, memory usage can become an issue. (See "[State Storage Strategies](StoreCompTable.md)" for alternative ways of storing this information.) Take care that your application only stores state for active sessions and stores the smallest amount of state possible. WOSession lets you control these factors by providing a timeout mechanism for inactive sessions and by providing a way to specify exactly what state to store between transactions.

[!Table of Contents](ManagingState.book.md)
[!Next Section](SessionTimeout.md)
