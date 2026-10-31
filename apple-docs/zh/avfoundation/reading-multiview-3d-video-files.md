---
title: 读取多视图 3D 视频文件
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 14.0+, Xcode 15.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/reading-multiview-3d-video-files
source_url: 'https://developer.apple.com/documentation/avfoundation/reading-multiview-3d-video-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/reading-multiview-3d-video-files.json'
content_hash: 'sha256:69849c0a810ec0e3'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读写](media-reading-and-writing.md)

# 读取多视图 3D 视频文件

<sub>示例代码</sub>

通过读取单独的视频帧，从多视图高效视频编码（MV-HEVC）格式文件渲染左眼和右眼的单一图像。

## 概述

多视图高效视频编码（Multiview High Efficiency Video Coding，MV-HEVC）媒体文件包含生成立体帧的信息——一帧供左眼、一帧供右眼——以营造深度效果并实现 3D 视频。这是在 visionOS 中呈现 3D 视频的标准格式，编码为 MPEG-4 或 QuickTime 文件。

在没有硬件的情况下预览和测试 MV-HEVC 文件，需要能够在时间线上加载、查看并逐帧步进视频数据。这个示例 App 会打开一个媒体文件，检查其是否为 MV-HEVC 格式，然后呈现一个视图，显示时间戳处的各个帧。通过将滑块拖动到特定时间戳来在时间线上步进，或按空格键前进到下一帧。

