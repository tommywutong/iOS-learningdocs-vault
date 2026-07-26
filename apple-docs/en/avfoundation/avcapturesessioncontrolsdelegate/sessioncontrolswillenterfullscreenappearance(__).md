---
title: 'sessionControlsWillEnterFullscreenAppearance(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance%28_%3A%29.json'
content_hash: 'sha256:9a32c280a1781bf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md)

# sessionControlsWillEnterFullscreenAppearance(_:)

<sub>Instance Method</sub>

Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func sessionControlsWillEnterFullscreenAppearance(_ session: AVCaptureSession)
```

## Parameters

- `session` — The capture session with controls that are entering a fullscreen appearance.

## Discussion

When controls enter a fullscreen appearance, your app should hide portions of its user interface, including duplicative or unnecessary elements. Few onscreen elements should be visible so people can focus on their control interactions while viewing the camera preview unobstructed.

## See Also

### Responding to control events

- [- sessionControlsDidBecomeActive:](<sessioncontrolsdidbecomeactive(__).md>) — Tells the delegate when a capture session’s controls become active and available for interaction.
- [- sessionControlsWillExitFullscreenAppearance:](<sessioncontrolswillexitfullscreenappearance(__).md>) — Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [- sessionControlsDidBecomeInactive:](<sessioncontrolsdidbecomeinactive(__).md>) — Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.
