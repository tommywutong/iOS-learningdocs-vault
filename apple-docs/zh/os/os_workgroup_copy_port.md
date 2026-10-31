---
title: os_workgroup_copy_port
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_copy_port
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_copy_port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_copy_port.json'
content_hash: 'sha256:c5b0664290aeac8a'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_copy_port

<sub>函数</sub>

返回与该工作组关联的 Mach 端口。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_copy_port(os_workgroup_t wg, mach_port_t *mach_port_out);
```

## 参数

- `wg` — 你想要其 Mach 端口的工作组。

- `mach_port_out` — 指向 Mach 端口变量的指针。函数返回时，此参数包含指定工作组的 Mach 端口引用。

## 返回值

成功时为 `0`，出错时为非零错误码。

## 讨论

此函数返回内核中该工作组 Mach 端口的发送权。把此端口传给其他进程，并用它在那些进程中构造指向同一工作组的引用，从而使那些进程能够将其线程与 `wg` 参数中工作组的线程进行协调。

## 另请参阅

### 常用实用工具

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — 创建一个绑定到指定工作组的新工作组。
- [os_workgroup_create_with_port](os_workgroup_create_with_port.md) — 创建一个绑定到具有指定 Mach 端口的工作组的新工作组。
- [os_workgroup_t](os_workgroup_t.md) — 表示当前进程中默认工作组的不透明对象。
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — 用于存储与工作组相关属性的不透明结构。
