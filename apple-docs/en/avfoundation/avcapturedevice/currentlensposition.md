---
title: currentLensPosition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/currentlensposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentlensposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/currentlensposition.json'
content_hash: 'sha256:09d4db6ac8745eaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# currentLensPosition

<sub>Type Property</sub>

A constant that represents the current lens position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let currentLensPosition: Float
```

## Discussion

Pass this value to the [- setFocusModeLockedWithLensPosition:completionHandler:](<setfocusmodelocked(lensposition_completionhandler_).md>) method to lock focus without changing the current lens position.

## See Also

### Setting focus manually

- [lockingFocusWithCustomLensPositionSupported](islockingfocuswithcustomlenspositionsupported.md) — A Boolean value that indicates whether the device supports locking focus to a specific lens position.
- [lensPosition](lensposition.md) — The current focus position of the lens.
- [- setFocusModeLockedWithLensPosition:completionHandler:](<setfocusmodelocked(lensposition_completionhandler_).md>) — Locks the lens position at the specified value, and sets the focus mode to a locked state.
