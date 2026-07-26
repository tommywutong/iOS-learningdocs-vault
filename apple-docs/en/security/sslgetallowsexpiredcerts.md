---
title: SSLGetAllowsExpiredCerts
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetallowsexpiredcerts
source_url: 'https://developer.apple.com/documentation/security/sslgetallowsexpiredcerts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetallowsexpiredcerts.json'
content_hash: 'sha256:fc98b705d38f6323'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetAllowsExpiredCerts

<sub>Function</sub>

Retrieves the value specifying whether expired certificates are allowed.

> [!warning] Deprecated
> See the replacement procedure for allowing expired certificates in the deprecation summary of [SSLSetAllowsExpiredCerts](sslsetallowsexpiredcerts.md).

<sub>macOS</sub>

```objc
OSStatus SSLGetAllowsExpiredCerts(SSLContextRef context, Boolean *allowsExpired);
```

## Parameters

- `context` — An SSL session context reference.

- `allowsExpired` — On return, this flag is set to the value of the Boolean flag that specifies whether expired certificates are ignored. If this value is `true`, then Secure Transport does not return an error if any certificates in the certificate chain are expired.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can set the `allowsExpired` flag to allow the handshake to succeed even if one or more certificates in the certificate chain have expired. This function returns the current setting of this flag. Use the [SSLSetAllowsExpiredCerts](sslsetallowsexpiredcerts.md) function to set the value of the `allowsExpired` flag.
