---
title: os_workgroup_interval_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_t.json'
content_hash: 'sha256:045bbf26d101799a'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_interval_t

<sub>类型别名</sub>

支持按重复节奏调度线程的工作组对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef OS_os_workgroup<OS_os_workgroup_interval> * os_workgroup_interval_t;
```

## 讨论

使用 `os_workgroup_interval_create` 函数为你的 app 创建新的间隔工作组。使用该方法返回的工作组来配置组的属性，以及启动、更新和停止间隔工作。你也可以使用 [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) 函数创建对某个工作组的引用。

## 另请参阅

### 间隔任务

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — 在指定时间开始工作组线程的常规执行。
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — 为按固定间隔运行的工作组线程安排新的截止时间。
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — 停止工作组线程当前基于间隔的执行。
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — 包含间隔工作组附加配置数据的不透明结构。
- [os_clockid_t](os_clockid_t.md) — 在间隔工作组中指定时间相关值的方式选项。
