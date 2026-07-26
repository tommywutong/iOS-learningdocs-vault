---
title: AVCaptureSmartFramingMonitor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor.json'
content_hash: 'sha256:b505600ca9b359b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSmartFramingMonitor

<sub>Class</sub>

An object associated with a capture device that monitors the scene and suggests an optimal framing.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVCaptureSmartFramingMonitor
```

## Overview

A smart framing monitor observes its associated device for objects of interest entering and exiting the camera’s field of view and recommends an optimal framing for good photographic composition. This framing recommendation consists of an aspect ratio and zoom factor. You may respond to the device’s framing recommendation by calling [- setDynamicAspectRatio:completionHandler:](<avcapturedevice/setdynamicaspectratio(__completionhandler_).md>) and setting [videoZoomFactor](avcapturedevice/videozoomfactor.md) on the associated device in whatever order best matches your animation between old and new framings.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Observable](../observation/observable.md)

## Topics

### Configuring framings

- [supportedFramings](avcapturesmartframingmonitor/supportedframings.md) — An array of framings supported by the monitor in its current configuration.
- [enabledFramings](avcapturesmartframingmonitor/enabledframings.md) — An array of framings that the monitor is allowed to suggest.
- [recommendedFraming](avcapturesmartframingmonitor/recommendedframing.md) — The latest recommended framing from the monitor.

### Managing the life cycle

- [monitoring](avcapturesmartframingmonitor/ismonitoring.md) — Yes when the receiver is actively monitoring.
- [- startMonitoringWithError:](<avcapturesmartframingmonitor/startmonitoring().md>) — Begins monitoring the device’s active scene and making framing recommendations.
- [- stopMonitoring](<avcapturesmartframingmonitor/stopmonitoring().md>) — Stops monitoring the device’s active scene and making framing recommendations.

## See Also

### Configuring smart framing

- [smartFramingMonitor](avcapturedevice/smartframingmonitor.md) — A monitor owned by the device that recommends an optimal framing based on the content in the scene.
- [AVCaptureFraming](avcaptureframing.md) — A framing, consisting of an aspect ratio and a zoom factor.
