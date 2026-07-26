---
title: guidedAccessStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccessstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccessstatusdidchangenotification.json'
content_hash: 'sha256:a9a04a68551d2ea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# guidedAccessStatusDidChangeNotification

<sub>Type Property</sub>

A notification that indicates when a Guided Access session starts or ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let guidedAccessStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

Use the [UIAccessibilityIsGuidedAccessEnabled](isguidedaccessenabled.md) property to determine whether the Guided Access setting is enabled.

## See Also

### Assistive apps

- [UIAccessibilityAssistiveTouchStatusDidChangeNotification](assistivetouchstatusdidchangenotification.md) — A notification that indicates a change in the status of AssistiveTouch.
- [UIAccessibilityPauseAssistiveTechnologyNotification](notification/pauseassistivetechnology.md) — A notification that pauses an assistive app’s operations temporarily.
- [UIAccessibilityResumeAssistiveTechnologyNotification](notification/resumeassistivetechnology.md) — A notification that resumes an assistive app’s operations temporarily.
- [AssistiveTechnologyIdentifier](assistivetechnologyidentifier.md) — Identifiers for assistive apps.
