---
title: 'setControlsDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/setcontrolsdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/setcontrolsdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/setcontrolsdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:8b23cc39b6b8e64f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# setControlsDelegate(_:queue:)

<sub>Instance Method</sub>

Sets a delegate object for the system to call when it activates and presents controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setControlsDelegate(_ controlsDelegate: (any AVCaptureSessionControlsDelegate)?, queue controlsDelegateCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `controlsDelegate` — An object that adopts the controls delegate protocol.

- `controlsDelegateCallbackQueue` — A serial dispatch queue on which to call the delegate methods. You must specify a serial queue to ensure callbacks occur in order. This argument must not be `nil` unless the `controlsDelegate` argument is also `nil;` otherwise, the system throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md).

## Discussion

People interact with capture controls by performing specific gestures to enable their visibility. Specify a delegate to for the system to call when it presents and dismisses controls. The system calls the delegate’s methods on the specified callback queue.

## See Also

### Configuring capture controls

- [supportsControls](supportscontrols.md) — A Boolean value that indicates whether a capture session supports controls.
- [maxControlsCount](maxcontrolscount.md) — The maximum number of controls a capture session supports.
- [controls](controls.md) — The controls that allow configuring the camera system from device hardware.
- [- canAddControl:](<canaddcontrol(__).md>) — Returns a Boolean value that indicates whether a capture session add the specified control.
- [- addControl:](<addcontrol(__).md>) — Adds a control to a capture session.
- [- removeControl:](<removecontrol(__).md>) — Removes a control from a capture session.
- [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md) — A protocol that defines the interface to respond to capture control activation and presentation events.
- [controlsDelegate](controlsdelegate.md) — A delegate object that observes changes to the state of capture controls.
- [controlsDelegateCallbackQueue](controlsdelegatecallbackqueue.md) — The dispatch queue on which the system calls controls delegate methods.
