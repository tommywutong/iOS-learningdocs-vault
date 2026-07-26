---
title: 'readinessCoordinator(_:captureReadinessDidChange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(_:capturereadinessdidchange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(_:capturereadinessdidchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator%28_%3Acapturereadinessdidchange%3A%29.json'
content_hash: 'sha256:b6b46f00ee7e4547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutputReadinessCoordinatorDelegate](../avcapturephotooutputreadinesscoordinatordelegate.md)

# readinessCoordinator(_:captureReadinessDidChange:)

<sub>Instance Method</sub>

Tells the delegate that the capture readiness state of a photo output changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func readinessCoordinator(_ coordinator: AVCapturePhotoOutputReadinessCoordinator, captureReadinessDidChange captureReadiness: AVCapturePhotoOutput.CaptureReadiness)
```

## Parameters

- `coordinator` — The delegate’s coordinator object.

- `captureReadiness` — An updated capture readiness value.

## Discussion

The system always performs this call on the main queue, so you can use it to update your user interface’s shutter button availability and appearance.