有关 MV-HEVC 格式的完整细节，请参阅 [Apple HEVC Stereo Video - Interoperability Profile (PDF)](https://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) 和 [ISO Base Media File Format and Apple HEVC Stereo Video (PDF)](https://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf)。

### 加载并检查媒体资源

该 App 首先显示一个标签为 Open MVHEVC File 的按钮。选中后，该按钮会呈现一个 [NSOpenPanel](../appkit/nsopenpanel.md) 用于选择视频媒体。接下来，App 初始化一个 `MediaDetailViewModel`，将该文件加载为 [AVURLAsset](avurlasset.md)。在打开文件以呈现立体视频帧的任何元素之前，App 会确保该文件可播放、可读取，并获取其总时长。这一切都在初始化方法中完成。

```swift
init(filename: URL) {
    asset = AVURLAsset(url: filename)
    Task { @MainActor in
        do {
            let (duration, isPlayable, isReadable) = try await asset.load(.duration, .isPlayable, .isReadable)
            self.duration = duration.seconds
            self.isPlayable = isPlayable
            self.isReadable = isReadable
        } catch {
            self.error = error
        }
    }
}
```

### 加载轨道数据和时间戳

在确认轨道是可读取的视频数据后，App 通过调用 [- loadTracksWithMediaCharacteristic:completionHandler:](<avasset/loadtracks(withmediacharacteristic_completionhandler_).md>) 请求一个 [AVMediaCharacteristicContainsStereoMultiviewVideo](avmediacharacteristic/containsstereomultiviewvideo.md) 轨道来初始化 `StereoViewModel`。这项检查确认文件符合 MV-HEVC 规范并拥有有效的立体数据。

```swift
if let track = try await asset.loadTracks(withMediaCharacteristic: .containsStereoMultiviewVideo).first {
    self.track = track
```

接下来，App 通过调用 `presentationTimesFor(track:asset:)` 获取轨道中每一帧的可用时间戳。App 使用 [- makeSampleCursorAtFirstSampleInDecodeOrder](<avassettrack/makesamplecursoratfirstsampleindecodeorder().md>) 将视频样本光标放在轨道的开头，然后创建一个新的 [AVSampleBufferGenerator](avsamplebuffergenerator.md) 和 [AVSampleBufferRequest](avsamplebufferrequest.md)。

```swift
guard let cursor = track.makeSampleCursorAtFirstSampleInDecodeOrder() else {
    return []
}
let sampleBufferGenerator = AVSampleBufferGenerator(asset: asset, timebase: nil)
var presentationTimes = [CMTime]()
let request = AVSampleBufferRequest(start: cursor)
var numSamples: Int64 = 0
```

要读取时间戳，请通过 [- createSampleBufferForRequest:error:](<avsamplebuffergenerator/makesamplebuffer(for_).md>) 获取当前光标的样本缓冲区，然后添加该帧的 [presentationTimeStamp](../coremedia/cmsamplebuffer/presentationtimestamp.md)。通过调用 [- stepInDecodeOrderByCount:](<avsamplecursor/stepindecodeorder(bycount_).md>) 让光标向前步进，读取并缓存缓冲区中每一帧的时间戳。当 `stepInDecodeOrder(byCount:)` 不再返回下一帧时，样本时间已全部进入缓存，视频轨道的读取即告完成。

```swift
repeat {
    let buf = try sampleBufferGenerator.makeSampleBuffer(for: request)
    presentationTimes.append(buf.presentationTimeStamp)
    numSamples = cursor.stepInDecodeOrder(byCount: 1)
} while numSamples == 1
```

### 加载视频图层信息

准备好时间戳后，App 调用 `loadVideoLayerIdsForTrack()` 来获取与左眼和右眼相关联的两个轨道的图层 ID。App 调用 [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) 来获取元数据，然后从第一个可用轨道的 [tagCollections](../coremedia/cmformatdescription/tagcollections.md) 中过滤出图层数据。过滤谓词是 [value(onlyIfMatching:)](<../coremedia/cmtag-swift.class/value(onlyifmatching_).md>)，只提取视频图层 ID。

```swift
private func loadVideoLayerIdsForTrack(_ videoTrack: AVAssetTrack) async throws -> [Int64]? {
    let formatDescriptions = try await videoTrack.load(.formatDescriptions)
    var tags = [Int64]()
    if let tagCollections = formatDescriptions.first?.tagCollections {
        tags = tagCollections.flatMap({ $0 }).compactMap { tag in
            tag.value(onlyIfMatching: .videoLayerID)
        }
    }
    return tags
}
```

### 从缓冲区加载视频帧

在识别出时间戳以及左眼和右眼视频图层之后，`readBufferFromAsset(at:)` 会调用 App 的 `readNextBufferFromAsset()` 方法来获取并显示帧数据。该方法以一系列 `guard` 检查开始，以确保对轨道的读取权限，通过调用 [- copyNextSampleBuffer](<avassetreaderoutput/copynextsamplebuffer().md>) 创建样本缓冲区的本地副本，并从轨道中获取带标签的视频缓冲区。

```swift
guard let assetReader, let trackOutput else {
    return
}
guard assetReader.status == .reading else {
    publishState(.error(message: "UNEXPECTED STATUS \(assetReader.status)"))
    return
}
guard let sampleBuffer = trackOutput.copyNextSampleBuffer() else {
    publishState(.error(message: "READING SAMPLE BUFFER, STATUS \(assetReader.status), ERROR \(String(describing: assetReader.error))"))
    return
}
guard let taggedBuffers = sampleBuffer.taggedBuffers else {
    publishState(.error(message: "SAMPLE BUFFER CONTAINS NO TAGGED BUFFERS: \(sampleBuffer)"))
    return
}
guard taggedBuffers.count == 2 else {
    publishState(.error(message: "EXPECTED 2 TAGGED BUFFERS, GOT \(taggedBuffers.count)"))
    return
}
```

App 使用 [init(cvPixelBuffer:)](<../coreimage/ciimage/init(cvpixelbuffer_)-3wng7.md>) 将返回的样本缓冲区中的每个 [CMTaggedBuffer.Buffer.pixelBuffer(_:)](<../coremedia/cmtaggedbuffer/buffer-swift.enum/pixelbuffer(__).md>) 解析为用于显示的图像。App 创建一个 [NSImage](../appkit/nsimage.md)，并根据视图包含的是左眼还是右眼的 [stereoView(_:)](<../coremedia/cmtag-swift.class/stereoview(__).md>)，将其设置为视图内容 `leftEye` 或 `rightEye`。

```swift
taggedBuffers.forEach { taggedBuffer in
    switch taggedBuffer.buffer {
    case let .pixelBuffer(pixelBuffer):
        let ciimage = CIImage(cvPixelBuffer: pixelBuffer)
        let context: CIContext = CIContext(options: nil)
        let cgImage: CGImage = context.createCGImage(ciimage, from: ciimage.extent)!
        let tags = taggedBuffer.tags
        Task {
            await MainActor.run {
                let nsImage = NSImage(cgImage: cgImage, size: NSSize(width: 320, height: 240))
                if tags.contains(.stereoView(.leftEye)) {
                    leftEye = nsImage
                } else if tags.contains(.stereoView(.rightEye)) {
                    rightEye = nsImage
                }
            }
        }
    case .sampleBuffer(let samp):
        publishState(.error(message: "EXPECTED PIXEL BUFFER, GOT SAMPLE BUFFER \(samp)"))
    @unknown default:
        publishState(.error(message: "EXPECTED PIXEL BUFFER TYPE, GOT \(taggedBuffer.buffer)"))
    }
}
```

## 另请参阅

### 媒体读取

- [AVAssetReader](avassetreader.md) — 一个从媒体资源读取媒体数据的对象。
- [AVAssetReaderOutput](avassetreaderoutput.md) — 一个抽象类，定义了从媒体资源读取器读取媒体样本的接口。
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — 一个从媒体资源的单个轨道读取媒体数据的对象。
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — 一个读取混音结果音频样本的对象，混音来自一个或多个轨道的音频。
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — 一个从媒体资源的一个或多个轨道读取合成视频帧的对象。
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — 一个从媒体资源轨道读取样本引用的对象。
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — 一个为媒体资源轨道创建定时元数据组对象的对象。 _(已废弃)_

## 下载

- [ReadingMultiview3DVideoFiles.zip](https://docs-assets.developer.apple.com/published/03b0a926288f/ReadingMultiview3DVideoFiles.zip)
