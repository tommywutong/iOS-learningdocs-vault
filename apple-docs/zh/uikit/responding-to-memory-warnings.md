---
title: 响应内存警告
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/responding-to-memory-warnings
source_url: 'https://developer.apple.com/documentation/uikit/responding-to-memory-warnings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/responding-to-memory-warnings.json'
content_hash: 'sha256:55bcadc896923c01'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [管理 App 生命周期](managing-your-app-s-life-cycle.md)

# 响应内存警告

<sub>文章</sub>

在系统要求时释放内存。

## 概述

如果系统可用内存不足，且无法通过终止已挂起的 App 来回收内存，UIKit 会向正在运行的 App 发送低内存警告。UIKit 会通过以下方式传递低内存警告：

- 调用 App 委托（app delegate）的 [- applicationDidReceiveMemoryWarning:](<uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) 方法。
- 调用所有活跃 [UIViewController](uiviewcontroller.md) 类的 [- didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) 方法。
- 向所有已注册的观察者发布 [UIApplicationDidReceiveMemoryWarningNotification](uiapplication/didreceivememorywarningnotification.md) 对象。
- 向类型为 [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](../dispatch/dispatch_source_type_memorypressure.md) 的调度队列传递警告。

当 App 收到低内存警告时，请尽可能快速地释放尽可能多的内存。移除对图像、媒体文件或任何已有磁盘表示且稍后可重新加载的大型数据文件的引用。移除对不再需要的所有临时对象的引用。如果活跃任务可能消耗大量内存，请暂停调度队列，或限制 App 同时执行的操作数量。

> [!important] 重要
> 如果未能降低 App 的内存用量，App 可能会被终止。因此，请考虑在清理过程中将所有未保存的数据写入磁盘。

要测试 App 对低内存警告的响应，请使用 iOS Simulator 中的 Simulate Memory Warning 命令。
