---
title: isLockingFocusWithCustomLensPositionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/islockingfocuswithcustomlenspositionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingfocuswithcustomlenspositionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/islockingfocuswithcustomlenspositionsupported.json'
content_hash: 'sha256:fa969d443824b166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isLockingFocusWithCustomLensPositionSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports locking focus to a specific lens position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLockingFocusWithCustomLensPositionSupported: Bool { get }
```

## Discussion

If this property’s value is [false](../../swift/false.md), calling the [- setFocusModeLockedWithLensPosition:completionHandler:](<setfocusmodelocked(lensposition_completionhandler_).md>) method with a lens position value other than [AVCaptureLensPositionCurrent](currentlensposition.md) raises an exception.

## See Also

### Setting focus manually

- [lensPosition](lensposition.md) — The current focus position of the lens.
- [AVCaptureLensPositionCurrent](currentlensposition.md) — A constant that represents the current lens position.
- [- setFocusModeLockedWithLensPosition:completionHandler:](<setfocusmodelocked(lensposition_completionhandler_).md>) — Locks the lens position at the specified value, and sets the focus mode to a locked state.
