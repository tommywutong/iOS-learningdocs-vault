---
title: os_workgroup_interval_data_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_data_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_data_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_data_t.json'
content_hash: 'sha256:9c2207b4365233fe'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_interval_data_t

<sub>类型别名</sub>

包含间隔工作组附加配置数据的不透明结构。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_workgroup_interval_data_opaque_s * os_workgroup_interval_data_t;
```

## 另请参阅

### 间隔任务

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — 在指定时间开始工作组线程的常规执行。
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — 为按固定间隔运行的工作组线程安排新的截止时间。
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — 停止工作组线程当前基于间隔的执行。
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — 支持按重复节奏调度线程的工作组对象。
- [os_clockid_t](os_clockid_t.md) — 在间隔工作组中指定时间相关值的方式选项。
