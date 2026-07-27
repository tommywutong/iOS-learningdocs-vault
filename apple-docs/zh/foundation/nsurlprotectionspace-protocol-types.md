---
title: NSURLProtectionSpace 的协议类型
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlprotectionspace-protocol-types
source_url: 'https://developer.apple.com/documentation/foundation/nsurlprotectionspace-protocol-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlprotectionspace-protocol-types.json'
content_hash: 'sha256:4efdec0cdf34d05f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLProtectionSpace](urlprotectionspace.md)

# NSURLProtectionSpace 的协议类型

<sub>API 集合</sub>

这些常量描述了某个保护空间所支持的协议，即 [protocol](urlprotectionspace/protocol.md) 所返回的值。

## 主题

### 协议类型

- [NSURLProtectionSpaceHTTP](nsurlprotectionspacehttp.md) — HTTP 的协议类型。
- [NSURLProtectionSpaceHTTPS](nsurlprotectionspacehttps.md) — HTTPS 的协议类型。
- [NSURLProtectionSpaceFTP](nsurlprotectionspaceftp.md) — FTP 的协议类型。 _(已废弃)_

## 另请参阅

### 识别保护空间属性

- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md) — 这些常量描述了用于 [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) 并由 [proxyType](urlprotectionspace/proxytype.md) 返回的受支持代理类型。
- [NSURLProtectionSpace authentication method constants](nsurlprotectionspace-authentication-method-constants.md) — 描述 [URLProtectionSpace](urlprotectionspace.md) 的 [authenticationMethod](urlprotectionspace/authenticationmethod.md) 属性的已知值的常量。
