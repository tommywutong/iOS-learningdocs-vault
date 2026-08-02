---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/ControllingSessionState.html
archived_at: '2026-07-15T07:52:14.830512Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](UsingNSCoding.md)

# Controlling Session State

Maintaining state in memory on the server can consume considerable resources, so WebObjects provides a number of mechanisms to control how much state is stored. This section takes a closer look at how you manage sessionwide state.
Take care that your application only stores state for active sessions and stores the smallest amount of state possible. WOSession lets you control these factors by providing a time-out mechanism for inactive sessions and by providing a way to specify exactly what state to store between request-response loop cycles.

[!Table of Contents](StateTOC.md) [!Next Section](SessionTimeOut.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
