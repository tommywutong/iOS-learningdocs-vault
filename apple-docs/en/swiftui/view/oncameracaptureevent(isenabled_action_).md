---
title: 'onCameraCaptureEvent(isEnabled:action:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncameracaptureevent(isenabled:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncameracaptureevent%28isenabled%3Aaction%3A%29.json'
content_hash: 'sha256:18c659970712937a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onCameraCaptureEvent(isEnabled:action:)

<sub>Instance Method</sub>

Used to register an action triggered by system capture events.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, action: @escaping (AVCaptureEvent) -> Void) -> some View

```

## Parameters

- `isEnabled` — A boolean value indicating whether capture events trigger the provided action or not. Set this value to `false` when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.

- `action` — An event handler called when either the primary or secondary events are triggered.

## Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

If an event from one source begins, then events from other sources will be ignored until the first event ends or is cancelled.

This API is for media capture use cases only.

## See Also

### Responding to capture events

- [onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)](<oncameracaptureevent(isenabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
