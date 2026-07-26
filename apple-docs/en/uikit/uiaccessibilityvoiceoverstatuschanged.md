---
title: UIAccessibilityVoiceOverStatusChanged
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+（11.0 起废弃）, iPadOS 4.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiaccessibilityvoiceoverstatuschanged
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityvoiceoverstatuschanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityvoiceoverstatuschanged.json'
content_hash: 'sha256:38e1434c1a912841'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityVoiceOverStatusChanged

<sub>Global Variable</sub>

A notification that UIKit posts when VoiceOver starts or stops.

> [!warning] Deprecated
> Use [UIAccessibilityVoiceOverStatusDidChangeNotification](uiaccessibility/voiceoverstatusdidchangenotification.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated let UIAccessibilityVoiceOverStatusChanged: String
```

## Discussion

This notification doesn’t include a parameter.

Use this notification to customize your application’s user interface (UI) for VoiceOver users. For example, if you display a UI element that briefly overlays other parts of your UI, you can make the display persistent for VoiceOver users, but allow it to disappear as designed for users who are not using VoiceOver. You can also use the [UIAccessibilityIsVoiceOverRunning](uiaccessibility/isvoiceoverrunning.md) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center.

## See Also

### VoiceOver

- [UIAccessibilityAnnouncementNotification](uiaccessibility/notification/announcement.md) — A notification that an app posts when it needs to convey an announcement to the assistive app.
- [UIAccessibilityVoiceOverStatusDidChangeNotification](uiaccessibility/voiceoverstatusdidchangenotification.md) — A notification that UIKit posts when VoiceOver starts or stops.
- [UIAccessibilityAnnouncementDidFinishNotification](uiaccessibility/announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
