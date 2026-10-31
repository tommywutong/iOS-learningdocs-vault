---
title: 附加数据捕捉
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/additional-data-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/additional-data-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/additional-data-capture.json'
content_hash: 'sha256:bfc9ffb3ee012bd1'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 附加数据捕捉

<sub>API 集合</sub>

捕捉深度和元数据等附加数据，并同步来自多个输出的捕捉。

## 主题

### 深度数据捕捉

- [捕捉带深度的照片](capturing-photos-with-depth.md) — 获取带深度图的照片，以创建类似系统相机人像模式的效果（在兼容设备上）。
- [手动创建辅助深度数据](creating-auxiliary-depth-data-manually.md) — 生成深度图像并将其附加到你自己的图像上。
- [使用 LiDAR 相机捕捉深度数据](capturing-depth-using-the-lidar-camera.md) — 在支持的设备上访问 LiDAR 相机，以捕捉精确的深度数据。
- [AVCamFilter：为捕捉流应用滤镜](avcamfilter-applying-filters-to-a-capture-stream.md) — 以玫瑰色滤镜和深度效果渲染捕捉流。
- [从 TrueDepth 相机串流深度数据](streaming-depth-data-from-the-truedepth-camera.md) — 以 2D 和 3D 形式可视化来自 TrueDepth 相机的深度数据。
- [利用 TrueDepth 相机数据增强实况视频](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — 为来自前置 TrueDepth 相机的实况捕捉画面应用你自己的背景。
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — 一种捕捉输出，在兼容的相机设备上记录场景深度信息。
- [AVDepthData](avdepthdata.md) — 一个容器，用于存放由兼容相机设备捕捉的逐像素距离或视差信息。
- [AVCameraCalibrationData](avcameracalibrationdata.md) — 关于用于捕捉图像和深度数据的相机特性的信息。

### 元数据捕捉

- [AVCaptureMetadataInput](avcapturemetadatainput.md) — 一种向捕捉会话提供定时元数据的捕捉输入。
- [AVCaptureMetadataOutput](avcapturemetadataoutput.md) — 一种处理由捕捉会话产生的定时元数据的捕捉输出。
- [AVMetadataObject](avmetadataobject.md) — 由元数据捕捉输出提供的对象的抽象超类。
- [元数据类型](metadata-types.md) — 检查该框架支持的元数据对象类型。

### 同步捕捉

- [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) — 一个协调多个捕捉输出按时匹配交付数据的对象。
- [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) — 同时从多个捕捉输出收集的一组数据样本。
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — 使用同步捕捉收集的视频或音频样本的容器。
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — 使用同步捕捉收集的元数据对象的容器。
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md) — 使用同步捕捉收集的场景深度信息的容器。
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md) — 使用同步捕捉收集的媒体样本的抽象超类。

## 另请参阅

### 捕捉

- [捕捉设置](capture-setup.md) — 为媒体捕捉配置内置相机和麦克风，以及外部捕捉设备。
- [照片捕捉](photo-capture.md) — 捕捉高质量静态图像、实况照片以及配套的照片数据。
- [音频与视频捕捉](audio-and-video-capture.md) — 将音频和视频直接捕捉到媒体文件，或捕捉媒体流以直接访问媒体样本缓冲区。
