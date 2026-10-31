---
title: 已废弃符号
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols.json'
content_hash: 'sha256:d18157ced6d41947'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [样本缓冲区播放](sample-buffer-playback.md) · [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md)

# 已废弃符号

<sub>API 集合</sub>

查阅不再支持的符号及其替代方案。

## 主题

### 发起媒体数据请求

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avsamplebufferdisplaylayer/requestmediadatawhenready(on_using_).md>) — 指示目标在其方便时反复调用客户端提供的 block，以收集用于显示的样本缓冲区。
- [readyForMoreMediaData](avsamplebufferdisplaylayer/isreadyformoremediadata.md) — 一个布尔值，指示图层是否准备好接受更多样本缓冲区。 _(已废弃)_
- [requiresFlushToResumeDecoding](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md) — 一个布尔值，指示图层是否需要清空其状态才能继续解码帧。 _(已废弃)_
- [- stopRequestingMediaData](<avsamplebufferdisplaylayer/stoprequestingmediadata().md>) — 取消当前的任何媒体数据请求。
- [hasSufficientMediaDataForReliablePlaybackStart](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md) — 一个布尔值，指示已入队的媒体数据是否达到渲染器的预卷（preroll）级别。 _(已废弃)_

### 清空样本缓冲区

- [- flush](<avsamplebufferdisplaylayer/flush().md>) — 指示图层丢弃所有处于待处理状态的已入队样本缓冲区。
- [- flushAndRemoveImage](<avsamplebufferdisplaylayer/flushandremoveimage().md>) — 指示图层丢弃待处理的已入队样本缓冲区，并移除当前显示的任何图像。 _(已废弃)_

### 配置时间基准

- [timebase](avsamplebufferdisplaylayer/timebase.md) — 渲染器的时间基准，决定图层如何解释时间戳。 _(已废弃)_

### 将样本缓冲区入队

- [- enqueueSampleBuffer:](<avsamplebufferdisplaylayer/enqueue(__).md>) — 发送一个样本缓冲区用于显示。

### 获取显示图层设置

- [status](avsamplebufferdisplaylayer/status.md) — 显示图层用于将样本缓冲区入队的能力。 _(已废弃)_
- [AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md) — 样本缓冲区渲染的状态。 _(已废弃)_

### 处理错误

- [error](avsamplebufferdisplaylayer/error.md) — 导致失败的错误。 _(已废弃)_
