---
title: textMessageAvailabilityDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/textmessageavailabilitydidchange
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/textmessageavailabilitydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/textmessageavailabilitydidchange.json'
content_hash: 'sha256:09970ea2534cde56'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# textMessageAvailabilityDidChange

<sub>Type Property</sub>

Notification posted when text message availability changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var textMessageAvailabilityDidChange: NotificationCenter.BaseMessageIdentifier<MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage> { get }
```

## Discussion

This notification is posted when the device’s ability to send text messages changes (e.g., SIM card inserted/removed, airplane mode toggled, iMessage account status changed).

> [!note] Note
> This notification may be delivered on any thread.
