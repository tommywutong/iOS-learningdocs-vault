---
title: NSURLProtectionSpace authentication method constants
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLProtectionSpace](urlprotectionspace.md)

# NSURLProtectionSpace authentication method constants

<sub>API Collection</sub>

Constants describing known values of the [authenticationMethod](urlprotectionspace/authenticationmethod.md) property of a [URLProtectionSpace](urlprotectionspace.md).

## Overview

These constants are also used with the [URLProtectionSpace](urlprotectionspace.md) initializers [- initWithHost:port:protocol:realm:authenticationMethod:](<urlprotectionspace/init(host_port_protocol_realm_authenticationmethod_).md>) and [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>).

## Topics

### Session-wide authentication challenges

- [NSURLAuthenticationMethodClientCertificate](nsurlauthenticationmethodclientcertificate.md) — Use client certificate authentication for this protection space.
- [NSURLAuthenticationMethodNegotiate](nsurlauthenticationmethodnegotiate.md) — Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [NSURLAuthenticationMethodNTLM](nsurlauthenticationmethodntlm.md) — Use NTLM authentication for this protection space.
- [NSURLAuthenticationMethodServerTrust](nsurlauthenticationmethodservertrust.md) — Perform server trust authentication (certificate validation) for this protection space.

### Task-specific authentication challenges

- [NSURLAuthenticationMethodDefault](nsurlauthenticationmethoddefault.md) — Use the default authentication method for a protocol.
- [NSURLAuthenticationMethodHTMLForm](nsurlauthenticationmethodhtmlform.md) — Use HTML form authentication for this protection space.
- [NSURLAuthenticationMethodHTTPBasic](nsurlauthenticationmethodhttpbasic.md) — Use HTTP basic authentication for this protection space.
- [NSURLAuthenticationMethodHTTPDigest](nsurlauthenticationmethodhttpdigest.md) — Use HTTP digest authentication for this protection space.

## See Also

### Related Documentation

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — Respond appropriately when a server demands authentication for a URL request.
- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md) — Evaluate the server’s security credentials in your app.

### Identifying protection space properties

- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md) — These constants describe the supported protocols for a protection space, as returned by [protocol](urlprotectionspace/protocol.md).
- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md) — These constants describe the supported proxy types used in [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) and returned by [proxyType](urlprotectionspace/proxytype.md).
