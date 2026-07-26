---
title: controlsDelegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/controlsdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/controlsdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/controlsdelegate.json'
content_hash: 'sha256:2aa9f43bef6e2821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# controlsDelegate

<sub>Instance Property</sub>

A delegate object that observes changes to the state of capture controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var controlsDelegate: (any AVCaptureSessionControlsDelegate)? { get }
```

## Discussion

Call the [- setControlsDelegate:queue:](<setcontrolsdelegate(__queue_).md>) method to set the controls delegate for a session.

> [!important] Important
> You must specify a controls delegate for controls to become active.

## See Also

### Configuring capture controls

- [supportsControls](supportscontrols.md) — A Boolean value that indicates whether a capture session supports controls.
- [maxControlsCount](maxcontrolscount.md) — The maximum number of controls a capture session supports.
- [controls](controls.md) — The controls that allow configuring the camera system from device hardware.
- [- canAddControl:](<canaddcontrol(__).md>) — Returns a Boolean value that indicates whether a capture session add the specified control.
- [- addControl:](<addcontrol(__).md>) — Adds a control to a capture session.
- [- removeControl:](<removecontrol(__).md>) — Removes a control from a capture session.
- [- setControlsDelegate:queue:](<setcontrolsdelegate(__queue_).md>) — Sets a delegate object for the system to call when it activates and presents controls.
- [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md) — A protocol that defines the interface to respond to capture control activation and presentation events.
- [controlsDelegateCallbackQueue](controlsdelegatecallbackqueue.md) — The dispatch queue on which the system calls controls delegate methods.
