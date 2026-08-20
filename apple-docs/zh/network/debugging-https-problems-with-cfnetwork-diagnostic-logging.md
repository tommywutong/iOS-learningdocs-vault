---
title: 使用 CFNetwork 诊断日志调试 HTTPS 问题
framework: Network
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging
source_url: 'https://developer.apple.com/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging.json'
content_hash: 'sha256:6017748ada6b096e'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# 使用 CFNetwork 诊断日志调试 HTTPS 问题

<sub>文章</sub>

使用 CFNetwork 诊断日志来调查 HTTP 和 HTTPS 问题。

## 概述

如果你在使用 [URLSession](../foundation/urlsession.md) 并需要调试复杂的网络问题，可以启用 CFNetwork 诊断日志来获取关于网络请求进度的详细信息。CFNetwork 诊断日志相对于其他网络调试工具有独特的优势，包括：

- 最简配置
- 能够查看受传输层安全性（TLS）保护的网络流量
- 提供关于 CFNetwork 内部状态的信息，例如保存和应用了哪些 cookie

关于其他网络调试工具，请参阅[选择网络调试工具](choosing-a-network-debugging-tool.md)。

> [!note] 注意
> Xcode 13 包含了 HTTP Tracing 工具来帮助调试 HTTP 问题。请参阅[使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md)。

### 了解安全影响

CFNetwork 诊断日志可能包含已解密的 TLS 数据及其他安全敏感信息。请采取以下预防措施：

- 限制对任何捕获日志的访问。
- 如果你构建的 App 以编程方式启用此日志，请确保收到该 App 的任何人了解使用它的安全影响。
- 如果你将日志发送给 Apple，请对任何安全敏感信息进行脱敏处理。

> [!important] 重要
> CFNetwork 诊断日志可能包含**极其**敏感的信息。请妥善保护这些日志。

### 在 Xcode 中启用日志

要启用 CFNetwork 诊断日志，请编辑当前方案（选择 Product \> Scheme \> Edit Scheme），进入 Arguments 标签页，并在环境变量列表中添加一个 `CFNETWORK_DIAGNOSTICS` 项。此项的值范围是 0 到 3，其中 0 关闭日志，更大的数字提供更详细的日志。下次运行你的 App 并使用 [URLSession](../foundation/urlsession.md) 时，CFNetwork 诊断日志条目将出现在 Xcode 的调试控制台区域。如果控制台区域不可见，请选择 View \> Debug Area \> Show Debug Area 以显示它。

### 以编程方式启用日志以在 Xcode 外查看问题

要调查 Xcode 外的问题，请通过直接设置环境变量以编程方式启用 CFNetwork 诊断日志。

```objc
setenv("CFNETWORK_DIAGNOSTICS", "3", 1);
```

在 App 启动序列的一开始就执行此操作：

- 如果你使用 Objective-C 编程，请将代码放在 `main` 函数的开头。
- 如果你的程序包含 C++ 组件，请确保此代码在任何使用了 CFNetwork 或任何使用了 CFNetwork 的 API（如 [URLSession](../foundation/urlsession.md)）的 C++ 静态初始化器之前运行。
- 如果你使用 Swift 编程，请将此代码放在 `main.swift` 中。

> [!note] 注意
> 默认情况下，Swift App 没有 `main.swift`；[The Swift Programming Language](https://docs.swift.org/swift-book/) 说明了如何添加一个。

### 查看日志条目

查看生成的日志条目的方式取决于你的具体情况：

- 在 macOS 上，如果你能在本地重现问题，请在你的 Mac 上运行 Console 实用工具并在那里查看日志条目。
- 在 iOS 上，如果你能在本地重现问题，并且能够通过 USB 将设备连接到你的 Mac，请在你的 Mac 上运行 Console 实用工具并在那里查看日志条目。确保在主 Console 窗口左侧的源列表中选择了你的 iOS 设备（如果源列表不可见，请选择 View \> Show Sources）。
- 如果上述两种方法都不适用——例如，你正在尝试调试一个只能由你的某个用户在实际环境中重现的问题——请从出现问题的机器获取 sysdiagnose 日志，然后从中提取日志条目。请参阅开发者网站上的 [Bug Reporting \> Profiles and Logs](https://developer.apple.com/bug-reporting/profiles-and-logs/) 页面以了解如何获取 sysdiagnose 日志的详细信息。

## 另请参阅

### 网络调试

- [选择网络调试工具](choosing-a-network-debugging-tool.md) — 决定哪种工具最适合你的网络调试问题。
- [调试 HTTP 服务器端错误](debugging-http-server-side-errors.md) — 了解 HTTP 服务器端错误以及如何调试它们。
- [录制数据包追踪](recording-a-packet-trace.md) — 学习如何录制网络流量的底层追踪。
- [利用第三方网络调试工具](taking-advantage-of-third-party-network-debugging-tools.md) — 了解可用的第三方网络调试工具。
- [在你的 App 中测试和调试 L4S](testing-and-debugging-l4s-in-your-app.md) — 学习如何在支持 L4S 的主机和网络上验证你的 App，以提高其响应速度。
