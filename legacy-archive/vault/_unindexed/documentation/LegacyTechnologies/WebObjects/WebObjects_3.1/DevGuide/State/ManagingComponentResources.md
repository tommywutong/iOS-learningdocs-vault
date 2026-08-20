---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/ManagingComponentResources.html
archived_at: '2026-07-15T07:47:45.882988Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](CreatingComponentState.md)

# Managing Component Resources

Typically, page caching occurs on both the client machine and on the WebObjects application server. WOApplication provides methods to control caching on either end of a web connection. This section discusses server-side caching and the section "[Client-Side Page Caching](ClientCaching.md)" looks at the consequences of page caching on the client.

Techniques for controlling component resources include:

- Adjusting the page cache size
- Using __awake__ and __sleep__ to initial and release resources
- Controlling page instantiation by implementing __pageWithName:__

[!Table of Contents](ManagingState.book.md)
[!Next Section](PageCacheSize.md)
