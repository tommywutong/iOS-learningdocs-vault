---
title: 使用自定视频合成器处理空间视频
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, Xcode 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/processing-spatial-video-with-a-custom-video-compositor
source_url: 'https://developer.apple.com/documentation/avfoundation/processing-spatial-video-with-a-custom-video-compositor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/processing-spatial-video-with-a-custom-video-compositor.json'
content_hash: 'sha256:9b60b6cb6ef475f3'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [视频效果](video-effects.md)

# 使用自定视频合成器处理空间视频

<sub>示例代码</sub>

创建自定视频合成器来编辑空间视频，以供播放和导出。

## 概述

空间视频内容需要专门的处理，以保持其立体呈现，或将其转换为单目输出以适应不同的观看场景。虽然 AVFoundation 为变换和淡入淡出等基本效果提供了内置的视频合成能力，但处理空间视频的双眼数据流需要更精细的控制。

AVFoundation 的 [AVVideoCompositing](avvideocompositing.md) 协议为构建可完全控制视频处理的自定视频合成器提供了框架。本示例演示如何实现处理空间视频带标记缓冲区数据的自定合成器，让你能够为播放和导出场景处理立体内容。

## 配置示例代码项目

要运行示例 App，请在你的设备上放置一个或多个要处理的空间视频文件。项目中包含一个用于测试的示例空间视频文件，你也可以在 Apple Vision Pro 或 iPhone 16 上捕捉你自己的内容。

运行 App 时，它会提示你通过所在平台的系统文件选择器选择一个空间视频文件。

## 创建自定合成器

示例提供了两个 [AVVideoCompositing](avvideocompositing.md) 实现：`MonoOutputCompositor` 和 `StereoOutputCompositor`。两者都处理单目或立体输入，但分别输出单目或立体视频。

为了表明它们支持处理空间视频，两个实现都重写了 [supportsSourceTaggedBuffers](avvideocompositing/supportssourcetaggedbuffers.md) 属性并将其设为 `true`。

```swift
/// 一个布尔值，指示自定合成器是否支持来源带标记缓冲区。
let supportsSourceTaggedBuffers = true
```

框架会调用合成器的 [- startVideoCompositionRequest:](<avvideocompositing/startrequest(__).md>) 方法来处理每一帧视频，并传入一个 [AVAsynchronousVideoCompositionRequest](avasynchronousvideocompositionrequest.md)，它提供对来源帧数据的访问。该实现同时处理空间和单目视频来源：

```swift
func startRequest(_ request: AVAsynchronousVideoCompositionRequest) {

    // 如果未找到轨道标识符，则取消请求并返回。
    guard let firstTrackIDNumber = request.sourceTrackIDs.first else {
        request.finishCancelledRequest()
        return
    }

    let firstTrackID = CMPersistentTrackID(truncating: firstTrackIDNumber)

    // 尝试检索来源轨道中的带标记缓冲区。
    if let taggedBuffers = request.sourceTaggedDynamicBuffers(byTrackID: firstTrackID) {
        // 处理来自立体来源轨道的带标记缓冲区。
        processTaggedBuffers(taggedBuffers: taggedBuffers, request: request)
    }
    // 尝试检索来源轨道中的单目视频帧。
    else if let pixelBuffer = request.sourceFrame(byTrackID: firstTrackID) {
        // 处理来自单目来源轨道的像素缓冲区。
        processMonoscopicBuffer(sourcePixelBuffer: pixelBuffer, request: request)
    }
    // 未找到来源帧。以错误结束。
    else {
        request.finish(with: CompositorError.invalidSource)
    }
}
```

该方法首先尝试检索带标记缓冲区，这表明视频数据是空间的。如果未找到带标记缓冲区，它会将来源按单目视频处理。如果两次尝试都未成功，则以错误结束请求。

> [!note] 注意
> 有关每个合成器所执行处理的细节，请参阅各自的实现。

## 构建视频合成对象

示例使用 App 的 `VideoCompositionBuilder` 结构体创建视频合成。该类型的 `build()` 方法为选定的资产创建一个 [Configuration](avvideocomposition/configuration.md)，并指示使用自定合成器：

```swift
/// 构建一个视频合成对象。
func build() async throws -> AVVideoComposition {

    // 为该资产创建视频合成配置对象。
    var configuration = try await AVVideoComposition.Configuration(for: asset)
    // 指定要使用的自定合成器实现类。
    configuration.customVideoCompositorClass = compositorConfiguration.class

    ...

    return AVVideoComposition(configuration: configuration)
}
```

该配置包含两个与空间视频相关的关键属性：

- **[spatialVideoConfigurations](avvideocomposition/configuration/spatialvideoconfigurations.md)** — 包含描述视频数据相机基线（baseline）和视差调整的 [AVSpatialVideoConfiguration](avspatialvideoconfiguration-swift.struct.md) 对象。仅当你的合成器输出与来源不同时才修改此项。
- **[outputBufferDescription](avvideocomposition/configuration/outputbufferdescription.md)** — 使用 `CMTag` 数组配置带标记缓冲区输出。每个顶层数组元素对应一只眼睛，指定该眼睛输出缓冲区的标签。对于单目输出，将其保留为 `nil`，并将 `spatialVideoConfigurations` 设为空数组。

构建器根据合成器产生立体还是单目输出来配置输出：

