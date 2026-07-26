---
title: 高效访问设备的位置
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/accessing-the-device-s-location-efficiently
source_url: 'https://developer.apple.com/documentation/xcode/accessing-the-device-s-location-efficiently'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/accessing-the-device-s-location-efficiently.json'
content_hash: 'sha256:6bd3f5706b21757d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# 高效访问设备的位置

<sub>文章</sub>

使用 Core Location 特性来管理能耗、接收更新，并将位置更新的频率降到最低。

## 概述

发现一个人所在的位置——尤其是要达到较高的 [desiredAccuracy](../corelocation/cllocationmanager/desiredaccuracy.md)——需要综合多个设备子系统的信息，而这些子系统在工作时都会消耗电量。要把你的 App 请求位置更新的频率降到最低，并且在不需要位置更新时不要让它一直运行。

使用 [CLLocationUpdate](../corelocation/cllocationupdate.md) 来接收系统发出的设备位置变化更新。如果设备静止不动，Core Location 会设置 [stationary](../corelocation/cllocationupdate/stationary.md) 标志，并停止提供更新，直到设备再次移动。发生这种情况时，如果你预计设备短期内不会再次移动，可以考虑停止位置更新，改用 [CLMonitor](../corelocation/clmonitor-2r51v.md) 来在设备位置发生显著变化时获得通知。将 [distanceFilter](../corelocation/cllocationmanager/distancefilter.md) 设置为设备需要移动的距离，系统达到该距离后才会通知你的 App。

如果你需要在 App 处于后台时接收位置更新，请使用 [CLBackgroundActivitySession](../corelocation/clbackgroundactivitysession-3mzv3.md)，或调用 [requestAlwaysAuthorization()](<../corelocation/cllocationmanager/requestalwaysauthorization().md>)。更多信息，请参阅 [Handling location updates in the background](../corelocation/handling-location-updates-in-the-background.md)。不过，只有当你 App 的功能离开后台位置更新就无法运行时，才应注册后台位置更新，因为后台更新会增加你 App 的能耗。

## 另请参阅

### Networking and location

- [Reducing networking and Bluetooth power usage](reducing-networking-and-bluetooth-power-usage.md) — 有策略地安排请求并将后台网络活动降到最低，以降低你 App 的能耗。
