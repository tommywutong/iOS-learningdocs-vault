---
title: lensPosition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/lensposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/lensposition.json'
content_hash: 'sha256:98685cf7e06fad0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# lensPosition

<sub>Instance Property</sub>

The current focus position of the lens.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var lensPosition: Float { get }
```

## Discussion

A lens position value doesn’t correspond to an exact physical distance, nor does it represent a consistent focus distance from device to device.

The range of possible positions is `0.0` to `1.0`, with `0.0` being the shortest distance at which the lens can focus and `1.0` the furthest. Note that `1.0` doesn’t represent focus at infinity. The default value is `1.0`.

This property is key-value observable.

## See Also

### Setting focus manually

- [lockingFocusWithCustomLensPositionSupported](islockingfocuswithcustomlenspositionsupported.md) — A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [AVCaptureLensPositionCurrent](currentlensposition.md) — A constant that represents the current lens position.
- [- setFocusModeLockedWithLensPosition:completionHandler:](<setfocusmodelocked(lensposition_completionhandler_).md>) — Locks the lens position at the specified value, and sets the focus mode to a locked state.
