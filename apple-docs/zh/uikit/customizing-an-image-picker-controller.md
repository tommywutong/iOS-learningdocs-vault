---
title: 自定义图像选择器控制器
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, Xcode 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-an-image-picker-controller
source_url: 'https://developer.apple.com/documentation/uikit/customizing-an-image-picker-controller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-an-image-picker-controller.json'
content_hash: 'sha256:ff049ffc42f78c8d'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [UIImagePickerController](uiimagepickercontroller.md)

# 自定义图像选择器控制器

<sub>示例代码</sub>

通过为图像选择器（image picker）添加覆盖视图（overlay view），在拍照时管理用户交互并呈现自定义信息。

## 概述

本示例在默认图像选择器界面之上应用一个覆盖视图，以显示自定义的视图层级结构。

示例 App 使用覆盖视图来：

- 创建一个响应用户输入的界面。
- 显示自定义信息（例如用来增强界面的图片）。
- 实现若干独特的相机功能，例如单张拍摄、定时拍摄，以及像高速快门相机那样的连续拍摄。

### 配置示例代码项目

由于 Simulator 中没有相机，你需要在装有 iOS 10 或更高版本的设备上构建并运行本示例。

首次在设备上启动示例 App 时，你需要授予该 App 使用相机的权限。

### 设置覆盖视图

示例 App 使用 [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) 属性提供一个包含自定义视图层次的覆盖视图。图像选择器会把自定义覆盖视图放在其他图像选择器视图之上。

```swift
/*
应用覆盖视图。这个视图包含一个工具栏，带有
以各种方式拍摄静态图像的自定义控制。
*/
overlayView?.frame = (imagePickerController.cameraOverlayView?.frame)!
imagePickerController.cameraOverlayView = overlayView
```

只有当图像选择器的源类型设为 `UIImagePickerController.SourceType.camera` 时，App 才能访问 [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) 属性。

当用户与自定义视图中的界面元素交互时，App 会调用图像选择器的方法（例如 [- takePicture](<uiimagepickercontroller/takepicture().md>)）拍摄照片，并实现其他功能。本示例的自定义图像选择器控制器界面提供以下功能：

- Take a Picture（拍照）
- Take a Delayed Picture（延时拍照）
- Take Repeated Pictures（连拍）
- Browse Media in the Photo Library（浏览照片图库中的媒体）

[showsCameraControls](uiimagepickercontroller/showscameracontrols.md) 属性表示图像选择器是否显示默认相机控制。该属性只有在图像选择器的源类型为 `UIImagePickerController.SourceType.camera` 时才可访问。本示例把 [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) 设为 `false`，从而隐藏默认控制并提供自定义覆盖视图。

```swift
if sourceType == UIImagePickerController.SourceType.camera {
	/*
 用户在 App 界面中轻点了相机按钮，该按钮指定
 设备的内建相机作为图像选择器
 控制器的来源。
	*/

	/*
 隐藏默认控制。
 本示例在覆盖视图中提供了自己用于拍摄
 静态图像的自定义控制。
	*/
	imagePickerController.showsCameraControls = false

	/*
 Apply the overlay view. This view contains a toolbar with custom
 controls for capturing still images in various ways.
	*/
	overlayView?.frame = (imagePickerController.cameraOverlayView?.frame)!
	imagePickerController.cameraOverlayView = overlayView
}
```

### 拍摄照片

用 Snap 按钮拍摄照片。它的动作方法调用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法来真正拍摄照片。

```swift
@IBAction func takePhoto(_ sender: UIBarButtonItem) {
imagePickerController.takePicture()
}
```

### 延时拍摄照片

用 Delayed 按钮在短暂延迟后拍摄照片。它的动作方法调用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法，在计时器到期时拍摄照片。

