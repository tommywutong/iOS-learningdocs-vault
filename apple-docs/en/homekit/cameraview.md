---
title: CameraView
framework: HomeKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/homekit/cameraview
source_url: 'https://developer.apple.com/documentation/homekit/cameraview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/homekit/cameraview.json'
content_hash: 'sha256:09c86a22282c8cc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [HomeKit](../homekit.md)

# CameraView

<sub>Structure</sub>

A SwiftUI view into which a video stream or an image snapshot is rendered.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct CameraView
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a camera view

- [init(source:)](<cameraview/init(source_).md>) — Creates a new camera view using the given source.
- [HMCameraSource](hmcamerasource.md) — An abstract class for a camera’s data source.

## See Also

### Managing camera profiles

- [cameraProfiles](hmaccessory/cameraprofiles.md) — An array of camera profiles implemented by the accessory.
- [HMCameraProfile](hmcameraprofile.md) — A camera profile that interacts with an accessory’s camera.
- [HMCameraView](hmcameraview.md) — The view into which a video stream or an image snapshot is rendered.
