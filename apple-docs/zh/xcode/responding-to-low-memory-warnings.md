---
title: 响应低内存警告
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/responding-to-low-memory-warnings
source_url: 'https://developer.apple.com/documentation/xcode/responding-to-low-memory-warnings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/responding-to-low-memory-warnings.json'
content_hash: 'sha256:28673d365e4eefa4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)

# 响应低内存警告

<sub>文章</sub>

检测 App 何时使用了过多内存，并使内存使用恢复到可控范围。

## 概述

当 App 的内存使用量接近设备可用内存的限制时，iOS 会向 App 发送警告。触发内存警告的内存使用量对应于 Xcode 内存仪表中的黄色区域。你的 App 可以通过以下任一方式收到内存警告：

- UIKit 调用 App 委托（app delegate）的 [applicationDidReceiveMemoryWarning(_:)](<../uikit/uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) 方法。
- UIKit 调用活跃 [UIViewController](../uikit/uiviewcontroller.md) 对象的 [didReceiveMemoryWarning()](<../uikit/uiviewcontroller/didreceivememorywarning().md>) 方法。
- iOS 将 [didReceiveMemoryWarningNotification](../uikit/uiapplication/didreceivememorywarningnotification.md) 发布到默认通知中心（notification center）。
- Dispatch 队列接收源类型为 [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](../dispatch/dispatch_source_type_memorypressure.md) 的事件。

操作系统会尽力发送低内存警告，你的 App 需要尽快响应。如果系统的内存需求增长速度快于警告缓解内存压力的速度，系统可能来不及发送低内存警告并等待 App 响应。出现这种情况时，系统会转而移除 App 以回收其内存，并将原因记录在日志文件中，详情参见[通过 jetsam 事件报告识别高内存使用情况](identifying-high-memory-use-with-jetsam-event-reports.md)。

确保 App 在收到内存警告时改变分配内存的方式，采用保守策略，在使用对象时寻找释放对象或缩减对象大小的机会。如果 App 一次分配大量内存，并在这次大规模分配期间还未来得及收到低内存警告就崩溃，请修改代码以逐步分配所需内存，让系统有足够时间在整个系统范围内释放内存。

如果 App 加载的是可以轻松重新创建的数据，请考虑使用 [NSPurgeableData](../foundation/nspurgeabledata.md)。当 [NSPurgeableData](../foundation/nspurgeabledata.md) 的内容未通过 [beginContentAccess()](<../foundation/nsdiscardablecontent/begincontentaccess().md>) 标记为正在使用时，系统会在低内存情况下自动丢弃这些内容。此自动丢弃过程可帮助 App 更快地响应低内存警告，因为由内核负责丢弃数据，而不是让 App 等到收到低内存通知后再丢弃数据。

> [!important] 重要
> App 收到内存警告时，不要遍历其整个对象图来寻找可释放的内存，并避免结合使用 [NSCache](../foundation/nscache.md) 与 [NSPurgeableData](../foundation/nspurgeabledata.md)。iOS 会压缩 App 最近未访问的内存页。搜索可清除的内存会将这些页面移出压缩器，增加系统的内存需求。

## 另请参阅

### 相关文档

- [通过 jetsam 事件报告识别高内存使用情况](identifying-high-memory-use-with-jetsam-event-reports.md) — 了解可用内存不足时操作系统终止 App 的原因。

### 任务

- [收集内存使用信息](gathering-information-about-memory-use.md) — 通过测量和分析你的 App，识别内存使用效率低下的问题。
- [进行更改以减少内存使用](making-changes-to-reduce-memory-use.md) — 处理内存使用过量的常见原因，以减少 App 的内存使用。
- [防止内存使用衰退](preventing-memory-use-regressions.md) — 测量 App 功能所使用的内存，并使用 XCTest 性能测试检测内存使用量的增加。
