---
title: registerGestureConflictWithZoom()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/registergestureconflictwithzoom()
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/registergestureconflictwithzoom()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/registergestureconflictwithzoom%28%29.json'
content_hash: 'sha256:160a77c62306738e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# registerGestureConflictWithZoom()

<sub>Type Method</sub>

Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func registerGestureConflictWithZoom()
```

## Discussion

Use this function if your application uses multi-finger gestures that conflict with the gestures used by system Zoom (that is, three-finger gestures). When this is the case, the user is presented with the choice of turning off Zoom or continuing.

## See Also

### Convenience functions

- [UIAccessibilityFocusedElement](<focusedelement(using_).md>) — Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibilityHearingDevicePairedEar](hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [HearingDeviceEar](hearingdeviceear.md) — Constants that specify how a person is using a hearing device.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIAccessibilityZoomFocusChanged](<zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
