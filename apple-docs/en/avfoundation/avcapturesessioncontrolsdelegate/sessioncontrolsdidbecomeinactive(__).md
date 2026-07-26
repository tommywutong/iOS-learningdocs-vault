---
title: 'sessionControlsDidBecomeInactive(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive%28_%3A%29.json'
content_hash: 'sha256:a3bdc9a4a5b9876c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md)

# sessionControlsDidBecomeInactive(_:)

<sub>Instance Method</sub>

Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func sessionControlsDidBecomeInactive(_ session: AVCaptureSession)
```

## Parameters

- `session` — The capture session with inactive controls.

## See Also

### Responding to control events

- [- sessionControlsDidBecomeActive:](<sessioncontrolsdidbecomeactive(__).md>) — Tells the delegate when a capture session’s controls become active and available for interaction.
- [- sessionControlsWillEnterFullscreenAppearance:](<sessioncontrolswillenterfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [- sessionControlsWillExitFullscreenAppearance:](<sessioncontrolswillexitfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
