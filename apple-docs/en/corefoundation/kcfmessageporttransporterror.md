---
title: kCFMessagePortTransportError
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfmessageporttransporterror
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfmessageporttransporterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfmessageporttransporterror.json'
content_hash: 'sha256:90c04cdf60ac84eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFMessagePortTransportError

<sub>Global Variable</sub>

An error occurred trying to send the message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFMessagePortTransportError: Int32 { get }
```

## See Also

### Constants

- [kCFMessagePortSuccess](kcfmessageportsuccess.md) — The message was successfully sent and, if a reply was expected, a reply was received.
- [kCFMessagePortSendTimeout](kcfmessageportsendtimeout.md) — The message could not be sent before the send timeout.
- [kCFMessagePortReceiveTimeout](kcfmessageportreceivetimeout.md) — No reply was received before the receive timeout.
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — The message could not be sent because the message port is invalid.
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — The message port was invalidated.
