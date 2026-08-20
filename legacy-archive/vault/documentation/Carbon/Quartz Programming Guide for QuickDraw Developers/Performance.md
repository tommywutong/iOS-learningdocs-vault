---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_perf/tq_perf.html
archived_at: '2026-07-15T05:24:40.094753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Document%20Revision%20History.md)[Previous](Offscreen%20Drawing.md)

# Performance

Performance is important to all graphics programs, whether they are based on QuickDraw or Quartz. When you rewrite your application to use only Quartz, you’ll want to pay particular attention to performance issues. Although Quartz optimizes its operations “under the hood,” there are coding practices you can adopt to ensure that your code works in concert with Quartz optimization strategies.

As you develop your application, you can analyze its performance using the debugging tools (Shark, Quartz Debug, Sampler, and so on) provided with Mac OS X. In particular, Quartz Debug is useful for identifying issues related to drawing performance.

Part of adopting good coding practices is to understand how Quartz works. Your code may be performing some task that either isn’t necessary or is working at cross-purposes with Quartz.

Consider following these guidelines:

- Don’t overdraw. Mac OS X v10.4 introduces a coalesced update feature. Quartz draws at a set rate (1/60 sec.) for optimal results. Don’t try to draw faster by flushing or synchronizing. In fact, Quartz enforces deferred updating to prevent you from drawing too fast.
- Make your code cache-friendly. If you keep any Quartz object that you reuse, such as images, layers, colors,and patterns, Quartz notices and caches that object. Cached objects are drawn faster than those that aren’t. Make sure you are not creating, disposing, and recreating the same thing over and over again.
- Use CGLayers for offscreen rendering. They are a better choice from a performance standpoint than bitmap graphics contexts.
- Be kind to the window server by not overflushing. It’s important to understand the difference between the function [CGContextFlush](https://developer.apple.com/documentation/coregraphics/cgcontext/1454895-flush) and the function [CGContextSynchronize](https://developer.apple.com/documentation/coregraphics/cgcontext/1455450-synchronize). The function `CGContextFlush` performs the flush immediately by calling into the window server. (It is not equivalent to `CGContextSynchronize` + `QDFlushPortBuffer`.)

  The purpose of `CGContextSynchronize` is to delay flushing. Synchronizing allows you to draw to the window backing store multiple times using multiple contexts. Given that each flushing operation is synchronized with the beam, you want to minimize the number of flushes (which is what calling the function `CGContextSynchronize` achieves).

For more information, see:

- _[Drawing Performance Guidelines](../../Performance/Drawing%20Performance%20Guidelines/Introduction%20to%20Drawing%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tc2i)_, which describes some basic ways to improve drawing performance in your code, contains specific tips for Carbon and Cocoa, describes how to measure performance, and discusses other issues, such as flushing.
- Quartz Performance: A Look Under the Hood, in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.
- _[CGLayer Reference](https://developer.apple.com/documentation/coregraphics/cglayer)_, which provides a complete reference to the functions that create and manage CGLayer objects.

[Next](Document%20Revision%20History.md)[Previous](Offscreen%20Drawing.md)

