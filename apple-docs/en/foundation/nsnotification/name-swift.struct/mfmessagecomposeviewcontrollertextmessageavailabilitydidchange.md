---
title: MFMessageComposeViewControllerTextMessageAvailabilityDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.json'
content_hash: 'sha256:6a358e07278d62c6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# MFMessageComposeViewControllerTextMessageAvailabilityDidChange

<sub>Type Property</sub>

Posted when the current device’s ability to send text messages changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name
```

## Discussion

The system posts this notification when the value [canSendText()](<../../../messageui/mfmessagecomposeviewcontroller/cansendtext().md>) returns has changed.

Upon receiving this notification, query its `userInfo` dictionary with the [MFMessageComposeViewControllerTextMessageAvailabilityKey](../../../messageui/mfmessagecomposeviewcontrollertextmessageavailabilitykey.md) key. If the availability of text message sending has changed, your app should invalidate caches and update its user interface as appropriate.

## See Also

### MessageUI

- [MFMessageComposeViewControllerTextMessageAvailabilityDidChange](mfmessagecomposeviewcontrollertextmessageavailabilitydidchange.md) — Posted when the current device’s ability to send text messages changes.
