---
title: NSURLProtectionSpace 的认证方式常量
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlprotectionspace-authentication-method-constants
source_url: 'https://developer.apple.com/documentation/foundation/nsurlprotectionspace-authentication-method-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlprotectionspace-authentication-method-constants.json'
content_hash: 'sha256:0aecb09a88d8cf3b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLProtectionSpace](urlprotectionspace.md)

# NSURLProtectionSpace 的认证方式常量

<sub>API 集合</sub>

描述 [URLProtectionSpace](urlprotectionspace.md) 的 [authenticationMethod](urlprotectionspace/authenticationmethod.md) 属性的已知值的常量。

## 概述

这些常量也用于 [URLProtectionSpace](urlprotectionspace.md) 的初始化方法 [- initWithHost:port:protocol:realm:authenticationMethod:](<urlprotectionspace/init(host_port_protocol_realm_authenticationmethod_).md>) 和 [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>)。

## 主题

### 会话级认证挑战

- [NSURLAuthenticationMethodClientCertificate](nsurlauthenticationmethodclientcertificate.md) — 对此保护空间使用客户端证书认证。
- [NSURLAuthenticationMethodNegotiate](nsurlauthenticationmethodnegotiate.md) — 协商是否对此保护空间使用 Kerberos 或 NTLM 认证。
- [NSURLAuthenticationMethodNTLM](nsurlauthenticationmethodntlm.md) — 对此保护空间使用 NTLM 认证。
- [NSURLAuthenticationMethodServerTrust](nsurlauthenticationmethodservertrust.md) — 对此保护空间执行服务器信任认证（证书验证）。

### 特定于任务的认证挑战

- [NSURLAuthenticationMethodDefault](nsurlauthenticationmethoddefault.md) — 对某个协议使用默认的认证方式。
- [NSURLAuthenticationMethodHTMLForm](nsurlauthenticationmethodhtmlform.md) — 对此保护空间使用 HTML 表单认证。
- [NSURLAuthenticationMethodHTTPBasic](nsurlauthenticationmethodhttpbasic.md) — 对此保护空间使用 HTTP 基本认证。
- [NSURLAuthenticationMethodHTTPDigest](nsurlauthenticationmethodhttpdigest.md) — 对此保护空间使用 HTTP 摘要认证。

## 另请参阅

### 相关文档

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — 在服务器要求对 URL 请求进行认证时做出恰当的响应。
- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md) — 在你的 App 中评估服务器的安全凭据。

### 识别保护空间属性

- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md) — 这些常量描述了某个保护空间所支持的协议，即 [protocol](urlprotectionspace/protocol.md) 所返回的值。
- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md) — 这些常量描述了用于 [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) 并由 [proxyType](urlprotectionspace/proxytype.md) 返回的受支持代理类型。
