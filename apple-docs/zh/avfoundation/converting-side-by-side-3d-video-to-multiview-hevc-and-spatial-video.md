---
title: 将并排 3D 视频转换为多视图 HEVC 和空间视频
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 15.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video
source_url: 'https://developer.apple.com/documentation/avfoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.json'
content_hash: 'sha256:d268b1b2fc648bfe'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md)

# 将并排 3D 视频转换为多视图 HEVC 和空间视频

<sub>示例代码</sub>

通过把现有的 3D HEVC 文件转换为多视图 HEVC 格式来为 visionOS 创建视频内容，并可选择添加空间元数据以创建空间视频。

## 概述

在 visionOS 中，3D 视频采用 _多视图高效视频编码_（Multiview High Efficiency Video Encoding，MV-HEVC）格式，由 MPEG4 和 QuickTime 支持。与其他 3D 媒体不同，MV-HEVC 存储单个轨道，其中包含视频的多个图层，轨道和图层共享一个帧尺寸。这个轨道帧尺寸与其他 3D 视频类型（例如 _并排视频_）不同。并排视频使用单个轨道，把左眼和右眼图像并排放置，作为单个视频帧的一部分。

要把并排视频转换为 MV-HEVC，你需要载入源视频、提取每一帧，然后把帧水平切开。接着把切分后帧的左右两侧分别复制到左眼和右眼图层，并将一个同时包含两个图层的帧写入输出。

这个示例 App 演示了把并排视频文件转换为 MV-HEVC 的流程，并把输出编码为 QuickTime 文件。输出文件与输入文件放在同一目录中，文件名在原名后面附加 `_MVHEVC`。

对于用一致的相机配置拍摄的视频，你可以选择向输出文件添加空间元数据。_空间元数据_ 描述拍摄立体场景的左右眼相机的属性。

为立体 MV-HEVC 视频添加空间元数据，会让 Apple 平台把该视频视为 _空间的_（spatial）而不仅仅是立体的，并让视频有资格在 Apple Vision Pro 上获得可以尽量减少常见立体观看不适原因的视觉处理。

要进一步了解何时应为立体 MV-HEVC 视频提供空间元数据以及应提供哪些元数据值，参见[使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md)。

你可以用[读取多视图 3D 视频文件](reading-multiview-3d-video-files.md)中的示例项目打开并验证这个示例的 MV-HEVC 输出。

