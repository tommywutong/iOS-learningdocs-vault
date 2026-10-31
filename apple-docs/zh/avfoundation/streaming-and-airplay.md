---
title: 流媒体与隔空播放
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/streaming-and-airplay
source_url: 'https://developer.apple.com/documentation/avfoundation/streaming-and-airplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/streaming-and-airplay.json'
content_hash: 'sha256:6b95a419b0f03ffb'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 流媒体与隔空播放

<sub>API 集合</sub>

使用隔空播放（AirPlay）将内容无线串流到其他设备，并处理涉及 FairPlay 保护资产的请求。

## 主题

### 基础

- [在你的 App 中支持隔空播放](supporting-airplay-in-your-app.md) — 设置你的 App 使用隔空播放无线发送内容。

### 路由选择

- [AVRouteDetector](avroutedetector.md) — 一个检测可用媒体播放路由的对象。

### 缓冲播放

- [为你的内容实现简单增强缓冲](implementing-simple-enhanced-buffering-for-your-content.md) — 为你的 App 配置简单增强缓冲，以更快地将内容串流到支持隔空播放的设备和受支持的 CarPlay 车辆。
- [为你的内容实现灵活增强缓冲](implementing-flexible-enhanced-buffering-for-your-content.md) — 为你的 App 配置灵活增强缓冲，以更快地将内容串流到支持隔空播放的设备和受支持的 CarPlay 车辆。
- [为长视频 App 集成隔空播放](integrating-airplay-for-long-form-video-apps.md) — 通过为长视频播放准备路由系统，集成隔空播放功能并实现专门的外部播放体验。

### 资源加载

- [AVAssetResourceLoader](avassetresourceloader.md) — 一个为来自 URL 资源的资源请求充当中间人的对象。
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — 你可以实现以处理来自 URL 资源的资源加载请求的方法。
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — 一个封装来自资源加载器对象的资源请求信息的对象。
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — 一个封装来自资源加载器的资源请求信息的对象，用于续订之前发出的请求。
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — 一个包含资源加载请求发起方信息的对象。
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — 一个用于从资源资产加载请求所引用的资源中请求数据的对象。
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — 一个查询，用于检索资源资产加载请求所引用资源的基本信息。

### FairPlay 串流

- [AVContentKeySession](avcontentkeysession.md) — 一个为媒体数据创建并跟踪解密密钥的对象。
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — 一个处理内容密钥请求的协议。
- [AVContentKey](avcontentkey.md) — 一个表示内容密钥解密器的对象。
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — 一个唯一标识内容密钥的对象。
- [AVContentKeyRequest](avcontentkeyrequest.md) — 一个封装来自内容密钥会话对象的内容解密密钥请求信息的对象。
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — 一个封装来自内容密钥会话的可持久化内容解密密钥请求信息的对象。
- [AVContentKeyResponse](avcontentkeyresponse.md) — 一个封装对内容解密密钥请求的响应信息的对象。
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — 指定是否存在足以显示内容的保护的常量。
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — 将内容密钥附加到样本缓冲区以进行内容解密。_(已废弃)_

## 另请参阅

### 播放

- [媒体播放](media-playback.md) — 管理媒体资源和插播内容的播放，与你在界面中呈现这些内容的方式无关。
- [离线播放与存储](offline-playback-and-storage.md) — 将流媒体内容下载到磁盘以支持离线播放，并定义自动移除已下载资产的策略。
- [样本缓冲区播放](sample-buffer-playback.md) — 创建自定控制器来播放样本缓冲区流并同步其计时。
