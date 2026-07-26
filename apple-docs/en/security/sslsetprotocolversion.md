---
title: SSLSetProtocolVersion
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetprotocolversion
source_url: 'https://developer.apple.com/documentation/security/sslsetprotocolversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetprotocolversion.json'
content_hash: 'sha256:a1fd66e6b4b941d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetProtocolVersion

<sub>Function</sub>

Sets the SSL protocol version.

> [!warning] Deprecated
> Use [SSLSetProtocolVersionMin](<sslsetprotocolversionmin(____).md>) and/or [SSLSetProtocolVersionMax](<sslsetprotocolversionmax(____).md>) to specify which protocols are enabled.

<sub>macOS</sub>

```objc
OSStatus SSLSetProtocolVersion(SSLContextRef context, SSLProtocol version);
```

## Parameters

- `context` — An SSL session context reference.

- `version` — The SSL protocol version to negotiate.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function cannot be called when a session is active.
