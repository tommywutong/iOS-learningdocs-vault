---
title: Getting the GPU that drives a view’s display
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/getting-the-gpu-that-drives-a-views-display
source_url: 'https://developer.apple.com/documentation/metal/getting-the-gpu-that-drives-a-views-display'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/getting-the-gpu-that-drives-a-views-display.json'
content_hash: 'sha256:342f0a9dc9e88dd4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [Multi-GPU systems](multi-gpu-systems.md)

# Getting the GPU that drives a view’s display

<sub>Article</sub>

Keep up to date with the optimal device for your display.

## Overview

A user can have multiple external displays connected directly to a Mac or to an external GPU. Each view in your app shows on a single display, and a single GPU drives each display. The display in which your view appears and the GPU that drives the display can change dynamically; therefore, you need to prepare your app to handle these changes. Register for display change notifications, get the device that drives your view’s display, and decide if your app should use that device to present rendered graphics.

### Handle display change notifications

Register for the following notifications so the system can notify your app about specific display changes:

- **[didChangeScreenNotification](../appkit/nswindow/didchangescreennotification.md)** — The system posts this notification when any window, including the window containing your view, moves to a different display.
- **[didChangeScreenParametersNotification](../appkit/nsapplication/didchangescreenparametersnotification.md)** — The system posts this notification when the Mac system’s display configuration changes; for example, when the user connects or disconnects an external display from the system. Another example is when the GPU driving the display changes, such as when system has automatic graphics switching enabled and switches between the discrete and integrated GPUs to drive the display.

When the system posts a display change notification, you can decide if you should get and use a new device.

**Swift**

```swift
@objc func handleDisplayChanges(notification: NSNotification) {
    // Handle display changes
}

func registerForDisplayChangeNotifications() {
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSWindowDidChangeScreenNotification"),
                                           object: nil)
    
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSApplicationDidChangeScreenParametersNotification"),
                                           object: nil)
}
```

**Objective-C**

```objective-c
- (void)handleDisplayChanges:(NSNotification *)notification
{
    // Handle display changes
}

- (void)registerForDisplayChangeNotifications
{
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSWindowDidChangeScreenNotification
                                               object:nil];
    
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSApplicationDidChangeScreenParametersNotification
                                               object:nil];
}
```

To deregister from the previous notifications, call the [removeObserver(_:name:object:)](<../foundation/notificationcenter/removeobserver(__name_object_).md>) method.

### Identify the device that drives your view’s display

Get the [CGDirectDisplayID](../coregraphics/cgdirectdisplayid.md) value for the display in which your view currently appears. Then call the [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) function to get the device that drives that display.

**Swift**

```swift
guard let viewDisplayID = mtkView.window?.screen?.deviceDescription[NSDeviceDescriptionKey("NSScreenNumber")] as? CGDirectDisplayID else { return }
let displayDevice = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID)
```

**Objective-C**

```objective-c
NSNumber           *screenNumber = _mtkView.window.screen.deviceDescription[@"NSScreenNumber"];
CGDirectDisplayID  viewDisplayID  = [screenNumber unsignedIntValue];
id <MTLDevice>     displayDevice  = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID);
```

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_
