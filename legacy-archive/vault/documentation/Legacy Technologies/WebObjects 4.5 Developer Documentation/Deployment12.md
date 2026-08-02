---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment12.html
archived_at: '2026-07-15T08:05:18.493874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment11.md)

## Limit Database Fetches

Every database access that your application performs is a potential drag on performance. One easy way to limit trips to the database is to perform prefetching. For more information, see the chapter "Answers to Common Design Questions" in the _Enterprise Objects Framework Developer's Guide_.
If you have components that load images from a database, you should store the image in the WOResourceManager object's application-wide data cache if you know that the image is used more than once. To have the image stored in the cache, set the dynamic element's __key__ attribute. When the key attribute is set, the image is stored in the cache under that key and WOResourceManager tries to retrieve the image from the cache before loading it from the database.

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment13.md)