```swift
if compositorConfiguration.outputsStereo {
    // 将指令包装在 App 的自定指令类型中。
    configuration.instructions = configuration.instructions.compactMap {
        SpatialVideoCompositionInstruction(
            instruction: $0,
            spatialConfiguration: spatialConfiguration,
            projectionTag: projectionTag
        )
    }
    configuration.outputBufferDescription = [
        [.stereoView(.leftEye), projectionTag, .mediaType(.video)],
        [.stereoView(.rightEye), projectionTag, .mediaType(.video)]
    ]
} else {
    configuration.outputBufferDescription = nil
    configuration.spatialVideoConfigurations = []
}
```

## 使用自定合成器进行播放

为播放集成自定合成器非常简单。示例的 `SampleModel` 类使用视频合成创建一个 [AVPlayer](avplayer.md)：

```swift
/// 创建一个新的播放器来播放指定 URL 处的电影。
/// - Parameter url: 要播放的电影文件的 URL。
private func makePlayer(url: URL) async throws -> AVPlayer {
    let asset = AVURLAsset(url: url)
    let playerItem = AVPlayerItem(asset: asset)
    // 为当前用户选择的自定合成器创建视频合成。
    if let videoComposition = try await makeVideoComposition(for: asset) {
        playerItem.videoComposition = videoComposition
        playerItem.seekingWaitsForVideoCompositionRendering = true
    }
    return AVPlayer(playerItem: playerItem)
}
```

该方法使用选定的合成器配置创建视频合成。如果成功创建了有效的合成，就将其赋给播放器条目并启用渲染同步。

## 使用资产导出会话导出

示例的 `ExportSessionExporter` 类演示如何使用 [AVAssetExportSession](avassetexportsession.md) 进行导出。导出方法会根据视频合成的输出类型选择合适的预设：

```swift
func export(asset: AVAsset, videoComposition: AVVideoComposition? = nil) async throws {

    // 如果此方法收到的视频合成会产生立体输出，则使用 MV-HEVC 预设。
    // 注意：`outputsStereo` 属性是 App 专属的扩展。
    let preset = if let videoComposition, videoComposition.outputsStereo {
        AVAssetExportPresetMVHEVC4320x4320
    }
    // 否则，使用标准 HEVC 预设。
    else {
        AVAssetExportPresetHEVCHighestQuality
    }

    // 尝试使用选定的预设创建导出会话。
    guard let exportSession = AVAssetExportSession(asset: asset, presetName: preset) else {
        throw ExportError.noExportSession
    }

    // 如果向此方法传入了有效的视频合成，则将其设置到导出会话上。
    if let videoComposition {
        exportSession.videoComposition = videoComposition
    }

    ...
}
```

对于立体输出，该方法使用 MV-HEVC 预设以保持空间视频格式。对于单目输出，它使用标准 HEVC 预设。创建导出会话后，它会指定视频合成并执行导出操作。

## 使用资产读取器和写入器导出

示例的 `ReaderWriterExporter` 类使用 [AVAssetReader](avassetreader.md) 和 [AVAssetWriter](avassetwriter.md) 提供细粒度的导出控制。这种方式需要更多设置，但在导出过程上提供了更大的灵活性。

核心导出操作使用一个读写循环来处理每一帧视频：

```swift
// 读写循环在专用分派队列中执行。
writerInput.requestMediaDataWhenReady(on: DispatchQueue(label: "com.apple.spatialcompositor.reader")) {
    while writerInput.isReadyForMoreMediaData {

        guard let sampleBuffer = readerOutput.copyNextSampleBuffer() else {
            // 样本缓冲区为 nil 表示输入已结束。
            finishWritingAndResume()
            return
        }

        if let taggedBuffers = sampleBuffer.taggedBuffers, let taggedPixelBufferGroupReceiver {
            // 通过带标记像素缓冲区组接收器将带标记缓冲区发送给写入器输入。
            // 确保这些带标记缓冲区是带有 `layerID` 标签的 `CMTaggedDynamicBuffers`。
            let wellFormedTaggedBuffers = taggedBuffers.ensureLayerIDTagsAndMakeDynamic(leftEyeLayer: 0, rightEyeLayer: 1)
            do {
                let pts = sampleBuffer.presentationTimeStamp
                if try !taggedPixelBufferGroupReceiver.appendImmediately(wellFormedTaggedBuffers, with: pts) {
                    finishWritingAndResume(error: .appendTaggedBuffersFailed)
                    return
                }
            } catch {
                finishWritingAndResume(error: .appendTaggedBuffersFailed)
                return
            }
        } else {
            // 读取器输出是普通样本缓冲区。直接发送给写入器输入。
            writerInput.append(sampleBuffer)
        }
        // 发送异步通知以更新进度。
        let percent = (Double) (sampleBuffer.presentationTimeStamp.seconds / assetDuration)
        statusContinuation.yield(ExporterStatus.exporting(progress: percent))
    }
}
```

该循环从 [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) 读取样本缓冲区，后者应用了自定视频合成。对于空间视频输出，它使用带标记的像素缓冲区组；对于单目输出，它将样本缓冲区直接追加到写入器输入。

## 另请参阅

### 自定视频合成

- [AVVideoCompositing](avvideocompositing.md) — 一个协议，定义自定视频合成器必须实现的方法。

## 下载

- [ProcessingSpatialVideoWithACustomVideoCompositor.zip](https://docs-assets.developer.apple.com/published/31c34ca0bfce/ProcessingSpatialVideoWithACustomVideoCompositor.zip)
