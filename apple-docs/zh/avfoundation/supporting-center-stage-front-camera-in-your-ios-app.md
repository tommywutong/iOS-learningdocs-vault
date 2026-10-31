---
title: 在 iOS App 中支持舞台居中前置相机
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/supporting-center-stage-front-camera-in-your-ios-app
source_url: 'https://developer.apple.com/documentation/avfoundation/supporting-center-stage-front-camera-in-your-ios-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/supporting-center-stage-front-camera-in-your-ios-app.json'
content_hash: 'sha256:eb1823c92330ed2e'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md)

# 在 iOS App 中支持舞台居中前置相机

<sub>示例代码</sub>

在 iPhone 前置相机上为照片和视频启用舞台居中。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC26 场次 341：[Support Center Stage front camera in your iOS app](https://developer.apple.com/videos/play/wwdc2026/341)。

## 配置示例代码项目

在配备舞台居中前置相机的 iPhone 上运行本示例代码，例如 iPhone 17、iPhone Air 或 iPhone 17 Pro。

## 另请参阅

### 捕捉会话

- [设置捕捉会话](setting-up-a-capture-session.md) — 在捕捉照片或视频之前配置输入设备、输出媒体、预览视图和基本设置。
- [在 iPad 上多任务处理时访问相机](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — 在分屏浏览、侧拉、画中画和舞台管理模式下操作相机。
- [AVCam：构建相机 App](avcam-building-a-camera-app.md) — 使用 iPhone 和 iPad 的前后置相机拍摄照片和录制视频。
- [构建启动迅速的响应式相机 App](build-a-responsive-camera-app-that-launches-quickly.md) — 为你的 iOS 和 iPadOS App 构建快速的相机启动体验。
- [捕捉电影效果视频](capturing-cinematic-video.md) — 捕捉具有可调景深和焦点的视频。
- [AVMultiCamPiP：从多个相机捕捉](avmulticampip-capturing-from-multiple-cameras.md) — 使用多相机捕捉会话，将前后相机的输出同时录制到单个电影文件中。
- [AVCamBarcode：检测条形码和人脸](avcambarcode-detecting-barcodes-and-faces.md) — 使用相机识别机器可读代码或人脸。
- [AVCaptureSession](avcapturesession.md) — 一个配置捕捉行为并协调从输入设备到捕捉输出数据流的对象。
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — 一种捕捉会话，支持从同一媒体类型的多个输入同时捕捉。
- [AVCaptureInput](avcaptureinput.md) — 为捕捉会话提供输入数据的对象的抽象超类。
- [AVCaptureOutput](avcaptureoutput.md) — 为捕捉会话提供媒体输出目的地的对象的抽象超类。
- [AVCaptureConnection](avcaptureconnection.md) — 一个表示从捕捉输入到捕捉输出之间连接的对象。

## 下载

- [SupportingCenterStageFrontCameraInYourIOSApp.zip](https://docs-assets.developer.apple.com/published/8670064af87f/SupportingCenterStageFrontCameraInYourIOSApp.zip)
