---
title: 工作流与控制
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/iokit_fundamentals/workflow_and_control
source_url: 'https://developer.apple.com/documentation/kernel/iokit_fundamentals/workflow_and_control'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/iokit_fundamentals/workflow_and_control.json'
content_hash: 'sha256:b3bd7525e13345b3'
translated: true
---

> 导航：[技术](../../technologies.md) · [Kernel](../../kernel.md) · [IOKit 基础知识](../iokit_fundamentals.md)

# 工作流与控制

<sub>API 集合</sub>

## 主题

### 工作循环

- [IOWorkLoop](../ioworkloop.md)

### 定时器

- [IOTimerEventSource](../iotimereventsource.md) — 基于时间的事件源机制。
- [IOWatchDogTimer](../iowatchdogtimer.md)
- [IOGetTime](../1575332-iogettime.md) _(已废弃)_
- [IOTimeStampConstant](../1535203-iotimestampconstant.md)
- [IOTimeStampEndConstant](../1535232-iotimestampendconstant.md)
- [IOTimeStampStartConstant](../1535234-iotimestampstartconstant.md)

### 休眠

- [IODelay](../1575328-iodelay.md) — 自旋延迟指定微秒数。
- [IOPause](../1575333-iopause.md) — 自旋延迟指定纳秒数。
- [IOSleep](../1575320-iosleep.md) — 将调用线程休眠指定毫秒数。
- [IOSleepWithLeeway](../1575303-iosleepwithleeway.md)

### 调度队列

- [IODispatchQueueInterface](../iodispatchqueueinterface.md)
- [IODispatchSourceInterface](../iodispatchsourceinterface.md)
- [IODispatchQueue](../iodispatchqueue.md)

### 数据队列

- [IODataQueueDispatchSource](../iodataqueuedispatchsource.md)
- [IODataQueueDispatchSourceInterface](../iodataqueuedispatchsourceinterface.md)
- [IODataQueue](../iodataqueue.md) — 一个通用的队列，用于将数据从内核传递到用户进程。

### 输出队列

- [IOGatedOutputQueue](../iogatedoutputqueue.md) — IOBasicOutputQueue 的扩展（extension）。
- [IOBasicOutputQueue](../iobasicoutputqueue.md) — IOOutputQueue 的一个具体实现。
- [IOOutputQueue](../iooutputqueue.md) — 一个支持多个生产者与单个消费者的数据包队列。

### 通知

- [IOServiceNotificationDispatchSource](../ioservicenotificationdispatchsource.md)
- [IOServiceNotificationDispatchSourceInterface](../ioservicenotificationdispatchsourceinterface.md)
- [IONotifier](../ionotifier.md) — 一个抽象基类，定义了控制（control）通知请求的通用方法。

### 中断

- [IOInterruptDispatchSource](../iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](../iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](../iofilterinterrupteventsource.md) — $link IOInterruptEventSource 的过滤变体。
- [IOInterruptEventSource](../iointerrupteventsource.md) — 用于向基于工作循环的驱动传递中断的事件源。
- [IOInterruptController](../iointerruptcontroller.md)
- [PassthruInterruptController](../passthruinterruptcontroller.md)
- [IOInterruptSource](../iointerruptsource.md)
- [IOInterruptVector](../iointerruptvector.md)

### 基础类型

- [IOCommandPool](../iocommandpool.md) — 操作继承自 IOCommand 的命令池。
- [IOCommandGate](../iocommandgate.md) — 单线程的工作循环客户端请求机制。
- [IOCommand](../iocommand.md) — 此类是一个抽象类，表示一个 I/O 命令。
- [IODispatchSource](../iodispatchsource.md)
- [IOEventSource](../ioeventsource.md) — 所有工作循环事件源的抽象类。

## 另请参阅

### 相关资源

- [内存](memory.md) — 在内核中分配、映射、释放和管理内存。 
- [锁](locks.md)
- [数据类型](../libkern/data_types.md) — 创建由驱动程序和内核扩展所使用的字符串、数字、集合（collection）、数据对象和其他标准类型。
