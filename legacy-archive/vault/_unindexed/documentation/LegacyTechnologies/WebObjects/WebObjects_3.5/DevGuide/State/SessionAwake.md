---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/SessionAwake.html
archived_at: '2026-07-15T07:52:18.801061Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](SessionTimeOut.md)

## Using awake and sleep

Another strategy for managing session state is to create it at the beginning of the request-response loop and then release it at the end. The session object's awake and sleep methods provide the hooks you need to implement this strategy. A session object receives an awake message at the beginning of the request-response loop (where you can reinitialize the session state) and a sleep message at the end (where you can release it).

[!Table of Contents](StateTOC.md) [!Next Section](ControllingComponentState.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
