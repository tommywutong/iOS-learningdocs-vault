---
title: UIAccessibility.HearingDeviceEar
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/hearingdeviceear
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/hearingdeviceear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/hearingdeviceear.json'
content_hash: 'sha256:8ccae44db7640925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.HearingDeviceEar

<sub>Structure</sub>

Constants that specify how a person is using a hearing device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct HearingDeviceEar
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIAccessibilityHearingDeviceEarLeft](hearingdeviceear/left.md) — A constant that represents the left ear.
- [UIAccessibilityHearingDeviceEarRight](hearingdeviceear/right.md) — A constant that represents the right ear.
- [UIAccessibilityHearingDeviceEarBoth](hearingdeviceear/both.md) — A constant that represents both ears.

### Initializers

- [init(rawValue:)](<hearingdeviceear/init(rawvalue_).md>) — Creates a structure that represents a hearing-device ear with the specified raw value.

## See Also

### Convenience functions

- [UIAccessibilityFocusedElement](<focusedelement(using_).md>) — Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibilityHearingDevicePairedEar](hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [UIAccessibilityRegisterGestureConflictWithZoom](<registergestureconflictwithzoom().md>) — Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIAccessibilityZoomFocusChanged](<zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
