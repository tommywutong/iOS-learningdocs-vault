---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/sleepAnddealloc.html
archived_at: '2026-07-15T07:47:32.855165Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](StructureOfInitAwake.md)

# The sleep and dealloc Methods

Complementing __awake__ and __init__, respectively, are the __sleep__ and __dealloc__ methods. These methods let objects deallocate their instance variables and perform other clean-up tasks. The __sleep__ method is invoked at the end of an object's involvement in a transaction. The __dealloc__ method is invoked just before an object is destroyed.

In Objective-C you deallocate instance variables by sending them __release__. In WebScript, on the other hand, all you need to do (in __sleep__) is set the instance variables to __nil__. WebScript has a "garbage-collection" mechanism that automatically disposes of unreferenced objects. For this reason, there's seldom a reason for implementing __dealloc__ in a script.

[!Table of Contents](RunLoop.book.md)
[!Next Section](initOrAwake.md)
