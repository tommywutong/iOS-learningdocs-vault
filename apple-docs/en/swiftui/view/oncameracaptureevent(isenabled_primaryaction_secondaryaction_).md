---
title: 'onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncameracaptureevent(isenabled:primaryaction:secondaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:primaryaction:secondaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncameracaptureevent%28isenabled%3Aprimaryaction%3Asecondaryaction%3A%29.json'
content_hash: 'sha256:b2142e3cf9c0186f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)

<sub>Instance Method</sub>

Used to register actions triggered by system capture events.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, primaryAction: @escaping (AVCaptureEvent) -> Void, secondaryAction: @escaping (AVCaptureEvent) -> Void) -> some View

```

## Parameters

- `isEnabled` — A boolean value indicating whether capture events trigger the provided actions or not. Set this value to `false` when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.

- `primaryAction` — An event handler called when a primary capture event is triggered.

- `secondaryAction` — An event handler called when a secondary capture event is triggered.

## Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

This API is for media capture use cases only.

## See Also

### Responding to capture events

- [onCameraCaptureEvent(isEnabled:action:)](<oncameracaptureevent(isenabled_action_).md>) — Used to register an action triggered by system capture events.
