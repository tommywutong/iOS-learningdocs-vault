---
title: 响应电源通知
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/responding-to-power-notifications
source_url: 'https://developer.apple.com/documentation/xcode/responding-to-power-notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/responding-to-power-notifications.json'
content_hash: 'sha256:412a03002806c52c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减少 App 的电池消耗](reducing-your-app-s-battery-use.md)

# 响应电源通知

<sub>文章</sub>

采用更节能的策略来延长设备的电池续航时间。

## 概述

在某些情况下，设备会减少工作量和耗电量。希望延长设备充电间隔时间的用户可以打开低电量模式（Low Power Mode）。设备处于低电量模式时，系统会采取节能措施，包括减少动画，以及延长通过网络获取数据等特定耗电操作之间的间隔时间。

此外，如果系统检测到温度过高，会降低耗电量，直到温度下降。

注册关于电源状态和热状态变化的系统通知，以便采取措施帮助系统节省能量并降低温度。

### 检测并响应电源状态通知

在 App 中注册 [NSProcessInfoPowerStateDidChange](../foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md)，以获知设备的电源状态何时发生变化。收到通知后，查询 [isLowPowerModeEnabled](../foundation/processinfo/islowpowermodeenabled.md) 的值，确定系统是否处于低电量模式。

如果低电量模式处于启用状态，请采取其他措施帮助系统节省能量，包括：

- 暂停所有可选活动
- 减少显示更新
- 尽量减少动画
- 降低网络连接频率
- 停止位置更新

### 检测并响应热状态通知

在 App 中注册 [thermalStateDidChangeNotification](../foundation/processinfo/thermalstatedidchangenotification.md)，以获知设备的热状态何时发生变化。收到通知后，根据 [thermalState](../foundation/processinfo/thermalstate-swift.property.md) 的值调整 App 的行为：

- **[ProcessInfo.ThermalState.nominal](../foundation/processinfo/thermalstate-swift.enum/nominal.md)** — 启用 App 的全部功能。
- **[ProcessInfo.ThermalState.fair](../foundation/processinfo/thermalstate-swift.enum/fair.md)** — 推迟用户不需要立即获得结果的工作，例如后台视频处理。
- **[ProcessInfo.ThermalState.serious](../foundation/processinfo/thermalstate-swift.enum/serious.md)** — 减少网络和定位活动、屏幕更新及动画。
- **[ProcessInfo.ThermalState.critical](../foundation/processinfo/thermalstate-swift.enum/critical.md)** — 为防止设备进一步升温而可能无法使用，请减少或停止 App 正在执行的所有工作。尽量减少计算，并停止或大幅减少对摄像头、蓝牙、定位和其他高耗电子系统的使用。

## 另请参阅

### 基础

- [高效调度 CPU 工作](scheduling-cpu-work-efficiently.md) — 使用并发（concurrency）编程并调整后台活动的优先级，以提升 App 性能。
