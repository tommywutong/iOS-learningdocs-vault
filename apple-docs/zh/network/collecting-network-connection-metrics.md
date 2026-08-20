---
title: 收集网络连接指标
framework: Network
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/collecting-network-connection-metrics
source_url: 'https://developer.apple.com/documentation/network/collecting-network-connection-metrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/collecting-network-connection-metrics.json'
content_hash: 'sha256:a7833c3e0e51f45c'
translated: true
---

> 导航：[技术](../technologies.md) · [Network](../network.md) · [NWConnection](nwconnection.md)

# 收集网络连接指标

<sub>示例代码</sub>

使用报告来了解 DNS 和协议握手如何影响连接建立。

## 概述

> [!note] 注意
> 本示例代码项目关联的是 WWDC 2019 的讲座 [713：网络技术进展，第 2 部分](https://developer.apple.com/videos/play/wwdc19/713/)。

## 另请参阅

### 收集连接指标

- [requestEstablishmentReport(queue:completion:)](<nwconnection/requestestablishmentreport(queue_completion_).md>) — 连接进入就绪状态后，请求该连接建立报告的副本。
- [EstablishmentReport](nwconnection/establishmentreport.md) — 提供有关连接建立指标的报告。
- [startDataTransferReport()](<nwconnection/startdatatransferreport().md>) — 开始一份新的数据传输报告，该报告可在之后收集。
- [PendingDataTransferReport](nwconnection/pendingdatatransferreport.md) — 一份尚未收集的数据传输报告。
- [DataTransferReport](nwconnection/datatransferreport.md) — 提供有关连接上发送和接收数据的指标的报告。

## 下载

- [CollectingNetworkConnectionMetrics.zip](https://docs-assets.developer.apple.com/published/017625187506/CollectingNetworkConnectionMetrics.zip)
