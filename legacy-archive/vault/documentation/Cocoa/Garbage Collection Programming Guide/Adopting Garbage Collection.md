---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcAdoption.html
archived_at: '2026-07-15T07:15:55.979352Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Architecture.md)[Previous](Garbage%20Collection%20for%20Cocoa%20Essentials.md)

# Adopting Garbage Collection

Garbage collection provides trade-offs that you need to consider when choosing whether to adopt the technology.

Potentially, any application that uses a runloop may use garbage collection, however there are issues you should consider when deciding whether it is appropriate for your application. Garbage collection provides several advantages when compared with manual reference counting—although some of these are diminished or negated with Automatic Reference Counting (ARC—see _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_); there are also, though, some disadvantages. The benefits tend to be greater if the application is threaded and has a reasonably large working set; they tend to be less if the latency of memory recovery is important. Moreover, reference-counted and garbage collected applications use a number of different idioms and patterns.

Garbage collection offers some significant advantages over a manually reference-counted environment (as described in _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_):

- Most obviously, it typically simplifies the task of managing memory in your application and obviates most of the memory-related problems that occur, such as retain cycles.
- It reduces the amount of code you have to write and maintain, and may make some aspects of development easier—for example, zeroing weak references facilitate use of objects that may disappear.
- It usually makes it easier to write multi-threaded code: you do not have to use locks to ensure the atomicity of accessor methods and you do not have to deal with per-thread autorelease pools. (Note that although garbage collection simplifies some aspects of multi-threaded programming, it does not automatically make your application thread-safe. For more about thread-safe application development, see _[Threading Programming Guide](../Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_.)

Garbage collection does though have some disadvantages:

- The application’s working set may be larger.
- Performance may not be as good as if you hand-optimize memory management (for more details, see [Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjxfvjvomq)).
- A common design pattern whereby resources are tied to the lifetime of objects does not work effectively under GC.
- You must ensure that for any object you want to be long-lived you maintain a chain of strong references to it from a root object, or resort to reference counting for that object.
- Not all frameworks and technologies support garbage collection; for example, iCloud is not supported in applications that use garbage collection.

The performance characteristics of an application that uses garbage collection are different from those of an application that uses reference-counting. In some areas, a garbage-collected application may have better performance, for example:

- Multi-threaded applications may perform better with garbage collection because of better thread support;
- Accessor methods are much more efficient (you can implement them using simple assignment with no locks);
- Your application is unlikely to have leaks or stale references.

In other areas, however, performance may be worse:

- Allocation may be a significant consideration if your application allocates large numbers of (possibly short-lived) objects.
- The working set may be larger—in particular, the overall heap can grow larger due to allocation outpacing collection.
- The collector scans heap memory to find reachable objects, so by definition keeps the working set hot. This may be a significant consideration, particularly if your application uses a large cache.
- The collector runs in a secondary thread. As such, a GC-enabled application will in almost all cases consume more CPU cycles than a reference-counted application.

When analyzing the performance of a garbage-collected application, you typically need to take a longer-term approach than with a reference-counted application. When assessing its memory footprint, it may be appropriate to measure after the application has been running for several minutes since the memory footprint may be greater shortly after launch. The profiling tools you can use include `heap`, `gdb` flags, and the Instruments application.

[Next](Architecture.md)[Previous](Garbage%20Collection%20for%20Cocoa%20Essentials.md)

