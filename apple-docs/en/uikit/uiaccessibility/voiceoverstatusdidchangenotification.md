---
title: voiceOverStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/voiceoverstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/voiceoverstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/voiceoverstatusdidchangenotification.json'
content_hash: 'sha256:f970f351a92cfebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# voiceOverStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when VoiceOver starts or stops.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let voiceOverStatusDidChangeNotification: NSNotification.Name
```

## Discussion

Use this notification to customize your app’s UI for VoiceOver users. For example, if you display a UI element that briefly overlays other parts of your UI, you can make the display persistent for VoiceOver users, but allow it to not appear for users who aren’t using VoiceOver. You can also use the [UIAccessibilityIsVoiceOverRunning](isvoiceoverrunning.md) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### VoiceOver

- [UIAccessibilityAnnouncementNotification](notification/announcement.md) — A notification that an app posts when it needs to convey an announcement to the assistive app.
- [UIAccessibilityAnnouncementDidFinishNotification](announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
- [UIAccessibilityVoiceOverStatusChanged](../uiaccessibilityvoiceoverstatuschanged.md) — A notification that UIKit posts when VoiceOver starts or stops. _(deprecated)_
