---
title: SSLGetProtocolVersion
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetprotocolversion
source_url: 'https://developer.apple.com/documentation/security/sslgetprotocolversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetprotocolversion.json'
content_hash: 'sha256:b301c1726e4a8395'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetProtocolVersion

<sub>Function</sub>

Gets the SSL protocol version.

> [!warning] Deprecated
> Use [SSLGetProtocolVersionMin](<sslgetprotocolversionmin(____).md>) and/or [SSLGetProtocolVersionMax](<sslgetprotocolversionmax(____).md>) to check whether a protocol is enabled.

<sub>macOS</sub>

```objc
OSStatus SSLGetProtocolVersion(SSLContextRef context, SSLProtocol *protocol);
```

## Parameters

- `context` — An SSL session context reference.

- `protocol` — On return, a pointer to the SSL protocol version.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
