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

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UIImagePickerController](uiimagepickercontroller.md)

# 自定义图像选择器控制器

<sub>示例代码</sub>

通过向图像选择器添加覆盖视图，管理用户交互并在拍照时呈现自定义信息。

## 概述

此示例在默认图像选择器界面上应用一个覆盖视图，以显示自定义的视图层级。

示例 App 使用覆盖视图来：

- 创建一个响应用户输入的界面。
- 显示自定义信息（例如增强界面的图像）。
- 实现若干独特的相机功能，例如单张拍照、定时拍照和类似快门速度相机的连拍。

### 配置示例代码项目

因为模拟器中没有相机，你需要在安装了 iOS 10 或更高版本的设备上构建并运行此示例。

当用户首次在设备上启动示例 App 时，需要授予 App 使用相机的权限。

### 设置覆盖视图

示例 App 使用 [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) 属性提供一个覆盖视图，其中包含自定义的视图层级。图像选择器会将自定义覆盖视图放置在其他图像选择器视图之上。

```swift
/*
Apply the overlay view. This view contains a toolbar with custom
controls for capturing still images in various ways.
*/
overlayView?.frame = (imagePickerController.cameraOverlayView?.frame)!
imagePickerController.cameraOverlayView = overlayView
```

App 只有在图像选择器的 source type 设置为 `UIImagePickerController.SourceType.camera` 时才能访问 [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) 属性。

当用户与自定义视图中的界面元素交互时，App 会调用诸如 [- takePicture](<uiimagepickercontroller/takepicture().md>) 之类的图像选择器方法来拍照，并实现其他功能。此示例的自定义图像选择器控制器界面提供以下功能：

- Take a Picture
- Take a Delayed Picture
- Take Repeated Pictures
- Browse Media in the Photo Library

[showsCameraControls](uiimagepickercontroller/showscameracontrols.md) 属性指示图像选择器是否显示默认的相机控件。[showsCameraControls](uiimagepickercontroller/showscameracontrols.md) 属性只有在图像选择器的 source type 为 `UIImagePickerController.SourceType.camera` 时才能访问。此示例将 [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) 设置为 `false`，以隐藏默认控件并提供自定义覆盖视图。

```swift
if sourceType == UIImagePickerController.SourceType.camera {
	/*
	 The user tapped the camera button in the app's interface which
	 specifies the device’s built-in camera as the source for the image
	 picker controller.
	*/

	/*
	 Hide the default controls.
	 This sample provides its own custom controls for still image
	 capture in an overlay view.
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

### 拍照

使用 Snap 按钮拍照。其 action 方法调用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法来实际拍照。

```swift
@IBAction func takePhoto(_ sender: UIBarButtonItem) {
imagePickerController.takePicture()
}
```

### 定时拍照

使用 Delayed 按钮在短暂延迟后拍照。其 action 方法在计时器到期时调用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法来拍照。

```swift
@IBAction func delayedTakePhoto(_ sender: UIBarButtonItem) {
	/*
	 Disable the photo controls during the delay time period.
	 The code in the timer completion block below captures a still image
	 when the delay period expires and re-enables the controls.
	*/
	doneButton?.isEnabled = false
	takePictureButton?.isEnabled = false
	delayedPhotoButton?.isEnabled = false
	startStopButton?.isEnabled = false
	
	let fireDate = Date(timeIntervalSinceNow: 5)
	cameraTimer = Timer(fire: fireDate, interval: 1.0, repeats: false, block: { timer in
		// The time interval expired. Capture a still image.
		self.imagePickerController.takePicture()

		// Enable the delayed photos controls.
		self.doneButton?.isEnabled = true
		self.takePictureButton?.isEnabled = true
		self.delayedPhotoButton?.isEnabled = true
		self.startStopButton?.isEnabled = true
	})
	RunLoop.main.add(cameraTimer, forMode: RunLoop.Mode.default)
}
```

### 连拍

使用 Start 按钮以一定间隔连拍；例如，每五秒一张照片。其 action 方法创建一个计时器，使用 [- takePicture](<uiimagepickercontroller/takepicture().md>) 方法按一定间隔拍照。

此示例会无限拍照，导致内存很快用尽。你必须为自己的 App 决定捕获照片数量的适当阈值（为简单起见，此 App 不强制限制）。为了避免内存约束，将每张拍摄的照片保存到磁盘，而不是将所有照片保存在内存中。在低内存情况下，系统可能会调用 App 的 [- didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) 方法，以便 App 恢复部分内存并继续拍照。

```swift
@IBAction func startTakingPicturesAtIntervals(_ sender: UIBarButtonItem) {
	// Start the timer to take a photo every 5 seconds.

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

用户轻点 Start 按钮（变为 Stop 按钮）后，相机立即开始拍照。相机持续捕获照片，直到用户轻点 Stop。捕获的图像按拍摄顺序出现在 App 的图像视图中。

```swift
@IBAction func stopTakingPicturesAtIntervals(_ sender: UIBarButtonItem) {
	// Stop and reset the timer.
	cameraTimer.invalidate()

	finishAndUpdate()
	
	// Make these buttons available again.
	self.doneButton?.isEnabled = true
	self.takePictureButton?.isEnabled = true
	self.delayedPhotoButton?.isEnabled = true
	
	// Reset the button to start taking pictures again.
	startStopButton?.title = NSLocalizedString("Start", comment: "Title for overlay view controller start/stop button")
	startStopButton?.action = #selector(startTakingPicturesAtIntervals)
}
```

### 在照片库中浏览媒体

要浏览设备照片相册中保存的图像，添加一个按钮，用户可以按它进入照片库。该按钮的 action 方法通过将 [sourceType](uiimagepickercontroller/sourcetype-swift.property.md) 属性设置为 `UIImagePickerController.SourceType.photoLibrary` 来配置选择器以浏览保存的媒体，然后呈现选择器的媒体浏览器用户界面。

```swift
@IBAction func showImagePickerForPhotoPicker(_ sender: UIBarButtonItem) {
showImagePicker(sourceType: UIImagePickerController.SourceType.photoLibrary, button: sender)
}
```

选择照片会调用 App 的 [- imagePickerController:didFinishPickingMediaWithInfo:](<uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) delegate 方法，它将所选图像保存到数组中并在 App 的图像视图中显示它。

轻点 Cancel 按钮会调用 App 的 [- imagePickerControllerDidCancel:](<uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(__).md>) delegate 方法，它调用 [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) 来关闭选择器。

## 另请参阅

### Customizing the camera controls

- [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) — 一个布尔值，指示图像选择器是否显示默认的相机控件。
- [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) — 显示在默认图像选择器界面上方的视图。
- [cameraViewTransform](uiimagepickercontroller/cameraviewtransform.md) — 应用于相机预览图像的 transform。

## 下载

- [CustomizingAnImagePickerController.zip](https://docs-assets.developer.apple.com/published/8a225e1270c0/CustomizingAnImagePickerController.zip)
