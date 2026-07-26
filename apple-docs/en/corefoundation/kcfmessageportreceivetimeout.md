---
title: kCFMessagePortReceiveTimeout
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfmessageportreceivetimeout
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfmessageportreceivetimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfmessageportreceivetimeout.json'
content_hash: 'sha256:cfb77e3d176364ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFMessagePortReceiveTimeout

<sub>Global Variable</sub>

No reply was received before the receive timeout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFMessagePortReceiveTimeout: Int32 { get }
```

## See Also

### Constants

- [kCFMessagePortSuccess](kcfmessageportsuccess.md) — The message was successfully sent and, if a reply was expected, a reply was received.
- [kCFMessagePortSendTimeout](kcfmessageportsendtimeout.md) — The message could not be sent before the send timeout.
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — The message could not be sent because the message port is invalid.
- [kCFMessagePortTransportError](kcfmessageporttransporterror.md) — An error occurred trying to send the message.
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — The message port was invalidated.
