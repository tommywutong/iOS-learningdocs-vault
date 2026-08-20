---
title: Code Size Performance Guidelines
apple_id: 10000149i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/CodeFootprint.html
archived_at: '2026-07-18T01:46:40.338874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20the%20Mach-O%20Executable%20Format.md)

# Introduction to Code Size Performance Guidelines

In the context of performance, there is a distinct correlation between memory usage and efficiency. The more memory your application occupies, the more inefficient it is going to be. More memory means more memory allocations, more code, and a greater potential for paging.

The focus of this programming topic is on the reduction of your executable code. Reducing your code footprint is not just a matter of turning on code optimizations in your compiler, although that does help. You can also reduce your code footprint by organizing your code so that only the minimum set of required functions is in memory at any given time. You implement this optimization by profiling your code.

Reducing the amount of memory allocated by your application is also important in reducing your memory footprint; however, that information is covered in _[Memory Usage Performance Guidelines](../Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_ in Performance Documentation.

This programming topic contains the following articles:

- [Overview of the Mach-O Executable Format](Overview%20of%20the%20Mach-O%20Executable%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dalkciffeossfjjbq) describes how to use the organization of the Mach-O executable format to improve the efficiency of your code.
- [Managing Code Size](Managing%20Code%20Size.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dclkdjjbeursjirca) describes several compiler options that you can use to reduce the overall size of your executables.
- [Improving Locality of Reference](Improving%20Locality%20of%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3delkdjjbeursjirca) describes how to profile and reorganize your code to improve loading times for code segments.
- [Reducing Shared Memory Pages](Reducing%20Shared%20Memory%20Pages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dglkdjjbeursjirca) describes ways to reduce the size of your `__DATA` segments.
- [Minimizing Your Exported Symbols](Minimizing%20Your%20Exported%20Symbols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dilkdjjbeursjirca) shows how you identify and eliminate unnecessary symbol information in your code.

[Next](Overview%20of%20the%20Mach-O%20Executable%20Format.md)

