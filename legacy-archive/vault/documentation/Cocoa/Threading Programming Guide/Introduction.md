---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html
archived_at: '2026-07-15T07:16:46.774022Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](About%20Threaded%20Programming.md)

# 简介

线程是多种可以让单个应用程序内部并发执行多条代码路径的技术之一。虽然诸如操作对象和 Grand Central Dispatch（GCD）这样更新的技术为实现并发提供了更现代、更高效的基础设施，但 OS X 和 iOS 也提供了用于创建和管理线程的接口。

本文档介绍了 OS X 中可用的线程包，并说明了如何使用它们。本文档还描述了用于支持应用程序内多线程编程及多线程代码同步的相关技术。

本文档包含以下章节和附录：

- [关于多线程编程](About%20Threaded%20Programming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedmlktk4za)介绍线程的概念及其在应用程序设计中的作用。
- [线程管理](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknlte)提供了关于 OS X 中多线程技术及其使用方法的信息。
- [运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)提供了关于如何在次线程中管理事件处理循环的信息。
- [同步](Synchronization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqlktk4yq)描述了同步问题，以及用于防止多个线程破坏数据或导致程序崩溃的工具。
- [线程安全总结](Thread%20Safety%20Summary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrnknltc)对 OS X 和 iOS 及其部分关键框架固有的线程安全性做了高层次的总结。

有关线程的替代方案的信息，请参阅 _[并发编程指南](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_。

本文档只对 POSIX 线程 API 的使用做了简略介绍。有关可用 POSIX 线程例程的更多信息，请参阅 [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread) man 页面。有关 POSIX 线程及其用法的更深入说明，请参阅 David R. Butenhof 所著的 _Programming with POSIX Threads_。

[下一页](About%20Threaded%20Programming.md)

