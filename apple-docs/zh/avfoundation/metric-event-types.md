---
title: 指标事件类型
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/metric-event-types
source_url: 'https://developer.apple.com/documentation/avfoundation/metric-event-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/metric-event-types.json'
content_hash: 'sha256:7c4c94791cce35df'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 指标事件类型

<sub>API 集合</sub>

## 主题

### HTTP Live Streaming

- [AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md) — 表示媒体资源请求的事件。
- [AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md) — 表示直播内容密钥资源请求的事件。
- [AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md) — 表示直播媒体片段资源请求的事件。
- [AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md) — 表示直播播放列表资源请求的事件。
- [AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md) — 表示播放器尝试进行变体切换的事件。
- [AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md) — 表示播放器完成变体切换的事件。
- [AVMetricMediaRendition](avmetricmediarendition.md)

### 缓冲

- [AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md) — 表示播放发生停滞的事件。
- [AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md) — 表示播放有可能持续而不停滞的事件。
- [AVMetricPlayerItemInitialLikelyToKeepUpEvent](avmetricplayeriteminitiallikelytokeepupevent.md) — 表示播放有可能持续而不停滞这一初始状态的事件。

### 传输控制

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — 表示整个播放会话汇总指标的事件。
- [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md) — 表示播放速率发生变化的事件。
- [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md) — 表示播放跳转完成的事件。
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md) — 表示发生播放跳转的事件。

### 播放模式

- [AVMetricPlaybackMode](avmetricplaybackmode.md) — 这些常量是 AVMetricPlaybackModeSwitchEvent 上 “mode” 属性可返回的播放模式。
- [AVMetricPlaybackModeSwitchEvent](avmetricplaybackmodeswitchevent.md) — 表示播放状态的变化，进入 AVMetricPlaybackMode 之一。_(beta)_

### 摘要

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — 表示整个播放会话汇总指标的事件。
- [AVMetricDownloadSummaryEvent](avmetricdownloadsummaryevent.md) — 表示汇总了整个下载任务指标的摘要指标事件。

## 另请参阅

### 指标

- [AVMetrics](avmetrics.md) — 一个异步的指标信息流。
- [AVMergedMetrics](avmergedmetrics.md) — 一个来自不同发布者的异步指标信息流。
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — 一个提供与视频播放质量相关指标的对象。
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — 一种用于向事件流发布指标事件的对象的类型。
- [AVMetricEvent](avmetricevent.md) — 表示指标事件的基类。
- [AVMetricErrorEvent](avmetricerrorevent.md) — 一个表示错误发生时的指标事件的对象。
