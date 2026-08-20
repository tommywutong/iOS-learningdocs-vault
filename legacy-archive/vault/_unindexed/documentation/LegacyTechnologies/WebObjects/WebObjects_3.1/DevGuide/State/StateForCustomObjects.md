---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StateForCustomObjects.html
archived_at: '2026-07-15T07:47:52.430148Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](CustomStorageOptions.md)

# Storing State for Custom Objects

When state is stored in the server, the objects that hold state are kept intact in memory between transactions. In contrast, when state is stored in the page, in cookies, or in the filesystem, objects are asked to archive themselves before being put into storage. The objects that are part of the WebObjects and Foundation frameworks know how to archive themselves, so require no effort on your part. But if your application has custom classes that need to store state, these classes must know how to archive and unarchive themselves. How you implement archiving for custom classes depends on whether your application makes use of the Enterprise Objects framework and its EOEditingContext class.

[!Table of Contents](ManagingState.book.md)
[!Next Section](UsingEOEditingContext.md)
