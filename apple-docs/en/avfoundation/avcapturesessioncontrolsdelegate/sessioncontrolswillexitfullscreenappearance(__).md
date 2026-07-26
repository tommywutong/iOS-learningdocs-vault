---
title: 'sessionControlsWillExitFullscreenAppearance(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance%28_%3A%29.json'
content_hash: 'sha256:190eff11be719adf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md)

# sessionControlsWillExitFullscreenAppearance(_:)

<sub>Instance Method</sub>

Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func sessionControlsWillExitFullscreenAppearance(_ session: AVCaptureSession)
```

## Parameters

- `session` — The capture session with controls that are exiting a fullscreen appearance.

## Discussion

When your app receives this callback, it should resume showing portions of the interface it hid when controls entered a fullscreen appearance.

The system calls this method before [- sessionControlsDidBecomeInactive:](<sessioncontrolsdidbecomeinactive(__).md>).

## See Also

### Responding to control events

- [- sessionControlsDidBecomeActive:](<sessioncontrolsdidbecomeactive(__).md>) — Tells the delegate when a capture session’s controls become active and available for interaction.
- [- sessionControlsWillEnterFullscreenAppearance:](<sessioncontrolswillenterfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [- sessionControlsDidBecomeInactive:](<sessioncontrolsdidbecomeinactive(__).md>) — Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.
