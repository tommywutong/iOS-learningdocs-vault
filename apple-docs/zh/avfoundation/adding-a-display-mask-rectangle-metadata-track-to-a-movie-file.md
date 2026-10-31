---
title: 向影片文件添加显示遮罩矩形元数据轨道
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 26.0+, Xcode 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/adding-a-display-mask-rectangle-metadata-track-to-a-movie-file
source_url: 'https://developer.apple.com/documentation/avfoundation/adding-a-display-mask-rectangle-metadata-track-to-a-movie-file'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.json'
content_hash: 'sha256:24c038cb1da50bce'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md)

# 向影片文件添加显示遮罩矩形元数据轨道

<sub>示例代码</sub>

使用定时显示遮罩矩形元数据显示视频的特定区域。

## 概述

QuickTime 影片可以提供显示遮罩矩形元数据，用于指示播放期间要显示的视频区域。在 visionOS 26 及更高版本上，系统会读取这些元数据，把视频裁剪到指定的显示区域，并把显示遮罩之外的区域渲染为透明。你可以利用显示遮罩在渲染时去掉编码进去的黑边（上下或左右），或者为创意效果动态更改视频的可见部分。

这个示例是一个命令行 App，演示了如何创建一个带显示遮罩矩形元数据的 QuickTime 影片文件。它添加一个定时元数据轨道来存储显示遮罩矩形元数据，并向视频关联一个渲染轨道引用（render track reference），以便把这种关联告知视频播放系统。

下面的几段屏幕录制展示了这个示例 App 添加的显示遮罩矩形元数据（两种类型）与原始影片文件相比对显示出的视频有何影响。

**原始**

