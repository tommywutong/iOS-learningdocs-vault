---
title: CSSM_TP_ReceiveConfirmation
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_tp_receiveconfirmation
source_url: 'https://developer.apple.com/documentation/security/cssm_tp_receiveconfirmation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_tp_receiveconfirmation.json'
content_hash: 'sha256:6ab3edc7657a9c3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CSSM_TP_ReceiveConfirmation

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
CSSM_RETURN CSSM_TP_ReceiveConfirmation(CSSM_TP_HANDLE TPHandle, const SecAsn1Item *ReferenceIdentifier, CSSM_TP_CONFIRM_RESPONSE_PTR*Responses, sint32 *ElapsedTime);
```
