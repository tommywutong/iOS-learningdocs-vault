---
title: 'onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:primaryaction:secondaryaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:primaryaction:secondaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncameracaptureevent%28isenabled%3Adefaultsounddisabled%3Aprimaryaction%3Asecondaryaction%3A%29.json'
content_hash: 'sha256:eaeda12876ef4733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)

<sub>Instance Method</sub>

Used to register actions triggered by system capture events.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, defaultSoundDisabled: Bool = false, primaryAction: @escaping (AVCaptureEvent) -> Void, secondaryAction: @escaping (AVCaptureEvent) -> Void) -> some View

```

## Parameters

- `isEnabled` — A boolean value indicating whether capture events trigger the provided actions or not. Set this value to `false` when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.

- `defaultSoundDisabled` — A boolean value indicating whether or not the default sound is disabled.

- `primaryAction` — An event handler called when a primary capture event is triggered.

- `secondaryAction` — An event handler called when a secondary capture event is triggered.

## Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

This API is for media capture use cases only.

## See Also

### Camera

- [onCameraCaptureEvent(isEnabled:action:)](<oncameracaptureevent(isenabled_action_).md>) — Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](<oncameracaptureevent(isenabled_defaultsounddisabled_action_).md>) — Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)](<oncameracaptureevent(isenabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
- [cameraAnchor(isActive:)](<cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
