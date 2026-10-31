---
title: os_workgroup_interval_finish
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_finish
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_finish'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_finish.json'
content_hash: 'sha256:8e5c580dc78e1bee'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_interval_finish

<sub>函数</sub>

停止工作组线程当前基于间隔的执行。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_interval_finish(os_workgroup_interval_t wg, os_workgroup_interval_data_t data);
```

## 参数

- `wg` — 包含一个或多个线程的工作组，其中必须包括当前线程。如果当前线程不属于此工作组，此函数会中止进程。

- `data` — 附加的间隔数据。为此参数指定 `NULL`。

## 返回值

成功时返回 `0`，失败时返回表示失败原因的非零错误码。常见错误码包括 `EINVAL` 或 `EPERM`。例如，若尚未启动该工作组，此方法返回 `EINVAL`。

## 讨论

当你不再需要工作组的线程按固定间隔运行时，调用此函数。例如，当用户的视频播放结束、不再需要解码视频帧时，调用此函数。此函数会把工作组重新置于空闲状态，之后你可以通过调用 [os_workgroup_interval_start](os_workgroup_interval_start.md) 再次启动它。

如果工作组是通过 [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) 或 [os_workgroup_create_with_port](os_workgroup_create_with_port.md) 创建的，此函数会返回错误。此函数仅适用于使用 `os_workgroup_interval_create` 创建的工作组。

## 另请参阅

### 间隔任务

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — 在指定时间开始工作组线程的常规执行。
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — 为按固定间隔运行的工作组线程安排新的截止时间。
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — 支持按重复节奏调度线程的工作组对象。
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — 包含间隔工作组附加配置数据的不透明结构。
- [os_clockid_t](os_clockid_t.md) — 在间隔工作组中指定时间相关值的方式选项。
