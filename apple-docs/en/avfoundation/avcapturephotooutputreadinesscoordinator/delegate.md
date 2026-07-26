---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutputreadinesscoordinator/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/delegate.json'
content_hash: 'sha256:950cb730e559d1b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutputReadinessCoordinator](../avcapturephotooutputreadinesscoordinator.md)

# delegate

<sub>Instance Property</sub>

The coordinator’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
weak var delegate: (any AVCapturePhotoOutputReadinessCoordinatorDelegate)? { get set }
```

## Discussion

The capture delegate receives callbacks when the photo output’s captureReadiness changes. It calls its delegate on the main queue, which allows you to perform user interface updates directly from the delegate’s [- readinessCoordinator:captureReadinessDidChange:](<../avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(__capturereadinessdidchange_).md>) method.

The coordinator provides an initial value to the delegate when you first set it on this object.
