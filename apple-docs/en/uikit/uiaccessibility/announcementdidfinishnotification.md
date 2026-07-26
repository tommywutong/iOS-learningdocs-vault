---
title: announcementDidFinishNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/announcementdidfinishnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/announcementdidfinishnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/announcementdidfinishnotification.json'
content_hash: 'sha256:046ceb33185910ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# announcementDidFinishNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system finishes reading an announcement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let announcementDidFinishNotification: NSNotification.Name
```

## Discussion

The parameter is a dictionary with two keys, [UIAccessibilityAnnouncementKeyStringValue](announcementstringvalueuserinfokey.md) and [UIAccessibilityAnnouncementKeyWasSuccessful](announcementwassuccessfuluserinfokey.md). Observe this notification using the default notification center.

## See Also

### VoiceOver

- [UIAccessibilityAnnouncementNotification](notification/announcement.md) — A notification that an app posts when it needs to convey an announcement to the assistive app.
- [UIAccessibilityVoiceOverStatusDidChangeNotification](voiceoverstatusdidchangenotification.md) — A notification that UIKit posts when VoiceOver starts or stops.
- [UIAccessibilityVoiceOverStatusChanged](../uiaccessibilityvoiceoverstatuschanged.md) — A notification that UIKit posts when VoiceOver starts or stops. _(deprecated)_
