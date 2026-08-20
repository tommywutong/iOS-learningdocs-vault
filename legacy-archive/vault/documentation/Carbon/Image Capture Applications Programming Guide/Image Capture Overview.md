---
title: Image Capture Applications Programming Guide
apple_id: TP40005196
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2009-08-29'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ImageCaptureServicesProgrammingGuide/02Overview/02Overview.html
archived_at: '2026-07-15T05:23:12.597609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image Capture Applications Programming Guide](Introduction.md)


[Next](Creating%20an%20Application%20Using%20ImageKit.md)[Previous](Introduction.md)

# Image Capture Overview

Starting with Mac OS 10.6, you can use `ImageKit` and the `ImageCaptureCore` framework to find and control image capture devices (cameras, scanners, and multifunction devices such as camera/phones and printer/scanners).

You can open a browser that dynamically detects all cameras and scanners attached by USB or available over the network. You can limit the browser to displaying only cameras, only scanners, only local, or only network devices, or any combination of these. You can choose any available device using the browser, and can open a session with the selected device to list and fetch thumbnails, images, video, and other files from cameras, or to control the scan process of scanners.

`ImageKit` provides a complete UI for these tasks, allowing you to create applications that find and control cameras and scanners entirely by dragging and dropping objects using Interface Builder.

`ImageCaptureCore` provides the same capabilities using a programmatic interface, allowing you to write headless applications or to provide your own custom UI. `ImageCaptureCore` also includes some controls not available from `ImageKit`, such as choosing the default application to launch when a camera is connected.

You can use both `ImageKit` and `ImageCaptureCore` in the same application. For example, you could use `ImageKit` to provide the main interface and add additional custom controls using `ImageCaptureCore`.

To create an `ImageKit` application, link your Xcode project to the Quartz framework. For `ImageCaptureCore`, link to QuartzFoundation. If you are using both, add both frameworks.

`ImageKit` provides four image capture classes:

- `IKDeviceBrowserView`—A browser that displays a list of available cameras and scanners. The browser shows both USB and network devices. It displays their names, types, and icons. The list is updated dynamically as devices are plugged in, removed, or renamed. The camera device type includes camera-phones (including the iPhone) and memory card readers. The scanner device type includes multifunction devices such as printer-scanner-FAX machines.
- `IKCameraDeviceView`—A camera viewer that displays the camera’s name and icon, a list of the images available, metadata such as image name, date, exposure, and color depth, and a set of controls to rotate, delete, or download the images. The viewer supports a list view and a matrix view of the image thumbnails.
- `IKScannerDeviceView`—A viewer that displays the scanner’s name and icon and allows you to scan and capture images. Controls are provided to get a preview, to identify and create multiple discrete images from a single scan, to rotate or crop images, and to control aspects of the scan such as pixels per inch and color depth.
- `IKImageView`—A view for displaying images obtained from a camera or scanner.

These four classes are available as drag-and-drop objects in the `ImageKit` library for Interface Builder, so it’s possible to create an application that browses for and controls cameras and scanners literally without writing a line of code. For an example, see [Creating an Application Using ImageKit](Creating%20an%20Application%20Using%20ImageKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojwfvbuqnbnknltk).

Adding scanning and image capture to an existing application with these classes requires only the few lines of "glue" code to integrate the window constructed in Interface Builder into your application.

The `ImageCaptureCore` framework contains classes that allow you to browse for image capture devices and control them programatically. These classes are strongly analogous to the `ImageKit` classes, but they provide no UI. Instead, they have methods for which you create delegates, allowing you to take whatever action you choose in response to the events these objects respond to.

For example, `ImageCaptureCore` contains a device browser class, `ICDeviceBrowser`. This performs the same functions as `ImageKit’s` `IKDeviceBrowserView`—it dynamically detects available image capture devices. But instead of displaying a list of devices, it has methods such as `didAddDevice` and `didRemoveDevice` whose delegates are called when the device browser detects a device or sees a device removed.

Your application defines these delegate methods. For example, when a device is detected, your version of `didAddDevice` is called. It might get the device and store it in a mutable array, then go on to display the array of devices using a table view.

Similarly, `ImageCaptureCore` contains a camera device class and a scanner device class, analogous to `ImageKit’s` camera view and scanner view.

All the `ImageCaptureCore` classes support Cocoa bindings, so you can, for example, use Interface Builder to assign your own custom view as the delegate for an `ImageCaptureCore` device browser object, obviating the need to construct the entire UI programatically.

You can mix and match `ImageKit` and `ImageCaptureCore` objects in your code. For example, you might use an ImageKit device browser to allow users to find and select a scanner, but use your own UI to control the scanner using `ImageCaptureCore`.

You can write an `ImageCaptureCore` application in as little as a few dozen lines of code. For an example, see [Creating an Application Using ImageCaptureCore](Creating%20an%20Application%20Using%20ImageCaptureCore.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojwfvbuqnjnknltc).

[Next](Creating%20an%20Application%20Using%20ImageKit.md)[Previous](Introduction.md)

