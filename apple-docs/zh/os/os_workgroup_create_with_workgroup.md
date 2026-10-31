---
title: os_workgroup_create_with_workgroup
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_create_with_workgroup
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_create_with_workgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_create_with_workgroup.json'
content_hash: 'sha256:aa85906f79a9b8b2'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_create_with_workgroup

<sub>函数</sub>

创建一个绑定到指定工作组的新工作组。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_workgroup_tos_workgroup_create_with_workgroup(const char *name, os_workgroup_t wg);
```

## 参数

- `name` — 新工作组的可选名称。使用此名称来标识你创建的工作组。此参数可以指定为 `NULL`。

- `wg` — 一个现有的工作组对象。

## 返回值

一个与所提供工作组类型相同、属性相同的新工作组。

## 讨论

使用此函数在你的 App 中为现有工作组创建新的引用。你可能在一个线程上创建原始工作组，并为其他线程创建该工作组的副本。系统会将原始工作组中的线程与任何已复制工作组中的线程当作属于同一组来管理。使用独立的组可避免多个线程需要协调对共享数据结构的访问。

新工作组最初不包含任何已加入的线程，也不包含任何上下文数据。此函数将新工作组的名称设置为 `name` 属性中的值，并配置对 `wg` 参数中原始组的引用。

你不能使用返回的工作组对象对原始工作组进行配置更改。你也不能对该工作组调用任何调度函数。例如，在使用返回的工作组对象时，尝试启动、停止或更新间隔工作组的截止时间会返回错误。相反，请仅使用原始工作组对象进行所有配置和调度调用。

## 另请参阅

### 常用实用工具

- [os_workgroup_create_with_port](os_workgroup_create_with_port.md) — 创建一个绑定到具有指定 Mach 端口的工作组的新工作组。
- [os_workgroup_copy_port](os_workgroup_copy_port.md) — 返回与该工作组关联的 Mach 端口。
- [os_workgroup_t](os_workgroup_t.md) — 表示当前进程中默认工作组的不透明对象。
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — 用于存储与工作组相关属性的不透明结构。