[一段屏幕录制，显示一段流淌的河流的视频文件。整个编码后的视频都被显示出来。](https://docs-assets.developer.apple.com/published/73779de5438404660b1bf88425ff2be3/river_orig.mov)

**类型 1 - 静态显示遮罩**

[一段屏幕录制，显示视频播放期间应用固定且居中的显示遮罩。只有视频中央的方形部分被显示出来，其余部分为透明，并显示环境的穿透画面。](https://docs-assets.developer.apple.com/published/a78d1cae2c07ead6531541896828d66d/river_displaymasktype1.mov)

**类型 2 - 动态显示遮罩**

[一段屏幕录制，显示视频播放期间应用弹跳方块显示遮罩。只有视频的一小块方形区域可见，其余部分为透明，并显示环境的穿透画面。播放期间，这小块方形视频在编码后的视频尺寸范围内移动。](https://docs-assets.developer.apple.com/published/a0418ac0f91dc5f5a1250a07339fa6f3/river_displaymasktype2.mov)

> [!note] 注意
> 有关这种元数据类型细节的信息，参见 [Rectangular Mask Payload Metadata within the QuickTime Movie File Format - Format addition](https://developer.apple.com/av-foundation/Rectangular-Dynamic-Mask-Metadata.pdf)。

## 配置示例代码项目

这个示例需要三个参数：

```bash
./AVAddDisplayMaskTrack <input-path> <output-path> <display-mask-type>
```

- **`<input-path>`** — 现有源 QuickTime 影片文件的路径，该文件需带有视频轨道。
- **`<output-path>`** — 新的输出 QuickTime 影片文件的路径，其中包含源影片文件的媒体轨道以及额外的显示遮罩矩形定时元数据轨道。
- **`<display-mask-type>`** — 显示遮罩的整数类型。只有两种类型：`1` 或 `2`；如果未提供第三个参数或该值无效，默认为 `1`。

`display-mask-type` 参数指示要写入影片文件的显示遮罩：

- 类型 1 显示遮罩是一个静态正方形，占视频尺寸较短边的 75%，并在影片的整个时长内居中于视频画面。例如，如果视频尺寸为 1920 x 1080，则显示遮罩为 810 x 810（1080 `*` 0.75 = 810），中心位于 (960, 540)。
- 类型 2 显示遮罩是逐帧的正方形遮罩，占视频尺寸较短边的 30%，并在视频画面上移动。这种类型演示了以关联视频轨道的帧率更新的动态显示遮罩元数据。

## 设置显示遮罩矩形元数据轨道

这个示例提供了一个 `MovieProcessor` 类，其中包含 App 的元数据处理逻辑。运行 App 时，它会把指定的命令行参数传给 `MovieProcessor` 类的 `processMovie(inputPath:outputPath:displayMaskType:)` 方法。这个方法分别使用 [AVAssetReader](avassetreader.md) 和 [AVAssetWriter](avassetwriter.md) 搭建读取和写入功能。

为了让 App 在进行 asset 写入期间能够追加元数据，该方法调用 `addDisplayMaskMetadataTrack(to:videoInput:videoInfo:)` 创建一个 [AVAssetWriterInput](avassetwriterinput.md)，为显示遮罩矩形写入定时元数据轨道。在创建这个 writer 输入之前，该方法会为显示遮罩元数据创建一个 [CMMetadataFormatDescription](../coremedia/cmmetadataformatdescription.md)。该格式描述使用装箱元数据（`mebx`）类型，并把 [kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono](../coremedia/kcmmetadataidentifier_quicktimemetadatadisplaymaskrectanglemono.md) 标识符与 [kCMMetadataBaseDataType_RasterRectangleValue](../coremedia/kcmmetadatabasedatatype_rasterrectanglevalue.md) 数据类型配对：

```swift
// Define the metadata specifications for the monoscopic display mask rectangle.
let metadataSpecifications: [[String: Any]] = [[
    kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier as String:
        kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono as String,
    kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType as String:
        kCMMetadataBaseDataType_RasterRectangleValue as String
]]

// Create the `CMMetadataFormatDescription` for the monoscopic display mask rectangle
// in boxed metadata (`mebx`) type.
var metadataFormatDesc: CMMetadataFormatDescription? = nil
let status = CMMetadataFormatDescriptionCreateWithMetadataSpecifications(
    allocator: kCFAllocatorDefault,
    metadataType: kCMMetadataFormatType_Boxed,
    metadataSpecifications: metadataSpecifications as CFArray,
    formatDescriptionOut: &metadataFormatDesc
)
```

> [!note] 注意
> 如果你需要在这个定时元数据轨道中存储其他元数据，`metadataSpecifications` 数组可以包含更多的标识符与数据类型配对。其他元数据标识符和数据类型的列表参见 [CMMetadata](../coremedia/cmmetadata.md)。

格式描述就绪后，该方法为元数据轨道创建一个 [AVAssetWriterInput](avassetwriterinput.md)。它把 [expectsMediaDataInRealTime](avassetwriterinput/expectsmediadatainrealtime.md) 设为 `false`，因为 App 以其处理能力允许的速度尽快写入元数据样本，而不是从实时采集源接收它们。它还把 [mediaTimeScale](avassetwriterinput/mediatimescale.md) 设为与视频轨道一致，使元数据样本的时间戳与视频帧精确对齐：

```swift
// Create the `AVAssetWriterInput` for the display mask metadata track and attach it to `AVAssetWriter`.
metadataInput = AVAssetWriterInput(mediaType: .metadata, outputSettings: nil, sourceFormatHint: metadataFormatDesc)
guard let metadataInput else {
    throw ProcessingError.writerInputCreationFailed("DisplayMask metadata.")
}

metadataInput.expectsMediaDataInRealTime = false
metadataInput.mediaTimeScale = videoInfo.timescale
```

该方法随后创建一个 [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) 来向 writer 输入追加定时元数据组。这个适配器提供了一种便捷方式来写入 [AVTimedMetadataGroup](avtimedmetadatagroup.md) 对象——它们把元数据项目与其时间范围打包在一起——而无需直接操作样本缓冲：

```swift
// Create the metadata adaptor for the display mask metadata's `AVAssetWriterInput`.
metadataAdaptor = AVAssetWriterInputMetadataAdaptor(assetWriterInput: metadataInput)
```

最后，该方法把元数据输入添加到 asset writer，并在元数据轨道与视频轨道之间建立轨道关联。渲染元数据源关联（`rndr`）是必需的，这样播放系统才知道显示遮罩元数据作用于哪条视频轨道。如果不存在这种关联，播放系统会忽略这些元数据。

```swift
if writer.canAdd(metadataInput) {
    writer.add(metadataInput)

    // Add the `rndr` track association between the display mask metadata track and
    // the enabled video track.
    metadataInput.addTrackAssociation(withTrackOf: videoInput, type: AVAssetTrack.AssociationType.renderMetadataSource.rawValue)
} else {
    throw ProcessingError.cannotAddWriterInput("DisplayMask metadata.")
}
```

## 写入显示遮罩矩形元数据

`setupDisplayMaskMetadataTransfer(videoInfo:maskType:)` 方法负责把显示遮罩元数据样本写入定时元数据轨道。该方法使用视频轨道的尺寸来计算光栅矩形参数，并使用先前创建的适配器写入元数据样本。

根据你在命令行指定的显示遮罩类型，该方法走两条路径之一：

- 类型 1 创建一个静态显示遮罩——一个居中的正方形，在视频的整个时长内保持固定。
- 类型 2 创建一个动态显示遮罩——一个在画面上移动的较小正方形，每个视频帧都有一个对应的元数据样本。

要查看每条路径使用的具体计算，请查看示例项目中的 `MovieProcessor.swift` 文件，找到 `Type 1 static display mask calculation.` 和 `Type 2 dynamic display mask initialization/update calculation.` 标记。

尽管写入的元数据不同，两条路径都遵循相似的模式：在元数据输入就绪时请求数据，为显示遮罩矩形创建一个定时元数据组，然后把它追加到元数据适配器：

```swift
metadataInput.requestMediaDataWhenReady(on: queue) {
    while metadataInput.isReadyForMoreMediaData {
        let rasterRectangle = // Calculate the raster rectangle parameters for this media sample.

        // Create the timed metadata group and append it.
        let metadataGroup = self.createMetadataGroupForDisplayMask(
            rasterRectangle: rasterRectangle,
            sampleTime: sampleTime,
            sampleDuration: sampleDuration
        )
        // Append the metadata group.
        metadataAdaptor.append(metadataGroup)
    }
}
```

`createMetadataGroupForDisplayMask(rasterRectangle:sampleTime:sampleDuration:)` 方法创建这个定时元数据组：

```swift
private func createMetadataGroupForDisplayMask(rasterRectangle: [Int],
                sampleTime: CMTime, sampleDuration: CMTime) -> AVTimedMetadataGroup {
    let metadataItem = AVMutableMetadataItem()
    metadataItem.identifier = AVMetadataIdentifier(
        kCMMetadataIdentifier_QuickTimeMetadataDisplayMaskRectangleMono as String)
    metadataItem.value = rasterRectangle as NSArray
    metadataItem.dataType = kCMMetadataBaseDataType_RasterRectangleValue as String

    // Wrap the metadata item in `AVTimedMetadataGroup`.
    let timedMetadataGroup = AVTimedMetadataGroup(
        items: [metadataItem],
        timeRange: CMTimeRange(start: sampleTime, duration: sampleDuration)
    )

    return timedMetadataGroup
}
```

这个方法创建一个带显示遮罩标识符和数据类型的 [AVMutableMetadataItem](avmutablemetadataitem.md)，把它的值设为光栅矩形数组，并用指定的时间范围把它包装进一个 [AVTimedMetadataGroup](avtimedmetadatagroup.md)。`rasterRectangle` 参数是一个包含六个整数的数组：`[rasterWidth, rasterHeight, left, width, top, height]`。时间范围决定这些元数据在播放期间的生效时机：

- 对于静态遮罩，时间范围横跨整个视频时长。
- 对于动态遮罩，时间范围与单个视频帧的时长相匹配。

当 asset writer 完成后，输出文件就包含了带显示遮罩矩形元数据轨道的原始视频。在 visionOS 26 或更高版本上，你可以在“文件”等 App 中播放该文件，查看显示遮罩效果。

## 另请参阅

### 媒体写入

- [将投影视频转换为 Apple 投影媒体配置文件](converting-projected-video-to-apple-projected-media-profile.md) — 将等距柱状或半等距柱状投影的内容转换为 APMP。
- [将并排 3D 视频转换为多视图 HEVC 和空间视频](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — 通过把现有的 3D HEVC 文件转换为多视图 HEVC 格式来为 visionOS 创建视频内容，并可选择添加空间元数据以创建空间视频。
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

- [AddingADisplayMaskRectangleMetadataTrackToAMovieFile.zip](https://docs-assets.developer.apple.com/published/bd2961a0172a/AddingADisplayMaskRectangleMetadataTrackToAMovieFile.zip)