```swift
@IBAction func delayedTakePhoto(_ sender: UIBarButtonItem) {
	/*
 在延迟期间禁用拍照控制。
 下方计时器完成块中的代码会在延迟期结束时
 拍摄一张静态图像，并重新启用这些控制。
	*/
	doneButton?.isEnabled = false
	takePictureButton?.isEnabled = false
	delayedPhotoButton?.isEnabled = false
	startStopButton?.isEnabled = false
	
	let fireDate = Date(timeIntervalSinceNow: 5)
	cameraTimer = Timer(fire: fireDate, interval: 1.0, repeats: false, block: { timer in
		// 时间间隔已到。拍摄一张静态图像。
		self.imagePickerController.takePicture()

		// 启用延时拍照控制。
		self.doneButton?.isEnabled = true
		self.takePictureButton?.isEnabled = true
		self.delayedPhotoButton?.isEnabled = true
		self.startStopButton?.isEnabled = true
	})
	RunLoop.main.add(cameraTimer, forMode: RunLoop.Mode.default)
}
```

### 连续拍摄照片

用 Start 按钮按一定间隔连续拍摄照片，例如每五秒一张。它的动作方法创建一个计时器，用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法按特定间隔拍照。

本示例会不限次数地连续拍照，这会很快耗尽内存。你必须为自己的 App 决定一个合理的拍摄数量上限（为简单起见，本 App 没有强制限制）。为避免内存吃紧，请把每张拍好的照片保存到磁盘，而不是把所有照片都留在内存里。在内存不足的情况下，系统可能调用你的 App 的 [- didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) 方法，让 App 回收一些内存并继续拍照。

```swift
@IBAction func startTakingPicturesAtIntervals(_ sender: UIBarButtonItem) {
	// 启动计时器，每 5 秒拍一张照片。

	startStopButton?.title = NSLocalizedString("Stop", comment: "Title for overlay view controller start/stop button")
	startStopButton?.action = #selector(stopTakingPicturesAtIntervals)
	
	// Enable these buttons while capturing photos.
	doneButton?.isEnabled = false
	delayedPhotoButton?.isEnabled = false
	takePictureButton?.isEnabled = false

	// Start taking pictures.
	cameraTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { timer in
		self.imagePickerController.takePicture()
	}
}
```

用户轻点 Start 按钮（它会变成 Stop 按钮）后，相机立即开始拍照，并持续拍摄直到用户轻点 Stop。拍摄到的图像按拍摄顺序显示在 App 的图像视图里。

```swift
@IBAction func stopTakingPicturesAtIntervals(_ sender: UIBarButtonItem) {
	// 停止并重置计时器。
	cameraTimer.invalidate()

	finishAndUpdate()
	
	// 让这些按钮重新可用。
	self.doneButton?.isEnabled = true
	self.takePictureButton?.isEnabled = true
	self.delayedPhotoButton?.isEnabled = true
	
	// 重置按钮，以便再次开始拍照。
	startStopButton?.title = NSLocalizedString("Start", comment: "Title for overlay view controller start/stop button")
	startStopButton?.action = #selector(startTakingPicturesAtIntervals)
}
```

### 浏览照片图库中的媒体

要浏览设备上相册中保存的图像，添加一个按钮让用户可以前往他们的照片图库。该按钮的动作方法把选择器的 [sourceType](uiimagepickercontroller/sourcetype-swift.property.md) 属性设为 `UIImagePickerController.SourceType.photoLibrary` 来配置浏览已保存媒体的功能，然后呈现选择器的媒体浏览界面。

```swift
@IBAction func showImagePickerForPhotoPicker(_ sender: UIBarButtonItem) {
showImagePicker(sourceType: UIImagePickerController.SourceType.photoLibrary, button: sender)
}
```

选定一张照片会触发 App 的 [- imagePickerController:didFinishPickingMediaWithInfo:](<uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) 委托方法，它把选中的图像保存到一个数组并显示在 App 的图像视图里。

轻点 Cancel 按钮会触发 App 的 [- imagePickerControllerDidCancel:](<uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(__).md>) 委托方法，它调用 [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) 来关闭选择器。

## 另请参阅

### 自定义相机控制

- [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) — 表示图像选择器是否显示默认相机控制的布尔值。
- [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) — 显示在默认图像选择器界面之上的视图。
- [cameraViewTransform](uiimagepickercontroller/cameraviewtransform.md) — 应用于相机预览图像的变换。

## 下载

- [CustomizingAnImagePickerController.zip](https://docs-assets.developer.apple.com/published/8a225e1270c0/CustomizingAnImagePickerController.zip)
