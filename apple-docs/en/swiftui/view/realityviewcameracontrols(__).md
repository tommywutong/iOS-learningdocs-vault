---
title: 'realityViewCameraControls(_:)'
framework: RealityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/realityviewcameracontrols(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/realityviewcameracontrols(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/realityviewcameracontrols%28_%3A%29.json'
content_hash: 'sha256:a720ac5268271c17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# realityViewCameraControls(_:)

<sub>Instance Method</sub>

Adds gestures that control the position and direction of a virtual camera.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@MainActor @preconcurrency func realityViewCameraControls(_ controls: CameraControls) -> some View

```

## Discussion

You can use a drag gesture from a mouse, trackpad, or screen touches with iOS and iPadOS devices to `.tilt`, `.pan`, `.orbit`, or `.dolly` a virtual camera.

## See Also

### Configuring camera controls

- [realityViewCameraControls](../environmentvalues/realityviewcameracontrols.md) — The camera controls for the reality view.
- [realityViewLayoutBehavior(_:)](<realityviewlayoutbehavior(__).md>) — A view modifier that controls the frame sizing and content alignment behavior for `RealityView`
