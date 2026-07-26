---
title: UIAccessibility.AssistiveTechnologyIdentifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 5.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/assistivetechnologyidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetechnologyidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/assistivetechnologyidentifier.json'
content_hash: 'sha256:b1db747e6b6f2d0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.AssistiveTechnologyIdentifier

<sub>Structure</sub>

Identifiers for assistive apps.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct AssistiveTechnologyIdentifier
```

## Overview

Manage pausing and resuming assistive apps with these identifiers.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Identifiers

- [UIAccessibilityNotificationSwitchControlIdentifier](assistivetechnologyidentifier/notificationswitchcontrol.md) — The Switch Control accessibility feature.
- [UIAccessibilityNotificationVoiceOverIdentifier](assistivetechnologyidentifier/notificationvoiceover.md) — The VoiceOver assistive app.

### Initializer

- [init(rawValue:)](<assistivetechnologyidentifier/init(rawvalue_).md>) — Creates an assistive app identifier with the specified raw value.

## See Also

### Notification keys

- [UIAccessibilityAnnouncementKeyStringValue](announcementstringvalueuserinfokey.md) — The text of the announcement.
- [UIAccessibilityAnnouncementKeyWasSuccessful](announcementwassuccessfuluserinfokey.md) — A Boolean value that indicates whether the announcement is successful.
- [UIAccessibilityFocusedElementKey](focusedelementuserinfokey.md) — The element currently in focus by the assistive app.
- [UIAccessibilityUnfocusedElementKey](unfocusedelementuserinfokey.md) — The element previously in focus by the assistive app.
- [UIAccessibilityAssistiveTechnologyKey](assistivetechnologyuserinfokey.md) — The identifier of the assistive app.
