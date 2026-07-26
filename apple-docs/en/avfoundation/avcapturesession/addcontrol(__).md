---
title: 'addControl(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addcontrol(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addcontrol(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addcontrol%28_%3A%29.json'
content_hash: 'sha256:1aa3fcdb100dafcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addControl(_:)

<sub>Instance Method</sub>

Adds a control to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func addControl(_ control: AVCaptureControl)
```

## Parameters

- `control` — The capture control to add.

## Discussion

A capture session may not be able to add a control due to configuration reasons or limits of the host platform. Before calling this method, determine whether you can successfully add a control by calling the capture session’s [- canAddControl:](<canaddcontrol(__).md>) method.

You may call this method while the session is running.

> [!important] Important
> For a control to become active, you must set a [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md) on the session.

## See Also

### Configuring capture controls

- [supportsControls](supportscontrols.md) — A Boolean value that indicates whether a capture session supports controls.
- [maxControlsCount](maxcontrolscount.md) — The maximum number of controls a capture session supports.
- [controls](controls.md) — The controls that allow configuring the camera system from device hardware.
- [- canAddControl:](<canaddcontrol(__).md>) — Returns a Boolean value that indicates whether a capture session add the specified control.
- [- removeControl:](<removecontrol(__).md>) — Removes a control from a capture session.
- [- setControlsDelegate:queue:](<setcontrolsdelegate(__queue_).md>) — Sets a delegate object for the system to call when it activates and presents controls.
- [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md) — A protocol that defines the interface to respond to capture control activation and presentation events.
- [controlsDelegate](controlsdelegate.md) — A delegate object that observes changes to the state of capture controls.
- [controlsDelegateCallbackQueue](controlsdelegatecallbackqueue.md) — The dispatch queue on which the system calls controls delegate methods.
