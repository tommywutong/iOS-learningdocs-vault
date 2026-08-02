---
title: Memory Usage Performance Guidelines
apple_id: 10000160i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/ManagingMemory.html
archived_at: '2026-07-18T01:48:56.176004Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20the%20Virtual%20Memory%20System.md)

# Introduction

Memory is an important system resource that all programs use. Programs must be loaded into memory before they can run and, while running, they allocate additional memory (both explicitly and implicitly) to store and manipulate program-level data. Making room in memory for a program’s code and data requires time and resources and therefore affect the overall performance of the system. Although you cannot avoid using memory altogether, there are ways to minimize the impact your memory usage has on the rest of the system.

This document provides background information about the memory systems of OS X and iOS and how you use them efficiently. You can use this information to tune your program’s memory usage by ensuring you are allocating the right amount of memory at the right time. This document also provides tips on how to detect memory-related performance issues in your program.

This programming topic includes the following articles:

- [About the Virtual Memory System](About%20the%20Virtual%20Memory%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dalkcineugskiifba) introduces the terminology and provides a high-level overview of the virtual memory systems of OS X and iOS.
- [Tips for Allocating Memory](Tips%20for%20Allocating%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dclkdjjbegrsei5aq) describes the best techniques for allocating, initializing, and copying memory. It also describes the proper ways to respond to low-memory notifications in iOS.
- [Caching and Purgeable Memory](Caching%20and%20Purgeable%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztcmbufvjvomi) discusses the benefits of caching, and how to avoid some of the problems that can arise from implementing caches. It also details the advantages of implementing purgeable memory into a caching system and how to successfully implement this beneficial technology.
- [Tracking Memory Usage](Tracking%20Memory%20Usage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4delkdjjbeursjirca) describes the tools and techniques for analyzing your application’s memory usage.
- [Finding Memory Leaks](Finding%20Memory%20Leaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dglkdjjbeursjirca) describes the tools and techniques for finding memory leaks in your application.
- [Enabling the Malloc Debugging Features](Enabling%20the%20Malloc%20Debugging%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dilkdjjbeursjirca) describes the environment variables used to enable malloc history logging. You must set some of these variables before using some of the memory analysis tools.
- [Viewing Virtual Memory Usage](Viewing%20Virtual%20Memory%20Usage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dklkdjjbeursjirca) describes the tools and techniques for analyzing your application’s in-memory footprint.

[Next](About%20the%20Virtual%20Memory%20System.md)

