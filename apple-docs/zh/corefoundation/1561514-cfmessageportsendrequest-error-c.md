---
title: CFMessagePortSendRequest 错误码
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
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFMessagePort](cfmessageport.md)

# CFMessagePortSendRequest 错误码

<sub>API 集合</sub>

`CFMessagePortSendRequest` 的错误码。

## 主题

### 常量

- [kCFMessagePortSuccess](kcfmessageportsuccess.md) — 消息已成功发送，并且若期望回复，则已收到回复。
- [kCFMessagePortSendTimeout](kcfmessageportsendtimeout.md) — 在发送超时之前未能发送消息。
- [kCFMessagePortReceiveTimeout](kcfmessageportreceivetimeout.md) — 在接收超时之前未收到回复。
- [kCFMessagePortIsInvalid](kcfmessageportisinvalid.md) — 因消息端口无效而未能发送消息。
- [kCFMessagePortTransportError](kcfmessageporttransporterror.md) — 尝试发送消息时发生错误。
- [kCFMessagePortBecameInvalidError](kcfmessageportbecameinvaliderror.md) — 消息端口已失效。