有关 MV-HEVC 格式的完整细节，参见 [Apple HEVC Stereo Video - Interoperability Profile (PDF)](https://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) 和 [ISO Base Media File Format and Apple HEVC Stereo Video (PDF)](https://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf)。

### 配置示例代码项目

这个 App 把一个并排立体输入视频文件的路径作为唯一的命令行参数。要在 Xcode 中运行这个 App，选择 Product \> Scheme \> Edit Scheme（Command-\<），并把你的文件路径添加到 Arguments Passed On Launch 中。

若还要为文件添加空间元数据，请在 Arguments Passed On Launch 中追加以下四个参数：

- `--spatial`（或 `-s`），表示你要包含空间元数据
- `--baseline`（或 `-b`），提供以毫米为单位的基线距离（例如，64mm 基线用 `--baseline 64.0`）
- `--fov`（或 `-f`），提供以度为单位的水平视场角（例如，80 度视场角用 `--fov 80.0`）
- `--disparityAdjustment`（或 `-d`），提供视差调整（例如，+2% 的正向视差偏移用 `--disparityAdjustment 0.02`）

默认情况下，项目的 scheme 会从 Xcode 项目文件夹载入名为 `Hummingbird.mov` 的并排视频。这段视频是一个 3D 场景的渲染序列，展示一个动画蜂鸟模型。默认情况下，App 会把这个示例视频转换为不带空间元数据的立体 MV-HEVC 文件。

要在转换时为蜂鸟视频添加空间元数据，选择 Product \> Scheme \> Edit Scheme（Command-\<），并勾选 Arguments Passed On Launch 栏中第二行参数左侧的复选框。这会启用以下附加参数：`--spatial --baseline 64.0 --fov 80.0 --disparityAdjustment 0.02`。

`--spatial` 参数告诉 App 把空间元数据写入输出视频。用于创建这些渲染的虚拟相机相距 64mm，水平视场角为 80 度，因此 `--baseline` 参数的值为 `64.0`，`--fov` 参数的值为 `80.0`。

对于这段视频，图像宽度 +2% 的视差调整可以在 Apple Vision Pro 的窗口中呈现空间视频时产生舒适的深度效果。这个 2% 的视差调整值把空间视频中最近的物体——蜂鸟——正好放在窗口前缘的后面，同时仍在蜂鸟与背景之间保持有效的深度错觉。scheme 的参数用 `--disparityAdjustment` 值 `0.02` 来表示这个 +2% 的视差调整。

### 载入并排视频

App 首先载入并排视频，创建一个 [AVAssetReader](avassetreader.md)。App 调用 [- loadTracksWithMediaCharacteristic:completionHandler:](<avasset/loadtracks(withmediacharacteristic_completionhandler_).md>) 来载入视频轨道，然后选择第一个可用轨道作为并排输入。

```swift
let asset = AVURLAsset(url: url)
reader = try AVAssetReader(asset: asset)

// Get the side-by-side video track.
guard let videoTrack = try await asset.loadTracks(withMediaCharacteristic: .visual).first else {
    fatalError("Error loading side-by-side video input")
}
```

App 还会存储并排视频的帧尺寸，并计算输出帧的尺寸。

```swift
sideBySideFrameSize = try await videoTrack.load(.naturalSize)
eyeFrameSize = CGSize(width: sideBySideFrameSize.width / 2, height: sideBySideFrameSize.height)
```

为完成视频载入，App 创建一个 [AVAssetReaderTrackOutput](avassetreadertrackoutput.md)，然后把这个输出流添加到 `AVAssetReader`。

```swift
let readerSettings: [String: Any] = [
    kCVPixelBufferIOSurfacePropertiesKey as String: [String: String]()
]
sideBySideTrack = AVAssetReaderTrackOutput(track: videoTrack, outputSettings: readerSettings)

if reader.canAdd(sideBySideTrack) {
    reader.add(sideBySideTrack)
}

if !reader.startReading() {
    fatalError(reader.error?.localizedDescription ?? "Unknown error during track read start")
}
```

创建 reader 轨道输出时，App 在 `readerSettings` 字典中指定文件的像素格式和 [IOSurface](../iosurface.md) 设置。App 通过使用 [kCVPixelBufferPixelFormatTypeKey](../corevideo/kcvpixelbufferpixelformattypekey.md) 并把值设为 [kCVPixelFormatType_32ARGB](../corevideo/kcvpixelformattype_32argb.md)，表明输出进入 32 位 ARGB 像素缓冲。这个示例 App 还管理自己的像素缓冲分配，把一个空数组作为 [kCVPixelBufferIOSurfacePropertiesKey](../corevideo/kcvpixelbufferiosurfacepropertieskey.md) 的值传入。

### 配置输出 MV-HEVC 文件

reader 初始化完成后，App 调用 `async` 方法 `transcodeToMVHEVC(output:spatialMetadata:)` 来生成输出文件。App 首先创建一个指向视频输出位置的新 [AVAssetWriter](avassetwriter.md)，然后在输出上配置必要的信息，表明该文件包含 MV-HEVC 视频。

```swift
var multiviewCompressionProperties: [CFString: Any] = [
    kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: MVHEVCVideoLayerIDs,
    kVTCompressionPropertyKey_MVHEVCViewIDs: MVHEVCViewIDs,
    kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: MVHEVCLeftAndRightViewIDs,
    kVTCompressionPropertyKey_HasLeftStereoEyeView: true,
    kVTCompressionPropertyKey_HasRightStereoEyeView: true
]
```

[kVTCompressionPropertyKey_HasLeftStereoEyeView](../videotoolbox/kvtcompressionpropertykey_hasleftstereoeyeview.md) 和 [kVTCompressionPropertyKey_HasRightStereoEyeView](../videotoolbox/kvtcompressionpropertykey_hasrightstereoeyeview.md) 为 `true`，因为输出为每只眼睛各包含一个图层。[kVTCompressionPropertyKey_MVHEVCVideoLayerIDs](../videotoolbox/kvtcompressionpropertykey_mvhevcvideolayerids.md)、[kVTCompressionPropertyKey_MVHEVCViewIDs](../videotoolbox/kvtcompressionpropertykey_mvhevcviewids.md) 和 [kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs](../videotoolbox/kvtcompressionpropertykey_mvhevcleftandrightviewids.md) 定义用于多视图 HEVC 编码的图层和视图 ID。在这个示例 App 中，它们完全相同。

这个示例 App 用 `0` 作为左眼图层/视图 ID，用 `1` 作为右眼图层/视图 ID。

```swift
let MVHEVCVideoLayerIDs = [0, 1]

// For simplicity, choose view IDs that match the layer IDs.
let MVHEVCViewIDs = [0, 1]

// The first element in this array is the view ID of the left eye.
let MVHEVCLeftAndRightViewIDs = [0, 1]
```

### 包含空间元数据

如果调用这个命令行 App 的人要求向输出文件添加空间元数据，并且提供了必要的空间元数据，App 会把这些元数据转换为预期的单位和标度，并为每个元数据值添加一个额外的压缩属性键。App 还会指定输入使用线性投影（rectilinear projection），以表明它具备空间视频所期望的投影方式。

```swift
if let spatialMetadata {

    let baselineInMicrometers = UInt32(1000.0 * spatialMetadata.baselineInMillimeters)
    let encodedHorizontalFOV = UInt32(1000.0 * spatialMetadata.horizontalFOV)
    let encodedDisparityAdjustment = Int32(10_000.0 * spatialMetadata.disparityAdjustment)

    multiviewCompressionProperties[kVTCompressionPropertyKey_ProjectionKind] = kCMFormatDescriptionProjectionKind_Rectilinear
    multiviewCompressionProperties[kVTCompressionPropertyKey_StereoCameraBaseline] = baselineInMicrometers
    multiviewCompressionProperties[kVTCompressionPropertyKey_HorizontalFieldOfView] = encodedHorizontalFOV
    multiviewCompressionProperties[kVTCompressionPropertyKey_HorizontalDisparityAdjustment] = encodedDisparityAdjustment

}
```

### 配置 MV-HEVC 输入源

App 通过直接从源帧复制像素来转码视频。向视频文件写入轨道数据需要一个 [AVAssetWriterInput](avassetwriterinput.md)。这个示例 App 使用 [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) 来提供来自源文件的像素数据并写入输出。

```swift
let multiviewSettings: [String: Any] = [
    AVVideoCodecKey: AVVideoCodecType.hevc,
    AVVideoWidthKey: self.eyeFrameSize.width,
    AVVideoHeightKey: self.eyeFrameSize.height,
    AVVideoCompressionPropertiesKey: multiviewCompressionProperties
]

guard multiviewWriter.canApply(outputSettings: multiviewSettings, forMediaType: AVMediaType.video) else {
    fatalError("Error applying output settings")
}

let frameInput = AVAssetWriterInput(mediaType: .video, outputSettings: multiviewSettings)

let sourcePixelAttributes: [String: Any] = [
    kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB,
    kCVPixelBufferWidthKey as String: self.sideBySideFrameSize.width,
    kCVPixelBufferHeightKey as String: self.sideBySideFrameSize.height
]

let bufferInputAdapter = AVAssetWriterInputTaggedPixelBufferGroupAdaptor(assetWriterInput: frameInput, sourcePixelBufferAttributes: sourcePixelAttributes)
```

`AVAssetWriterInput` 源使用与 `videoWriter` 相同的 `outputSettings`，创建的像素缓冲适配器与源具有相同的帧尺寸。App 遵循最佳实践：先调用 [- canAddInput:](<avassetwriter/canadd(__)-6al7j.md>) 检查输入适配器的兼容性，再调用 [- addInput:](<avassetwriter/add(__)-4c4d0.md>) 把它用作源。

```swift
guard multiviewWriter.canAdd(frameInput) else {
    fatalError("Error adding side-by-side video frames as input")
}
multiviewWriter.add(frameInput)
```

### 在输入可用时进行处理

App 依次调用 [- startWriting](<avassetwriter/startwriting().md>) 和 [- startSessionAtSourceTime:](<avassetwriter/startsession(atsourcetime_).md>) 来启动视频写入流程，然后使用 [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avassetwriterinput/requestmediadatawhenready(on_using_).md>) 迭代处理可用的帧输入。

```swift
guard multiviewWriter.startWriting() else {
    fatalError("Failed to start writing multiview output file")
}
multiviewWriter.startSession(atSourceTime: CMTime.zero)

// The dispatch queue executes the closure when media reads from the input file are available.
frameInput.requestMediaDataWhenReady(on: DispatchQueue(label: "Multiview HEVC Writer")) {
```

`requestMediaDataWhenReady(on:using:)` 的闭包参数会在第一次数据读取可用时在提供的 [DispatchQueue](../dispatch/dispatchqueue.md) 上运行。闭包自身负责管理处理媒体数据的资源，并运行一个循环来高效处理数据。

### 创建视频帧传输会话和输出像素缓冲池

为了执行从源轨道的数据传输，像素输入适配器需要一个像素缓冲作为源。App 创建一个 [VTPixelTransferSession](../videotoolbox/vtpixeltransfersession.md) 以便从视频源读取数据，并使用 `AVAssetWriterInputTaggedPixelBufferGroupAdaptor` 现有的像素缓冲池为新的多视图眼睛图层分配像素缓冲。

```swift
var session: VTPixelTransferSession? = nil
guard VTPixelTransferSessionCreate(allocator: kCFAllocatorDefault, pixelTransferSessionOut: &session) == noErr, let session else {
    fatalError("Failed to create pixel transfer")
}
guard let pixelBufferPool = bufferInputAdapter.pixelBufferPool else {
    fatalError("Failed to retrieve existing pixel buffer pool")
}
```

### 把帧图像从输入复制到输出

准备好资源后，App 开始一个循环来处理帧，直到没有更多数据，或输入读取已暂停以缓冲数据。输入源的 [readyForMoreMediaData](avassetwriterinput/isreadyformoremediadata.md) 属性为 `true` 时，表示立即可处理另一帧。当一帧就绪时，会由它创建一个 [CVImageBuffer](../corevideo/cvimagebuffer.md) 实例。

App 此时已准备好进行采样。如果有可用样本，App 会在 `convertFrame` 方法中处理它，然后调用 [appendTaggedBuffers(_:withPresentationTime:)](<avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(__withpresentationtime_).md>)，把并排样本缓冲的 [outputPresentationTimeStamp](../coremedia/cmsamplebuffer/outputpresentationtimestamp.md) 时间戳复制到新的多视图时间戳上。

```swift
while frameInput.isReadyForMoreMediaData && bufferInputAdapter.assetWriterInput.isReadyForMoreMediaData {
    if let sampleBuffer = self.sideBySideTrack.copyNextSampleBuffer() {
        guard let imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else {
            fatalError("Failed to load source samples as an image buffer")
        }
        let taggedBuffers = self.convertFrame(fromSideBySide: imageBuffer, with: pixelBufferPool, in: session)
        let newPTS = sampleBuffer.outputPresentationTimeStamp
        if !bufferInputAdapter.appendTaggedBuffers(taggedBuffers, withPresentationTime: newPTS) {
            fatalError("Failed to append tagged buffers to multiview output")
        }
```

当输入流中没有更多要处理的样本缓冲时，输入读取结束。App 调用 [- markAsFinished](<avassetwriterinput/markasfinished().md>) 关闭流，并调用 [- finishWritingWithCompletionHandler:](<avassetwriter/finishwriting(completionhandler_).md>) 完成多视图视频写入。App 还会在其关联的 [CheckedContinuation](../swift/checkedcontinuation.md) 上调用 [resume()](<../swift/checkedcontinuation/resume().md>) 以返回到 `await` 调用，然后跳出处理循环。

```swift
frameInput.markAsFinished()
multiviewWriter.finishWriting {
    continuation.resume()
}

break
```

### 把并排输入转换为视频图层输出

在 `convertFrame` 方法中，App 按 `layerID` 处理该帧的左右眼图像，左眼用 `0`，右眼用 `1`。首先，App 从缓冲池创建一个像素缓冲。

```swift
var pixelBuffer: CVPixelBuffer?
CVPixelBufferPoolCreatePixelBuffer(kCFAllocatorDefault, pixelBufferPool, &pixelBuffer)
guard let pixelBuffer else {
    fatalError("Failed to create pixel buffer for layer \(layerID)")
}
```

然后，该方法使用传入的 `VTPixelTransferSession` 从并排源复制像素，通过把帧裁剪为仅包含一只眼睛的图像，把它们放入创建的输出样本缓冲中。

```swift
// Crop the transfer region to the current eye.
let apertureOffset = -(self.eyeFrameSize.width / 2) + CGFloat(layerID) * self.eyeFrameSize.width
let cropRectDict = [
    kCVImageBufferCleanApertureHorizontalOffsetKey: apertureOffset,
    kCVImageBufferCleanApertureVerticalOffsetKey: 0,
    kCVImageBufferCleanApertureWidthKey: self.eyeFrameSize.width,
    kCVImageBufferCleanApertureHeightKey: self.eyeFrameSize.height
]
CVBufferSetAttachment(imageBuffer, kCVImageBufferCleanApertureKey, cropRectDict as CFDictionary, CVAttachmentMode.shouldPropagate)
VTSessionSetProperty(session, key: kVTPixelTransferPropertyKey_ScalingMode, value: kVTScalingMode_CropSourceToCleanAperture)

// Transfer the image to the pixel buffer.
guard VTPixelTransferSessionTransferImage(session, from: imageBuffer, to: pixelBuffer) == noErr else {
    fatalError("Error during pixel transfer session for layer \(layerID)")
}
```

在 [CVBufferSetAttachment(_:_:_:_:)](<../corevideo/cvbuffersetattachment(________).md>) 上设置光圈视图属性，定义了如何采集和裁剪输入图像。这里的光圈是一只眼睛图像的尺寸，采集帧的中心通过 [kCVImageBufferCleanApertureHorizontalOffsetKey](../corevideo/kcvimagebuffercleanaperturehorizontaloffsetkey.md) 偏移：左眼为 `-0.5 * width`，右眼为 `+0.5 * width`，从而采集并排帧中正确的一半。

App 接着调用 [VTSessionSetProperty(_:key:value:)](<../videotoolbox/vtsessionsetproperty(__key_value_).md>)，用 [kVTScalingMode_CropSourceToCleanAperture](../videotoolbox/kvtscalingmode_cropsourcetocleanaperture.md) 把图像裁剪到光圈框架内。随后，App 调用 [VTPixelTransferSessionTransferImage(_:from:to:)](<../videotoolbox/vtpixeltransfersessiontransferimage(__from_to_).md>) 把源像素复制到目标缓冲。

最后一步是为眼睛图像创建一个 [CMTaggedBuffer](../coremedia/cmtaggedbuffer.md)，返回给调用方的输出写入器。

```swift
let tags: [CMTag] = [.videoLayerID(Int64(layerID)), .stereoView(eye)]
let buffer = CMTaggedBuffer(tags: tags, buffer: .pixelBuffer(pixelBuffer))
taggedBuffers.append(buffer)
```

## 另请参阅

### 媒体写入

- [将投影视频转换为 Apple 投影媒体配置文件](converting-projected-video-to-apple-projected-media-profile.md) — 将等距柱状或半等距柱状投影的内容转换为 APMP。
- [向影片文件添加显示遮罩矩形元数据轨道](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — 使用定时显示遮罩矩形元数据显示视频的特定区域。
- [为 HTTP Live Streaming 写入分片 MPEG-4 文件](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — 通过把影片文件变成一系列分片 MPEG-4 文件来创建 HTTP Live Streaming 演示。
- [使用空间元数据创建空间照片和视频](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — 向立体照片和视频添加空间元数据，以创建可在 Apple Vision Pro 上观看的空间媒体。
- [使用视频色彩信息标记媒体](tagging-media-with-video-color-information.md) — 在写入和转码媒体时检查并设置视频色彩空间信息。
- [评估 App 的视频色彩](evaluating-an-app-s-video-color.md) — 使用测试图案、视频测试设备和光照测量仪器检查 App 中视频的色彩再现。
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — 一个构建音频和视频输出设置字典的对象。
- [AVAssetWriter](avassetwriter.md) — 一个将媒体数据写入容器文件的对象。
- [AVAssetWriterInput](avassetwriterinput.md) — 一个将媒体样本追加到 asset writer 的输出文件中的轨道的对象。
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — 一个将视频样本追加到 asset writer 输入的对象。 _(已废弃)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — 一个将标记的缓冲区组追加到 asset writer 输入的对象。 _(已废弃)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — 一个将定时元数据组追加到 asset writer 输入的对象。 _(已废弃)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — 一组输入，其轨道在播放或处理时互斥。

## 下载

- [ConvertingSideBySide3DVideoToMultiviewHEVCAndSpatialVideo.zip](https://docs-assets.developer.apple.com/published/4a60632cecb7/ConvertingSideBySide3DVideoToMultiviewHEVCAndSpatialVideo.zip)
