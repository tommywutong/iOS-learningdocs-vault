---
title: os_workgroup_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_t.json'
content_hash: 'sha256:56f0f296d6cc6c2c'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_t

<sub>类型别名</sub>

表示当前进程中默认工作组的不透明对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef OS_os_workgroup * os_workgroup_t;
```

## 另请参阅

### 常用实用工具

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — 创建一个绑定到指定工作组的新工作组。
- [os_workgroup_create_with_port](os_workgroup_create_with_port.md) — 创建一个绑定到具有指定 Mach 端口的工作组的新工作组。
- [os_workgroup_copy_port](os_workgroup_copy_port.md) — 返回与该工作组关联的 Mach 端口。
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — 用于存储与工作组相关属性的不透明结构。
