---
title: Drawing Performance Guidelines
apple_id: 10000151i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Drawing/Articles/DrawingPerformance.html
archived_at: '2026-07-18T01:47:11.981148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Cocoa%20Drawing%20Tips.md)

# Introduction to Drawing Performance Guidelines

Unless you’re writing a command-line tool, your drawing code is an important area to tune for performance. Your application’s main drawing routines are called frequently to update the content of your windows. The faster these routines do their job, the more time there is for your application to do actual work.

This programming topic describes some basic ways to improve drawing performance in your code.

This programming topic contains the following articles:

- [Cocoa Drawing Tips](Cocoa%20Drawing%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinzqfvbecsskifdeori) provides tips on how to improve the drawing code of Cocoa applications.
- [Measuring Drawing Performance](Measuring%20Drawing%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tklkdjjbeursjirca) shows you how to find poorly performing drawing code in your applications.
- [Flushing to the Window Buffer](Flushing%20to%20the%20Window%20Buffer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzvfvbegskfirduqra) describes issues surrounding the coalesced updates feature.
- [Cocoa Live Window Resizing](Cocoa%20Live%20Window%20Resizing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbufvbecsshireueri) describes techniques for improving performance in live window resizing code for Cocoa applications.
- [Improving NSBezierPath Rendering Times](Improving%20NSBezierPath%20Rendering%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tolkdjjbeursjirca) describes ways to speed up drawing operations involving `NSBezierPath` objects.

[Next](Cocoa%20Drawing%20Tips.md)

