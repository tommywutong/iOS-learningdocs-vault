# 模块 4：线程、GCD、Operation、锁与 RunLoop

> 从共享可变状态出发，理解线程、队列、锁、QoS 和事件循环的约束。
> 对应仓库范围：并发与线程、RunLoop 与响应性、性能与调试。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 4.1 | 进程、线程、并发、并行、共享可变状态、竞态条件 | 两段数据竞争代码 + Thread Sanitizer 证据 |
| 4.2 | pthread 与 NSThread：创建、栈、退出、取消、RunLoop 关系，了解层即可 | pthread / NSThread / GCD / Operation 抽象层级表 |
| 4.3 | GCD 核心 API：queue、sync/async、group、semaphore、barrier、work item、source、after、once | 12 个 API 最小实验；串行/并发 × sync/async 结果矩阵 |
| 4.4 | NSOperation / NSOperationQueue：依赖、取消、状态、并发 Operation | 一个可取消、可观察状态的异步 Operation |
| 4.5 | 系统工作线程池、过度并发、QoS、优先级反转 | “队列 ≠ 线程”图；复现 semaphore + QoS 问题 |
| 4.6 | 锁：os_unfair_lock、mutex、recursive lock、rwlock、condition、semaphore、serial queue、atomic | 按“是否睡眠/是否公平/能否递归/读多写少”选锁表 |
| 4.7 | RunLoop、mode、source0/source1、timer、observer、休眠/唤醒 | RunLoop 单轮时序图，不死背固定 mode 列表 |
| 4.8 | RunLoop 应用：常驻线程、timer、滚动模式、腾讯 Matrix 卡顿监控基本思路 | 最小 RunLoop Observer；卡顿监控 observer + stack sampling 图 |
| 4.9 | AutoreleasePool：page、push/pop、ARC 下 autorelease、与 RunLoop 的关系 | 10 万对象循环前后内存曲线；事件循环边界释放图 |

## 计划指定材料

