---
title: captureReadiness
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutputreadinesscoordinator/capturereadiness
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/capturereadiness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/capturereadiness.json'
content_hash: 'sha256:eab7bab6eae51eda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutputReadinessCoordinator](../avcapturephotooutputreadinesscoordinator.md)

# captureReadiness

<sub>Instance Property</sub>

A value that indicates whether the coordinator’s photo output is ready to respond to new capture requests in a timely manner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var captureReadiness: AVCapturePhotoOutput.CaptureReadiness { get }
```

## Discussion

The value incorporates the photo output’s [captureReadiness](../avcapturephotooutput/capturereadiness-swift.property.md) property value and any requests registered by calling the [- startTrackingCaptureRequestUsingPhotoSettings:](<starttrackingcapturerequest(using_).md>) method. The system updates this value before calling the [- readinessCoordinator:captureReadinessDidChange:](<../avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(__capturereadinessdidchange_).md>) method.

This property is key-value observable.
