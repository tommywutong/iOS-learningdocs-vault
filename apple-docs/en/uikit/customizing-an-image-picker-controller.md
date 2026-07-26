---
title: Customizing an image picker controller
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UIImagePickerController](uiimagepickercontroller.md)

# Customizing an image picker controller

<sub>Sample Code</sub>

Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.

## Overview

This sample applies an overlay view to display a custom view hierarchy on top of the default image picker interface.

The sample app uses an overlay view to:

- Create an interface to respond to user input.
- Display custom information (such as images to enhance the interface).
- Implement a number of unique camera functions such as single picture capture, timed picture capture, and repeated pictures like a camera with a fast shutter speed.

### Configure the sample code project

Because the camera isn’t available in Simulator, you’ll need to build and run this sample on a device with iOS 10 or later installed.

When you first launch the sample app on device, you’ll need to grant the app permission to use the camera.

### Set up the overlay view

The sample app uses the [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) property to provide an overlay view that contains the custom view hierarchy. The image picker places the custom overlay view on top of the other image picker views.

```swift
/*
Apply the overlay view. This view contains a toolbar with custom
controls for capturing still images in various ways.
*/
overlayView?.frame = (imagePickerController.cameraOverlayView?.frame)!
imagePickerController.cameraOverlayView = overlayView
```

An app can access the [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) property only when the source type of the image picker is set to `UIImagePickerController.SourceType.camera`.

When the user interacts with interface elements in the custom view, the app calls an image picker method such as [- takePicture](<uiimagepickercontroller/takepicture().md>) to capture a photo, and implement other features. This sample’s custom image picker controller interface provides the following features:

- Take a Picture
- Take a Delayed Picture
- Take Repeated Pictures
- Browse Media in the Photo Library

The [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) property indicates whether the image picker displays the default camera controls. The [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) property is only accessible when the source type of the image picker is `UIImagePickerController.SourceType.camera`. This sample sets [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) to `false` to hide the default controls and provide a custom overlay view.

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

### Take a picture

Take a picture with the Snap button. Its action method calls the [- takePicture](<uiimagepickercontroller/takepicture().md>) method to actually take a picture.

```swift
@IBAction func takePhoto(_ sender: UIBarButtonItem) {
imagePickerController.takePicture()
}
```

### Take a delayed picture

Take a picture after a short delay with the Delayed button. Its action method calls the [- takePicture](<uiimagepickercontroller/takepicture().md>) method to take a picture when the timer expires.

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

### Take repeated pictures

Take repeated pictures at a certain interval with the Start button; for example, one photo every five seconds. Its action method creates a timer to take pictures at certain intervals using the [- takePicture](<uiimagepickercontroller/takepicture().md>) method.

This sample takes pictures indefinitely, causing it to run out of memory quickly. You must decide upon a proper threshold of the number of captured photos for your own app (for simplicity, this app does not enforce a limit). To avoid memory constraints, save each taken photo to disk rather than keeping all of the pictures in memory. The system may invoke your app’s [- didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>)  method in low memory situations so the app can recover some memory and continue taking photos.

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

The camera starts taking pictures as soon as the user taps the Start button (which changes to a Stop button). The camera continues to capture photos until the user taps Stop. Captured images appear in the order taken within the app’s image view.

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

### Browse media in the Photo Library

To browse images saved in the photo albums on the device, add a button that the user can press to go to their Photo Library. The button’s action method configures the picker for browsing saved media by setting its [sourceType](uiimagepickercontroller/sourcetype-swift.property.md) property to `UIImagePickerController.SourceType.photoLibrary`, before presenting the picker’s media browser user interface.

```swift
@IBAction func showImagePickerForPhotoPicker(_ sender: UIBarButtonItem) {
showImagePicker(sourceType: UIImagePickerController.SourceType.photoLibrary, button: sender)
}
```

Selecting a photo invokes the app’s [- imagePickerController:didFinishPickingMediaWithInfo:](<uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) delegate method which saves the selected image to an array and displays it in the app’s image view.

Tapping the Cancel button invokes the app’s [- imagePickerControllerDidCancel:](<uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(__).md>) delegate method which calls [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) to dismiss the picker.

## See Also

### Customizing the camera controls

- [showsCameraControls](uiimagepickercontroller/showscameracontrols.md) — A Boolean value that indicates whether the image picker displays the default camera controls.
- [cameraOverlayView](uiimagepickercontroller/cameraoverlayview.md) — The view to display on top of the default image picker interface.
- [cameraViewTransform](uiimagepickercontroller/cameraviewtransform.md) — The transform to apply to the camera’s preview image.

## Download

- [CustomizingAnImagePickerController.zip](https://docs-assets.developer.apple.com/published/8a225e1270c0/CustomizingAnImagePickerController.zip)
