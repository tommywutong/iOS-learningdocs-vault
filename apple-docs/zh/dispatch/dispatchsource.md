---
title: DispatchSource
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource.json'
content_hash: 'sha256:4d45ee26d340c811'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSource

<sub>类</sub>

一个用于协调处理特定底层系统事件的对象，例如文件系统事件、定时器和 UNIX 信号。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchSource
```

## 概述

使用此类的方法来构造适当类型的新调度源（dispatch source）。

## 关系

- **继承自**：[DispatchObject](dispatchobject.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[Copyable](../swift/copyable.md)、[DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)、[DispatchSourceMachReceive](dispatchsourcemachreceive.md)、[DispatchSourceMachSend](dispatchsourcemachsend.md)、[DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)、[DispatchSourceProcess](dispatchsourceprocess.md)、[DispatchSourceProtocol](dispatchsourceprotocol.md)、[DispatchSourceRead](dispatchsourceread.md)、[DispatchSourceSignal](dispatchsourcesignal.md)、[DispatchSourceTimer](dispatchsourcetimer.md)、[DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md)、[DispatchSourceUserDataOr](dispatchsourceuserdataor.md)、[DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md)、[DispatchSourceWrite](dispatchsourcewrite.md)、[Equatable](../swift/equatable.md)、[Escapable](../swift/escapable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 管理通用的调度源属性

- [DispatchSourceProtocol](dispatchsourceprotocol.md) — 定义所有调度源类型共享的一组通用属性和方法。

### 创建定时器源

- [makeTimerSource(flags:queue:)](<dispatchsource/maketimersource(flags_queue_).md>) — 创建一个用于监控定时器事件的新调度源对象。
- [DispatchSourceTimer](dispatchsourcetimer.md) — 一种基于定时器提交事件处理程序 block 的调度源。
- [TimerFlags](dispatchsource/timerflags.md) — 配置定时器调度源时使用的标志。

### 创建文件系统源

- [makeReadSource(fileDescriptor:queue:)](<dispatchsource/makereadsource(filedescriptor_queue_).md>) — 创建一个用于从指定文件读取字节的新调度源对象。
- [makeWriteSource(fileDescriptor:queue:)](<dispatchsource/makewritesource(filedescriptor_queue_).md>) — 创建一个用于向指定文件写入数据的新调度源对象。
- [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<dispatchsource/makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) — 创建一个用于监控文件系统事件的新调度源对象。
- [DispatchSourceRead](dispatchsourceread.md) — 一个用于从文件描述符读取数据的调度源对象。
- [DispatchSourceWrite](dispatchsourcewrite.md) — 一个用于向文件描述符写入数据的调度源对象。
- [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md) — 一种监控与文件描述符关联事件的调度源。
- [FileSystemEvent](dispatchsource/filesystemevent.md) — 涉及文件系统对象更改的事件。

### 创建进程源

- [makeProcessSource(identifier:eventMask:queue:)](<dispatchsource/makeprocesssource(identifier_eventmask_queue_).md>) — 创建一个用于监控指定进程的新调度源对象。
- [DispatchSourceProcess](dispatchsourceprocess.md) — 一种监控外部进程事件的调度源。
- [ProcessEvent](dispatchsource/processevent.md) — 与进程相关的事件。

### 创建内存压力源

- [makeMemoryPressureSource(eventMask:queue:)](<dispatchsource/makememorypressuresource(eventmask_queue_).md>) — 创建一个监控系统内存压力状况变化的新调度源对象。
- [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md) — 一种监控系统内存压力状况变化的调度源。
- [MemoryPressureEvent](dispatchsource/memorypressureevent.md) — 内存压力事件。

### 创建信号源

- [makeSignalSource(signal:queue:)](<dispatchsource/makesignalsource(signal_queue_).md>) — 创建一个监控 UNIX 信号到达的新调度源对象。
- [DispatchSourceSignal](dispatchsourcesignal.md) — 一种监控当前进程 UNIX 信号的调度源。

### 创建 Mach 端口源

- [makeMachReceiveSource(port:queue:)](<dispatchsource/makemachreceivesource(port_queue_).md>) — 创建一个用于监控 Mach 端口待处理消息的新调度源对象。
- [makeMachSendSource(port:eventMask:queue:)](<dispatchsource/makemachsendsource(port_eventmask_queue_).md>) — 一种监控 Mach 端口死名称通知的调度源。
- [DispatchSourceMachReceive](dispatchsourcemachreceive.md) — 一种监控 Mach 端口待处理消息的调度源。
- [DispatchSourceMachSend](dispatchsourcemachsend.md) — 一种监控 Mach 端口死名称通知（指示发送权不再有对应的接收权）的调度源。
- [MachSendEvent](dispatchsource/machsendevent.md) — 与 Mach 相关的事件。

### 创建自定义源

- [makeUserDataAddSource(queue:)](<dispatchsource/makeuserdataaddsource(queue_).md>) — 创建一个新的调度源对象，用于使用 AND 操作符合并自定义 App 数据。
- [makeUserDataOrSource(queue:)](<dispatchsource/makeuserdataorsource(queue_).md>) — 创建一个新的调度源对象，用于使用 OR 操作符合并自定义 App 数据。
- [makeUserDataReplaceSource(queue:)](<dispatchsource/makeuserdatareplacesource(queue_).md>) — 创建一个新的调度源对象，用于跟踪自定义 App 数据。
- [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md) — 一种使用 AND 操作符合并你提供的数据的调度源。
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md) — 一种使用 OR 操作符合并你提供的数据的调度源。
- [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md) — 一种用你提供的新值替换任何待处理数据的调度源。

## 另请参阅

### 系统事件监控

- [Dispatch Source](dispatch-source.md) — 一个用于协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [DispatchIO](dispatchio.md) — 一个使用基于流或随机访问语义管理文件描述符操作的对象。
- [DispatchData](dispatchdata.md) — 一个管理基于内存的数据缓冲区并将其暴露为连续内存块的对象。
- [DispatchDataIterator](dispatchdataiterator.md) — 一个对调度数据对象内容进行逐字节迭代的迭代器。
- [Dispatch I/O](dispatch-i-o.md) — 一个使用基于流或随机访问语义管理文件描述符操作的对象。
- [Dispatch Data](dispatch-data.md) — 一个管理基于内存的数据缓冲区并将其暴露为连续内存块的对象。
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — 定义所有调度源类型共享的一组通用属性和方法。
