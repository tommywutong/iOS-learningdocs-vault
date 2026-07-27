---
title: NSURLProtectionSpace 的代理类型
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlprotectionspace-proxy-types
source_url: 'https://developer.apple.com/documentation/foundation/nsurlprotectionspace-proxy-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlprotectionspace-proxy-types.json'
content_hash: 'sha256:d01fd43af16cdee0'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLProtectionSpace](urlprotectionspace.md)

# NSURLProtectionSpace 的代理类型

<sub>API 集合</sub>

这些常量描述了用于 [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) 并由 [proxyType](urlprotectionspace/proxytype.md) 返回的受支持代理类型。

## 主题

### 代理类型

- [NSURLProtectionSpaceHTTPProxy](nsurlprotectionspacehttpproxy.md) — HTTP 代理的代理类型。
- [NSURLProtectionSpaceHTTPSProxy](nsurlprotectionspacehttpsproxy.md) — HTTPS 代理的代理类型。
- [NSURLProtectionSpaceFTPProxy](nsurlprotectionspaceftpproxy.md) — FTP 代理的代理类型。 _(已废弃)_
- [NSURLProtectionSpaceSOCKSProxy](nsurlprotectionspacesocksproxy.md) — SOCKS 代理的代理类型。

## 另请参阅

### 识别保护空间属性

- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md) — 这些常量描述了某个保护空间所支持的协议，即 [protocol](urlprotectionspace/protocol.md) 所返回的值。
- [NSURLProtectionSpace authentication method constants](nsurlprotectionspace-authentication-method-constants.md) — 描述 [URLProtectionSpace](urlprotectionspace.md) 的 [authenticationMethod](urlprotectionspace/authenticationmethod.md) 属性的已知值的常量。
