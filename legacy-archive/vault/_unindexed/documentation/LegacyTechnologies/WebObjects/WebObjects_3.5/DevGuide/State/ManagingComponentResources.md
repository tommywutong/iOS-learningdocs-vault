---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/ManagingComponentResources.html
archived_at: '2026-07-15T07:52:15.883953Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](ControllingComponentState.md)

## Managing Component Resources

Typically, page caching occurs both on the client machine and on the WebObjects application server. WOApplication provides methods to control caching on either end of a web connection. This section discusses server-side caching and the section ["Client-Side Page Caching"](ClientCaching.md#apple-gy4tanq) looks at the consequences of page caching on the client.

There are three common techniques for controlling component resources:

- Adjusting the page cache size
- Using awake and sleep to initialize and release resources
- Controlling page instantiation by implementing pageWithName:

[!Table of Contents](StateTOC.md) [!Next Section](PageCacheSize.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