- [关于多线程编程](../../legacy-archive/vault/documentation/Cocoa/Threading%20Programming%20Guide/About%20Threaded%20Programming.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Threading%20Programming%20Guide/About%20Threaded%20Programming.md) — Apple 旧归档
- [线程管理](../../legacy-archive/vault/documentation/Cocoa/Threading%20Programming%20Guide/Thread%20Management.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Threading%20Programming%20Guide/Thread%20Management.md) — Apple 旧归档
- [Operation Queues](../../legacy-archive/vault/documentation/General/Concurrency%20Programming%20Guide/Operation%20Queues.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/General/Concurrency%20Programming%20Guide/Operation%20Queues.md) — Apple 旧归档
- [Operation](../../apple-docs/zh/foundation/operation.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/operation.md) — 本仓库资料
- [OperationQueue](../../apple-docs/zh/foundation/operationqueue.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/operationqueue.md) — 本仓库资料
- [线程安全性总结](../../legacy-archive/vault/documentation/Cocoa/Threading%20Programming%20Guide/Thread%20Safety%20Summary.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Threading%20Programming%20Guide/Thread%20Safety%20Summary.md) — Apple 旧归档
- [运行循环](../../legacy-archive/vault/documentation/Cocoa/Threading%20Programming%20Guide/Run%20Loops.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Threading%20Programming%20Guide/Run%20Loops.md) — Apple 旧归档
- [CFRunLoop](../../apple-docs/zh/corefoundation/cfrunloop.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/corefoundation/cfrunloop.md) — 本仓库资料
- [使用自动释放池块](../../legacy-archive/zh/documentation/Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/Using%20Autorelease%20Pool%20Blocks.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/Using%20Autorelease%20Pool%20Blocks.md) — Apple 旧归档
- [深入理解RunLoop](../../blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) — 本仓库资料
- [计划材料](https://github.com/Tencent/matrix/wiki) — GitHub 源码（待 clone 到 oss/）
- [Low-Level Concurrency APIs](../../blogs/en/objcio/low-level-concurrency-apis.md) · [原文网页](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/) — 第三方博客
- [计划材料](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html) — 第三方博客（未归档（pubs.opengroup.org））
- [计划材料](https://developer.apple.com/documentation/foundation/nsthread) — Apple 现行文档（未归档）
- [计划材料](http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB) — 第三方博客（未归档（stevenwuzheng.com））
- [计划材料](https://bujige.net/blog/iOS-Complete-learning-pthread-and-NSThread.html) — 第三方博客（未归档（bujige.net））
- [Friday Q&A 2016-04-15：常用操作性能对比，2016 版](../../blogs/zh/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md) — 本仓库资料
- [DispatchQueue](../../apple-docs/zh/dispatch/dispatchqueue.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/dispatch/dispatchqueue.md) — 本仓库资料
- [barrier](../../apple-docs/zh/dispatch/dispatchworkitemflags/barrier.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/dispatch/dispatchworkitemflags/barrier.md) — 本仓库资料
- [DispatchSource](../../apple-docs/zh/dispatch/dispatchsource.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/dispatch/dispatchsource.md) — 本仓库资料
- [Common Background Practices](../../blogs/en/objcio/common-background-practices.md) · [原文网页](https://www.objc.io/issues/2-concurrency/common-background-practices/) — 第三方博客
- [Friday Q&A 2015-09-04：让我们来构建 dispatch_queue](../../blogs/zh/mikeash/friday-q-a-2015-09-04-let-s-build-dispatch-queue.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2015-09-04-let-s-build-dispatch-queue.md) — 本仓库资料
- [Friday Q&A 2009-08-28：Grand Central Dispatch 入门（第一部分）：基础与派发队列](../../blogs/zh/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md) — 本仓库资料
- [计划材料](https://blog.devtang.com/2012/02/22/use-gcd/) — 第三方博客（未归档（blog.devtang.com））
- [计划材料](https://ming1016.github.io/2016/01/13/how-to-use-gcd/) — 第三方博客（未归档（ming1016.github.io））
- [计划材料](https://www.cnblogs.com/bbqzsl/p/5287970.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://dirtmelon.github.io/Knowledge/iDev/Multithreading/Grand-Central-Dispatch.html) — 第三方博客（未归档（dirtmelon.github.io））
- [NSOperation](../../blogs/zh/nshipster/nsoperation.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/nshipster/nsoperation.md) — 本仓库资料
- [计划材料](https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html) — 第三方博客（未归档（nsprogrammer.github.io））
- [计划材料](https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios) — 第三方博客（未归档（shakuro.com））
- [计划材料](https://ioscoachfrank.com/chaining-nsoperations.html) — 第三方博客（未归档（ioscoachfrank.com））
- [Introduction](../../legacy-archive/vault/documentation/General/Concurrency%20Programming%20Guide/Introduction.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/General/Concurrency%20Programming%20Guide/Introduction.md) — Apple 旧归档
- [DispatchQoS](../../apple-docs/zh/dispatch/dispatchqos.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/dispatch/dispatchqos.md) — 本仓库资料
- [Concurrent Programming: APIs and Challenges](../../blogs/en/objcio/concurrent-programming-apis-and-challenges.md) · [原文网页](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/) — 第三方博客
- [osunfairlock](../../apple-docs/zh/os/os_unfair_lock.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/os/os_unfair_lock.md) — 本仓库资料
- [Thread-Safe Class Design](../../blogs/en/objcio/thread-safe-class-design.md) · [原文网页](https://www.objc.io/issues/2-concurrency/thread-safe-class-design/) — 第三方博客
- [Friday Q&A 2017-10-27：锁、线程安全与 Swift：2017 版](../../blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) — 本仓库资料
- [计划材料](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/) — 第三方博客（未归档（mjtsai.com））
- [计划材料](https://zhuanlan.zhihu.com/p/587418305) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [计划材料](https://juejin.cn/post/7070416276564213791) — 第三方博客（未归档（juejin.cn））
- [计划材料](https://solarana.dev/2018/04/15/protecting-critical-sections/) — 第三方博客（未归档（solarana.dev））
- [计划材料](https://suelan.github.io/2021/02/13/20210213-dive-into-runloop-ios/) — 第三方博客（未归档（suelan.github.io））
- [计划材料](https://meldstudio.co/blog/macos-cfrunloop-internals-scheduling-high-precision-timers-and-recurring-tasks/) — 第三方博客（未归档（meldstudio.co））
- [计划材料](https://www.jianshu.com/p/aa0fae8c491b) — 第三方博客（未归档（jianshu.com））
- [计划材料](https://www.desgard.com/iOS-Source-Probe/Objective-C/Foundation/Run%20Loop%20%E8%AE%B0%E5%BD%95%E4%B8%8E%E6%BA%90%E7%A0%81%E6%B3%A8%E9%87%8A.html) — 第三方博客（未归档（desgard.com））
- [计划材料](https://cloud.tencent.cn/developer/article/1427933) — 第三方博客（未归档（cloud.tencent.cn））
- [在 iOS 上实现主线程看门狗](../../blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) — 本仓库资料
- [提供高滚动性能](../../blogs/zh/fbeng/delivering-high-scroll-performance.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/fbeng/delivering-high-scroll-performance.md) — 本仓库资料
- [计划材料](https://ai-chan.top/code/Runloop%E4%B8%8E%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7/) — 第三方博客（未归档（ai-chan.top））
- [计划材料](https://cloud.tencent.com/developer/article/1895911) — 第三方博客（未归档（cloud.tencent.com））
- [计划材料](https://github.com/didi/DoKit) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://blog.csdn.net/Deft_MKJing/article/details/82947706) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://jinxuebin.cn/2019/06/AutoReleasePool%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E6%8E%A2%E7%A9%B6/) — 第三方博客（未归档（jinxuebin.cn））
- [计划材料](https://devyang.space/2019/05/05/autoreleasepool/) — 第三方博客（未归档（devyang.space））
- [计划材料](http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/) — 第三方博客（未归档（matteogobbi.github.io））

## 中文资料

共 101 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [Autorelease 实现原理探析](../../blogs/snapshots-zh/matteogobbi.github.io/autorelease-under-the-hood.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/matteogobbi.github.io/autorelease-under-the-hood.md) | 已翻译 |
| 计划核心 | [GCD（Grand Central Dispatch） 介绍](../../blogs/snapshots/ming1016.github.io/%E7%BB%86%E8%AF%B4-gcd-grand-central-dispatch-%E5%A6%82%E4%BD%95%E7%94%A8.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/ming1016.github.io/%E7%BB%86%E8%AF%B4-gcd-grand-central-dispatch-%E5%A6%82%E4%BD%95%E7%94%A8.md) | 原生中文 |
| 计划核心 | [Grand Central Dispatch](../../blogs/snapshots/dirtmelon.github.io/grand-central-dispatch.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/dirtmelon.github.io/grand-central-dispatch.md) | 原生中文 |
| 计划核心 | [iOS 卡顿监测方案总结](../../blogs/snapshots/cloud.tencent.com/ios-%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%B5%8B%E6%96%B9%E6%A1%88%E6%80%BB%E7%BB%93.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cloud.tencent.com/ios-%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%B5%8B%E6%96%B9%E6%A1%88%E6%80%BB%E7%BB%93.md) | 原生中文 |
| 计划核心 | [iOS 多线程：『pthread、NSThread』详尽总结](../../blogs/snapshots/bujige.net/ios-%E5%A4%9A%E7%BA%BF%E7%A8%8B-pthread-nsthread-%E8%AF%A6%E5%B0%BD%E6%80%BB%E7%BB%93.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/bujige.net/ios-%E5%A4%9A%E7%BA%BF%E7%A8%8B-pthread-nsthread-%E8%AF%A6%E5%B0%BD%E6%80%BB%E7%BB%93.md) | 原生中文 |
| 计划核心 | [Matrix-iOS 卡顿监控](../../blogs/snapshots/cloud.tencent.cn/matrix-ios-%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cloud.tencent.cn/matrix-ios-%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7.md) | 原生中文 |
| 计划核心 | [NSOperation 与 NSOperationQueue：提升 iOS 并发 \| Shakuro](../../blogs/snapshots-zh/shakuro.com/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios-shakuro.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/shakuro.com/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios-shakuro.md) | 已翻译 |
| 计划核心 | [NSOperation 子类化](../../blogs/snapshots-zh/nsprogrammer.github.io/nsoperation-subclassing.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/nsprogrammer.github.io/nsoperation-subclassing.md) | 已翻译 |
| 计划核心 | [Objective-C之Autorelease Pool底层实现原理记录（双向链表）以及在Runloop中是如何参与进去的](../../blogs/snapshots/blog.csdn.net/objective-c%E4%B9%8Bautorelease-pool%E5%BA%95%E5%B1%82%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E8%AE%B0%E5%BD%95-%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8-%E4%BB%A5%E5%8F%8A%E5%9C%A8runloop%E4%B8%AD%E6%98%AF%E5%A6%82%E4%BD%95%E5%8F%82%E4%B8%8E%E8%BF%9B%E5%8E%BB%E7%9A%84.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/objective-c%E4%B9%8Bautorelease-pool%E5%BA%95%E5%B1%82%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E8%AE%B0%E5%BD%95-%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8-%E4%BB%A5%E5%8F%8A%E5%9C%A8runloop%E4%B8%AD%E6%98%AF%E5%A6%82%E4%BD%95%E5%8F%82%E4%B8%8E%E8%BF%9B%E5%8E%BB%E7%9A%84.md) | 原生中文 |
| 计划核心 | [OSSpinLock 不安全](../../blogs/snapshots-zh/mjtsai.com/osspinlock-is-unsafe.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/mjtsai.com/osspinlock-is-unsafe.md) | 已翻译 |
| 计划核心 | [Run Loop 记录与源码注释](../../blogs/snapshots/desgard.com/run-loop-%E8%AE%B0%E5%BD%95%E4%B8%8E%E6%BA%90%E7%A0%81%E6%B3%A8%E9%87%8A-%E4%BD%9C%E8%80%85kylin.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/desgard.com/run-loop-%E8%AE%B0%E5%BD%95%E4%B8%8E%E6%BA%90%E7%A0%81%E6%B3%A8%E9%87%8A-%E4%BD%9C%E8%80%85kylin.md) | 原生中文 |
| 计划核心 | [runloop 和线程有什么关系？](../../blogs/snapshots/stevenwuzheng.com/runloop-%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB-stevenwu.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/stevenwuzheng.com/runloop-%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB-stevenwu.md) | 原生中文 |
| 计划核心 | [Runloop 源码笔记：如何实现高可用的卡顿监控](../../blogs/snapshots/ai-chan.top/runloop-%E6%BA%90%E7%A0%81%E7%AC%94%E8%AE%B0-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E9%AB%98%E5%8F%AF%E7%94%A8%E7%9A%84%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/ai-chan.top/runloop-%E6%BA%90%E7%A0%81%E7%AC%94%E8%AE%B0-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E9%AB%98%E5%8F%AF%E7%94%A8%E7%9A%84%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7.md) | 原生中文 |
| 计划核心 | [保护临界区](../../blogs/snapshots-zh/solarana.dev/protecting-critical-sections.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/solarana.dev/protecting-critical-sections.md) | 已翻译 |
| 计划核心 | [前言](../../blogs/snapshots/jianshu.com/%E4%B8%80%E4%BB%BD%E8%B5%B0%E5%BF%83%E7%9A%84runloop%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/%E4%B8%80%E4%BB%BD%E8%B5%B0%E5%BF%83%E7%9A%84runloop%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90.md) | 原生中文 |
| 计划核心 | [对iOS中自旋锁与优先级反转（Priority inversion）的理解](../../blogs/snapshots/juejin.cn/%E5%AF%B9ios%E4%B8%AD%E8%87%AA%E6%97%8B%E9%94%81%E4%B8%8E%E4%BC%98%E5%85%88%E7%BA%A7%E5%8F%8D%E8%BD%AC-priority-inversion-%E7%9A%84%E7%90%86%E8%A7%A3.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/juejin.cn/%E5%AF%B9ios%E4%B8%AD%E8%87%AA%E6%97%8B%E9%94%81%E4%B8%8E%E4%BC%98%E5%85%88%E7%BA%A7%E5%8F%8D%E8%BD%AC-priority-inversion-%E7%9A%84%E7%90%86%E8%A7%A3.md) | 原生中文 |
| 计划核心 | [深入ObjC GCD中的dispatch group工作原理。](../../blogs/snapshots/cnblogs.com/%E6%B7%B1%E5%85%A5objc-gcd%E4%B8%AD%E7%9A%84dispatch-group%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/%E6%B7%B1%E5%85%A5objc-gcd%E4%B8%AD%E7%9A%84dispatch-group%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [深入理解 CFRunLoop](../../blogs/snapshots-zh/suelan.github.io/dive-into-cfrunloop.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/suelan.github.io/dive-into-cfrunloop.md) | 已翻译 |
| 官方资料 | [AtomicOptionalRepresentable 实现](../../apple-docs/zh/swift/unsafepointer/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/unsafepointer/atomicoptionalrepresentable-implementations.md) | 已翻译 |
| 官方资料 | [AtomicRepresentable 实现](../../apple-docs/zh/swift/int8/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/int8/atomicrepresentable-implementations.md) | 已翻译 |
| 官方资料 | [Dispatch 信号量](../../apple-docs/zh/dispatch/dispatch-semaphore.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-semaphore.md) | 已翻译 |
| 官方资料 | [Dispatch 函数](../../apple-docs/zh/dispatch/dispatch-functions.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-functions.md) | 已翻译 |
| 官方资料 | [Dispatch 函数原型](../../apple-docs/zh/objectivec/dispatch-function-prototypes.md) | Apple 文档 | Apple · Objective-C Runtime | [中文](../../apple-docs/zh/objectivec/dispatch-function-prototypes.md) | 已翻译 |
| 官方资料 | [Dispatch 对象](../../apple-docs/zh/dispatch/dispatch-objects.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-objects.md) | 已翻译 |
| 官方资料 | [Dispatch 屏障](../../apple-docs/zh/dispatch/dispatch-barrier.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-barrier.md) | 已翻译 |
| 官方资料 | [Dispatch 工作项](../../apple-docs/zh/dispatch/dispatch-work-item.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-work-item.md) | 已翻译 |
| 官方资料 | [Dispatch 常量](../../apple-docs/zh/dispatch/dispatch-constants.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-constants.md) | 已翻译 |
| 官方资料 | [Dispatch 数据](../../apple-docs/zh/dispatch/dispatch-data.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-data.md) | 已翻译 |
| 官方资料 | [Dispatch 数据类型](../../apple-docs/zh/dispatch/dispatch-data-types.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-data-types.md) | 已翻译 |
| 官方资料 | [Dispatch 源](../../apple-docs/zh/dispatch/dispatch-source.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-source.md) | 已翻译 |
| 官方资料 | [Dispatch 组](../../apple-docs/zh/dispatch/dispatch-group.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-group.md) | 已翻译 |
| 官方资料 | [Dispatch 输入输出（I/O）](../../apple-docs/zh/dispatch/dispatch-i-o.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-i-o.md) | 已翻译 |
| 官方资料 | [Dispatch 队列](../../apple-docs/zh/dispatch/dispatch-queue.md) | Apple 文档 | Apple · Dispatch | [中文](../../apple-docs/zh/dispatch/dispatch-queue.md) | 已翻译 |
| 官方资料 | [使用 GPU 计数器分析绘制命令和计算调度性能](../../apple-docs/zh/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) | 已翻译 |
| 官方资料 | [使用管线统计信息分析绘制命令和计算调度性能](../../apple-docs/zh/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) | 已翻译 |
| 官方资料 | [创建线程（Thread）与线程组（Threadgroup）](../../apple-docs/zh/metal/creating-threads-and-threadgroups.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/creating-threads-and-threadgroups.md) | 已翻译 |
| 官方资料 | [原子操作](../../apple-docs/zh/kernel/libkern/atomic_operations.md) | Apple 文档 | Apple · Kernel | [中文](../../apple-docs/zh/kernel/libkern/atomic_operations.md) | 已翻译 |
| 官方资料 | [在 Swift 6 App 中采用严格并发](../../apple-docs/zh/swift/adoptingswift6.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/adoptingswift6.md) | 已翻译 |
| 官方资料 | [处理并发](../../apple-docs/zh/security/working-with-concurrency.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/working-with-concurrency.md) | 已翻译 |
| 官方资料 | [尽早诊断内存、线程和崩溃问题](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | 已翻译 |
| 官方资料 | [并发](../../apple-docs/zh/swift/concurrency.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/concurrency.md) | 已翻译 |
| 官方资料 | [并发支持](../../apple-docs/zh/swiftdata/concurrencysupport.md) | Apple 文档 | Apple · SwiftData | [中文](../../apple-docs/zh/swiftdata/concurrencysupport.md) | 已翻译 |
| 官方资料 | [更新 App 以使用 Swift 并发](../../apple-docs/zh/swift/updating_an_app_to_use_swift_concurrency.md) | Apple 文档 | Apple · swift | [中文](../../apple-docs/zh/swift/updating_an_app_to_use_swift_concurrency.md) | 已翻译 |
| 官方资料 | [更新 App 以使用严格并发](../../apple-docs/zh/swift/updating-an-app-to-use-strict-concurrency.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/updating-an-app-to-use-strict-concurrency.md) | 已翻译 |
| 官方资料 | [线程泄漏](../../apple-docs/zh/xcode/thread-leaks.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/thread-leaks.md) | 已翻译 |
| 官方资料 | [调试绘制命令或计算调度中的着色器](../../apple-docs/zh/xcode/debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) | 已翻译 |
| 官方资料 | [进程与线程](../../apple-docs/zh/foundation/processes-and-threads.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/processes-and-threads.md) | 已翻译 |
| 官方资料 | [锁](../../apple-docs/zh/kernel/iokit_fundamentals/locks.md) | Apple 文档 | Apple · Kernel | [中文](../../apple-docs/zh/kernel/iokit_fundamentals/locks.md) | 已翻译 |
| 官方资料 | [随堂编码：借助 Swift 并发提升 App](../../apple-docs/zh/swift/code-along-elevating-an-app-with-swift-concurrency.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/code-along-elevating-an-app-with-swift-concurrency.md) | 已翻译 |
| 官方资料 | [Swift 并发：更新示例 App](../../wwdc/zh/wwdc2021/10194-swift-concurrency-update-a-sample-app.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10194-swift-concurrency-update-a-sample-app.md) | 已翻译 |
| 官方资料 | [Swift 并发：深入幕后](../../wwdc/zh/wwdc2021/10254-swift-concurrency-behind-the-scenes.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10254-swift-concurrency-behind-the-scenes.md) | 已翻译 |
| 官方资料 | [使用 Swift 并发消除数据争用](../../wwdc/zh/wwdc2022/110351-eliminate-data-races-using-swift-concurrency.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/110351-eliminate-data-races-using-swift-concurrency.md) | 已翻译 |
| 官方资料 | [可视化与优化 Swift 并发](../../wwdc/zh/wwdc2022/110350-visualize-and-optimize-swift-concurrency.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/110350-visualize-and-optimize-swift-concurrency.md) | 已翻译 |
| 官方资料 | [在 Network framework 中使用结构化并发](../../wwdc/zh/wwdc2025/250-use-structured-concurrency-with-network-framework.md) | WWDC | Apple · WWDC2025 | [中文](../../wwdc/zh/wwdc2025/250-use-structured-concurrency-with-network-framework.md) | 已翻译 |
| 官方资料 | [在 Swift 3 中使用 GCD 进行并发编程](../../wwdc/zh/wwdc2016/720-concurrent-programming-with-gcd-in-swift-3.md) | WWDC | Apple · WWDC2016 | [中文](../../wwdc/zh/wwdc2016/720-concurrent-programming-with-gcd-in-swift-3.md) | 已翻译 |
| 官方资料 | [在 SwiftUI 中探索并发](../../wwdc/zh/wwdc2021/10019-discover-concurrency-in-swiftui.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10019-discover-concurrency-in-swiftui.md) | 已翻译 |
| 官方资料 | [将 Core Data 并发引入 Swift 和 SwiftUI](../../wwdc/zh/wwdc2021/10017-bring-core-data-concurrency-to-swift-and-swiftui.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10017-bring-core-data-concurrency-to-swift-and-swiftui.md) | 已翻译 |
| 官方资料 | [拥抱 Swift 并发](../../wwdc/zh/wwdc2025/268-embracing-swift-concurrency.md) | WWDC | Apple · WWDC2025 | [中文](../../wwdc/zh/wwdc2025/268-embracing-swift-concurrency.md) | 已翻译 |
| 官方资料 | [探索 Swift 中的结构化并发](../../wwdc/zh/wwdc2021/10134-explore-structured-concurrency-in-swift.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10134-explore-structured-concurrency-in-swift.md) | 已翻译 |
| 官方资料 | [探索 SwiftUI 中的并发](../../wwdc/zh/wwdc2025/266-explore-concurrency-in-swiftui.md) | WWDC | Apple · WWDC2025 | [中文](../../wwdc/zh/wwdc2025/266-explore-concurrency-in-swiftui.md) | 已翻译 |
| 官方资料 | [深入理解结构化并发](../../wwdc/zh/wwdc2023/10170-beyond-the-basics-of-structured-concurrency.md) | WWDC | Apple · WWDC2023 | [中文](../../wwdc/zh/wwdc2023/10170-beyond-the-basics-of-structured-concurrency.md) | 已翻译 |
| 官方资料 | [现代化 Grand Central Dispatch 用法](../../wwdc/zh/wwdc2017/706-modernizing-grand-central-dispatch-usage.md) | WWDC | Apple · WWDC2017 | [中文](../../wwdc/zh/wwdc2017/706-modernizing-grand-central-dispatch-usage.md) | 已翻译 |
| 深度补充 | [GCD 不是 Block，Block 不是 GCD](../../blogs/zh/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md) | 已翻译 |
| 深度补充 | [俄语中的 Blocks 和 GCD](../../blogs/zh/mikeash/blocks-and-gcd-in-russian.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/blocks-and-gcd-in-russian.md) | 已翻译 |
| 深度补充 | [关于 Swift 中锁和线程安全的文章](../../blogs/zh/mikeash/an-article-about-locks-and-thread-safety-in-swift.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/an-article-about-locks-and-thread-safety-in-swift.md) | 已翻译 |
| 深度补充 | [内存和线程安全的自定义属性方法 \| Cocoa with Love](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [安全的线程化设计与线程间通信](../../blogs/zh/cocoawithlove/safe-threaded-design-and-inter-thread-communication-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/safe-threaded-design-and-inter-thread-communication-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [常见操作的性能比较](../../blogs/zh/mikeash/performance-comparisons-of-common-operations.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/performance-comparisons-of-common-operations.md) | 已翻译 |
| 深度补充 | [常见操作的性能比较，iPhone 版](../../blogs/zh/mikeash/performance-comparisons-of-common-operations-iphone-edition.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/performance-comparisons-of-common-operations-iphone-edition.md) | 已翻译 |
| 深度补充 | [常见操作的性能比较，Leopard 版](../../blogs/zh/mikeash/performance-comparisons-of-common-operations-leopard-edition.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/performance-comparisons-of-common-operations-leopard-edition.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-08-28：Grand Central Dispatch 入门，第一部分：基础与 Dispatch Queues](../../blogs/zh/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-09-04：Grand Central Dispatch 入门，第二部分：多核性能](../../blogs/zh/mikeash/friday-q-a-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-09-04-intro-to-grand-central-dispatch-part-ii-multi-core-performance.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-09-11：Grand Central Dispatch 入门，第三部分：Dispatch Sources](../../blogs/zh/mikeash/friday-q-a-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-09-18：Grand Central Dispatch 入门，第四部分：杂项](../../blogs/zh/mikeash/friday-q-a-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-09-18-intro-to-grand-central-dispatch-part-iv-odds-and-ends.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-09-25：GCD 实践](../../blogs/zh/mikeash/friday-q-a-2009-09-25-gcd-practicum.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-09-25-gcd-practicum.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-12-11：一个 GCD 案例研究：构建 HTTP 服务器](../../blogs/zh/mikeash/friday-q-a-2009-12-11-a-gcd-case-study-building-an-http-server.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-12-11-a-gcd-case-study-building-an-http-server.md) | 已翻译 |
| 深度补充 | [星期五问答 2010-01-01：NSRunLoop 内部机制](../../blogs/zh/mikeash/friday-q-a-2010-01-01-nsrunloop-internals.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2010-01-01-nsrunloop-internals.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-03-04：OSAtomic 漫游](../../blogs/zh/mikeash/friday-q-a-2011-03-04-a-tour-of-osatomic.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-03-04-a-tour-of-osatomic.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-10-14：GCD 的新特性](../../blogs/zh/mikeash/friday-q-a-2011-10-14-what-s-new-in-gcd.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-10-14-what-s-new-in-gcd.md) | 已翻译 |
| 深度补充 | [星期五问答 2013-08-16：让我们构建 Dispatch Groups](../../blogs/zh/mikeash/friday-q-a-2013-08-16-let-s-build-dispatch-groups.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2013-08-16-let-s-build-dispatch-groups.md) | 已翻译 |
| 深度补充 | [星期五问答 2015-05-29：Objective-C 运行时的并发内存释放](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 已翻译 |
| 深度补充 | [星期五问答 2016-04-15：常见操作性能比较（2016 版）](../../blogs/zh/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md) | 已翻译 |
| 深度补充 | [星期五问答 2017-10-27：锁、线程安全与 Swift：2017 版](../../blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) | 已翻译 |
| 深度补充 | [死锁与锁顺序：一则小品](../../blogs/zh/mikeash/deadlocks-and-lock-ordering-a-vignette.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/deadlocks-and-lock-ordering-a-vignette.md) | 已翻译 |
| 深度补充 | [深入理解RunLoop](../../blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) | 技术博客 | ibireme (郭曜源) | [中文](../../blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) | 原生中文 |
| 深度补充 | [生成线程的开销（性能实验） \| Cocoa with Love](../../blogs/zh/cocoawithlove/the-overhead-of-spawning-threads-a-performance-experiment-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/the-overhead-of-spawning-threads-a-performance-experiment-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Swift 并发编程现状和展望 - async/await 和参与者模式](../../blogs/zh/onevcat/swift-%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E7%8E%B0%E7%8A%B6%E5%92%8C%E5%B1%95%E6%9C%9B-async-await-%E5%92%8C%E5%8F%82%E4%B8%8E%E8%80%85%E6%A8%A1%E5%BC%8F.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/swift-%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E7%8E%B0%E7%8A%B6%E5%92%8C%E5%B1%95%E6%9C%9B-async-await-%E5%92%8C%E5%8F%82%E4%B8%8E%E8%80%85%E6%A8%A1%E5%BC%8F.md) | 原生中文 |
| 补充资料 | [[objc 解析]: 单形分发](../../blogs/zh/sealiesoftware/objc-explain-monomorphic-dispatch.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-monomorphic-dispatch.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 线程本地垃圾回收](../../blogs/zh/sealiesoftware/objc-explain-thread-local-garbage-collection.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-thread-local-garbage-collection.md) | 已翻译 |
| 补充资料 | [Core Data 并发调试](../../blogs/zh/oleb/core-data-concurrency-debugging.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/core-data-concurrency-debugging.md) | 已翻译 |
| 补充资料 | [OSAtomic原子操作](../../blogs/zh/southpeak/osatomic%E5%8E%9F%E5%AD%90%E6%93%8D%E4%BD%9C.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/osatomic%E5%8E%9F%E5%AD%90%E6%93%8D%E4%BD%9C.md) | 原生中文 |
| 补充资料 | [Swift 全局变量和静态成员是原子性的且延迟计算](../../blogs/zh/jessesquires/swift-globals-and-static-members-are-atomic-and-lazily-computed.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/swift-globals-and-static-members-are-atomic-and-lazily-computed.md) | 已翻译 |
| 补充资料 | [Swift 并发不等待任何人](../../blogs/zh/saagarjha/swift-concurrency-waits-for-no-one.md) | 技术博客 | Saagar Jha | [中文](../../blogs/zh/saagarjha/swift-concurrency-waits-for-no-one.md) | 已翻译 |
| 补充资料 | [UIKit DiffableDataSource API 与 Swift Concurrency 注解的不一致性解析](../../blogs/zh/jessesquires/uikit-diffabledatasource-api-inconsistencies-with-swift-concurrency-annotations-explained.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/uikit-diffabledatasource-api-inconsistencies-with-swift-concurrency-annotations-explained.md) | 已翻译 |
| 补充资料 | [为 Instagram 和 Threads 带来 HDR 照片支持](../../blogs/zh/fbeng/bringing-hdr-photo-support-to-instagram-and-threads.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/bringing-hdr-photo-support-to-instagram-and-threads.md) | 已翻译 |
| 补充资料 | [传递非 Sendable 闭包的 Swift 并发黑科技](../../blogs/zh/jessesquires/swift-concurrency-hack-for-passing-non-sendable-closures.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/swift-concurrency-hack-for-passing-non-sendable-closures.md) | 已翻译 |
| 补充资料 | [协议扩展中的方法派发](../../blogs/zh/oleb/method-dispatch-in-protocol-extensions.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/method-dispatch-in-protocol-extensions.md) | 已翻译 |
| 补充资料 | [在 iOS 上实现主线程看门狗](../../blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/implementing-a-main-thread-watchdog-on-ios.md) | 已翻译 |
| 补充资料 | [我们如何看待 Threads 的 iOS 性能](../../blogs/zh/fbeng/how-we-think-about-threads-ios-performance.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/how-we-think-about-threads-ios-performance.md) | 已翻译 |
| 补充资料 | [用 GCD 并行化你的 for 循环](../../blogs/zh/oleb/parallelize-your-for-loops-with-gcd.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/parallelize-your-for-loops-with-gcd.md) | 已翻译 |
| 补充资料 | [线程局部存储详解](../../blogs/zh/maskray/all-about-thread-local-storage.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/all-about-thread-local-storage.md) | 已翻译 |

## 未翻译资料

共 49 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [常见的后台处理实践](../../blogs/en/objcio/common-background-practices.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/common-background-practices.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [并发编程：API 与挑战](../../blogs/en/objcio/concurrent-programming-apis-and-challenges.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/concurrent-programming-apis-and-challenges.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [底层并发 API](../../blogs/en/objcio/low-level-concurrency-apis.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/low-level-concurrency-apis.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [线程安全的类设计](../../blogs/en/objcio/thread-safe-class-design.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/thread-safe-class-design.md) | 仅标题中文，正文待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/unsafemutablepointer/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablepointer/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/objectidentifier/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/objectidentifier/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/unsafemutablerawpointer/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablerawpointer/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/opaquepointer/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/opaquepointer/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/unmanaged/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unmanaged/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicOptionalRepresentable Implementations](../../apple-docs/en/swift/unsaferawpointer/atomicoptionalrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsaferawpointer/atomicoptionalrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint64/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint64/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint8/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint8/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/int16/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int16/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafemutablepointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablepointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/objectidentifier/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/objectidentifier/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafemutablerawpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablerawpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/never/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/never/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/int32/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int32/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafebufferpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafebufferpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/float16/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/float16/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/optional/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/optional/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint32/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint32/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/int/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsaferawbufferpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsaferawbufferpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/float/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/float/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/bool/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/bool/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafemutablerawbufferpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablerawbufferpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafepointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafepointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/opaquepointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/opaquepointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unmanaged/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unmanaged/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/double/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/double/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/int64/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int64/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/duration/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/duration/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint16/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint16/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/uint128/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint128/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsaferawpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsaferawpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/unsafemutablebufferpointer/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/unsafemutablebufferpointer/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/swift/int128/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int128/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [AtomicRepresentable Implementations](../../apple-docs/en/synchronization/wordpair/atomicrepresentable-implementations.md) | Apple 文档 | Apple · Synchronization | [英文](../../apple-docs/en/synchronization/wordpair/atomicrepresentable-implementations.md) | 待翻译 |
| 官方资料 | [CFRunLoopRunInMode Exit Codes](../../apple-docs/en/corefoundation/cfrunloopruninmode_exit_codes.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/cfrunloopruninmode_exit_codes.md) | 待翻译 |
| 官方资料 | [Dispatch](../../apple-docs/en/dispatch.md) | Apple 文档 | Apple · Dispatch | [英文](../../apple-docs/en/dispatch.md) | 待翻译 |
| 官方资料 | [Specifying drawing and dispatch arguments indirectly](../../apple-docs/en/metal/specifying-drawing-and-dispatch-arguments-indirectly.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/specifying-drawing-and-dispatch-arguments-indirectly.md) | 待翻译 |
| 深度补充 | [在 Swift 中优化写时复制的双端队列 \| Cocoa with Love](../../blogs/en/cocoawithlove/optimizing-a-copy-on-write-double-ended-queue-in-swift-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/optimizing-a-copy-on-write-double-ended-queue-in-swift-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [星期五问答 2009-04-10：ChemicalBurn 中的多线程优化](../../blogs/en/mikeash/friday-q-a-2009-04-10-multithreaded-optimization-in-chemicalburn.md) | 技术博客 | mikeash.com Friday Q&A | [英文](../../blogs/en/mikeash/friday-q-a-2009-04-10-multithreaded-optimization-in-chemicalburn.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试并发应用](../../blogs/en/objcio/testing-concurrent-applications.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/testing-concurrent-applications.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [2018 年 11 月 2 日 React Conf 回顾：Hooks、Suspense 和 Concurrent Rendering](../../blogs/en/fbeng/nov-02-2018-react-conf-recap-hooks-suspense-and-concurrent-rendering.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/nov-02-2018-react-conf-recap-hooks-suspense-and-concurrent-rendering.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Meta 如何在 5 个月内构建 Threads](../../blogs/en/fbeng/how-meta-built-threads-in-5-months.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/how-meta-built-threads-in-5-months.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [没有所谓的“隐式原子”](../../blogs/en/belkadan/there-s-no-such-thing-as-implicitly-atomic.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [英文](../../blogs/en/belkadan/there-s-no-such-thing-as-implicitly-atomic.md) | 仅标题中文，正文待翻译 |
