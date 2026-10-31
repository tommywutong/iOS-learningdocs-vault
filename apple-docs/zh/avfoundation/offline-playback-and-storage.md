---
title: 离线播放与存储
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/offline-playback-and-storage
source_url: 'https://developer.apple.com/documentation/avfoundation/offline-playback-and-storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/offline-playback-and-storage.json'
content_hash: 'sha256:2371774ebc38d4e9'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 离线播放与存储

<sub>API 集合</sub>

将流式内容下载到磁盘以支持离线播放，并定义自动移除已下载媒体资源的策略。

## 主题

### 媒体资源下载

- [使用 AVFoundation 播放和持久化 HTTP 直播流](using-avfoundation-to-play-and-persist-http-live-streams.md) — 使用 AVFoundation 播放 HTTP 直播流并将流持久化到磁盘以供离线播放。
- [AVAssetDownloadURLSession](avassetdownloadurlsession.md) — 一个创建和管理媒体资源下载任务的 URL 会话。
- [AVAssetDownloadTask](avassetdownloadtask.md) — 一个将远程媒体资源下载到设备以供离线播放的 URL 会话任务。
- [AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md) — 一个为媒体资源下载多个媒体选择项的任务。 _(已废弃)_

### 离线存储管理

- [AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md) — 一个管理自动清除已下载媒体资源策略的对象。
- [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md) — 一个定义自动管理已下载媒体资源存储策略的对象。
- [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md) — 一个用于创建新存储管理策略的可变对象。

### 缓存监控

- [AVAssetCache](avassetcache.md) — 一个用于检查本地缓存的媒体数据的对象。

## 另请参阅

### 播放

- [媒体播放](media-playback.md) — 管理媒体资产和插播内容的播放，与你在界面中呈现这些内容的方式无关。
- [流媒体与隔空播放](streaming-and-airplay.md) — 使用隔空播放将内容以无线方式流传输到其他设备，并处理涉及 FairPlay 保护媒体资产的请求。
- [样本缓冲区播放](sample-buffer-playback.md) — 创建自定义控制器来播放样本缓冲区流并同步其时间。
