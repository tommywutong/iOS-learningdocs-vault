---
title: 照片捕捉
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/photo-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/photo-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/photo-capture.json'
content_hash: 'sha256:35c5337625d69daa'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 照片捕捉

<sub>API 集合</sub>

捕捉高质量静态图像、实况照片以及配套的照片数据。

## 主题

### 照片捕捉

- [捕捉颜色一致的图像](capturing-consistent-color-images.md) — 借助新的 Constant Color API，为你的 App 带来摄影棚和灯光设备的力量。
- [捕捉静态照片和实况照片](capturing-still-and-live-photos.md) — 配置并捕捉单张或多张静态图像、实况照片以及其他形式的摄影内容。
- [以 RAW 和 Apple ProRAW 格式捕捉照片](capturing-photos-in-raw-and-apple-proraw-formats.md) — 通过在相机 App 中启用最少处理的图像捕捉，支持专业摄影工作流程。
- [在 Mac App 中支持连续互通相机](../appkit/supporting-continuity-camera-in-your-mac-app.md) — 使用连续互通相机，将用户 iPhone、iPad 或 iPod touch 扫描的文稿和图片融入你的 Mac App。
- [AVCapturePhoto](avcapturephoto.md) — 来自照片捕捉输出的图像数据容器。
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — 一种经轻度处理的照片，其中的数据可供系统稍后用于处理和获取更高分辨率的资产。
- [AVCapturePhotoOutput](avcapturephotooutput.md) — 用于静态图像、实况照片和其他摄影工作流程的捕捉输出。
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — 用于监控进度并接收照片捕捉输出结果的方法。
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — 一个监控照片输出捕捉就绪状态变化的对象。
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — 用于接收照片输出捕捉就绪状态更新的委托协议。
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — 用于捕捉静态照片的捕捉输出。_(已废弃)_

### 照片设置

- [AVCapturePhotoSettings](avcapturephotosettings.md) — 对单次照片捕捉请求所使用的特性与设置的规范。
- [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md) — 对以不同设置捕捉多张图像的照片捕捉请求所使用的特性与设置的规范。
- [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md) — 对进行中或已完成的照片捕捉请求所使用特性与设置的描述。

### 遮罩数据

- [AVPortraitEffectsMatte](avportraiteffectsmatte.md) — 一种辅助图像，用于以高分辨率将前景与背景分离。
- [AVSemanticSegmentationMatte](avsemanticsegmentationmatte.md) — 一个封装特定语义分割抠图图像的对象。

## 另请参阅

### 捕捉

- [捕捉设置](capture-setup.md) — 为媒体捕捉配置内置相机和麦克风，以及外部捕捉设备。
- [音频与视频捕捉](audio-and-video-capture.md) — 将音频和视频直接捕捉到媒体文件，或捕捉媒体流以直接访问媒体样本缓冲区。
- [附加数据捕捉](additional-data-capture.md) — 捕捉深度和元数据等附加数据，并同步来自多个输出的捕捉。
