---
title: SSLGetAllowsExpiredRoots
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetallowsexpiredroots
source_url: 'https://developer.apple.com/documentation/security/sslgetallowsexpiredroots'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetallowsexpiredroots.json'
content_hash: 'sha256:e992d33128618d7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetAllowsExpiredRoots

<sub>Function</sub>

Retrieves the value indicating whether expired roots are allowed.

> [!warning] Deprecated
> See the replacement procedure for allowing expired root certificates in the deprecation summary of [SSLSetAllowsExpiredRoots](sslsetallowsexpiredroots.md).

<sub>macOS</sub>

```objc
OSStatus SSLGetAllowsExpiredRoots(SSLContextRef context, Boolean *allowsExpired);
```

## Parameters

- `context` — An SSL session context reference.

- `allowsExpired` — On return, points to a Boolean value indicating whether expired roots are allowed. If this value is `true`, no errors are returned if the certificate chain ends in an expired root.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Use the [SSLSetAllowsExpiredRoots](sslsetallowsexpiredroots.md) function to change the setting of the `allowsExpired` flag.
