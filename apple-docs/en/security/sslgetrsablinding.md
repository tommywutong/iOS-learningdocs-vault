---
title: SSLGetRsaBlinding
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetrsablinding
source_url: 'https://developer.apple.com/documentation/security/sslgetrsablinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetrsablinding.json'
content_hash: 'sha256:5b7126cf2351689c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetRsaBlinding

<sub>Function</sub>

Obtains a value indicating whether RSA blinding is enabled.

> [!warning] Deprecated
> RSA blinding is now enabled unconditionally as it prevents a known way for an attacker to recover the private key and the performance gain of disabling it is negligible.

<sub>macOS</sub>

```objc
OSStatus SSLGetRsaBlinding(SSLContextRef context, Boolean *blinding);
```

## Parameters

- `context` — An SSL session context reference.

- `blinding` — On return, a pointer to a Boolean value indicating whether RSA blinding is enabled.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function is used only on the server side of a connection.

Call the [SSLSetRsaBlinding](sslsetrsablinding.md) function to enable or disable RSA blinding.
