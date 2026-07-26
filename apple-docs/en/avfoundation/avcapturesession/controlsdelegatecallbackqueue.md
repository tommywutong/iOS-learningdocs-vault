---
title: controlsDelegateCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/controlsdelegatecallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/controlsdelegatecallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/controlsdelegatecallbackqueue.json'
content_hash: 'sha256:e9190c04ac56ddb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# controlsDelegateCallbackQueue

<sub>Instance Property</sub>

The dispatch queue on which the system calls controls delegate methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var controlsDelegateCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

Call the [- setControlsDelegate:queue:](<setcontrolsdelegate(__queue_).md>) method to specify the dispatch queue on which to call the controls delegate methods.

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
- [controlsDelegate](controlsdelegate.md) — A delegate object that observes changes to the state of capture controls.
