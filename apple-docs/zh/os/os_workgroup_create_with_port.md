---
title: os_workgroup_create_with_port
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_create_with_port
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_create_with_port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_create_with_port.json'
content_hash: 'sha256:097c064cda05d4f0'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_create_with_port

<sub>函数</sub>

创建一个绑定到具有指定 Mach 端口的工作组的新工作组。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_workgroup_tos_workgroup_create_with_port(const char *name, mach_port_t mach_port);
```

## 参数

- `name` — 工作组的可选名称。使用此名称来标识你创建的工作组。此参数可以指定为 `NULL`。

- `mach_port` — 表示内核工作组对象发送权的端口。通常，你从另一个进程获得此端口，该进程使用 [os_workgroup_copy_port](os_workgroup_copy_port.md) 函数创建它。此函数不会消耗该端口发送权的引用。

## 返回值

一个不可变的工作组对象，它引用具有指定端口的工作组。

## 讨论

使用此函数将你的 App 的线程加入到另一个进程中的工作组。进程可以导出其工作组的 Mach 端口，以便将其正在进行的工作与其他进程中的类似工作进行协调。例如，系统的音频 API 会导出工作组，使其他进程能够按与系统相同的时间表提供音频数据。使用此函数可根据提供的端口信息构造一个本地工作组。

此函数返回的工作组是对具有指定端口的工作组的引用。你可以向新创建的工作组添加线程，但不能更改原始组的配置或调度细节。例如，你不能启动、停止或更新间隔工作组的截止时间，若尝试这样做，这些函数会返回错误。相反，拥有原始工作组的进程会处理所有配置和调度细节。

此函数将新工作组的名称设置为 `name` 属性中的值。然后将新工作组配置为对 `wg` 参数中工作组的引用。新创建的工作组最初不包含任何线程，也不包含任何上下文数据。

## 另请参阅

### 常用实用工具

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — 创建一个绑定到指定工作组的新工作组。
- [os_workgroup_copy_port](os_workgroup_copy_port.md) — 返回与该工作组关联的 Mach 端口。
- [os_workgroup_t](os_workgroup_t.md) — 表示当前进程中默认工作组的不透明对象。
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — 用于存储与工作组相关属性的不透明结构。
