---
title: 'focusedElement(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/focusedelement(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/focusedelement(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/focusedelement%28using%3A%29.json'
content_hash: 'sha256:2cbb4dfae3886188'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# focusedElement(using:)

<sub>Type Method</sub>

Returns the accessibility element that’s currently in focus by the specified assistive app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func focusedElement(using assistiveTechnologyIdentifier: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?
```

## Return Value

The element that is currently focused by the specified assistive technology or the element that was most recently focused, if no technology is specified.

## See Also

### Convenience functions

- [UIAccessibilityHearingDevicePairedEar](hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [HearingDeviceEar](hearingdeviceear.md) — Constants that specify how a person is using a hearing device.
- [UIAccessibilityRegisterGestureConflictWithZoom](<registergestureconflictwithzoom().md>) — Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIAccessibilityZoomFocusChanged](<zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
