---
title: kCFMessagePortSendTimeout
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfmessageportsendtimeout
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfmessageportsendtimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfmessageportsendtimeout.json'
content_hash: 'sha256:c8ee615efc164ba6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFMessagePortSendTimeout

<sub>Global Variable</sub>

The message could not be sent before the send timeout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFMessagePortSendTimeout: Int32 { get }
```

## See Also

### Constants

- [kCFMessagePortSuccess](kcfmessageportsuccess.md) — The message was successfully sent and, if a reply was expected, a reply was received.
- [kCFMessagePortReceiveTimeout](kcfmessageportreceivetimeout.md) — No reply was received before the receive timeout.
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — The message could not be sent because the message port is invalid.
- [kCFMessagePortTransportError](kcfmessageporttransporterror.md) — An error occurred trying to send the message.
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — The message port was invalidated.
