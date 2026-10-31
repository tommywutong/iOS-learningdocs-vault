---
title: 为你的内容实现灵活增强缓冲
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/implementing-flexible-enhanced-buffering-for-your-content
source_url: 'https://developer.apple.com/documentation/avfoundation/implementing-flexible-enhanced-buffering-for-your-content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/implementing-flexible-enhanced-buffering-for-your-content.json'
content_hash: 'sha256:5ca04fb951ad7623'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [流媒体与隔空播放](streaming-and-airplay.md)

# 为你的内容实现灵活增强缓冲

<sub>文章</sub>

为你的 App 配置灵活增强缓冲，以更快地将内容串流到支持隔空播放的设备和受支持的 CarPlay 车辆。

## 概述

如果你处理的内容在缓冲方面需要灵活性，请使用 [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) 和 [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) 类。

要实现灵活增强缓冲，请完成以下步骤。

1. 创建一个串行化队列来执行所有播放操作，并创建音频渲染器和渲染同步器以建立媒体时间线。

```swift
let serializationQueue = DispatchQueue(label: "sample.buffer.player.serialization.queue")
let audioRenderer = AVSampleBufferAudioRenderer()
let renderSynchronizer = AVSampleBufferRenderSynchronizer()
```

1. 观察渲染器何时清空了已排队的音频（例如播放速率增大或减小时），并从清空发生的时间点开始重新将音频数据排入队列。

```swift
automaticFlushObserver = NotificationCenter.default.addObserver(forName: .AVSampleBufferAudioRendererWasFlushedAutomatically,
                                                                object: audioRenderer,
                                                                queue: nil) { [weak self] notification in
    self?.serializationQueue.async { [weak self] in
        guard let self = self else { return } 
        // 从清空中断音频的位置重新开始。
        let restartTime = (notification.userInfo?[AVSampleBufferAudioRendererFlushTimeKey] as? NSValue)?.timeValue
        self.autoflushPlayback(restartingAt: restartTime)
    }
}
```

1. 将音频渲染器添加到渲染同步器，告诉音频渲染器遵循媒体时间线。

```swift
renderSynchronizer.addRenderer(audioRenderer)
```

1. 告诉音频渲染器开始处理音频数据，并将渲染同步器的速率设为 `1` 以开始播放。

```swift
serializationQueue.async { [weak self] in
    guard let self = self else { return }
    // 开始处理音频数据，并在没有更多数据时停止。
    self.audioRenderer.requestMediaDataWhenReady(on: serializationQueue) { [weak self] in
        guard let self = self else { return }
        while self.audioRenderer.isReadyForMoreMediaData {
            let sampleBuffer = self.nextSampleBuffer() // 在数据末尾返回 nil。
            if let sampleBuffer = sampleBuffer {
                self.audioRenderer.enqueue(sampleBuffer)
            } else {
                // 告诉渲染器停止请求音频数据。
                audioRenderer.stopRequestingMediaData()
            }
        }
    }

    // 以媒体的自然速率开始播放。
    self.renderSynchronizer.rate = 1.0
}
```

## 另请参阅

### 缓冲播放

- [为你的内容实现简单增强缓冲](implementing-simple-enhanced-buffering-for-your-content.md) — 为你的 App 配置简单增强缓冲，以更快地将内容串流到支持隔空播放的设备和受支持的 CarPlay 车辆。
- [为长视频 App 集成隔空播放](integrating-airplay-for-long-form-video-apps.md) — 通过为长视频播放准备路由系统，集成隔空播放功能并实现专门的外部播放体验。
