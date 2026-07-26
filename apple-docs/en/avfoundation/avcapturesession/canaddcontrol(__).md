---
title: 'canAddControl(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/canaddcontrol(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddcontrol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/canaddcontrol%28_%3A%29.json'
content_hash: 'sha256:e8bdef302c0f421f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# canAddControl(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a capture session add the specified control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func canAddControl(_ control: AVCaptureControl) -> Bool
```

## Parameters

- `control` — The capture control to add.

## Return Value

[true](../../swift/true.md) if the capture session can add the control; otherwise, [false](../../swift/false.md).

## Discussion

Call this method to determine whether you can successfully add a control to a capture session using the [- addControl:](<addcontrol(__).md>) method. A capture session may not be able to add a control due to its current session configuration or if unsupported by the host platform.

## See Also

### Configuring capture controls

- [supportsControls](supportscontrols.md) — A Boolean value that indicates whether a capture session supports controls.
- [maxControlsCount](maxcontrolscount.md) — The maximum number of controls a capture session supports.
- [controls](controls.md) — The controls that allow configuring the camera system from device hardware.
- [- addControl:](<addcontrol(__).md>) — Adds a control to a capture session.
- [- removeControl:](<removecontrol(__).md>) — Removes a control from a capture session.
- [- setControlsDelegate:queue:](<setcontrolsdelegate(__queue_).md>) — Sets a delegate object for the system to call when it activates and presents controls.
- [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md) — A protocol that defines the interface to respond to capture control activation and presentation events.
- [controlsDelegate](controlsdelegate.md) — A delegate object that observes changes to the state of capture controls.
- [controlsDelegateCallbackQueue](controlsdelegatecallbackqueue.md) — The dispatch queue on which the system calls controls delegate methods.
