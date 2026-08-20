---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/SessionCode.html
archived_at: '2026-07-15T07:52:45.790039Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](AppCode.md)

## Session Code

_Sessions_ are periods during which one user is accessing your application. Because users on different clients may be accessing your application at the same time, a single application may have more than one session accessing it at a time (see [Figure 3](#apple-gu4dqmq)). Each session has its own copy of the components that its user has requested.

!Figure 3. Application, Sessions, and Components 
You perform tasks that affect a single session and store variables that persist throughout a session in the _session code file_. The session code file is named Session and has the appropriate extension (__Session.wos__, __Session.java__, or __Session.m__).

[!Table of Contents](WhatIsWOApp.md) [!Next Section](NoteOnClasses.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
