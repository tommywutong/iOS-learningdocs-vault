---
title: SSLSetProtocolVersionEnabled
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetprotocolversionenabled
source_url: 'https://developer.apple.com/documentation/security/sslsetprotocolversionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetprotocolversionenabled.json'
content_hash: 'sha256:9d3568749129f6ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetProtocolVersionEnabled

<sub>Function</sub>

Sets the allowed Secure Sockets Layer (SSL) protocol versions.

> [!warning] Deprecated
> Use [SSLSetProtocolVersionMin](<sslsetprotocolversionmin(____).md>) and/or [SSLSetProtocolVersionMax](<sslsetprotocolversionmax(____).md>) to specify which protocols are enabled.

<sub>macOS</sub>

```objc
OSStatus SSLSetProtocolVersionEnabled(SSLContextRef context, SSLProtocol protocol, Boolean enable);
```

## Parameters

- `context` — An SSL session context reference.

- `protocol` — The SSL protocol version to enable. Pass `kSSLProtocolAll` to enable all protocols.

- `enable` — A Boolean value indicating whether to enable or disable the specified protocol. Specify `true` to enable the protocol.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Calling this function is optional. The default is that all supported protocols are enabled. When you call this function, only the specified protocol is affected. Therefore, if you call it once to disable SSL version 2 (for example), the other protocols all remain enabled. You may call this function as many times as you wish to enable and disable specific protocols. You can specify one of the following values for the `protocol` parameter:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolAll`

This function cannot be called when a session is active.
