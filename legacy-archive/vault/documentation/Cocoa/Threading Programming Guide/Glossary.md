---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Glossary/Glossary.html
archived_at: '2026-07-15T07:16:46.767076Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [多线程编程指南](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Thread%20Safety%20Summary.md)

# 术语表

- __application__

  一种特定风格的[程序](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmznknltg)，用于向用户显示图形界面。

- __condition__

  一种用于同步访问某个资源的构造。等待条件的线程在另一个线程显式发出该条件的信号之前，不允许继续执行。

- __critical section__

  一段一次只能由一个线程执行的代码。

- __input source__

  线程异步事件的来源。输入源可以是基于端口的，也可以是手动触发的，并且必须附加到线程的运行循环上。

- __joinable thread__

  一种在终止后不会立即回收其资源的线程。可合并线程必须先被显式分离，或者被另一个线程合并，然后才能回收其资源。可合并线程会向与其合并的线程提供一个返回值。

- __main thread__

  一种特殊类型的[线程](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmznknltc)，在其所属进程被创建时一并创建。当程序的主线程退出时，进程也随之结束。

- __mutex__

  一种为共享资源提供互斥访问的锁。互斥锁一次只能被一个线程持有。尝试获取被另一个线程持有的互斥锁，会使当前线程进入休眠，直到最终获得该锁为止。

- __operation object__

  [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) 类的实例。操作对象把与某项任务相关的代码和数据封装成一个可执行单元。

- __operation queue__

  [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue) 类的实例。操作队列管理操作对象的执行。

- __process__

  应用程序或程序的运行时实例。进程拥有自己的虚拟内存空间和系统资源（包括端口权限），这些资源独立于分配给其他程序的资源。一个进程总是至少包含一个线程（主线程），也可能包含任意数量的额外线程。

- __program__

  代码和资源的组合，可以运行以执行某项任务。程序不必具有图形用户界面，不过图形应用程序也被视为程序。

- __recursive lock__

  一种可被同一线程多次加锁的锁。

- __run loop__

  一种事件处理循环，在此循环中接收事件并将其分派给相应的处理程序。

- __run loop mode__

  与特定名称关联的一组输入源、定时器源和运行循环观察者的集合。当以特定"模式"运行时，运行循环只会监视与该模式关联的源和观察者。

- __run loop object__

  [NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop) 类或 [CFRunLoopRef](https://developer.apple.com/documentation/corefoundation/cfrunloopref) 不透明类型的实例。这些对象为在线程中实现事件处理循环提供了接口。

- __run loop observer__

  在运行循环执行的不同阶段接收通知的接收者。

- __semaphore__

  一种限制对共享资源访问的受保护变量。互斥锁和条件都是不同类型的信号量。

- __task__

  待执行的一定量的工作。

- __thread__

  进程中的一条执行流。每个线程都有自己的栈空间，但除此之外与同一进程中的其他线程共享内存。

- __timer source__

  线程同步事件的来源。定时器会在预定的未来时间生成一次性或重复性事件。

[下一页](Document%20Revision%20History.md)[上一页](Thread%20Safety%20Summary.md)

