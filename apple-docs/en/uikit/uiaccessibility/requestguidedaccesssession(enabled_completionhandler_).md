---
title: 'requestGuidedAccessSession(enabled:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/requestguidedaccesssession(enabled:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/requestguidedaccesssession(enabled:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/requestguidedaccesssession%28enabled%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c2dffd42833eec3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# requestGuidedAccessSession(enabled:completionHandler:)

<sub>Type Method</sub>

Transitions the app to or from Single App mode asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func requestGuidedAccessSession(enabled enable: Bool, completionHandler: @escaping @MainActor @Sendable (Bool) -> Void)
```

## Parameters

- `enable` — Specify [true](../../swift/true.md) to put the device into Single App mode for this app or [false](../../swift/false.md) to exit Single App mode.

- `completionHandler` — The block that notifies your app of the success or failure of the operation. This block takes the following parameter: - **didSucceed** — If [true](../../swift/true.md), the app transitioned to or from Single App mode successfully. If [false](../../swift/false.md), the app or device is not eligible for Single App mode or there was some other error.

## Discussion

You can use this method to lock your app into Single App mode and to release it from that mode later. For example, a test-taking app might enter this mode at the beginning of a test and exit it when the user completes the test. Entering Single App mode is supported only for devices that are supervised using Mobile Device Management (MDM), and the app itself must be enabled for this mode by MDM. You must balance each call to enter Single App mode with a call to exit that mode.

Because entering or exiting Single App mode might take some time, this method executes asynchronously and notifies you of the results using the `completionHandler` block.

## See Also

### Convenience functions

- [UIAccessibilityFocusedElement](<focusedelement(using_).md>) — Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibilityHearingDevicePairedEar](hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [HearingDeviceEar](hearingdeviceear.md) — Constants that specify how a person is using a hearing device.
- [UIAccessibilityRegisterGestureConflictWithZoom](<registergestureconflictwithzoom().md>) — Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [UIAccessibilityZoomFocusChanged](<zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
