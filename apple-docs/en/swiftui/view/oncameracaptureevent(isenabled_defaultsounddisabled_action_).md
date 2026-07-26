---
title: 'onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncameracaptureevent%28isenabled%3Adefaultsounddisabled%3Aaction%3A%29.json'
content_hash: 'sha256:85b2e7aec8956afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)

<sub>Instance Method</sub>

Used to register an action triggered by system capture events.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, defaultSoundDisabled: Bool = false, action: @escaping (AVCaptureEvent) -> Void) -> some View

```

## Parameters

- `isEnabled` — A boolean value indicating whether capture events trigger the provided action or not. Set this value to `false` when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.

- `defaultSoundDisabled` — A boolean value indicating whether or not the default sound is disabled.

- `action` — An event handler called when either the primary or secondary events are triggered.

## Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

If an event from one source begins, then events from other sources will be ignored until the first event ends or is cancelled.

This API is for media capture use cases only.

## See Also

### Camera

- [onCameraCaptureEvent(isEnabled:action:)](<oncameracaptureevent(isenabled_action_).md>) — Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](<oncameracaptureevent(isenabled_defaultsounddisabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)](<oncameracaptureevent(isenabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
- [cameraAnchor(isActive:)](<cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
