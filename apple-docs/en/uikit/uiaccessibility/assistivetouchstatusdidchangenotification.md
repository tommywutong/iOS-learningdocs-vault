---
title: assistiveTouchStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/assistivetouchstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetouchstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/assistivetouchstatusdidchangenotification.json'
content_hash: 'sha256:8a7ddb0b0cc4c4b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# assistiveTouchStatusDidChangeNotification

<sub>Type Property</sub>

A notification that indicates a change in the status of AssistiveTouch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let assistiveTouchStatusDidChangeNotification: NSNotification.Name
```

## Discussion

The user must enable Guided Access for this notification to post.

## See Also

### Assistive apps

- [UIAccessibilityGuidedAccessStatusDidChangeNotification](guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityPauseAssistiveTechnologyNotification](notification/pauseassistivetechnology.md) — A notification that pauses an assistive app’s operations temporarily.
- [UIAccessibilityResumeAssistiveTechnologyNotification](notification/resumeassistivetechnology.md) — A notification that resumes an assistive app’s operations temporarily.
- [AssistiveTechnologyIdentifier](assistivetechnologyidentifier.md) — Identifiers for assistive apps.
