---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState10.html
archived_at: '2026-07-15T08:05:38.944037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState9.md)

# Storing State for Custom Objects

When state is stored in the server, the objects that hold state are kept intact in memory between cycles of the request-response loop. In contrast, custom state storage mechanisms may ask objects to archive themselves (using classes and methods defined in the Foundation framework) before being put into storage. The objects that are part of the WebObjects and Foundation frameworks can archive themselves, so they require no effort on your part. But if your application has custom classes that need to store state, these classes must know how to archive and unarchive themselves. How you implement archiving for custom classes depends on whether your application accesses a database. If your application accesses a database, it uses the Enterprise Objects Framework and should use the EOEditingContext class to archive objects. If your application doesn't access a database, it should use the NSArchiver class to archive custom objects.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState11.md)
