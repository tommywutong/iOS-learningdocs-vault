---
title: AVCaptureSessionControlsDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesessioncontrolsdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioncontrolsdelegate.json'
content_hash: 'sha256:4544d93ccf8732b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSessionControlsDelegate

<sub>Protocol</sub>

A protocol that defines the interface to respond to capture control activation and presentation events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureSessionControlsDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to control events

- [- sessionControlsDidBecomeActive:](<avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(__).md>) — Tells the delegate when a capture session’s controls become active and available for interaction.
- [- sessionControlsWillEnterFullscreenAppearance:](<avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [- sessionControlsWillExitFullscreenAppearance:](<avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [- sessionControlsDidBecomeInactive:](<avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(__).md>) — Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.

## See Also

### Configuring capture controls

- [supportsControls](avcapturesession/supportscontrols.md) — A Boolean value that indicates whether a capture session supports controls.
- [maxControlsCount](avcapturesession/maxcontrolscount.md) — The maximum number of controls a capture session supports.
- [controls](avcapturesession/controls.md) — The controls that allow configuring the camera system from device hardware.
- [- canAddControl:](<avcapturesession/canaddcontrol(__).md>) — Returns a Boolean value that indicates whether a capture session add the specified control.
- [- addControl:](<avcapturesession/addcontrol(__).md>) — Adds a control to a capture session.
- [- removeControl:](<avcapturesession/removecontrol(__).md>) — Removes a control from a capture session.
- [- setControlsDelegate:queue:](<avcapturesession/setcontrolsdelegate(__queue_).md>) — Sets a delegate object for the system to call when it activates and presents controls.
- [controlsDelegate](avcapturesession/controlsdelegate.md) — A delegate object that observes changes to the state of capture controls.
- [controlsDelegateCallbackQueue](avcapturesession/controlsdelegatecallbackqueue.md) — The dispatch queue on which the system calls controls delegate methods.
