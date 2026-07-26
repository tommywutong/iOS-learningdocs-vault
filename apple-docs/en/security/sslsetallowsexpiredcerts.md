---
title: SSLSetAllowsExpiredCerts
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetallowsexpiredcerts
source_url: 'https://developer.apple.com/documentation/security/sslsetallowsexpiredcerts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetallowsexpiredcerts.json'
content_hash: 'sha256:af8baa38e60e3a00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetAllowsExpiredCerts

<sub>Function</sub>

Specifies whether certificate expiration times are ignored.

> [!warning] Deprecated
> To ignore expired certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [SSLSetSessionOption](<sslsetsessionoption(______).md>) to set [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) to true. When [SSLHandshake](<sslhandshake(__).md>) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [SecTrust](sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [SecTrust](sectrust.md) APIs (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)). The [SecTrustSetOptions](<sectrustsetoptions(____).md>) function allows you to specify that the expiration status of certificates should be ignored for this evaluation.

<sub>macOS</sub>

```objc
OSStatus SSLSetAllowsExpiredCerts(SSLContextRef context, Boolean allowsExpired);
```

## Parameters

- `context` — An SSL session context reference.

- `allowsExpired` — A Boolean flag representing whether the certificate expiration times are ignored. The default for this flag is `false`, meaning expired certificates result in an `errSSLCertExpired` result code.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can use this function to allow the handshake to succeed even if one or more certificates in the certificate chain have expired. You can use the [SSLGetAllowsExpiredCerts](sslgetallowsexpiredcerts.md) function to determine the current setting of the `allowsExpired` flag.

Use the [SSLSetAllowsExpiredRoots](sslsetallowsexpiredroots.md) function to set a flag specifying whether expired root certificates are allowed.
