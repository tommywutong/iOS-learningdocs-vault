---
title: SSLGetProtocolVersionEnabled
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetprotocolversionenabled
source_url: 'https://developer.apple.com/documentation/security/sslgetprotocolversionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetprotocolversionenabled.json'
content_hash: 'sha256:e4c8fa67db01ea48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetProtocolVersionEnabled

<sub>Function</sub>

Retrieves the enabled status of a given protocol.

> [!warning] Deprecated
> Use [SSLGetProtocolVersionMin](<sslgetprotocolversionmin(____).md>) and/or [SSLGetProtocolVersionMax](<sslgetprotocolversionmax(____).md>) to check whether a protocol is enabled.

<sub>macOS</sub>

```objc
OSStatus SSLGetProtocolVersionEnabled(SSLContextRef context, SSLProtocol protocol, Boolean *enable);
```

## Parameters

- `context` — An SSL session context reference.

- `protocol` — A value of type `SSLProtocol` representing an SSL protocol version.

- `enable` — On return, points to a Boolean value indicating whether the specified protocol version is enabled. If this value is `true`, the protocol is enabled.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can specify any one of the following values for the `protocol` parameter:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolAll` Specify this value to determine whether all protocols are enabled.
