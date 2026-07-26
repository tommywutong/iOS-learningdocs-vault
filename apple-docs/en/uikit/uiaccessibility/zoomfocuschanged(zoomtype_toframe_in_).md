---
title: 'zoomFocusChanged(zoomType:toFrame:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/zoomfocuschanged%28zoomtype%3Atoframe%3Ain%3A%29.json'
content_hash: 'sha256:de3c0620494b8040'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# zoomFocusChanged(zoomType:toFrame:in:)

<sub>Type Method</sub>

Notifies the system when the app’s focus changes to a new location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func zoomFocusChanged(zoomType type: UIAccessibility.ZoomType, toFrame frame: CGRect, in view: UIView)
```

## Parameters

- `type` — A `UIKit Functions` constant that identifies the type of Zoom.

- `frame` — The frame that’s currently zoomed, in screen coordinates.

- `view` — The view that contains the zoomed frame.

## See Also

### Convenience functions

- [UIAccessibilityFocusedElement](<focusedelement(using_).md>) — Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibilityHearingDevicePairedEar](hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [HearingDeviceEar](hearingdeviceear.md) — Constants that specify how a person is using a hearing device.
- [UIAccessibilityRegisterGestureConflictWithZoom](<registergestureconflictwithzoom().md>) — Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
