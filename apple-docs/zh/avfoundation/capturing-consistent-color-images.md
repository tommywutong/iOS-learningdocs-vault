---
title: 拍摄色彩一致的照片
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-consistent-color-images
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-consistent-color-images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-consistent-color-images.json'
content_hash: 'sha256:24306926edd5e44e'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [照片拍摄](photo-capture.md)

# 拍摄色彩一致的照片

<sub>示例代码</sub>

通过全新的 Constant Color API，为你的 App 带来摄影工作室和灯光设备的力量。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC24 场次 10162：[Capturing consistent color images](https://developer.apple.com/wwdc24/10162/)。

### 配置示例代码项目

在提供了所需闪光灯模块的设备上运行本示例代码，例如以下设备：

- iPhone 14 或更高机型
- iPhone 14 Pro 或更高机型
- iPad Pro 11 英寸（M4）或更高机型
- iPad Pro 13 英寸（M4）或更高机型

## 另请参阅

### 照片拍摄

- [拍摄静态图像和实况照片](capturing-still-and-live-photos.md) — 配置并拍摄单张或多张静态图像、实况照片（Live Photo）以及其他形式的摄影。
- [以 RAW 和 Apple ProRAW 格式拍摄照片](capturing-photos-in-raw-and-apple-proraw-formats.md) — 在你的相机 App 中启用最低程度处理的图像拍摄，以支持专业摄影工作流。
- [在你的 Mac App 中支持连续互通相机](../appkit/supporting-continuity-camera-in-your-mac-app.md) — 使用连续互通相机将用户 iPhone、iPad 或 iPod touch 上扫描的文稿和图片整合到你的 Mac App 中。
- [AVCapturePhoto](avcapturephoto.md) — 来自照片拍摄输出的图像数据的容器。
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — 一种轻度处理的照片，其数据可供系统稍后用于处理并获取更高分辨率的媒体资源。
- [AVCapturePhotoOutput](avcapturephotooutput.md) — 用于静态图像、实况照片和其他摄影工作流的捕获输出。
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — 用于监控进度并接收照片拍摄输出结果的方法。
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — 一个监控照片输出的拍摄就绪状态变化的对象。
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — 用于接收照片输出拍摄就绪状态更新的委托协议。
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — 用于拍摄静态照片的捕获输出。 _(已废弃)_

## 下载

- [CapturingConsistentColorImages.zip](https://docs-assets.developer.apple.com/published/abe78d7af292/CapturingConsistentColorImages.zip)
