---
title: 构建快速启动的响应式相机 App
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/build-a-responsive-camera-app-that-launches-quickly
source_url: 'https://developer.apple.com/documentation/avfoundation/build-a-responsive-camera-app-that-launches-quickly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/build-a-responsive-camera-app-that-launches-quickly.json'
content_hash: 'sha256:480e1aac4cd69be7'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕获设置](capture-setup.md)

# 构建快速启动的响应式相机 App

<sub>示例代码</sub>

为你的 iOS 和 iPadOS App 构建快速的相机启动体验。

## 概述

本示例演示了如何使用延迟启动 API，以及如何将 UI 元素推迟到预览开始运行之后再显示，从而优化相机 App 的启动。FastCameraLaunch 示例基于 AVCam 构建。有关 AVCam 的更多细节，请参阅 [AVCam：构建相机 App](avcam-building-a-camera-app.md)。

> [!note] 注意
> 本示例代码项目关联 WWDC26 场次 303：[Build a responsive camera app that launches quickly](https://developer.apple.com/wwdc26/303/)。

## 配置示例代码项目

示例 App FastCameraLaunch 需要以下条件：

- Xcode 27。
- 一台运行 iOS 27 或更高版本的 iOS 设备。
- FastCameraLaunch 在模拟器中无法工作，因为 Xcode 无法访问相机。

## 推迟非关键的 UI 元素

App 的 UI 在相机启动体验中扮演着重要角色。在设计启动流程时，请将 App 的启动划分为两个阶段：

- 启动和显示预览所需的关键资源
- 可以在预览开始运行之后再创建的资源

在 FastCameraLaunch 中，有以下几个 UI 元素：相机预览、快门按钮、图像池和模式选择器。相机预览是人们启动 App 时最关键的 UI 元素。图像池和模式选择器在预览渲染之前并不需要，因此这部分工作需要等到预览开始之后进行。

下面这个示例展示了如何考虑将元素推迟到启动之后：

```swift
@State var camera: CameraModel
var body: some View {
    HStack {
        if camera.status == .running {
            ThumbnailButton(camera: camera)
                // 当用户与拍摄控制交互时隐藏缩略图按钮。
                .opacity(camera.prefersMinimizedUI ? 0 : 1)
                .transition(.opacity.animation(.easeIn(duration: 0.3).delay(0.2)))
        }
        Spacer()
        CaptureButton(camera: camera)
        Spacer()
        if camera.status == .running {
            SwitchCameraButton(camera: camera)
                // 当用户与拍摄控制交互时隐藏相机选择。
                .opacity(camera.prefersMinimizedUI ? 0 : 1)
                .transition(.opacity.animation(.easeIn(duration: 0.3).delay(0.2)))
        }
    }
    .foregroundColor(.white)
}
```

## 选择加入延迟启动

初始化 [AVCaptureOutput](avcaptureoutput.md) 对象的开销很大，会显著拖慢启动速度。App 只需要初始化一个输出即可渲染预览。[AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) 和 [AVCapturePhotoOutput](avcapturephotooutput.md) 等输出对于预览来说并非必要，而 [AVCaptureVideoPreviewLayer](avcapturevideopreviewlayer.md) 则必不可少。要减少花在 `AVCaptureOutput` 初始化上的时间，请使用延迟启动（Deferred Start）API。

每个 `AVCaptureOutput` 和 `AVCaptureVideoPreviewLayer` 对象都有一个 `isDeferredStartEnabled` 属性。将此属性设置为 `true` 即可推迟一个输出。为了优化启动速度，请推迟除 App 用于渲染预览的那个输出之外的所有输出。

App 可以通过两种方式指定何时运行这些初始化：自动启动（Automatic Start）和手动启动（Manual Start）。

对于针对 iOS 26.0 SDK 重新编译的 App，默认行为是以自动模式运行。使用自动模式时，`automaticallyRunsDeferredStart` 属性被设置为 `true`

```swift
// 延迟启动。
captureSession.automaticallyRunsDeferredStart = true
photoCapture.output.isDeferredStartEnabled = true
captureSession.setDeferredStartDelegate(deferredStartDelegate, deferredStartDelegateCallbackQueue: sessionQueue)
// 提交捕获会话配置。
captureSession.commitConfiguration()
```

如果你想在 App 中对这个控制进行微调，延迟启动 API 通过 `runDeferredStartWhenNeeded` 属性提供了一个手动启动选项。

要选择加入这种模式，请将 [AVCaptureSession](avcapturesession.md) 上的 `automaticallyRunsDeferredStart` 属性设置为 `false`。

当 App 完成其启动操作（例如非关键资源的创建）后，调用 AVCaptureSession 上的 `runDeferredStartWhenNeeded` 方法，告知系统现在是运行延迟启动初始化的好时机。

## 另请参阅

### 捕获会话

- [设置捕获会话](setting-up-a-capture-session.md) — 在拍摄照片或视频之前配置输入设备、输出媒体、预览视图和基本设置。
- [在 iPad 上多任务处理时访问相机](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — 在分屏浏览、侧拉、画中画和台前调度模式下操作相机。
- [AVCam：构建相机 App](avcam-building-a-camera-app.md) — 使用 iPhone 和 iPad 的前后摄像头拍摄照片和录制视频。
- [拍摄电影效果视频](capturing-cinematic-video.md) — 拍摄具有可调景深和焦点的视频。
- [在你的 iOS App 中支持 Center Stage 前置摄像头](supporting-center-stage-front-camera-in-your-ios-app.md) — 在 iPhone 前置摄像头拍摄的照片和视频中启用人物居中功能。
- [AVMultiCamPiP：从多个相机捕获](avmulticampip-capturing-from-multiple-cameras.md) — 使用多相机捕获会话将前后摄像头的输出同时录制到一个影片文件中。
- [AVCamBarcode：检测条形码和人脸](avcambarcode-detecting-barcodes-and-faces.md) — 使用相机识别机器可读代码或人脸。
- [AVCaptureSession](avcapturesession.md) — 一个配置捕获行为并协调数据从输入设备流向捕获输出的对象。
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — 一种支持从相同媒体类型的多个输入同时捕获的捕获会话。
- [AVCaptureInput](avcaptureinput.md) — 向捕获会话提供输入数据的对象的抽象超类。
- [AVCaptureOutput](avcaptureoutput.md) — 为捕获会话提供媒体输出目的地的对象的抽象超类。
- [AVCaptureConnection](avcaptureconnection.md) — 一个表示从捕获输入到捕获输出的连接的对象。

## 下载

- [BuildAResponsiveCameraAppThatLaunchesQuickly.zip](https://docs-assets.developer.apple.com/published/950948118967/BuildAResponsiveCameraAppThatLaunchesQuickly.zip)
