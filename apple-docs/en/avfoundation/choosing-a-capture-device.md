---
title: Choosing a capture device
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/choosing-a-capture-device
source_url: 'https://developer.apple.com/documentation/avfoundation/choosing-a-capture-device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/choosing-a-capture-device.json'
content_hash: 'sha256:8e95d42313d471f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md)

# Choosing a capture device

<sub>Article</sub>

Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.

## Overview

Devices offer many options for capturing photos and video, including front- and back-facing cameras, dual cameras, and the TrueDepth camera. Choosing the appropriate camera automatically or offering a user interface for camera selection is an important part of developing any app with camera features.

AVFoundation offers two main paths to selecting a camera device: the [+ defaultDeviceWithDeviceType:mediaType:position:](<avcapturedevice/default(__for_position_).md>) method and the [DiscoverySession](avcapturedevice/discoverysession.md) class.

### Quickly choose a default device

If you know exactly what kind of capture devices you’re looking for, use one of the [AVCaptureDevice](avcapturedevice.md) convenience methods to select a default device. For example, the code below selects the best available back-facing camera: either the dual camera on supported devices, or the single (wide-angle) camera on single-camera devices.

```swift
if let device = AVCaptureDevice.default(.builtInDualCamera,
                                        for: .video, position: .back) {
    return device
} else if let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                               for: .video, position: .back) {
    return device
} else {
    fatalError("Missing expected back camera device.")
}
```

### Sort and filter devices with a discovery session

To see the entire set of devices matching certain criteria so that you can use your own logic to choose one, use the [DiscoverySession](avcapturedevice/discoverysession.md) class. First, create a discovery session for the kinds of devices you need:

```swift
let discoverySession = AVCaptureDevice.DiscoverySession(deviceTypes:
    [.builtInTrueDepthCamera, .builtInDualCamera, .builtInWideAngleCamera],
    mediaType: .video, position: .unspecified)
```

Then, read the discovery session’s [devices](avcapturedevice/discoverysession/devices.md) list to find matching devices and choose one that suits your needs. The discovery session automatically sorts its [devices](avcapturedevice/discoverysession/devices.md) list based on the device types you asked for, so you can use the array order to find the best device with certain features. For example, because the discovery session shown above searches for depth-capable devices before the wide-angle camera and allows any device position, the first item in its devices list matching a specified position is the best depth capture device for that position (or a fallback device):

```swift
func bestDevice(in position: AVCaptureDevice.Position) -> AVCaptureDevice {
    let devices = self.discoverySession.devices
    guard !devices.isEmpty else { fatalError("Missing capture devices.")}

    return devices.first(where: { device in device.position == position })!
}
```

## See Also

### Capture devices

- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md) — Capture the optimal shot by providing automatic framing recommendations.
- [AVCaptureDevice](avcapturedevice.md) — An object that represents a hardware or virtual capture device like a camera or microphone.
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — An object that provides media input from a capture device to a capture session.
- [AVContinuityDevice](avcontinuitydevice.md) — A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [AVExternalStorageDevice](avexternalstoragedevice.md) — Represents a physical external storage device that stores media assets.
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — Informs your app when the external storage devices connect to and disconnect from the system.
