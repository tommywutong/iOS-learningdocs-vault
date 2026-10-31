---
title: os_workgroup_interval_update
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_update
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_update'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_update.json'
content_hash: 'sha256:96d4c4d997fa99f0'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_interval_update

<sub>函数</sub>

为按固定间隔运行的工作组线程安排新的截止时间。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_interval_update(os_workgroup_interval_t wg, uint64_t deadline, os_workgroup_interval_data_t data);
```

## 参数

- `wg` — 包含一个或多个线程的工作组，其中必须包括当前线程。如果当前线程不属于此工作组，此函数会中止进程。

- `deadline` — 你期望线程完成当前间隔任务的理想时间。系统使用此参数评估你的线程是提前、准时还是晚于预期完成。使用该工作组的时间单位指定此值。可用时间单位列表见 [os_clockid_t](os_clockid_t.md)。此值必须大于 `start` 参数中的值。

- `data` — 附加的间隔数据。为此参数指定 `NULL`。

## 返回值

成功时返回 `0`，失败时返回表示失败原因的非零错误码。常见错误码包括 `EINVAL` 或 `EPERM`。例如，若尚未启动该工作组，此方法返回 `EINVAL`。

## 讨论

在 [os_workgroup_interval_start](os_workgroup_interval_start.md) 与 [os_workgroup_interval_finish](os_workgroup_interval_finish.md) 的调用之间调用此函数。通常，你会按固定间隔调用它，为任何正在进行的工作设置新的截止时间。例如，在交付当前视频帧的内容之后，调用此函数以设置完成下一视频帧的截止时间。每个新间隔只调用此函数一次。如果工作组包含多个线程，指定一个线程负责启动、停止和更新该组。

如果工作组是通过 [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) 或 [os_workgroup_create_with_port](os_workgroup_create_with_port.md) 创建的，此函数会返回错误。此函数仅适用于使用 `os_workgroup_interval_create` 创建的工作组。

## 另请参阅

### 间隔任务

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — 在指定时间开始工作组线程的常规执行。
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — 停止工作组线程当前基于间隔的执行。
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — 支持按重复节奏调度线程的工作组对象。
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — 包含间隔工作组附加配置数据的不透明结构。
- [os_clockid_t](os_clockid_t.md) — 在间隔工作组中指定时间相关值的方式选项。
