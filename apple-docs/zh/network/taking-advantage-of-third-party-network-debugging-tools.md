---
title: 利用第三方网络调试工具
framework: Network
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/taking-advantage-of-third-party-network-debugging-tools
source_url: 'https://developer.apple.com/documentation/network/taking-advantage-of-third-party-network-debugging-tools'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/taking-advantage-of-third-party-network-debugging-tools.json'
content_hash: 'sha256:d9bd459419f03a41'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md)

# 利用第三方网络调试工具

<sub>文章</sub>

了解可用的第三方网络调试工具。

## 概述

iOS 和 macOS 内置了网络调试工具（参阅[使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md)和[选择网络调试工具](choosing-a-network-debugging-tool.md)），但你可能也想利用此处讨论的第三方工具。

> [!important] 重要
> 此处提供关于非 Apple 制造的产品的信息，仅供参考，不构成推荐或认可。Apple 对此类第三方产品的选择、性能或使用不承担任何责任。如需更多信息，请联系[供应商](https://support.apple.com/en-us/HT201777)。其他公司和产品名称可能是其各自所有者的商标。

### 调试 HTTP 代理

- **[Charles HTTP Proxy](https://www.charlesproxy.com/)**——一个调试用 HTTP 代理，使开发者能够查看其机器与互联网之间所有的 HTTP 和 HTTPS 流量。
- **[mitmproxy](https://mitmproxy.org/)**——一个免费开源的交互式调试 HTTP 代理。其名称代表“machine-in-the-middle proxy（中间人代理）”。

### macOS App

- **[Debookee](https://www.iwaxx.com/debookee/)**——一个适用于 macOS 的简单而强大的网络流量分析器。
- **[IPNetMonitorX](http://www.sustworks.com/site/prod_ipmx_overview.html)**——一个用于排查互联网服务问题及优化性能的网络故障排除工具包。
- **[Wireshark](https://www.wireshark.org)**——一个支持 macOS 的免费开源数据包分析器。

### 命令行工具

- **[tcpflow](http://www.circlemud.org/jelson/software/tcpflow/)**——一个记录 TCP 连接（流）中传输的数据的程序，并以便于协议分析或调试的方式存储数据。
- **[tcptrace](http://tcptrace.org/)**——一个用于分析数据包追踪中 TCP 连接的开源工具。

## 另请参阅

### 网络调试

- [选择网络调试工具](choosing-a-network-debugging-tool.md)——判断哪种工具最适合你的网络调试问题。
- [调试 HTTP 服务器端错误](debugging-http-server-side-errors.md)——理解 HTTP 服务器端错误及其调试方法。
- [使用 CFNetwork 诊断日志调试 HTTPS 问题](debugging-https-problems-with-cfnetwork-diagnostic-logging.md)——使用 CFNetwork 诊断日志来调查 HTTP 和 HTTPS 问题。
- [记录数据包追踪](recording-a-packet-trace.md)——了解如何记录网络流量的底层追踪。
- [在你 App 中测试和调试 L4S](testing-and-debugging-l4s-in-your-app.md)——了解如何在支持 L4S 的主机和网络上验证你的 App，以提升其响应能力。
