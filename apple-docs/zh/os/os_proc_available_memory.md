---
title: os_proc_available_memory
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_proc_available_memory
source_url: 'https://developer.apple.com/documentation/os/os_proc_available_memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_proc_available_memory.json'
content_hash: 'sha256:7a5b982f968501c7'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_proc_available_memory

<sub>函数</sub>

确定当前 App 的可用内存量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern size_t os_proc_available_memory();
```

## 返回值

App 在触及内存限制之前还可分配的字节数。如果调用进程不是 App，或者该进程已经超出其内存限制，此函数返回 `0`。

## 讨论

调用此函数以确定你的 App 的可用内存量。返回值等于当前内存限制减去调用时你的 App 的内存占用空间（memory footprint）。你的 App 的内存占用空间由你在 RAM 中分配、且必须始终保留在 RAM（或等效位置）中的数据组成。内存限制会在 App 生命周期中发生变化，且不一定对应于设备上可用的物理内存量。

仅将返回值作为参考性信息使用，不要缓存它。当你的 App 执行任何影响内存的工作时，精确值会发生变化，而这可能频繁发生。

虽然此函数能让你确定你的 App 可安全消耗的内存量，但不要用它来最大化你的 App 的内存用量。显著的内存使用——即使仍低于当前内存限制——也会影响系统性能。例如，当你的 App 耗尽其全部可用内存时，系统可能需要终止其他 App 和系统进程，以满足你的 App 的请求。相反，应始终只消耗响应用户需求所需的最小内存量。

如果你需要关于可用内存资源的更详细信息，可以调用 [task_info](../kernel/1537934-task_info.md)。不过请注意，[task_info](../kernel/1537934-task_info.md) 是一次代价较高的调用，而此函数效率高得多。

## 另请参阅

### 内存

- [os_block_t](os_block_t.md) — 一个不接受参数且无返回值的 block。
- [os_function_t](os_function_t.md) — 指向函数的指针。
- [os_release](os_release-c.func.md)
- [os_retain](os_retain-c.func.md)
