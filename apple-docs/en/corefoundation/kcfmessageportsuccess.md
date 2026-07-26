---
title: kCFMessagePortSuccess
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfmessageportsuccess
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfmessageportsuccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfmessageportsuccess.json'
content_hash: 'sha256:9236eee5ccf9808d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFMessagePortSuccess

<sub>Global Variable</sub>

The message was successfully sent and, if a reply was expected, a reply was received.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFMessagePortSuccess: Int32 { get }
```

## See Also

### Constants

- [kCFMessagePortSendTimeout](kcfmessageportsendtimeout.md) — The message could not be sent before the send timeout.
- [kCFMessagePortReceiveTimeout](kcfmessageportreceivetimeout.md) — No reply was received before the receive timeout.
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — The message could not be sent because the message port is invalid.
- [kCFMessagePortTransportError](kcfmessageporttransporterror.md) — An error occurred trying to send the message.
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — The message port was invalidated.
