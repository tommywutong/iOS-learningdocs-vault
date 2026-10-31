---
title: 样本缓冲区播放
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/sample-buffer-playback
source_url: 'https://developer.apple.com/documentation/avfoundation/sample-buffer-playback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/sample-buffer-playback.json'
content_hash: 'sha256:6f3ef91f81c160ef'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 样本缓冲区播放

<sub>API 集合</sub>

创建自定义控制器来播放样本缓冲区流并同步其时间。

## 主题

### 样本缓冲区生成

- [使用你自己的播放器播放自定义音频](../avfaudio/playing-custom-audio-with-your-own-player.md) — 构建一个音频播放器来播放你的自定义音频数据，并可选择利用 AirPlay 2 的高级特性。
- [AVSampleBufferRequest](avsamplebufferrequest.md) — 一个描述样本缓冲区创建请求的对象。
- [AVSampleBufferGenerator](avsamplebuffergenerator.md) — 一个创建样本缓冲区的对象。
- [AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md) — 一个批量生成样本缓冲区的对象。

### 呈现

- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) — 你可以实现的方法，用于将样本缓冲区入队以供呈现。
- [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) — 一个用于将多个已入队的样本缓冲区同步到单一时间线的对象。
- [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) — 一个显示压缩或未压缩视频帧的对象。
- [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md) — 一个将视频样本缓冲区入队以供渲染的对象。
- [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) — 一个用于解压音频并播放压缩或未压缩音频的对象。

## 另请参阅

### 播放

- [媒体播放](media-playback.md) — 管理媒体资产和插播内容的播放，与你在界面中呈现这些内容的方式无关。
- [离线播放与存储](offline-playback-and-storage.md) — 将流式内容下载到磁盘以支持离线播放，并定义自动移除已下载媒体资源的策略。
- [流媒体与隔空播放](streaming-and-airplay.md) — 使用隔空播放将内容以无线方式流传输到其他设备，并处理涉及 FairPlay 保护媒体资产的请求。
