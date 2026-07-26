---
title: 降低网络和蓝牙的功耗
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-networking-and-bluetooth-power-usage
source_url: 'https://developer.apple.com/documentation/xcode/reducing-networking-and-bluetooth-power-usage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-networking-and-bluetooth-power-usage.json'
content_hash: 'sha256:2985f98a5f65c8bf'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# 降低网络和蓝牙的功耗

<sub>文章</sub>

有策略地安排请求并将后台网络活动降到最低，以降低你 App 的能耗。

## 概述

通过选择合适的网络技术、批量处理连接，以及在发起请求前等待合适的网络条件，降低你 App 在通信相关任务中消耗的电量。

### 选择合适的网络框架

你对网络框架的选择会直接影响你 App 的能耗。使用 [URLSession](../foundation/urlsession.md) 发送 HTTP 请求，因为它内置了连接池和智能调度等省电优化。如需更底层的网络访问，请使用 [Network](../network.md) 框架，它提供了高能效的协议，并让你能够控制连接的时机。

`URLSession` 和 Network 框架都利用了系统级的省电优化。

### 高效安排请求

通过有策略地决定你 App 何时以及如何访问网络，将能耗降到最低。使用单个 [URLSession](../foundation/urlsession.md) 实例（而不是多个实例），这样你就可以尽可能地复用连接。

将多个请求批量合并，并压缩负载，以减少网络接口保持活跃的总时长。

通过 [URLSession](../foundation/urlsession.md) 管理开销较大的网络请求，并在 [URLSessionConfiguration](../foundation/urlsessionconfiguration.md) 上设置属性以应对不同的网络状况。将 [waitsForConnectivity](../foundation/urlsessionconfiguration/waitsforconnectivity.md) 设为 `true`，以避免在网络不可用时进行无谓的连接尝试。

要防止网络任务使用高开销网络，请将 [allowsExpensiveNetworkAccess](../foundation/urlsessionconfiguration/allowsexpensivenetworkaccess.md) 设为 `false`。将非必要的任务推迟到诸如 Wi-Fi 之类的低开销网络可用时再执行。对于可自行决定时机的请求，将 [allowsConstrainedNetworkAccess](../foundation/urlsessionconfiguration/allowsconstrainednetworkaccess.md) 设为 `false`，以限制你 App 对受限网络的使用，并将这些任务推迟到非受限接口可用时再执行。

### 在后台安排网络请求

使用 [background(withIdentifier:)](<../foundation/urlsessionconfiguration/background(withidentifier_).md>) 来配置 [URLSessionDownloadTask](../foundation/urlsessiondownloadtask.md) 在后台运行。系统会在能耗条件允许时安排后台下载任务。将 [isDiscretionary](../foundation/urlsessionconfiguration/isdiscretionary.md) 设为 `true`，告诉系统使用智能调度，将下载推迟到设备正在充电或已连接 Wi-Fi 时再进行。

系统会自动合并多个 App 的后台下载，缩短网络硬件保持活跃的时长，降低每个 App 相关的能耗开销。

更多信息，请参阅 [Downloading files in the background](../foundation/downloading-files-in-the-background.md)。

### 在后台刷新 App 状态

有策略地使用 [BGAppRefreshTask](../backgroundtasks/bgapprefreshtask.md) 来保持你 App 状态的更新，同时将不必要的网络活动降到最低。只有在确实需要更新关键数据时才安排后台刷新任务，并且在发起请求前始终检查网络状况。

为你请求的 [earliestBeginDate](../backgroundtasks/bgtaskrequest/earliestbegindate.md) 设置合适的值，以避免频繁唤醒，并对失败的尝试使用指数退避，防止陷入消耗能量的重试循环。例如，如果你第一次刷新任务失败，将首次重试的 `earliestBeginDate` 设为 5 分钟后。如果再次失败，等待 10 分钟后重试，然后是 20 分钟，依此类推。

在你的任务成功或失败时，及时调用 [setTaskCompleted(success:)](<../backgroundtasks/bgtask/settaskcompleted(success_).md>)，让系统能够恢复休眠。在你实现的 [expirationHandler](../backgroundtasks/bgtask/expirationhandler.md) 中，妥善处理系统在超时后使你的任务过期的情况。

如果你的 App 在后台使用了过多资源，系统可能会将其停止，这会增加你 App 的能耗，因为下次有人试图使用它时，系统需要重新启动你的 App，而不是直接将其带回前台。

### 将你 App 对蓝牙的使用降到最低

只在你的 App 与蓝牙配件通信时才保持与该配件的连接。使用 [AccessorySetupKit](../accessorysetupkit.md) 来发现和配置配件，它会为你高效地维护蓝牙连接。

## 另请参阅

### Networking and location

- [Accessing the device’s location efficiently](accessing-the-device-s-location-efficiently.md) — 使用 Core Location 特性来管理能耗、接收更新，并将位置更新的频率降到最低。
