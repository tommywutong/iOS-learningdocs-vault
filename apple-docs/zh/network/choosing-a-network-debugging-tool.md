---
title: 选择网络调试工具
framework: Network
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/choosing-a-network-debugging-tool
source_url: 'https://developer.apple.com/documentation/network/choosing-a-network-debugging-tool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/choosing-a-network-debugging-tool.json'
content_hash: 'sha256:3e46df99d412d05e'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# 选择网络调试工具

<sub>文章</sub>

根据你的网络调试需求，决定哪种工具最合适。

## 概述

调试网络问题具有挑战性，这是由于网络的根本性质决定的。网络通信是异步的、对时间敏感的，并且容易出错。此外，涉及到的两个程序（例如客户端和服务器）通常由不同的开发者创建，他们对所交换数据的具体格式可能持有不同意见。幸运的是，有多种工具可以帮助你调试这类问题。

这些工具的一个关键目标是将问题一分为二。例如，如果你正在开发一个网络客户端，它向服务器发送请求后收到了来自服务器的错误，那么了解失败的原因究竟是请求不正确（你客户端的问题），还是服务器行为异常，这一点至关重要。你可以使用这些网络调试工具来查看网络上传输的数据流量，从而独立地检查这些数据的有效性。

使用的最佳工具取决于你使用的 API 以及你遇到的问题类型：

- 如果你在 HTTP 层面工作，你可能会发现你的请求成功到达服务器，然后服务器返回一个响应，指示请求以某种方式失败了（例如，你收到了一个状态码为 _500 Internal Server Error_ 的 HTTP 响应）。请参阅[调试 HTTP 服务端错误](debugging-http-server-side-errors.md)和[使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md)。
- 如果你使用 [URLSession](../foundation/urlsession.md)，或者某个内部使用了 [URLSession](../foundation/urlsession.md) 的子系统，你可以启用 CFNetwork 诊断日志来获取关于请求处理方式的详细视图。请参阅[使用 CFNetwork 诊断日志调试 HTTPS 问题](debugging-https-problems-with-cfnetwork-diagnostic-logging.md)。
- 如果你想获取网络上交换流量的底层视图，你需要进行数据包追踪。请参阅[记录数据包追踪](recording-a-packet-trace.md)。
- 如果你在 Safari 或各种 Web 视图（如 [WKWebView](../webkit/wkwebview.md)）中工作，你可以使用 Web Inspector 查看页面发出的网络请求。请参阅 [Web 开发工具](https://developer.apple.com/safari/tools/)。
- 一些最流行的网络调试工具（如 HTTP 调试代理）是第三方产品。请参阅[利用第三方网络调试工具](taking-advantage-of-third-party-network-debugging-tools.md)。

## 另请参阅

### 网络调试

- [调试 HTTP 服务端错误](debugging-http-server-side-errors.md) — 了解 HTTP 服务端错误及其调试方法。
- [使用 CFNetwork 诊断日志调试 HTTPS 问题](debugging-https-problems-with-cfnetwork-diagnostic-logging.md) — 使用 CFNetwork 诊断日志调查 HTTP 和 HTTPS 问题。
- [记录数据包追踪](recording-a-packet-trace.md) — 学习如何记录网络流量的底层追踪信息。
- [利用第三方网络调试工具](taking-advantage-of-third-party-network-debugging-tools.md) — 了解可用的第三方网络调试工具。
- [在 App 中测试和调试 L4S](testing-and-debugging-l4s-in-your-app.md) — 学习如何在支持 L4S 的主机和网络上验证你的 App，以提高 App 的响应能力。
