---
title: os_workgroup_interval_start
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_start
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_start'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_start.json'
content_hash: 'sha256:c754a4ad8770fdf5'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_interval_start

<sub>函数</sub>

在指定时间开始工作组线程的常规执行。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_interval_start(os_workgroup_interval_t wg, uint64_t start, uint64_t deadline, os_workgroup_interval_data_t data);
```

## 参数

- `wg` — 包含一个或多个线程的工作组，其中必须包括当前线程。如果当前线程不属于此工作组，此函数会中止进程。

- `start` — 你的线程开始执行与当前截止时间相关的工作时的时间。使用该工作组的时间单位指定此值。可用时间单位列表见 [os_clockid_t](os_clockid_t.md)。

- `deadline` — 你期望线程完成当前间隔任务的理想时间。系统使用此参数评估你的线程是提前、准时还是晚于预期完成。使用该工作组的时间单位指定此值。可用时间单位列表见 [os_clockid_t](os_clockid_t.md)。此值必须大于 `start` 参数中的值。

- `data` — 附加的间隔数据。为此参数指定 `NULL`。

## 返回值

成功时返回 `0`，失败时返回表示失败原因的非零错误码。常见错误码包括 `EINVAL` 或 `EPERM`。例如，若先前已启动或取消了该工作组，此方法返回 `EINVAL`。

## 讨论

在调用此函数之前，先将所有线程加入工作组，并让每个线程开始处理目标任务。仅从一个线程调用此函数，以标记任务开始并设置目标截止时间。当线程完成当前任务后，调用 [os_workgroup_interval_update](os_workgroup_interval_update.md) 开始下一个基于间隔的任务。当线程完成整体任务后，调用 [os_workgroup_interval_finish](os_workgroup_interval_finish.md)，让系统知道你的线程已结束基于间隔的工作。

对每次调用此函数，之后都必须在某个时刻调用一次 [os_workgroup_interval_finish](os_workgroup_interval_finish.md) 与之配对。其间，你可以按需多次调用 [os_workgroup_interval_update](os_workgroup_interval_update.md) 来更新当前间隔的截止时间。例如，在为播放解码视频时，你可能至少每 16.6 毫秒调用一次 [os_workgroup_interval_update](os_workgroup_interval_update.md)。

如果工作组是通过 [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) 或 [os_workgroup_create_with_port](os_workgroup_create_with_port.md) 创建的，此函数会返回错误。此函数仅适用于使用 `os_workgroup_interval_create` 创建的工作组。

## 另请参阅

### 间隔任务

- [os_workgroup_interval_update](os_workgroup_interval_update.md) — 为按固定间隔运行的工作组线程安排新的截止时间。
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — 停止工作组线程当前基于间隔的执行。
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — 支持按重复节奏调度线程的工作组对象。
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — 包含间隔工作组附加配置数据的不透明结构。
- [os_clockid_t](os_clockid_t.md) — 在间隔工作组中指定时间相关值的方式选项。
