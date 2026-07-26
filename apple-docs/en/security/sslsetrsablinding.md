---
title: SSLSetRsaBlinding
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetrsablinding
source_url: 'https://developer.apple.com/documentation/security/sslsetrsablinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetrsablinding.json'
content_hash: 'sha256:9cef6424f771097b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetRsaBlinding

<sub>Function</sub>

Enables or disables RSA blinding.

> [!warning] Deprecated
> RSA blinding is now enabled unconditionally as it prevents a known way for an attacker to recover the private key and the performance gain of disabling it is negligible.

<sub>macOS</sub>

```objc
OSStatus SSLSetRsaBlinding(SSLContextRef context, Boolean blinding);
```

## Parameters

- `context` — An SSL session context reference.

- `blinding` — A Boolean value indicating whether to enable RSA blinding. Pass `true` to enable RSA blinding.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function is used only on the server side of a connection.

This feature thwarts a known attack to which RSA keys are vulnerable: It is possible to guess the RSA key by timing how long it takes the server to calculate the response to certain queries. RSA blinding adds a random calculation to each query response, thus making the attack impossible. Enabling RSA blinding is a trade-off between performance and security.

RSA blinding is enabled by default. Use the [SSLGetRsaBlinding](sslgetrsablinding.md) function to determine the current setting.
