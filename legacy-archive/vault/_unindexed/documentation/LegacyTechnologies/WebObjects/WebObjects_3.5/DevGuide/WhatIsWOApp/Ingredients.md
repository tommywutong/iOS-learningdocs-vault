---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/Ingredients.html
archived_at: '2026-07-15T07:52:43.214897Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](WhatIsWOApp.md)

# The Ingredients of a WebObjects Application

WebObjects applications reside within a directory named __WebObjects__ in your web server's document root (<DocumentRoot>__/WebObjects__). Look in <DocumentRoot>__/WebObjects/Examples/WebScript__, and you'll see several directories. These are WebObjects application projects, provided with the WebObjects package as examples that you can use when learning WebObjects. These examples range from simple to highly complex. For now, you might want to focus on two of the simplest applications, named __HelloWorld__ and __Visitors__.
When you look inside any of these project directories, you may see these pieces:

- __.wo__ directories, which are called _components_. Components are dynamic HTML pages.
- An application code file (__Application.wos__), which creates and manages applicationwide resources.
- A session code file (__Session.wos__), which creates and manages sessionwide resources.
- Standard project files, such as makefiles.

The following sections describe the WebObjects application ingredients in more detail.

[!Table of Contents](WhatIsWOApp.md) [!Next Section](Components.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
