---
title: CFMessagePortSendRequest Error Codes
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1561514-cfmessageportsendrequest-error-c
source_url: 'https://developer.apple.com/documentation/corefoundation/1561514-cfmessageportsendrequest-error-c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1561514-cfmessageportsendrequest-error-c.json'
content_hash: 'sha256:392c74e03cb9b23d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFMessagePort](cfmessageport.md)

# CFMessagePortSendRequest Error Codes

<sub>API Collection</sub>

Error codes for `CFMessagePortSendRequest`.

## Topics

### Constants

- [kCFMessagePortSuccess](kcfmessageportsuccess.md) — The message was successfully sent and, if a reply was expected, a reply was received.
- [kCFMessagePortSendTimeout](kcfmessageportsendtimeout.md) — The message could not be sent before the send timeout.
- [kCFMessagePortReceiveTimeout](kcfmessageportreceivetimeout.md) — No reply was received before the receive timeout.
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — The message could not be sent because the message port is invalid.
- [kCFMessagePortTransportError](kcfmessageporttransporterror.md) — An error occurred trying to send the message.
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — The message port was invalidated.
