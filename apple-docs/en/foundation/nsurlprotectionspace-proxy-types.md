---
title: NSURLProtectionSpace proxy types
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLProtectionSpace](urlprotectionspace.md)

# NSURLProtectionSpace proxy types

<sub>API Collection</sub>

These constants describe the supported proxy types used in [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) and returned by [proxyType](urlprotectionspace/proxytype.md).

## Topics

### Proxy types

- [NSURLProtectionSpaceHTTPProxy](nsurlprotectionspacehttpproxy.md) — The proxy type for HTTP proxies.
- [NSURLProtectionSpaceHTTPSProxy](nsurlprotectionspacehttpsproxy.md) — The proxy type for HTTPS proxies.
- [NSURLProtectionSpaceFTPProxy](nsurlprotectionspaceftpproxy.md) — The proxy type for FTP proxies. _(deprecated)_
- [NSURLProtectionSpaceSOCKSProxy](nsurlprotectionspacesocksproxy.md) — The proxy type for SOCKS proxies.

## See Also

### Identifying protection space properties

- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md) — These constants describe the supported protocols for a protection space, as returned by [protocol](urlprotectionspace/protocol.md).
- [NSURLProtectionSpace authentication method constants](nsurlprotectionspace-authentication-method-constants.md) — Constants describing known values of the [authenticationMethod](urlprotectionspace/authenticationmethod.md) property of a [URLProtectionSpace](urlprotectionspace.md).
