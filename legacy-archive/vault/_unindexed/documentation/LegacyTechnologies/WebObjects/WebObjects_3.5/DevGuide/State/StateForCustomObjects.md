---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StateForCustomObjects.html
archived_at: '2026-07-15T07:52:20.869264Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](CustomStorageOptions.md)

# Storing State for Custom Objects

When state is stored in the server, the objects that hold state are kept intact in memory between cycles of the request-response loop. In contrast, when state is stored in the page, in cookies, or in the file system, objects are asked to archive themselves (using classes and methods defined in the Foundation framework) before being put into storage. The objects that are part of the WebObjects and Foundation frameworks can archive themselves, so they require no effort on your part. But if your application has custom classes that need to store state, these classes must know how to archive and unarchive themselves. How you implement archiving for custom classes depends on whether your application accesses a database. If your application accesses a database, it uses the Enterprise Objects Framework and should use the EOEditingContext class (EditingContext in Java) to archive objects. If your application doesn't access a database, it should use the NSArchiver class to archive custom objects.

[!Table of Contents](StateTOC.md) [!Next Section](UsingEOEditingContext.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
